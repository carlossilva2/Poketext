# **Poketext**
## *A text based Pokémon game inspired by [Zork](https://en.wikipedia.org/wiki/Zork)*
This project is an attempt in creating a text based RPG Game, more especifically Pokémon. It uses 2D Matrices and random number generators to create a map with collidable walls as well as soundtrack based on the original game series.
 
>**Disclaimer:** Game still runs very glitchy, so don't expect for everything to be working at 100%.
# **Available Pokémons In-game**:
* [Charmander](https://bulbapedia.bulbagarden.net/wiki/Charmander_(Pok%C3%A9mon))
    * *Rate: 7/36*
* [Charmeleon](https://bulbapedia.bulbagarden.net/wiki/Charmeleon_(Pok%C3%A9mon))
    * *Rate: 1/12*
* [Charizard](https://bulbapedia.bulbagarden.net/wiki/Charizard_(Pok%C3%A9mon))
    * *Rate: 1/36*
* [Dragonite](https://bulbapedia.bulbagarden.net/wiki/Dragonite_(Pok%C3%A9mon))
    * *Rate: 1/36*
* [Larvitar](https://bulbapedia.bulbagarden.net/wiki/Larvitar_(Pok%C3%A9mon))
    * *Rate: 5/36*
* [Pupitar](https://bulbapedia.bulbagarden.net/wiki/Pupitar_(Pok%C3%A9mon))
    * *Rate: 5/36*
* [Tyranitar](https://bulbapedia.bulbagarden.net/wiki/Tyranitar_(Pok%C3%A9mon))
    * *Rate: 1/12*
* [Swampert](https://bulbapedia.bulbagarden.net/wiki/Swampert_(Pok%C3%A9mon))
    * *Rate: 1/36*

>##### More will be added in due time

# **Map Generation**
>The map in the game is just a 2D Matrix filled with objects
### **Map Syntax**
* `0 = Grass Path`
* `1 = Wall`
* `2 = Pokécenter` 

### **Map Template**
<center>

Row | Row | Row | Row | Row | Row
--- | --- | --- | --- | --- | ---
Object | Object | Object | Object | Object | Object
Object | Object | Object | Object | Object | Object
Object | Object | Object | Object | Object | Object
Object | Object | Object | Object | Object | Object
Object | Object | Object | Object | Object | Object
Object | Object | Object | Object | Object | Object

</center>

### **Map Example**
<center>

Row | Row | Row | Row | Row | Row
--- | --- | --- | --- | --- | ---
1 | 0 | 0 | 0 | 0 | 0
0 | 0 | 1 | 0 | 0 | 0
0 | 1 | 0 | 1 | 0 | 0
0 | 1 | 0 | 1 | 1 | 0
0 | 0 | 0 | 0 | 0 | 0
1 | 0 | 0 | 0 | 0 | 1

</center>

# **Commands**
> Still adding more commands, keep an eye on this page
* Exit
    >Terminates the game
* Check Map
    >Shows Player position in the map, as well as the map generated in the session
* Movements
    * Up
    * Down
    * Left
    * Right
    * *Variants*
        * Upleft
        * Upright
        * Downleft
        * Downright
* Attack
    >Depends on the specific **Pokémon Moveset**
* Run
    >Exits from battle

# Getting Started
>### Install dependencies
```bash
python path/to/file/setup.py install
```
This will garantee you have the necessary dependencies from [PyPi](https://pypi.python.org/pypi) so you won't encounter import errors.


>### Running the game
```bash
python path/to/file/poketext.py
```
At this point we hope there are no bugs, however if you find one please report to us.



# Known Bugs
>**April 4th 2018**
* Damage output very high
>**April 2nd 2018**
* Pokécenter map does not load
* ~~Party Pokémon can only use the first move~~
* Index Out of Bounds errors
* ~~Upon checking map, if there's a Pokémon in the same spot as the player, the battle sequence will begin~~
* Problems generating random size maps *(will stay 6x6 until resolved)*
* Music stops playing after one full music loop
* ~~Wild Pokémons won't attack you~~