from cogs.utils import ToolUtils as t_utils
import cogs.character.character_tables as char_tables
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

        self.verbose_log += f"Starting stats - ({self.str}, {self.dex}, {self.con}, {self.int}, {self.wis}, {self.cha})\n"

        # Generating stat modifiers
        self.update_modifier()

        # Generating character class attribute
        self.char_class = self.gen_class(char_class)

        # Generating character background
        self.char_bg = self.gen_background(char_background)

        # Assigning the Free 14.
        self.free_14()

        # Generate Foci
        self.foci = self.gen_foci()

        # Add Foci Skills
        self.skills = self.foci_skills()

        # Add hobby skill
        if 'Warrior' in self.char_class:
            self.skills.append('Any Combat') # Not strictly necessary, but guarantees a warrior gets a combat skill
        else:
            self.skills.append('Any Skill')

        # Growth and Learning
        self.skills = self.growth_learning()

        # Checking stats after Growth and Learning - To raise via +1 and +2 Physical and Mental
        self.check_stats()
        self.update_modifier()

        # Checking Skills for Any Skill, etc
        self.check_skills()

        # Count Foci and Skills (for adding up multiple levels)

        # Calculate Max HP

        # Calculate rolled HP

        # Generate equipment

        # Final cleaning

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
        self.str_mod = char_tables.stat_mod_dict[self.str]
        self.dex_mod = char_tables.stat_mod_dict[self.dex]
        self.con_mod = char_tables.stat_mod_dict[self.con]
        self.int_mod = char_tables.stat_mod_dict[self.int]
        self.wis_mod = char_tables.stat_mod_dict[self.wis]
        self.cha_mod = char_tables.stat_mod_dict[self.cha]

    def gen_class(self, class_arg):
        char_class_list = []
        # Generates the class.
        if len(class_arg) == 0:  # No classes have been passed. Pick randomly.
            char_class = random.choice(char_tables.char_classes)  # Picks one out of our four classes.
            if char_class == "Adventurer":
                # Character is an adventurer, and needs to rolls two more classes.
                class_list = char_tables.char_classes[:-1]  # Removing adventurer.
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
            class_list = char_tables.char_classes[:-1]  # Removing adventurer.
            for i in range(2):
                choice = random.choice(class_list)
                class_list.remove(choice)
                char_class_list.append(choice)
            return char_class_list
        # TODO User can specify "expert warrior" "psychic warrior" "adventurer psychic" "adventurer expert warrior" - Handle it.
        else:  # Probably have more than one class.
            total_class_list = ['Warrior', 'Expert', 'Psychic']
            class_list = []
            class_arg = sorted(class_arg)
            if class_arg[0] != 'Adventurer':  # Sorted the list alphabetically. First class isn't adventurer. Easy.
                for i in class_arg:
                    class_list.append(i)
            else:  # Adventurer IS the first result. Replace that with whatever is left.
                total_class_list.remove(class_arg[1])  # Second result will be the class they specified.
                class_list.append(class_arg[1])
                class_list.append(random.choice(total_class_list))
            return class_list

    def gen_background(self, bg_arg):
        # Generates the class background.
        if len(bg_arg) == 0:
            return random.choice(list(char_tables.bgtables.keys()))
        else:
            return bg_arg[0]

    def free_14(self):
        # Uses the character class and the starting stats to determine where the free 14 should go.
        # This is entire section is ugly. Try to refactor in the future.
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
                        # print(f"{a} must not be lower than 14. Trying again.")
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
        """Generates foci based on character class."""
        foclist = []
        #First focus everyone gets.
        if 'Psychic' in self.char_class:
            foclist.append(random.choice(char_tables.psyfoci))
        else:
            foclist.append(random.choice(char_tables.nonpsyfoci))

        # Expert gets an extra non-combat, non-psychic focus.
        if 'Expert' in self.char_class:
            noncombat = list(set(char_tables.foci) - set(char_tables.combatfoci))
            foclist.append(random.choice(noncombat))

        # Warrior gets an extra combat focus.
        if 'Warrior' in self.char_class:
            foclist.append(random.choice(char_tables.combatfoci))
        self.verbose_log += f"Raw Foci List - {foclist}\n"
        return foclist

    def foci_skills(self):
        skills = []
        for x in self.foci:
            skills.append(char_tables.FociList[x])
        return skills


    def growth_learning(self):
        skills = self.skills
        skills.append(char_tables.bgtables[self.char_bg][0]) # Initial background skill.
        for i in range(3):  # Three rolls on the tables.
            table = char_tables.bgtables[self.char_bg][random.randint(1, 2)] # Chooses either growth or learning tables
            skills.append(random.choice(table))
        return skills

    def stat_booster(self):
        """Occasionally we need to boost stats. This function picks a stat to prioritize based on class."""
        possibles = []
        if 'Warrior' in self.char_class:
            possibles.append(0)  # Strength
            possibles.append(1)  # Dexterity
        if 'Expert' in self.char_class:
            possibles.append(3)  # Intelligence
            possibles.append(5)  # Charisma
        if 'Psychic' in self.char_class:
            possibles.append(2)  # Constitution
            possibles.append(4)  # Wisdom
        return random.choice(possibles)

    def check_stats(self):
        """Iterates through our list of skills and locates any +1 or +2 stats and applies them."""
        stat_stuff = ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma']
        statblock = [self.str, self.dex, self.con, self.int, self.wis, self.cha]
        priority_1 = [17, 3, 13, 7]  # +1 Stat priority amounts. Out of order on purpose.
        priority_2 = [17, 3, 13, 7, 16, 12, 6]  # +2 Stat priority amounts. Prioritizes giving +1s.
        for i in range(2): #Iterates twice, to fix a bug where it would not apply a +1 if a +2 was the last bonus.
            for skill in self.skills:
                if skill == "+1 Any Stat":
                    if any(x in priority_1 for x in statblock):
                        for i in priority_1: #Iterates in our priority order.
                            if i in statblock:
                                stat = statblock.index(i)
                                self.verbose_log += f"Boosted {stat_stuff[stat]} from {statblock[stat]} to {statblock[stat]+1} via +1 Any Stat\n"
                                statblock[stat] += 1
                                self.skills.remove(skill)
                                break
                    else:  # No stats in range to boost the modifier. Applying to preferred stats by class.
                        stat = self.stat_booster()  # Getting class preference
                        self.verbose_log += f"Boosted {stat_stuff[stat]} from {statblock[stat]} to {statblock[stat] + 1} via +1 Any Stat\n"
                        statblock[stat] += 1
                        self.skills.remove(skill)

                elif skill == '+2 Physical':
                    if any(x in priority_2 for x in statblock[0:3]):
                        for i in priority_2:
                            if i in statblock[0:3]:
                                if i in priority_1:
                                    self.skills.append('+1 Physical')
                                    stat = statblock.index(i)
                                    self.verbose_log += f"Boosted {stat_stuff[stat]} from {statblock[stat]} to {statblock[stat] + 1} via +2 Physical. Only +1 was applied here.\n"
                                    statblock[stat] += 1
                                    self.skills.remove(skill)
                                    break
                                else:
                                    stat = statblock.index(i)
                                    self.verbose_log += f"Boosted {stat_stuff[stat]} from {statblock[stat]} to {statblock[stat] + 2} via +2 Physical.\n"
                                    statblock[stat] += 2
                                    self.skills.remove(skill)
                                    break
                    else:  # No stats in range to boost modifier. Applying to preferred stats by class.
                        stat = self.stat_booster()  # Getting class preference
                        if statblock[stat] != 18: # 16 and 17 are already captured above. Anything else is fair game.
                            self.verbose_log += f"Boosted {stat_stuff[stat]} from {statblock[stat]} to {statblock[stat] + 2} via +2 Physical\n"
                            statblock[stat] += 2
                            self.skills.remove(skill)
                        else: # Selected stat *is* 18.
                            stat = statblock.index(min(statblock[0:3])) #Gets minimum physical score.
                            if statblock[stat] == 18:
                                self.verbose_log += f"Attempted to boost physical stats via +2 physical, but physical stats were all at 18 already.\n"
                                self.skills.remove(skill)
                            elif statblock[stat] == 17:
                                self.verbose_log += f"Attempted to boost physical stats via +2 physical, but lowest physical stat was {stat_stuff[stat]} at 17. \n"
                                self.skills.append("+1 Physical") #In case we have two physical stats at 17. Don't want to waste the point.
                                statblock[stat] += 1
                                self.skills.remove(skill)

                elif skill == '+2 Mental':
                    if any(x in priority_2 for x in statblock[3:6]):
                        for i in priority_2:
                            if i in statblock[3:6]:
                                if i in priority_1:
                                    self.skills.append('+1 Mental')
                                    stat = statblock.index(i)
                                    self.verbose_log += f"Boosted {stat_stuff[stat]} from {statblock[stat]} to {statblock[stat] + 1} via +2 Mental. Only +1 was applied here.\n"
                                    statblock[stat] += 1
                                    self.skills.remove(skill)
                                    break
                                else:
                                    stat = statblock.index(i)
                                    self.verbose_log += f"Boosted {stat_stuff[stat]} from {statblock[stat]} to {statblock[stat] + 2} via +2 Mental.\n"
                                    statblock[stat] += 2
                                    self.skills.remove(skill)
                                    break
                    else:  # No stats in range to boost modifier. Applying to preferred stats by class.
                        stat = self.stat_booster()  # Getting class preference
                        if statblock[stat] != 18:  # 16 and 17 are already captured above. Anything else is fair game.
                            self.verbose_log += f"Boosted {stat_stuff[stat]} from {statblock[stat]} to {statblock[stat] + 2} via +2 Mental\n"
                            statblock[stat] += 2
                            self.skills.remove(skill)
                        else:  # Selected stat *is* 18.
                            stat = statblock.index(min(statblock[3:6]))  # Gets minimum physical score.
                            if statblock[stat] == 18:
                                self.verbose_log += f"Attempted to boost mental stats via +2 Mental, but mental stats were all at 18 already.\n"
                                self.skills.remove(skill)
                            elif statblock[stat] == 17:
                                self.verbose_log += f"Attempted to boost mental stats via +2 Mental, but lowest mental stat was {stat_stuff[stat]} at 17. \n"
                                self.skills.append(
                                    "+1 Physical")  # In case we have two physical stats at 17. Don't want to waste the point.
                                statblock[stat] += 1
                                self.skills.remove(skill)

                elif skill == "+1 Physical":  # Cannot get through growth/skills, Given by a +2 Physical that applied only +1
                    if any(x in priority_1 for x in statblock[0:3]):
                        for i in priority_1:  # Iterates in our priority order.
                            if i in statblock[0:3]:
                                stat = statblock.index(i)
                                self.verbose_log += f"Boosted {stat_stuff[stat]} from {statblock[stat]} to {statblock[stat] + 1} via +1 Physical\n"
                                statblock[stat] += 1
                                self.skills.remove(skill)
                                break
                    else:  # No stats in range to boost the modifier. Applying to preferred stats by class.
                        stat = statblock.index(min(statblock[0:3]))
                        self.verbose_log += f"Boosted {stat_stuff[stat]} from {statblock[stat]} to {statblock[stat] + 1} via +1 Physical\n"
                        statblock[stat] += 1
                        self.skills.remove(skill)
                elif skill == "+1 Mental":  # Cannot get through growth/skills, Given by a +2 Mental that applied only +1
                    if any(x in priority_1 for x in statblock[3:6]):
                        for i in priority_1:  # Iterates in our priority order.
                            if i in statblock[3:6]:
                                stat = statblock.index(i)
                                self.verbose_log += f"Boosted {stat_stuff[stat]} from {statblock[stat]} to {statblock[stat] + 1} via +1 Mental\n"
                                statblock[stat] += 1
                                self.skills.remove(skill)
                                break
                    else:  # No stats in range to boost the modifier. Applying to preferred stats by class.
                        stat = statblock.index(min(statblock[3:6]))
                        self.verbose_log += f"Boosted {stat_stuff[stat]} from {statblock[stat]} to {statblock[stat] + 1} via +1 Mental\n"
                        statblock[stat] += 1
                        self.skills.remove(skill)

        #Apply statblock back to stats.
        self.str = statblock[0]
        self.dex = statblock[1]
        self.con = statblock[2]
        self.int = statblock[3]
        self.wis = statblock[4]
        self.cha = statblock[5]

    def check_skills(self):
        self.verbose_log += f"Raw Skill List before processing - {self.skills}\n"
        skill_list = ['Administer', 'Connect', 'Exert', 'Fix', 'Heal', 'Know', 'Lead', 'Notice', 'Perform', 'Pilot',
                  'Program', 'Punch', 'Shoot', 'Sneak', 'Stab', 'Survive', 'Talk', 'Trade', 'Work']
        for i in range(4):  # Repeating this process multiple times to avoid leakage
            for skill in self.skills:
                if skill == 'Any Combat':
                    combat_skills = ['Punch', 'Stab', 'Shoot']
                    self.skills.remove(skill)
                    new_skill = random.choice(combat_skills)
                    self.skills.append(new_skill)
                    self.verbose_log += f"Any Combat rerolled into {new_skill}\n"
                elif skill == 'Any Skill':
                    new_skill = random.choice(skill_list)
                    self.skills.remove(skill)
                    self.skills.append(new_skill)
                    self.verbose_log += f"Any Skill rerolled into {new_skill}\n"
                elif skill == 'Any Psychic':
                    psy_skills = ['Biopsionics', 'Metapsionics', 'Precognition', 'Telekinesis', 'Telepathy', 'Teleportation']
                    if 'Expert' in self.char_class or 'Warrior' in self.char_class:  # Restricted Psychic
                        if any(x in psy_skills for x in self.skills): #Checks if there is already a psychic skill. That's the one we have to use.
                            for pskill in self.skills:
                                if pskill in psy_skills:
                                    self.skills.remove(skill)
                                    self.skills.append(pskill)
                                    self.verbose_log += f"Partial Psychic forced to improve {pskill} with Any Psychic\n"
                        else: #No existing psychic skills.
                            self.skills.remove(skill)
                            new_skill = random.choice(psy_skills)
                            self.skills.append(new_skill)
                            self.verbose_log += f"Partial Psychic committed to {new_skill} with Any Psychic\n"
                    else: #Not a restricted psychic
                        self.skills.remove(skill)
                        new_skill = random.choice(psy_skills)
                        self.skills.append(new_skill)
                        self.verbose_log += f"Psychic learned {new_skill} with Any Psychic\n"
                elif self.skills.count(skill) > 2: #Excessive amounts of skills. Refunding an Any Skill
                    self.verbose_log += f"{skill} found too many times in the list. Refunding an Any Skill.\n"
                    self.skills.remove(skill)
                    self.skills.append('Any Skill')
                elif skill == '':
                    self.skills.remove(skill)


    def skill_counter(self):
        #Remember to sort after this.
        pass


    #Skill Counter
    #Foci Count
    #Max HP
    #Rolled HP
    #Equipment Package