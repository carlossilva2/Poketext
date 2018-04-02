"""MIT License

Copyright(c) 2018 Carlos Silva

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files(the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and / or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE. """

from random import randrange, randint
import random
import pygame as py
from time import sleep,time

movements = ["up", "down", "left", "right","upright","upleft","downright","downleft"]
comb_options = ["Attack","Run"]
oldX = 0
oldY = 0
worldSize = 6
alive = True
run = False
pokemons = [
    {
        "name": "Swampert",
        "type": ["Water","Ground"],
        "level": 100,
        "sound": "Swampert.mp3",
        "base": {
            "HP": 100,
            "Atk": 110,
            "Def": 90,
            "SpA": 85,
            "SpD": 90,
            "Spe": 60
        },
        "iv": {
            "HP": 20,
            "Atk": 28,
            "Def": 9,
            "SpA": 24,
            "SpD": 4,
            "Spe": 13
        },
        "ev": {
            "HP": 141,
            "Atk": 126,
            "Def": 53,
            "SpA": 34,
            "SpD": 43,
            "Spe": 113
        },
        "combat": {
            "Health": 0,
            "Atk": 0,
            "Def": 0,
            "SpA": 0,
            "SpD": 0,
            "Spe": 0,
            "Damage": 0,
            "Status": None,
            "Alive": True,
            "Moveset": [
                {"Move": "Surf", "Type": "Water", "Power": 95, "Accuracy": 100, "PP": 15, "PP_used": 0},
                {"Move": "Ice Beam", "Type": "Ice", "Power": 95, "Accuracy": 100, "PP": 10, "PP_used": 0},
                {"Move": "Mud Shot", "Type": "Ground", "Power": 55, "Accuracy": 95, "PP": 15, "PP_used": 0},
                {"Move": "Earthquake", "Type": "Ground", "Power": 110, "Accuracy": 100, "PP": 10, "PP_used": 0}
                ]
        }
    },
    {
        "name": "Dragonite",
        "type": ["Dragon","Flying"],
        "level": 100,
        "sound": "Dragonite.mp3",
        "base": {
            "HP": 91,
            "Atk": 134,
            "Def": 95,
            "SpA": 100,
            "SpD": 100,
            "Spe": 80
        },
        "iv": {
            "HP": 25,
            "Atk": 31,
            "Def": 7,
            "SpA": 6,
            "SpD": 15,
            "Spe": 15
        },
        "ev": {
            "HP": 146,
            "Atk": 142,
            "Def": 40,
            "SpA": 37,
            "SpD": 31,
            "Spe": 114
        },
        "combat": {
            "Health": 0,
            "Atk": 0,
            "Def": 0,
            "SpA": 0,
            "SpD": 0,
            "Spe": 0,
            "Damage": 0,
            "Status": None,
            "Alive": True,
            "Moveset": [
                {"Move": "Waterfall", "Type": "Water", "Power": 80, "Accuracy": 100, "PP": 15, "PP_used": 0},
                {"Move": "Wing Attack", "Type": "Flying", "Power": 60, "Accuracy": 100, "PP": 35, "PP_used": 0},
                {"Move": "Hyper Beam", "Type": "Normal", "Power": 150, "Accuracy": 90, "PP": 5, "PP_used": 0},
                {"Move": "Dragon Claw", "Type": "Dragon", "Power": 80, "Accuracy": 100, "PP": 15, "PP_used": 0}
                ]
        }
    },
    {
        "name": "Larvitar",
        "type": ["Rock","Ground"],
        "level": 100,
        "sound": "Larvitar.mp3",
        "base": {
            "HP": 50,
            "Atk": 64,
            "Def": 50,
            "SpA": 45,
            "SpD": 50,
            "Spe": 41
        },
        "iv": {
            "HP": 31,
            "Atk": 31,
            "Def": 31,
            "SpA": 31,
            "SpD": 31,
            "Spe": 31
        },
        "ev": {
            "HP": 146,
            "Atk": 142,
            "Def": 40,
            "SpA": 37,
            "SpD": 31,
            "Spe": 114
        },
        "combat": {
            "Health": 0,
            "Atk": 0,
            "Def": 0,
            "SpA": 0,
            "SpD": 0,
            "Spe": 0,
            "Damage": 0,
            "Status": None,
            "Alive": True,
            "Moveset": [
                {"Move": None, "Type": "Water", "Power": 80, "Accuracy": 100, "PP": 15, "PP_used": 0},
                {"Move": None, "Type": "Flying", "Power": 60, "Accuracy": 100, "PP": 35, "PP_used": 0},
                {"Move": None, "Type": "Normal", "Power": 150, "Accuracy": 90, "PP": 5, "PP_used": 0},
                {"Move": None, "Type": "Dragon", "Power": 80, "Accuracy": 100, "PP": 15, "PP_used": 0}
                ]
        }
    },
    {
        "name": "Pupitar",
        "type": ["Rock","Ground"],
        "level": 100,
        "sound": "Pupitar.mp3",
        "base": {
            "HP": 70,
            "Atk": 84,
            "Def": 70,
            "SpA": 65,
            "SpD": 70,
            "Spe": 51
        },
        "iv": {
            "HP": 31,
            "Atk": 31,
            "Def": 31,
            "SpA": 31,
            "SpD": 31,
            "Spe": 31
        },
        "ev": {
            "HP": 146,
            "Atk": 142,
            "Def": 40,
            "SpA": 37,
            "SpD": 31,
            "Spe": 114
        },
        "combat": {
            "Health": 0,
            "Atk": 0,
            "Def": 0,
            "SpA": 0,
            "SpD": 0,
            "Spe": 0,
            "Damage": 0,
            "Status": None,
            "Alive": True,
            "Moveset": [
                {"Move": None, "Type": "Water", "Power": 80, "Accuracy": 100, "PP": 15, "PP_used": 0},
                {"Move": None, "Type": "Flying", "Power": 60, "Accuracy": 100, "PP": 35, "PP_used": 0},
                {"Move": None, "Type": "Normal", "Power": 150, "Accuracy": 90, "PP": 5, "PP_used": 0},
                {"Move": None, "Type": "Dragon", "Power": 80, "Accuracy": 100, "PP": 15, "PP_used": 0}
                ]
        }
    },
    {
        "name": "Tyranitar",
        "type": ["Rock","Dark"],
        "level": 100,
        "sound": "Tyranitar.mp3",
        "base": {
            "HP": 100,
            "Atk": 134,
            "Def": 110,
            "SpA": 95,
            "SpD": 100,
            "Spe": 61
        },
        "iv": {
            "HP": 31,
            "Atk": 31,
            "Def": 31,
            "SpA": 31,
            "SpD": 31,
            "Spe": 31
        },
        "ev": {
            "HP": 146,
            "Atk": 142,
            "Def": 40,
            "SpA": 37,
            "SpD": 31,
            "Spe": 114
        },
        "combat": {
            "Health": 0,
            "Atk": 0,
            "Def": 0,
            "SpA": 0,
            "SpD": 0,
            "Spe": 0,
            "Damage": 0,
            "Status": None,
            "Alive": True,
            "Moveset": [
                {"Move": None, "Type": "Water", "Power": 80, "Accuracy": 100, "PP": 15, "PP_used": 0},
                {"Move": None, "Type": "Flying", "Power": 60, "Accuracy": 100, "PP": 35, "PP_used": 0},
                {"Move": None, "Type": "Normal", "Power": 150, "Accuracy": 90, "PP": 5, "PP_used": 0},
                {"Move": None, "Type": "Dragon", "Power": 80, "Accuracy": 100, "PP": 15, "PP_used": 0}
                ]
        }
    },
    {
        "name": "Charmander",
        "type": ["Fire"],
        "level": 100,
        "sound": "Charmander.mp3",
        "base": {
            "HP": 39,
            "Atk": 52,
            "Def": 43,
            "SpA": 60,
            "SpD": 50,
            "Spe": 65
        },
        "iv": {
            "HP": 31,
            "Atk": 31,
            "Def": 31,
            "SpA": 31,
            "SpD": 31,
            "Spe": 31
        },
        "ev": {
            "HP": 146,
            "Atk": 142,
            "Def": 40,
            "SpA": 37,
            "SpD": 31,
            "Spe": 114
        },
        "combat": {
            "Health": 0,
            "Atk": 0,
            "Def": 0,
            "SpA": 0,
            "SpD": 0,
            "Spe": 0,
            "Damage": 0,
            "Status": None,
            "Alive": True,
            "Moveset": [
                {"Move": None, "Type": "Water", "Power": 80, "Accuracy": 100, "PP": 15, "PP_used": 0},
                {"Move": None, "Type": "Flying", "Power": 60, "Accuracy": 100, "PP": 35, "PP_used": 0},
                {"Move": None, "Type": "Normal", "Power": 150, "Accuracy": 90, "PP": 5, "PP_used": 0},
                {"Move": None, "Type": "Dragon", "Power": 80, "Accuracy": 100, "PP": 15, "PP_used": 0}
                ]
        }
    },
    {
        "name": "Charmeleon",
        "type": ["Fire"],
        "level": 100,
        "sound": "Charmeleon.mp3",
        "base": {
            "HP": 58,
            "Atk": 64,
            "Def": 58,
            "SpA": 80,
            "SpD": 65,
            "Spe": 80
        },
        "iv": {
            "HP": 31,
            "Atk": 31,
            "Def": 31,
            "SpA": 31,
            "SpD": 31,
            "Spe": 31
        },
        "ev": {
            "HP": 146,
            "Atk": 142,
            "Def": 40,
            "SpA": 37,
            "SpD": 31,
            "Spe": 114
        },
        "combat": {
            "Health": 0,
            "Atk": 0,
            "Def": 0,
            "SpA": 0,
            "SpD": 0,
            "Spe": 0,
            "Damage": 0,
            "Status": None,
            "Alive": True,
            "Moveset": [
                {"Move": None, "Type": "Water", "Power": 80, "Accuracy": 100, "PP": 15, "PP_used": 0},
                {"Move": None, "Type": "Flying", "Power": 60, "Accuracy": 100, "PP": 35, "PP_used": 0},
                {"Move": None, "Type": "Normal", "Power": 150, "Accuracy": 90, "PP": 5, "PP_used": 0},
                {"Move": None, "Type": "Dragon", "Power": 80, "Accuracy": 100, "PP": 15, "PP_used": 0}
                ]
        }
    },
    {
        "name": "Charizard",
        "type": ["Fire","Flying"],
        "level": 100,
        "sound": "Charizard.mp3",
        "base": {
            "HP": 78,
            "Atk": 84,
            "Def": 78,
            "SpA": 109,
            "SpD": 85,
            "Spe": 100
        },
        "iv": {
            "HP": 31,
            "Atk": 31,
            "Def": 31,
            "SpA": 31,
            "SpD": 31,
            "Spe": 31
        },
        "ev": {
            "HP": 146,
            "Atk": 142,
            "Def": 40,
            "SpA": 37,
            "SpD": 31,
            "Spe": 114
        },
        "combat": {
            "Health": 0,
            "Atk": 0,
            "Def": 0,
            "SpA": 0,
            "SpD": 0,
            "Spe": 0,
            "Damage": 0,
            "Status": None,
            "Alive": True,
            "Moveset": [
                {"Move": None, "Type": "Water", "Power": 80, "Accuracy": 100, "PP": 15, "PP_used": 0},
                {"Move": None, "Type": "Flying", "Power": 60, "Accuracy": 100, "PP": 35, "PP_used": 0},
                {"Move": None, "Type": "Normal", "Power": 150, "Accuracy": 90, "PP": 5, "PP_used": 0},
                {"Move": None, "Type": "Dragon", "Power": 80, "Accuracy": 100, "PP": 15, "PP_used": 0}
                ]
        }
    }
    ]

