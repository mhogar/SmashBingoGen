from random import *
import json
from datetime import datetime
from weighted_random import weighted_random
from data import Data

data = Data()

def main():
    tiles = []

    for i in range(0, 25):
        tiles.append({ 'name': genTile() })
    
    f = open("cards/card-" + genTimestamp() + ".json", "w")
    f.write(json.dumps(tiles, indent=2))
    f.close()

def genTimestamp():
    dt = datetime.now()
    formatStr = "{year:04}{month:02}{day:02}{hour:02}{minute:02}{second:02}"
    return formatStr.format(year=dt.year, month=dt.month, day=dt.day, hour=dt.hour, minute=dt.minute, second=dt.second)

def genTile():
    tileType = weighted_random([.05, .38, .38, .19])

    if (tileType == 0):
        return data.randUnique()
    elif (tileType == 1):
        return fighterKills()
    elif (tileType == 2):
        return fighterWins()
    elif (tileType == 3):
        return figherFinalSmash()

def fighterWins():
    wins = randint(1, 3)

    plural = ""
    if wins > 1: plural = "s"

    return f"{wins} Win{plural} with {data.randFighter()}"

def fighterKills():
    kills = randint(3, 8)

    return f"{kills} Kills with {data.randFighter()}"

def figherFinalSmash():
    kills = wins = randint(1, 2)

    plural = ""
    if kills > 1: plural = "s"

    return f"{kills} Kill{plural} with {data.randFighter()}'s Final Smash"

main()
