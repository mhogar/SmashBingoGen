from random import *
import json
from data import *

def main():
    tiles = []

    for i in range(0, 25):
        tiles.append({ 'name': fighterWins() })
    
    f = open("card.json", "w")
    f.write(json.dumps(tiles, indent=2))
    f.close()


def fighterWins():
    fighter = fighters[randint(0, len(fighters)-1)]
    wins = randint(1, 4)

    return str(wins) + " Win(s) with " + fighter

main()