worldmap = [
    [{"TYPE": "WALL", "POKES": None}, {"TYPE": "GRASS", "POKES": None}, {"TYPE": "GRASS", "POKES": None}, {"TYPE": "GRASS", "POKES": 1}, {"TYPE": "GRASS", "POKES": None}, {"TYPE": "GRASS", "POKES": None}],
    [{"TYPE": "GRASS", "POKES": None}, {"TYPE": "GRASS", "POKES": None}, {"TYPE": "WALL", "POKES": None}, {"TYPE": "GRASS", "POKES": None}, {"TYPE": "GRASS", "POKES": None}, {"TYPE": "GRASS", "POKES": 1}],
    [{"TYPE": "GRASS", "POKES": 1}, {"TYPE": "WALL", "POKES": None}, {"TYPE": "GRASS", "POKES": None}, {"TYPE": "WALL", "POKES": None}, {"TYPE": "GRASS", "POKES": None}, {"TYPE": "GRASS", "POKES": None}],
    [{"TYPE": "GRASS", "POKES": None}, {"TYPE": "WALL", "POKES": None}, {"TYPE": "GRASS", "POKES": 0}, {"TYPE": "WALL", "POKES": None}, {"TYPE": "WALL", "POKES": None}, {"TYPE": "GRASS", "POKES": None}],
    [{"TYPE": "GRASS", "POKES": None}, {"TYPE": "GRASS", "POKES": None}, {"TYPE": "GRASS", "POKES": None}, {"TYPE": "GRASS", "POKES": None}, {"TYPE": "GRASS", "POKES": 1}, {"TYPE": "GRASS", "POKES": None}],
    [{"TYPE": "WALL", "POKES": None}, {"TYPE": "GRASS", "POKES": None}, {"TYPE": "GRASS", "POKES": None}, {"TYPE": "GRASS", "POKES": None}, {"TYPE": "GRASS", "POKES": None}, {"TYPE": "WALL", "POKES": None}],
]

