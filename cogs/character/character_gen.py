from cogs.utils import ToolUtils as t_utils
from cogs.character.character_tables import stat_mod_dict, char_classes
import random


class Character:

    def __init__(self, stat_roll_type="norm", char_class=None, char_background=None, seed=None):
        self.verbose_log = ""

        # Initial random stats
        self.seed = seed
        self.str = self.rand_stat(stat_roll_type)
        self.dex = self.rand_stat(stat_roll_type)
        self.con = self.rand_stat(stat_roll_type)
        self.int = self.rand_stat(stat_roll_type)
        self.wis = self.rand_stat(stat_roll_type)
        self.cha = self.rand_stat(stat_roll_type)

        self.verbose_log += f"Starting stats - ({self.str}{self.dex}{self.con}{self.int}{self.wis}{self.cha})\n"

        # Generating stat modifiers
        self.update_modifier()

        # Generating character class attribute
        self.char_class = self.gen_class(char_class)

        # Generating character background
        self.char_bg = self.gen_background(char_background)

        # Assigning the Free 14.
        self.free_14()

        #TODO Literally everything below

        # Generate Foci

        # Add Foci Skills

        # Growth and Learning

        # Checking stats after Growth and Learning - To raise via +1 and +2 Physical and Mental

        # Checking Skills for Any Skill, etc

        # Count Foci and Skills (for adding up multiple levels)

        # Calculate Max HP

        # Calculate rolled HP

        # Generate equipment

        #Final cleaning

    def rand_stat(self, arg="norm"):
        if arg == "norm":
            # Roll 3d6 for stats
            num = t_utils.diceroller(3, 6)
            return num
        elif arg == "4d6d1":
            pass
            # TODO Generate stats with drop dice.
            # Rolls 4d6 drop lowest for stats.
        else:
            print(f"Unexpected value in Character.rand_stat() - {arg}")

    def update_modifier(self):
        # We may need to update the modifiers several time throughout the process, therefore it's in its own method
        self.str_mod = stat_mod_dict[self.str]
        self.dex_mod = stat_mod_dict[self.dex]
        self.con_mod = stat_mod_dict[self.con]
        self.int_mod = stat_mod_dict[self.int]
        self.wis_mod = stat_mod_dict[self.wis]
        self.cha_mod = stat_mod_dict[self.cha]

    def gen_class(self, class_arg):
        char_class_list = []
        # Generates the class.
        if class_arg is None:
            char_class = random.choice(char_classes)  # Picks one out of our four classes.
            if char_class == "Adventurer":
                # Character is an adventurer, and needs to rolls two more classes.
                class_list = char_classes[:-1]  # Removing adventurer.
                for i in range(2):
                    choice = random.choice(class_list)
                    class_list.remove(choice)
                    char_class_list.append(choice)
                return char_class_list
            else:  # Character rolled a pure class, which will get put into our class list alone.
                char_class_list.append(char_class)
                return char_class_list
        elif class_arg == ["Warrior"] or class_arg == ["Expert"] or class_arg == ["Psychic"]:
            # Class_arg is a single class in the correct format
            return class_arg
        elif class_arg == ["Adventurer"]:
            # User specified an adventurer, but did not specify another class.
            char_class_list = []
            class_list = char_classes[:-1]  # Removing adventurer.
            for i in range(2):
                choice = random.choice(class_list)
                class_list.remove(choice)
                char_class_list.append(choice)
            return char_class_list
        # TODO User can specify "expert warrior" "psychic warrior" "adventurer psychic" "adventurer expert warrior" - Handle it.
        else:  # Probably have more than one class.
            pass

    def gen_background(self, bg_arg):
        # Generates the class background.
        if bg_arg is None:
            pass
            # TODO Background is none, and therefore will be randomly generated.
        else:
            pass
            # TODO Background is not none, and thus will be specified.

    def free_14(self):
        # Uses the character class and the starting stats to determine where the free 14 should go.
        if min(self.str, self.dex, self.con, self.int, self.wis, self.cha) < 14:
            stat_pool = []
            for i in self.char_class:  # char_class is a list, so we can iterate through it.
                if i == "Warrior":
                    stat_pool.append("str")
                    stat_pool.append("dex")
                elif i == "Expert":
                    stat_pool.append("int")
                    stat_pool.append("cha")
                else:  # Psychic
                    stat_pool.append("wis")
                    stat_pool.append("con")
            free_14 = True
            iter_count = 0
            while free_14 and iter_count < 4:  # This is to assign our free 14 somewhat smartly based on class.
                for a in stat_pool:
                    if a == "str" and self.str < 14:
                        self.verbose_log += f"Free 14 - Raised Strength from {self.str} to 14.\n"
                        self.str = 14
                        free_14 = False
                        break
                    elif a == "dex" and self.dex < 14:
                        self.verbose_log += f"Free 14 - Raised Dexterity from {self.dex} to 14.\n"
                        self.dex = 14
                        free_14 = False
                        break
                    elif a == "con" and self.con < 14:
                        self.verbose_log += f"Free 14 - Raised Constitution from {self.con} to 14.\n"
                        self.con = 14
                        free_14 = False
                        break
                    elif a == "int" and self.int < 14:
                        self.verbose_log += f"Free 14 - Raised Intelligence from {self.int} to 14.\n"
                        self.int = 14
                        free_14 = False
                        break
                    elif a == "wis" and self.wis < 14:
                        self.verbose_log += f"Free 14 - Raised Wisdom from {self.wis} to 14.\n"
                        self.wis = 14
                        free_14 = False
                        break
                    elif a == "cha" and self.cha < 14:
                        self.verbose_log += f"Free 14 - Raised Charisma from {self.cha} to 14.\n"
                        self.cha = 14
                        free_14 = False
                        break
                    else:
                        print(f"{a} must not be lower than 14. Trying again.")
                        iter_count += 1

            if free_14:  # Indicates that we have a stat below 14 and we didn't take care of it in the loop.
                stats = [self.str, self.dex, self.con, self.int, self.wis, self.cha]
                min_stat = min(stats)
                for index, value in enumerate(stats):
                    if value == min_stat:
                        if index == 0:
                            self.verbose_log += f"Free 14 - Raised Strength from {self.str} to 14.\n"
                            self.str = 14
                            break
                        elif index == 1:
                            self.verbose_log += f"Free 14 - Raised Dexterity from {self.dex} to 14.\n"
                            self.dex = 14
                            break
                        elif index == 2:
                            self.verbose_log += f"Free 14 - Raised Constitution from {self.con} to 14.\n"
                            self.con = 14
                            break
                        elif index == 3:
                            self.verbose_log += f"Free 14 - Raised Intelligence from {self.int} to 14.\n"
                            self.int = 14
                            break
                        elif index == 4:
                            self.verbose_log += f"Free 14 - Raised Wisdom from {self.wis} to 14.\n"
                            self.wis = 14
                            break
                        elif index == 5:
                            self.verbose_log += f"Free 14 - Raised Charisma from {self.cha} to 14.\n"
                            self.cha = 14
                            break

        else: # All of the character's stats are 14 or above.
            self.verbose_log += "Free 14 failed - All stats started at or above 14.\n"


    def gen_foci(self):
        pass

    def growth_learning(self):
        pass

    def foci_skills(self):
        pass

    #Check stats
    #Check Skills
    #Skill Counter
    #Foci Count
    #Max HP
    #Rolled HP
    #Equipment Package