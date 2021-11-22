from .PokeAttributes import PokeAttributes
from .PokeMove import PokeMove
from .PokeDot import PokeDot
from .PokeDB import PokeDB

class Pokemon:
    __class__ = "Pokemon"

    def __init__(self, db_output:dict, debug:bool=False):
        self.__debug = debug
        self.db = PokeDB('Poketext')
        self.name = db_output['name']
        self.level = db_output['level']
        self.type = db_output['type']
        self.EV = PokeAttributes(db_output['ev'])
        self.IV = PokeAttributes(db_output['iv'])
        self.BASE = PokeAttributes(db_output['base'])
        self.ALIVE = True
        self.status = None
        self.poison_counter = None
        self.nature = self.db.get_fields('Nature',filter=[('name','=',db_output['nature'])])[0]
        self.calculate_stats()
        self.MOVESET = {
            "1": PokeMove(db_output['moves'][0]),
            "2": PokeMove(db_output['moves'][1]),
            "3": PokeMove(db_output['moves'][2]),
            "4": PokeMove(db_output['moves'][3])
        }
    
    def __repr__(self) -> str:
        return f"{self.name} - lvl {self.level}"

    def calculate_stats(self):
        #GEN III Calculations
        self.stats = PokeAttributes({
            "HP":  round((((2 * self.BASE.HP + self.IV.HP + (self.EV.HP / 4)) * self.level) / 100) + self.level + 10),
            "Atk": round((((2 * self.BASE.Atk + self.IV.Atk + (self.EV.Atk / 4)) * self.level) / 100) + 5),
            "Def": round((((2 * self.BASE.Def + self.IV.Def + (self.EV.Def / 4)) * self.level) / 100) + 5),
            "SpA": round((((2 * self.BASE.SpA + self.IV.SpA + (self.EV.SpA / 4)) * self.level) / 100) + 5),
            "SpD": round((((2 * self.BASE.SpD + self.IV.SpD + (self.EV.SpD / 4)) * self.level) / 100) + 5),
            "Spe": round((((2 * self.BASE.Speed + self.IV.Speed + (self.EV.Speed / 4)) * self.level) / 100) + 5)
        })
        self.MAX_HP = self.stats.HP
        prev = None
        print(f"-------------------------------\n{self.name}: {self.nature[0]} Nature\n") if self.__get_debug() else None
        if self.nature[1]:
            prev = self.stats.get_stat(self.nature[1])
            self.stats.increase(self.nature[1],self.nature[2])
            print(f"{self.nature[1]}:",prev,"->",self.stats.get_stat(self.nature[1])) if self.__get_debug() else None
        if self.nature[3]:
            prev = self.stats.__dict__[self.nature[3]]
            self.stats.reduce(self.nature[3],self.nature[4])
            print(f"{self.nature[3]}:",prev,"->",self.stats.get_stat(self.nature[3])) if self.__get_debug() else None
        print("-------------------------------") if self.__get_debug() else None
    
    def reduce_health(self, amount: int) -> None:
        prev = self.stats.HP
        self.stats.HP -= amount
        if self.__get_debug():
            print(f"HP: {prev} -> {self.stats.HP} ({prev - self.stats.HP} points)")
    
    def apply_dot(self) -> None:
        if self.status:
            if self.status[0] != "Poison":
                self.reduce_health(round(self.MAX_HP * self.status[1]))
            else:
                if self.poison_counter == None:
                    self.poison_counter = 0
                if self.poison_counter < 16:
                    self.poison_counter += 1
                print(f"-------------------------------\n{self.name}: DoT\n") if self.__get_debug() else None
                print("Poison Counter:", self.poison_counter) if self.__get_debug() else None
                ini = self.stats.HP
                #MAX HP * (Poison counter * 1 / 16)
                self.reduce_health(round(self.MAX_HP * (self.poison_counter * self.status[1])))
                print(f"HP:",ini,"->",self.stats.HP) if self.__get_debug() else None
                print("DoT:", self.stats.HP - ini) if self.__get_debug() else None
                print("-------------------------------") if self.__get_debug() else None
    
    def add_status(self, status: str) -> PokeDot:
        pkdot = PokeDot()
        self.status = eval(f"pkdot.{status}")()
        if self.__get_debug():
            print(f"-------------------------------\n{self.name}: Status\n")
            print(f"Applied '{self.status[0]}' to {self.name}")
        if self.status[7]:
            prev = self.stats.get_stat(self.status[8])
            self.stats.reduce(self.status[8],self.status[9])
            print(f"{self.status[8]}:",prev,"->",self.stats.get_stat(self.status[8]))
        print("-------------------------------")
        return self.status
    
    def remove_status(self) -> None:
        if self.status:
            print(f"{self.name} is no longer with {self.status[0]}")
            if self.status[7]:
                self.stats.increase(self.status[8],self.status[9])
            self.poison_counter = None
            self.status = None
    
    def __set_debug(self, state:bool) -> bool:
        self.__debug = state
        return state
    
    def __get_debug(self) -> bool:
        return self.__debug