map2 = [
    [{"TYPE": 1, "POKES": None}, {"TYPE": 1, "POKES": None}, {"TYPE": 0, "POKES": None}, {"TYPE": 0, "POKES": None}, {"TYPE": 1, "POKES": None}, {"TYPE": 1, "POKES": None}],
    [{"TYPE": 1, "POKES": None}, {"TYPE": 1, "POKES": None}, {"TYPE": 1, "POKES": None}, {"TYPE": 1, "POKES": None}, {"TYPE": 1, "POKES": None}, {"TYPE": 1, "POKES": None}],
    [{"TYPE": 1, "POKES": None}, {"TYPE": 0, "POKES": None}, {"TYPE": 0, "POKES": None}, {"TYPE": 0, "POKES": None}, {"TYPE": 0, "POKES": None}, {"TYPE": 1, "POKES": None}],
    [{"TYPE": 1, "POKES": None}, {"TYPE": 0, "POKES": None}, {"TYPE": 0, "POKES": None}, {"TYPE": 0, "POKES": None}, {"TYPE": 0, "POKES": None}, {"TYPE": 1, "POKES": None}],
    [{"TYPE": 1, "POKES": None}, {"TYPE": 0, "POKES": None}, {"TYPE": 0, "POKES": None}, {"TYPE": 0, "POKES": None}, {"TYPE": 0, "POKES": None}, {"TYPE": 1, "POKES": None}],
    [{"TYPE": 1, "POKES": None}, {"TYPE": 1, "POKES": None}, {"TYPE": 0, "POKES": None}, {"TYPE": 0, "POKES": None}, {"TYPE": 1, "POKES": None}, {"TYPE": 1, "POKES": None}],
]

