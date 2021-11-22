from PokeUtils import *
from PokeUtils.Player import Player
from PokeUtils.PokeDB import PokeDB
#import sqlite3
DB = PokeDB('Poketext')
#print(DB.get_fields("Poketext",['name','level'],[('name','=','Dragonite','OR'),('name','=','Swampert')], json=False))
#print(DB.get_fields("Weather",['name','boost','btype','bamount','weak','wtype','wamount','afterturn','aftamount','type']))
#print(DB.get_fields("Attacks", filter=[('power','>=',100,'AND'),('name','=','Fire Blast')], json=True))
#print(DB.get_fields("DMG_CHART",['Ice','Water'],[('name','=','Fire')], json=True))
#print(DB.get_fields("Nature", json=False))
debug = True
#pk1 = Pokemon(DB.get("Swampert","Poketext", json=True),debug=debug)
#print(pk1.MOVESET)
#pk2 = Pokemon(DB.get("Dragonite","Poketext", json=True),debug=debug)
DB.close_db()

""" p1 = Player("Carlos",[pk1,pk2])
#print(p1.get_party())
pkutils = PokeUtils()
#pkutils.set_weather("Hail")
pkutils.setPokemons(pk1,pk2,debug=False)
pkutils.Attack(3, debug=debug) """
#pkutils.apply_weather()
#print(pkutils.source.name, pkutils.target.name)
#print(pkutils.check_speed())
#pkutils._reverse_sources()
#print(pkutils.source.name, pkutils.target.name)
#pk1.add_status("Poison")
#pkutils.Attack(3)
#pkutils.Attack(3,debug=True)
#pk2.stats.print()
""" n = [
    
]

d = sqlite3.connect("Poketext.db")
cursor = d.cursor()
for a in n:
    cursor.execute("INSERT INTO XXX VALUES (?,?,?,?,?)", a)
d.commit()
d.close() """