

class char:
    def __init__(self):
        self.str = 15
        self.dex = 15
        self.con = 14
        self.wis = 15
        self.int = 15
        self.cha = 15

    def raise_stat(self):

        stats = [self.str, self.dex, self.con, self.int, self.wis, self.cha]
        min_stat = min(stats)
        for index, value in enumerate(stats):
            if value == min_stat:
                if index == 0:
                    #self.verbose_log += f"Free 14 - Raised Strength from {self.str} to 14."
                    self.str = 14
                    break
                elif index == 1:
                    #self.verbose_log += f"Free 14 - Raised Dexterity from {self.dex} to 14."
                    self.dex = 14
                    break
                elif index == 2:
                    #self.verbose_log += f"Free 14 - Raised Constitution from {self.con} to 14."
                    self.con = 14
                    break
                elif index == 3:
                    #self.verbose_log += f"Free 14 - Raised Intelligence from {self.int} to 14."
                    self.int = 14
                    break
                elif index == 4:
                    #self.verbose_log += f"Free 14 - Raised Wisdom from {self.wis} to 14."
                    self.wis = 14
                    break
                elif index == 5:
                    #self.verbose_log += f"Free 14 - Raised Charisma from {self.cha} to 14."
                    self.cha = 14
                    break
        print("Prints after for loop")

    def change_stat(self):
        self.cha = 15

newchar = char()

#newchar.raise_stat()

# print(newchar.cha)
# newchar.raise_stat()
# print(newchar.cha)
#
# class_type = None
# list(class_type)
# print(class_type, type(class_type))

listthing = [0, 1, 2, 3, 4, 5]

for i in listthing:
    if i == 2:
        listthing.append(1)
    elif i == 1:
        print("I FOUND A ONE! HOPEFULLY I'LL FIND ANOTHER")
    elif i == 3:
        listthing.remove(i)
print(listthing)