n = 0

party = [pokemons[0]]

def calcStats():
    for i in range(0, len(pokemons)):
        pokemons[i]["combat"]["Health"] = round((((2 * pokemons[i]["base"]["HP"] + pokemons[i]["iv"]["HP"] + (pokemons[i]["ev"]["HP"] / 4)) * pokemons[i]["level"]) / 100) + pokemons[i]["level"] + 10 - 0.5)
        pokemons[i]["combat"]["Atk"] = round((((2 * pokemons[i]["base"]["Atk"] + pokemons[i]["iv"]["Atk"] + (pokemons[i]["ev"]["Atk"] / 4)) * pokemons[i]["level"]) / 100) + 5 - 0.5)
        pokemons[i]["combat"]["Def"] = round((((2 * pokemons[i]["base"]["Def"] + pokemons[i]["iv"]["Def"] + (pokemons[i]["ev"]["Def"] / 4)) * pokemons[i]["level"]) / 100) + 5 - 0.5)
        pokemons[i]["combat"]["SpA"] = round((((2 * pokemons[i]["base"]["SpA"] + pokemons[i]["iv"]["SpA"] + (pokemons[i]["ev"]["SpA"] / 4)) * pokemons[i]["level"]) / 100) + 5 - 0.5)
        pokemons[i]["combat"]["SpD"] = round((((2 * pokemons[i]["base"]["SpD"] + pokemons[i]["iv"]["SpD"] + (pokemons[i]["ev"]["SpD"] / 4)) * pokemons[i]["level"]) / 100) + 5 - 0.5)
        pokemons[i]["combat"]["Spe"] = round((((2 * pokemons[i]["base"]["Spe"] + pokemons[i]["iv"]["Spe"] + (pokemons[i]["ev"]["Spe"] / 4)) * pokemons[i]["level"]) / 100) + 5 - 0.5)
        #print(pokemons[i]["combat"]["Health"],pokemons[i]["combat"]["Atk"],pokemons[i]["combat"]["Def"],pokemons[i]["combat"]["SpA"],pokemons[i]["combat"]["SpD"],pokemons[i]["combat"]["Spe"])
