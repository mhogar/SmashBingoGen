from random import *
import json
from datetime import datetime
from data import randFighter

def main():
    tiles = []

    for i in range(0, 25):
        tiles.append({ 'name': fighterWins() })
    
    f = open("card-" + genTimestamp() + ".json", "w")
    f.write(json.dumps(tiles, indent=2))
    f.close()

def genTimestamp():
    dt = datetime.now()
    formatStr = "{year:04}{month:02}{day:02}{hour:02}{minute:02}{second:02}"
    return formatStr.format(year=dt.year, month=dt.month, day=dt.day, hour=dt.hour, minute=dt.minute, second=dt.second)

def fighterWins():
    wins = randint(1, 4)
    return str(wins) + " Win(s) with " + randFighter()

main()
