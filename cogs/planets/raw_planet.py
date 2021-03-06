"""
raw_planet
Generates a planet based on the rules as written with no special weighting.
"""

import random
import cogs.utils.ToolUtils as ut
import cogs.planets.planet_tables as tables


class Raw_Planet():
    """Generates the planet based on the RAW with no special weighting"""

    def __init__(self, num_tags=2):

        self.world_tag_ids = self.world_tags_gen(num_tags)
        self.world_tags = self.world_tag_string()

        self.atmo = self.atmosphere()
        self.temp = self.temperature()
        self.bio = self.biosphere()
        self.pop = self.population()
        self.tl = self.tech_level()

    def world_tags_gen(self, num_tags):
        """
        Generates the world tags indexes to be used by the string later.
        :param num_tags: Specified number of tags to generate. Should be between 1 and 9
        :return: Sorted list of unique world tags
        """
        if 0 < num_tags < 10:
            tags = []
            while len(set(tags)) < num_tags:
                tags.append(random.randint(1, len(tables.PlanetTagTable)))
            return sorted(list(set(tags)))
        raise Exception(f"Raw_Planet.world_tags_gen attempted to generate a strange number of "
                        f"tags: {num_tags}")

    def world_tag_string(self):
        """
        Generates the world tags from the list of indeces in self.world_tag_ids.
        :return: String
        """
        return_string = ""
        for tag in self.world_tag_ids:
            return_string += f"{tables.PlanetTagTable[tag][0]}, "
        return return_string[:-2]

    def atmosphere(self):
        """
        Generates an atmosphere type based on a 2d6 roll. Original table on page XX of SWN:R.
        :return: String
        """
        num = ut.diceroller(2, 6)
        atmotable = {2: "Corrosive",
                     3: "Inert Gas",
                     4: "Airless/Thin",
                     5: "Breathable Mix",
                     6: "Breathable Mix",
                     7: "Breathable Mix",
                     8: "Breathable Mix",
                     9: "Breathable Mix",
                     10: "Thick",
                     11: "Invasive",
                     12: "Corrosive and Invasive"}
        return atmotable[num]

    def temperature(self):
        """
        Generates a temperature string based on a 2d6 roll. Original table on page XX of SWN:R.
        :return: String
        """
        num = ut.diceroller(2, 6)
        temptable = {2: "Frozen",
                     3: "Cold",
                     4: "Variable Cold",
                     5: "Variable Cold",
                     6: "Temperate",
                     7: "Temperate",
                     8: "Temperate",
                     9: "Variable Warm",
                     10: "Variable Warm",
                     11: "Warm",
                     12: "Burning"}
        return temptable[num]

    def biosphere(self):
        """
        Generates a biosphere string based on a 2d6 roll. Original table on page XX of SWN:R.
        :return: String
        """
        num = ut.diceroller(2, 6)
        biotable = {2: "Remnant",
                    3: "Microbial",
                    4: "None",
                    5: "None",
                    6: "Human Miscible",
                    7: "Human Miscible",
                    8: "Human Miscible",
                    9: "Human Immiscible",
                    10: "Human Immiscible",
                    11: "Hybrid Miscible/Immiscible",
                    12: "Engineered"}
        return biotable[num]

    def population(self):
        """
        Generates a population string based on a 2d6 roll. Original table on page XX of SWN:R.
        :return: String
        """
        num = ut.diceroller(2, 6)
        poptable = {2: "Failed Colony",
                    3: "Outpost",
                    4: "Fewer than a million inhabitants",
                    5: "Fewer than a million inhabitants",
                    6: "Several Million Inhabitants",
                    7: "Several Million Inhabitants",
                    8: "Several Million Inhabitants",
                    9: "Hundreds of Millions of Inhabitants",
                    10: "Hundreds of Millions of Inhabitants",
                    11: "Billion of Inhabitants",
                    12: "Alien Inhabitants"}
        return poptable[num]

    def tech_level(self):
        """
        Generates a tech level string based on a 2d6 roll. Original table on page XX of SWN:R.
        :return: String
        """
        num = ut.diceroller(2, 6)
        tltable = {2: "TL0 - Stone Age Tech",
                   3: "TL1 - Medieval Tech",
                   4: "TL2- Early Industrial Age",
                   5: "TL2- Early Industrial Age",
                   6: "TL4 - Modern Postech",
                   7: "TL4 - Modern Postech",
                   8: "TL4 - Modern Postech",
                   9: "TL3 - Present Day Earth Tech",
                   10: "TL3 - Present Day Earth Tech",
                   11: "TL4+ - Postech with Specialties",
                   12: "TL5 - Pretech with Surviving Infrastructure"}
        return tltable[num]