startT = time()
calcStats()
stopT = time()
print("Stats took {0} seconds to calculate".format(stopT-startT))
#print("Movements:", movements)

def placePlayer(map):
    x = randint(0, worldSize-1)
    y = randint(0, worldSize-1)
    while int(worldmap[y][x]["TYPE"]) == 1:
        x = randint(0, worldSize-1)
        y = randint(0, worldSize-1)
    print("POS: {} {}".format(x,y))
    return x,y

def generateWorld():
    """
    Generates world with collidable walls and grass paths\n
    Types:\n
    Grass -> 0\n
    Wall  -> 1\n
    Pokécenter -> 2
    """
    walls = 0
    grass = 0
    #possibility = [None,0,1,None,None,None]
    for i in range(0, worldSize):
        for j in range(0, worldSize):
            worldmap[i][j]["TYPE"] = randint(0, 1)
            #worldmap[i][j]["POKES"] = possibility[randint(0, len(possibility)-1)]
            print(worldmap[i][j]["TYPE"]," ", end='')
            if int(worldmap[i][j]["TYPE"]) == 0:
                grass = grass + 1
            else:
                walls = walls + 1
        print("")
    print("")
    #print(grass, walls)            
    #if walls >= grass:
    #    return generateWorld()

def placeCenter():
    pX = randint(0, 5)
    pY = randint(0, 5)
    worldmap[pY][pX]["TYPE"] = 2
    worldmap[pY][pX]["POKES"] = None
    worldmap[pY + 1][pX]["TYPE"] = 0
    worldmap[pY + 1][pX - 1]["TYPE"] = 0
    worldmap[pY + 1][pX + 1]["TYPE"] = 0
    return pX, pY

def teleportPlayer(mapz,x, y, pokeX, pokeY):
    if (mapz[y][x]["TYPE"] == 2 and x == pokeX and y == pokeY):
        worldmap = map2
        oldX = x
        oldY = y+1
        x = 2
        y = 4
    else:
        pass
    if (mapz == map2 and x == 2 and y == 5):
        worldmap = map1
        x = oldX
        y = oldY

def createMap(mapz):
    block = {"TYPE": "WALL", "POKES": None}  # mapz[0][0]
    for l in range(0, worldSize):
        mapz[0].append(block)
    for o in range(0, worldSize):
        mapz.append(mapz[0])
    return mapz

def placePoke():
    possibility = [None, 0, 1, 7, 6, 6, 6, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, None, None, None, None, None, None, None, None, None]
    for i in range(0, worldSize):
        for j in range(0, worldSize):
            seed = randint(0, len(possibility) - 1)
            worldmap[i][j]["POKES"] = possibility[seed]
    
