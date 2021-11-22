
from random import random, uniform, choice
from PokeUtils.PokeMove import PokeMove
from PokeUtils.Pokemon import Pokemon
from .PokeDB import PokeDB

class PokeUtils:

    def __init__(self) -> None:
        self.db = PokeDB("Poketext")
        self.weathers = self.db.get_fields("Weather",['name','boost','btype','bamount','weak','wtype','wamount','afterturn','aftamount','type'])
        self.weather = None

    def __repr__(self) -> str:
        return "PokeUtils"
    
    def close(self):
        self.db.close()
    
    def calculate_damage(self, source: Pokemon, move: PokeMove, target: Pokemon, debug:bool=False) -> int:
        A = source.stats.SpA if move.category == "Special" else source.stats.Atk
        D = target.stats.SpD if move.category == "Special" else target.stats.Def
        if debug:
            print(move)
            print("A:",A)
            print("D:",D)
        #Critical chance: 1/16 ~ 0.0625=6.25%
        crit = 2 if random() >= 0.9375 else 1
        randomN = round(uniform(0.85, 1.00),2)
        weather = 1
        if self.weather:
            if self.weather[1]:
                if self.weather[2] == move.mtype:
                    weather += self.weather[3]
            if self.weather[4]:
                if self.weather[5] == move.mtype:
                    weather -= self.weather[6]

        #Move Affinity
        stab = 1
        if move.mtype in source.type:
            stab = 1.5
        effectiveness = 1
        if len(target.type) > 1:
            #Multi type Pokemon
            t1 = self.db.get_fields('DMG_CHART',[target.type[0]],[('name','=',move.mtype)])[0][0]
            t2 = self.db.get_fields('DMG_CHART',[target.type[1]],[('name','=',move.mtype)])[0][0]
            effectiveness = t1 * t2
        else:
            #Single type Pokemon
            effectiveness = self.db.get_fields('DMG_CHART',[target.type[0]],[('name','=',move.mtype)])[0][0]
        modifier = weather * crit * randomN * stab * effectiveness
        part1 = ((2 * source.level) / 5) + 2
        part2 = (part1 * move.power * (A / D)) / 50
        damage = (part2 + 2) * modifier
        if debug:
            print("Weather:",weather,"\nCrit:",crit,"\nRandom:",randomN,"\nSTAB:",stab,"\nEffectiveness:",effectiveness,"\nModifier:",modifier,"\nTotal:",round(damage),"\n-------------------------------")
        return round(damage)

    def Attack(self, move_index: int, debug=False) -> None:
        if self.can_attack():
            if self.verify_accuracy(self.source.MOVESET[f"{move_index}"]):
                self.target.reduce_health(self.calculate_damage(self.source, self.source.MOVESET[f"{move_index}"], self.target,debug=debug))
                self.add_dot(self.source.MOVESET[f"{move_index}"])
            else:
                print("Attack Missed....")
    
    def set_weather(self, weather: str) -> None:
        names = [n[0] for n in self.weathers]
        if weather not in names:
            print("Unknown weather")
            exit(1)
        self.weather = self.weathers[self.weathers.index([n for n in self.weathers if n[0] == weather][0])]
    
    def apply_weather(self):
        if self.weather[7]:
            if not self.__in_types(self.source.type, self.weather[9]):
                print(f"{self.source.name} hit by {self.weather[0]}")
                self.source.reduce_health(round(self.source.MAX_HP / 16))
            if not self.__in_types(self.target.type, self.weather[9]):
                print(f"{self.target.name} hit by {self.weather[0]}")
                self.target.reduce_health(round(self.target.MAX_HP / 16))

    def end_of_turn(self):
        self.source.apply_dot()
        self.target.apply_dot()
        self.apply_weather()

    def setPokemons(self, source: Pokemon, target: Pokemon, debug:bool=False) -> None:
        self.source = source
        self.target = target
        if debug:
            print(f"Pokemon set:\nSource: {source.name}\nTarget: {target.name}\n-------------------------------")
    
    def verify_accuracy(self, move: PokeMove) -> bool:
        seed = round(random(),2)
        return True if (move.accuracy == 1 or seed <= move.accuracy) else False
    
    def add_dot(self, move: PokeMove) -> None:
        if move.has_dot:
            seed = round(random(),2)
            if seed <= move.dot_chance:
                if self.target.status == None:
                    self.target.add_status(move.dot)
    
    def can_attack(self) -> bool:
        status_immobility = ["Paralysis","Freeze"]
        answer = True
        #if pokemon has status attached
        if self.source.status:
            status = self.source.status
            #if status creates immobility
            if status[0] in status_immobility and status[4]:
                seed = round(random(),2)
                #if status runs indefinetely
                if status[6] == -1:
                    if seed > status[5]:
                        answer = False
                elif status[6] >= 0:
                    if status[6] == 0 or status[6] == 1:
                        self.source.remove_status()
                    else:
                        self.source.status = [x for x in self.source.status]
                        self.source.status[6] -= 1
                        self.source.status = tuple(self.source.status)
                        if seed > status[5] and status[0] != "Freeze":
                            answer = False
                        elif seed > status[10] and status[0] == "Freeze":
                            answer = False
                        elif seed <= status[10] and status[0] == "Freeze":
                            self.source.remove_status()
                else:
                    print("Error Unknown")
                    exit(1)
        return answer
    
    def check_speed(self) -> 'list[Pokemon]|str':
        order = []
        sp1 = self.source.stats.Speed
        sp2 = self.target.stats.Speed
        if sp1 > sp2:
            order = [self.source,self.target]
        elif sp2 == sp1:
            f = choice([self.source,self.target])
            order = [f, self.source if f.name == self.source.name else self.target]
        else:
            order = [self.target, self.source]
        return order, 'CPU' if order[0].name == self.target.name else 'Player'
    
    def _reverse_sources(self) -> None:
        self.source, self.target = self.target, self.source
    
    def __in_types(self,t1: list, t2: list) -> bool:
        for t in t1:
            if t in t2:
                return True
        return False