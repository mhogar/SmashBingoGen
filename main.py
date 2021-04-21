from random import *
import json

characters = [
    "Mario",
    "Donkey Kong",
    "Link",
    "Samus",
    "Dark Samus",
    "Yoshi",
    "Kirby",
    "Fox",
    "Pikachu",
    "Luigi",
    "Ness",
    "Captian Falcon",
    "Jigglypuff"
]

def main():
    tiles = []

    for i in range(0, 25):
        tiles.append({ 'name': characterWins() })
    
    f = open("foo.json", "w")
    f.write(json.dumps(tiles, indent=2))
    f.close()


def characterWins():
    character = characters[randint(0, len(characters)-1)]
    wins = randint(1, 4)

    return str(wins) + " Win(s) with " + character

main()
