from random import randint

class PokeDot:

    #Structure:
    #(NAME, MAX HP RATE, INCREASES BY TURN?, INCREASE RATE, IMMOBILIZED?, IMMOBILIZE CHANCE, N TURNS[-1-X], APPLIES DEBUFF?, STAT DEBUFF, DEBUFF AMOUNT, ESCAPE CHANCE)

    def Poison(self):
        return ("Poison",0.0625,True,1,False,0,-1,False,None,0,0)
    
    def Burn(self):
        return ("Burn",0.125,False,None,False,0,-1,False,None,0,0)
    
    def Paralyze(self):
        return ("Paralysis",0,False,None,True,0.25,-1,True,"Speed",0.25,0)
    
    def Freeze(self):
        return ("Freeze",0,False,None,True,1,randint(1,7),False,None,0,0.2)