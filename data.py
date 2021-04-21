from random import shuffle

class Data:
    def __init__(self):
        self.fighterIndex = -1
        self.fighters = [
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
            "Jigglypuff",
            "Peach",
            "Daisy",
            "Bowser",
            "Ice Climbers",
            "Sheik",
            "Zelda",
            "Dr. Mario",
            "Pichu",
            "Falco",
            "Marth",
            "Lucina",
            "Young Link",
            "Ganondorf",
            "Mewtwo",
            "Roy",
            "Chrom",
            "Mr. Game & Watch",
            "Meta Knight",
            "Pit",
            "Dark Pit",
            "Zero Suit Samus",
            "Wario",
            "Snake",
            "Ike",
            "Pokemon Trainer",
            "Diddy Kong",
            "Lucas",
            "Sonic",
            "King Dedede",
            "Olimar",
            "Lucario",
            "R.O.B",
            "Toon Link",
            "Wolf",
            "Villager",
            "Mega Man",
            "Wii Fit Trainer",
            "Rosalina and Luma",
            "Little Mac",
            "Greninja",
            "Mii Fighter",
            "Palutena",
            "Pac-Man",
            "Robin",
            "Shulk",
            "Bowser Jr.",
            "Duck Hunt",
            "Ryu",
            "Ken",
            "Cloud",
            "Corrin",
            "Bayonetta",
            "Inkling",
            "Ridley",
            "Simon",
            "Richter",
            "King K. Rool",
            "Isabelle",
            "Incineroar",
            "Piranha Plant",
            "Joker",
            "Hero",
            "Banjo-Kazooie",
            "Terry",
            "Byleth",
            "Min Min",
            "Steve",
            "Sephiroth",
            "Pyra/Mythra",
        ]
        shuffle(self.fighters)

        self.uniqueIndex = -1
        self.unique = [
            "Send Someone to Space with Luigi",
            "Knock Someone off of the Edge Whose Holding a Jack-Hammer",
            "Get a Goldeen from a Pokeball",
            "Kill Yourself with Hero's Kamikaze",
            "Get a Kill with the Dragon Parts",
            "Get a Kill with the Daybreak Parts",
            "Use a Fairy Bottle",
            "Launch Someone with the Home-Run Bat",
            "Kill someone with Death's Scythe",
            "Get an Extra Stock with the Special Flag",
        ]
        shuffle(self.unique)
    
    def randFighter(self):
        self.fighterIndex += 1
        if self.fighterIndex > len(self.fighters):
            shuffle(self.fighters)
            self.fighterIndex = 0

        return self.fighters[self.fighterIndex]

    def randUnique(self):
        self.uniqueIndex += 1
        if self.uniqueIndex > len(self.unique):
            shuffle(self.unique)
            self.uniqueIndex = 0

        return self.unique[self.uniqueIndex]
