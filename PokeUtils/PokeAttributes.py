class PokeAttributes:

    def __init__(self, stats: dict):
        self.HP = stats['HP']
        self.Atk = stats['Atk']
        self.Def = stats['Def']
        self.SpA = stats['SpA']
        self.SpD = stats['SpD']
        self.Speed = stats['Spe']
    
    def print_stat(self, stat: str) -> None:
        if stat in self.__dict__:
            print(f"{stat}: {self.__dict__[stat]}")
    
    def print(self):
        print("HP:",self.HP,"\nAtk:",self.Atk,"\nDef:",self.Def,"\nSpA:",self.SpA,"\nSpD:",self.SpD,"\nSpeed:",self.Speed,"\n-------------------------------")
    
    def reduce(self, stat: str, percentage: float) -> None:
        if stat in self.__dict__:
            self.__dict__[stat] = round(float(self.__dict__[stat] * (1.0 - percentage)))
        else:
            print(f"{stat} does not exist")
            exit(1)
    
    def increase(self, stat: str, percentage: float) -> None:
        if stat in self.__dict__:
            self.__dict__[stat] = round(float(self.__dict__[stat] * (1.0 + percentage)))
        else:
            print(f"{stat} does not exist")
            exit(1)
    
    def get_stat(self, stat: str) -> float:
        return self.__dict__[stat]