from cogs.suns_of_gold.trade_table_helpers import *
import random


class Good():
    def __init__(self, name, tags):
        self.name = name
        self.tags = tags
        self.price = get_price(self.tags)

class TradePlanet():
    def __init__(self, tl):
        self.tl = tl
        self.goods = self.generate_goods()
        self.trouble_chance = random.randint(1, 4)
        self.troubles = [random.choice(troubles) for i in range(6)]
        self.ptags = self.generate_ptags()

    def generate_goods(self):
        tables = {
            0: tl0_goods,
            1: tl1_goods,
            2: tl2_goods,
            3: tl3_goods,
            4: tl4_goods,
            5: tl5_goods
        }
        tech_table = tables[self.tl]
        goods = []
        random_counter = 1
        while len(goods) < 10:
            choice = random.choice(list(tech_table.keys()))
            if choice.strip() != 'Random Cargo':
                for good in goods:
                    if good.name == choice:
                        continue
                else:
                    goods.append(Good(choice, tech_table[choice]))
            else:
                goods.append(Good(f'Random Cargo {random_counter}', tech_table['Random Cargo']()))
                random_counter += 1

        return goods

    def generate_ptags(self):
        tags = []
        vals = [-2, -1, "+1", "+2"]
        while len(tags) < 4:
            choice = random.choice(list(modifier_table.keys()))
            if choice in ['Bulky', 'Compact', 'Common', 'Rare'] or choice in tags:
                continue
            else:
                tags.append(choice)
        ret_string = ""
        for i, v in enumerate(tags):
            ret_string += f" {vals[i]} {v}\n"
        return ret_string




def get_price(tags, start_mod=0):
    "Uses the tags of the good to generate a price via the price table."
    total_mod = start_mod
    for tag in tags:
        total_mod += modifier_table[tag]
    return price_table[total_mod]