def generateWorld2():
    """
    Generates world with collidable walls and grass paths\n
    Types:\n
    Grass -> 0\n
    Wall  -> 1
    """
    walls = 0
    grass = 0
    #possibility = [None, 0, 1, None, None]
    for i in range(0, worldSize):
        for j in range(0, worldSize):
            worldmap[i][j]["TYPE"] = randint(0, 1)
            #worldmap[i][j]["POKES"] = possibility[randint(0, len(possibility) - 1)]
            print(worldmap[i][j]["TYPE"], " ", end='')
            if int(worldmap[i][j]["TYPE"]) == 0:
                grass = grass + 1
            else:
                walls = walls + 1
        print("")
    print("")
    #print(grass, walls)
    if walls >= grass:
        return generateWorld()
            
def movCheck(map, x, y):
    mov_options = ["exit","check map"]
    if ((int(worldmap[y + 1][x]["TYPE"]) == 0) and y + 1 <= (worldSize - 1)):
         mov_options.append("down")
    if ((int(worldmap[y - 1][x]["TYPE"]) == 0) and y - 1 >= 0):
         mov_options.append("up")
    if ((int(worldmap[y][x + 1]["TYPE"]) == 0) and x + 1 <= (worldSize - 1)):
         mov_options.append("right")
    if ((int(worldmap[y][x - 1]["TYPE"]) == 0) and x - 1 >= 0):
         mov_options.append("left")
    if ((int(worldmap[y - 1][x + 1]["TYPE"]) == 0) and x + 1 <= (worldSize - 1) and y - 1 >= 0):
         mov_options.append("upright")
    if ((int(worldmap[y - 1][x - 1]["TYPE"]) == 0) and x - 1 >= 0 and y - 1 >= 0):
         mov_options.append("upleft")
    if ((int(worldmap[y + 1][x - 1]["TYPE"]) == 0) and x - 1 >= 0 and y + 1 <= (worldSize - 1)):
         mov_options.append("downleft")
    if ((int(worldmap[y + 1][x + 1]["TYPE"]) == 0) and x + 1 <= (worldSize - 1) and y + 1 <= (worldSize - 1)):
         mov_options.append("downright")            
    return mov_options

def movCheckCenter(mov_options,map, x, y):
    if ((int(worldmap[y + 1][x]["TYPE"]) == 2) and y + 1 <= (worldSize - 1)):
         mov_options.append("down")
    if ((int(worldmap[y + 1][x]["TYPE"]) == 2) and y - 1 >= 0):
         mov_options.append("up")
    if ((int(worldmap[y + 1][x]["TYPE"]) == 2) and x + 1 <= (worldSize - 1)):
         mov_options.append("right")
    if ((int(worldmap[y + 1][x]["TYPE"]) == 2) and x - 1 >= 0):
         mov_options.append("left")
    if ((int(worldmap[y + 1][x]["TYPE"]) == 2) and x + 1 <= (worldSize - 1) and y - 1 >= 0):
         mov_options.append("upright")
    if ((int(worldmap[y + 1][x]["TYPE"]) == 2) and x - 1 >= 0 and y - 1 >= 0):
         mov_options.append("upleft")
    if ((int(worldmap[y + 1][x]["TYPE"]) == 2) and x - 1 >= 0 and y + 1 <= (worldSize - 1)):
         mov_options.append("downleft")
    if ((int(worldmap[y + 1][x]["TYPE"]) == 2) and x + 1 <= (worldSize - 1) and y + 1 <= (worldSize - 1)):
         mov_options.append("downright")

def doMovement(option, mov_options, x, y):
    if (option == "down" and option in mov_options):
        y = y + 1
    if (option == "up" and option in mov_options):
        y = y - 1
    if (option == "left" and option in mov_options):
        x = x - 1
    if (option == "right" and option in mov_options):
        x = x + 1
    if (option == "upright" and option in mov_options):
        x = x + 1
        y = y - 1
    if (option == "upleft" and option in mov_options):
        x = x - 1
        y = y - 1
    if (option == "downleft" and option in mov_options):
        x = x - 1
        y = y + 1
    if (option == "downright" and option in mov_options):
        x = x + 1
        y = y + 1      
    if (option not in mov_options):
        print("Choose a correct movement")
    #print(x, y)
    return x, y

