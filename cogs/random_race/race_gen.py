import random
import cogs.utils.ToolUtils as ut

class Race():
    def __init__(self):

        #Config values
        self.limb_novelty_chance = 0.5
        self.skin_novelty_chance = 0.5
        self.weapon_novelty_chance = 0.5

        self.name = ut.random_namer(2, 4)
        self.base = self.base_gen()
        self.body = self.body_gen()
        self.limb = self.limb_gen()
        self.skin = self.skin_gen()
        self.weapon = self.weapon_gen()
        self.size = self.size_gen()
        self.discharge = self.discharge_gen()
        self.poison = self.poison_gen()
        self.lens = self.lens_gen()
        self.social = self.social_gen()
        self.tl = self.tl_gen()
        self.perk = self.focus_gen()


    def base_gen(self):
        die= ut.diceroller(1, 10, 0)
        features = []
        featuredict = {1:"Amphibian",2:"Bird",3:"Fish",4:"Insect",5:"Mammal",6:"Reptile",7:"Spider",8:"Exotic"}
        if die in [9, 10]: #If 9 or 10, roll twice and combine the results
            for i in range(2):
                die = ut.diceroller(1, 8, 0)
                features.append(featuredict[die])
        else:
            features.append(featuredict[die])
        if len(features) == 1:
            return features[0]
        else:
            return f"Combination of {features[0]} and {features[1]}"

    def body_gen(self):
        die= ut.diceroller(1, 6, 0)
        features = []
        featuredict = {1: "Humanoid", 2: "Quadruped", 3: "Many-legged", 4: "Bulbous", 5: "Amorphous"}
        if die == 6:  # If 6, roll twice and combine the results
            for i in range(2):
                die = ut.diceroller(1, 5, 0)
                features.append(featuredict[die])
        else:
            features.append(featuredict[die])
        if len(features) == 1:
            return features[0]
        else:
            return f"Combination of {features[0]} and {features[1]}"

    def limb_gen(self):
        if random.uniform(0, 1) > self.limb_novelty_chance:
            return None
        else:
            limb_dict = {1: "Wings", 2: "Many Joints", 3: "Tentacles", 4: "Opposable Thumbs", 5: "Retractable", 6:"Varying Sizes"}
            die = ut.diceroller(1, 6, 0)
            return limb_dict[die]

    def skin_gen(self):
        if random.uniform(0, 1) > self.skin_novelty_chance:
            return None
        else:
            skin_dict = {1: "Hard Shell", 2: "Exoskeleton", 3: "Odd Texture", 4: "Molts Regularly", 5: "Harmful to Touch",
                         6: "Wet or Slimy"}
            die = ut.diceroller(1, 6, 0)
            return skin_dict[die]

    def weapon_gen(self):
        if random.uniform(0, 1) > self.weapon_novelty_chance:
            return None
        else:
            weapon_dict = {1: "Teeth or Mandibles", 2: "Claws", 3: "Poison", 4: "Harmful Discharge", 5: "Pincers",
                         6: "Horns"}
            die = ut.diceroller(1, 6, 0)
            return weapon_dict[die]

    def size_gen(self):
        size_dict = {1: "Cat-sized", 2: "Wolf-sized", 3: "Calf-sized", 4: "Bull-sized", 5: "Hippo-sized", 6: "Elephant-sized"}
        die = ut.diceroller(1, 6, 0)
        return size_dict[die]

    def discharge_gen(self):
        if self.weapon != "Harmful Discharge":
            return None
        else:
            die = ut.diceroller(1, 8, 0)
            discharge_dict = {1:"Acidic Spew doing its damage on a hit", 2:"Toxic spittle or cloud", 3:"Super-heated or super-chilled spew", 4:"Sonic drill or other disabling noise",
                              5:"Natural laser or plasma discharge", 6:"Nauseating stench or disabling chemical", 7:"Equipment-melting corrosive", 8:"Explosive pellets or chemical catalysts"}
            return discharge_dict[die]

    def poison_gen(self):
        if self.weapon == "Poison" or str(self.discharge).startswith("T"): #The only discharge to start with T is toxic poison
            poison_type_dict = {1:"Death", 2:"Paralysis", 3:"1d4 dmg per onset interval", 4:"Convulsions", 5:"Blindness", 6:"Hallucinations"}
            poison_onset_dict = {1:"Instant", 2:"1 round", 3:"1d6 rounds", 4:"1 minute", 5:"1d6 minutes", 6:"1 hour"}
            poison_dur_dict = {1:"1d6 rounds", 2:"1 minute", 3:"10 minutes", 4:"1 hour", 5:"1d6 hours", 6:"1d6 days"}
            die1 = ut.diceroller(1, 6, 0)
            die2 = ut.diceroller(1, 6, 0)
            die3 = ut.diceroller(1, 6, 0)
            data = []
            data.append(poison_type_dict[die1])
            data.append(poison_onset_dict[die2])
            data.append(poison_dur_dict[die3])
            return data
        else:
            return None

    def lens_gen(self):
        die1, die2 = ut.diceroller(1, 20, 0), ut.diceroller(1, 20, 0)
        lens_dict = {1:"Collectivity", 2:"Curiosity", 3:"Despair", 4:"Domination", 5:"Faith", 6:"Fear", 7:"Gluttony", 8:"Greed",
                     9:"Hate", 10:"Honor", 11:"Journeying", 12:"Joy", 13:"Pacifism", 14:"Pride", 15:"Sagacity", 16:"Subtlety",
                     17:"Tradition", 18:"Treachery", 19:"Tribalism", 20:"Wrath"}
        return [lens_dict[die1], lens_dict[die2]]

    def social_gen(self):
        die = ut.diceroller(1, 8, 0)
        #print(f'Race Die = {die}')
        social_table = {1:"Democratic", 2:"Monarchic", 3:"Tribal", 4:"Oligarchic"}
        social = []
        if die in [5, 6]: #Multipolar Competitive
            #print('Race rolled Mult-Compet')
            social.append("Multipolar Competitive")
            num = ut.diceroller(1, 3, 0) + 1
            for i in range(num):
                social.append(social_table[ut.diceroller(1, 4, 0)])
        elif die in [7, 8]: #Multipolar Cooperative
            #print('Race rolled Mult-Coop')
            social.append("Multipolar Cooperative")
            num = ut.diceroller(1, 3, 0) + 1
            for i in range(num):
                social.append(social_table[ut.diceroller(1, 4, 0)])
        else:
            social.append(social_table[ut.diceroller(1, 4, 0)])
        return social

    def tl_gen(self):
        # Import from planet gen
        return "TL3"
        #return TLString()

    def focus_gen(self):
        focus_dict = {1:"Aptitude for Violence", 2:"Environmental Native", 3:"Innate Ability", 4:"Natural Defenses",
                      5:"Origin Skill", 6:"Psychic Aptitude", 7:"Shapeshifting", 8:"Strong Attribute", 9:"Tough",
                      10:"Unusual Movement Mode", 11:"Useful Immunity"}
        foci = []
        for i in range(2):
            die = ut.diceroller(1, len(focus_dict), 0)
            foci.append(focus_dict[die])
        return foci