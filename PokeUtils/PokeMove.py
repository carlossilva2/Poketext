from .PokeDB import PokeDB

class PokeMove:

    def __init__(self, move: str) -> None:
        db = PokeDB('Poketext')
        mv = db.get_fields("Attacks", filter=[('name','=',move)])
        if len(mv) == 0:
            print(f"{move} does not exist in DB")
            exit(1)
        mv = mv[0]
        self.name = mv[0]
        self.category = mv[1]
        self.mtype = mv[2]
        self.power = mv[3]
        self.accuracy = mv[4]
        self.pp = mv[5]
        self.pp_left = mv[5]
        self.has_dot = mv[6]
        self.dot_chance = mv[7]
        self.dot = mv[8]
    
    def __repr__(self):
        return f"Name: {self.name}\nCategory: {self.category}\nType: {self.mtype}\nPower: {self.power}\nAccuracy: {self.accuracy}\nPP: {self.pp}\n-------------------------------"
    
    def reduce_pp(self, n: int):
        self.pp_left -= 1
        if self.pp_left < 0:
            self.pp_left = 0