def batCheck(x,y):
    """
    Verifies if there's a Pokémon in the location of the player.\n
    Return True if there is, False if not.
    """
    if worldmap[y][x]["POKES"] == None:
        return False
    else:
        return True

def getWildPoke(x,y):
   return worldmap[y][x]["POKES"]

def damageCalc(poke, move):
    iv = poke["iv"]["SpA"]/100
    min_iv = iv * 0.38
    return round(move + move * random.uniform(min_iv,iv))

def checkMap(maps, x, y, size):
    a = maps.copy()
    a[y][x]["TYPE"] = "X"
    for i in range(0, worldSize):
        for j in range(0, worldSize):
            print(a[i][j]["TYPE"], " ", end='')
        print("")
    a[y][x]["TYPE"] = 0
#worldmap = createMap(worldmap)
generateWorld()
map1 = worldmap
placePoke()
pokeX,pokeY = placeCenter()
#print(worldmap)

x, y = placePlayer(worldmap)

#------------------DEBUG----------------------
def getPokeMap():
    for i in range(0, worldSize):
        for j in range(0, worldSize):
            print(worldmap[i][j]["POKES"], " ", end='')
        print("")

#getPokeMap() 
#---------------------------------------------
music = 1
py.mixer.init()
py.mixer.music.load("Media/Route2.mp3")
py.mixer.music.play(loops=-1)
while alive:
    if music < 1:
        py.mixer.music.load("Media/Route2.mp3")
        py.mixer.music.play(loops=-1)
        music = music + 1
    teleportPlayer(worldmap,x,y,pokeX,pokeY)
    mov_options = movCheck(worldmap, x, y)
    movCheckCenter(mov_options,worldmap, x, y)
    if len(mov_options) == 2:
        print("There's no possible movements.")
        op = input("Would you like to restart?(yes/no):")
        if op == "yes":
            generateWorld()
            x, y = placePlayer(worldmap)
        if op == "no":
            alive = False
            break
    else:        
        print("Possible movements: ", mov_options)
        option = input("Choose: ")
        if (option == "exit"):
            alive = False
            break
        if option == "check map":
            checkMap(worldmap, x, y, worldSize)
        gX, gY = doMovement(option, mov_options, x, y)
        x = gX; y = gY
        check = batCheck(x, y)
        #--------------------COMBAT--------------------
        if check == True and alive:
            run = True
            music = 0
            poke = pokemons[int(getWildPoke(x, y))]
            py.mixer.music.load("Media/Pokemon.mp3")
            py.mixer.music.play()
            sleep(5.3)
            py.mixer.music.pause()
            py.mixer.music.load("Media/" + poke["sound"])
            py.mixer.music.play()
            sleep(2)
            py.mixer.music.load("Media/Pokemon.mp3")
            py.mixer.music.play(loops=4, start=5.3)
            print("A wild {0} appeared".format(poke["name"]))
            while(poke["combat"]["Alive"] == True or run):
                py.mixer.music.queue("Media/Pokemon.mp3")
                print(comb_options)
                opt = input("Choose: ")
                if opt == "attack":
                    print(party[0]["combat"]["Moveset"][0]["Move"])
                    atk = input("Choose an attack: ")
                    if atk == "surf":
                        print(party[0]["name"],"used",party[0]["combat"]["Moveset"][0]["Move"])
                        dmg = damageCalc(party[0], party[0]["combat"]["Moveset"][0]["Power"])
                        poke["combat"]["Health"] = poke["combat"]["Health"] - dmg
                        if poke["combat"]["Health"] < 0:
                            poke["combat"]["Health"] = 0
                            poke["combat"]["Alive"] = False
                            print("You defeated {}".format(poke["name"]))
                            break
                        print("You took {} points".format(dmg))
                        print("{} has {} points remaining".format(poke["name"],poke["combat"]["Health"]))
                if opt == "run":
                    run = False
                    print("Got away safely!")
                    break
        #----------------------------------------------

print("Thanks for playing!")
