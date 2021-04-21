from random import *
import json
from datetime import datetime
from weighted_random import weighted_random
from data import randFighter

def main():
    tiles = []

    for i in range(0, 25):
        name = ""
        tileType = weighted_random([.5, .5])

        if (tileType == 0):
            name = fighterWins()
        elif (tileType == 1):
            name = fighterKills()

        tiles.append({ 'name': name })
    
    f = open("cards/card-" + genTimestamp() + ".json", "w")
    f.write(json.dumps(tiles, indent=2))
    f.close()

def genTimestamp():
    dt = datetime.now()
    formatStr = "{year:04}{month:02}{day:02}{hour:02}{minute:02}{second:02}"
    return formatStr.format(year=dt.year, month=dt.month, day=dt.day, hour=dt.hour, minute=dt.minute, second=dt.second)

def fighterWins():
    wins = randint(1, 4)

    plural = ""
    if wins > 1: plural = "s"

    return f"{wins} Win{plural} with {randFighter()}"

def fighterKills():
    kills = randint(3, 8)

    return f"{kills} Kills with {randFighter()}"

main()
