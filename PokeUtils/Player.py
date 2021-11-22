from .Pokemon import Pokemon
from typing import List

class Player:

    def __init__(self, name: str, party: 'list[Pokemon]') -> None:
        self.name = name if name else "Ash"
        self.party = self.__verify_party__(party)
    
    def get_party(self):
        return [p.name for p in self.party]
    
    def __verify_party__(self, party: 'list[Pokemon]') -> List[Pokemon]:
        if len(party) > 6:
            print("Only 6 Pokemon are allowed inside of Party")
            exit(1)
        for pokemon in party:
            if pokemon.__class__ != "Pokemon":
                print("Only Pokemons are allowed in Party")
                exit(1)
        return party
