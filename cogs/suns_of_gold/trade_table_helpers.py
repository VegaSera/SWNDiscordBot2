import random

def gen_tags():
    tags = []

    max_num_tags = random.randint(2, 4)

    while len(tags) < max_num_tags:
        choice = random.choice(list(modifier_table.keys()))
        if choice in tags:
            continue
        elif choice in ['Bulky', 'Compact']:
            if 'Bulky' in tags or 'Compact' in tags:
                continue
            tags.append(choice)
        elif choice in ['Common', 'Rare']:
            if 'Common' in tags or 'Rare' in tags:
                continue
            tags.append(choice)
        elif choice in ['Low Tech', 'Postech', 'Pretech', 'Maltech']:
            if 'Low Tech' in tags or 'Postech' in tags or 'Pretech' in tags or 'Maltech' in tags:
                continue
            tags.append(choice)
        else:
            tags.append(choice)

    return tags


price_table = {
    -6:50,
    -5:100,
    -4:250,
    -3:500,
    -2:1000,
    -1:2000,
    0:5000,
    1:10000,
    2:25000,
    3:50000,
    4:100000,
    5:200000,
    6:400000,
    7:800000,
    8:1600000
}


tl0_goods = {
    'Clothing':['Common', 'Low Tech', 'Cultural'],
    'Drugs, Raw Materials':['Agricultural', 'Biotech', 'Bulky'],
    'Exotic Jewels':['Rare', 'Mineral', 'Luxury', 'Compact'],
    'Fine Liquor':['Luxury', 'Low Tech', 'Compact'],
    'Livestock, Common':['Common', 'Livestock'],
    'Livestock, Gengineered':['Biotech', 'Livestock'],
    'Livestock, Luxury Pets':['Luxury', 'Livestock'],
    'Metawheat':['Common','Agricultural','Bulky'],
    'Native Artwork':['Cultural', 'Luxury'],
    'Pretech Junk, Salvaged':['Pretech'],
    'Slaves':['Sentient'],
    'Randomized Cargo':gen_tags,
    'Randomized Cargo ':gen_tags,
    'Randomized Cargo  ':gen_tags,
}

tl1_goods = {
    'Housewares, Basic':['Low Tech', 'Consumer'],
    'Metal Ingots, Common':['Common', 'Mineral', 'Bulky'],
    'Tools, Basic Hand Tools':['Low Tech', 'Tool'],
    **tl0_goods
}

tl2_goods = {
    'Parts, Basic Industry':['Low Tech', 'Tool'],
    'Postech Building Material':['Tool', 'Postech', 'Bulky'],
    **tl1_goods
}

tl3_goods = {
    'Drugs, Recreational':['Luxury', 'Biotech', 'Compact'],
    'Metal Ingots, Rare Alloys':['Mineral', 'Bulky', 'Rare'],
    'Small Arms, Projectile':['Military', 'Low Tech'],
    **tl2_goods
}

tl4_goods = {
    'Colonial Materials':['Survival', 'Postech', 'Common'],
    'Colonial Supplies':['Agricultural', 'Survival'],
    'Fusion Plants':['Postech', 'Tool', 'Bulky'],
    'Housewares, Postech':['Consumer', 'Postech'],
    'Medical Supplies, Postech':['Medical', 'Postech', 'Compact'],
    'Parts, Pretech Industry':['Pretech', 'Tool'],
    'Parts, Starship Maintenance':['Postech', 'Astronautic', 'Rare'],
    'Small Arms, Energy':['Military', 'Postech'],
    'Tools, Astronautic':['Tool', 'Postech', 'Astronautic'],
    'Tools, Industrial':['Tool', 'Postech'],
    'Tools, Medical Equipment':['Tool', 'Postech', 'Medical'],
    **tl3_goods
}

tl5_goods = {
    'Ghoul Immortality Tech':['Medical', 'Maltech', 'Compact'],
    'Housewares, Pretech':['Consumer', 'Pretech'],
    'Medical Supplies, Pretech':['Medical', 'Pretech', 'Compact'],
    'Pretech Junk, Manufactured':['Pretech'],
    'Small Arms, Pretech':['Military', 'Pretech'],
    **tl4_goods
}

modifier_table = {
    'Agricultural':-2,
    'Alien':2,
    'Astronautic':1,
    'Biotech':1,
    'Consumer':0,
    'Cultural':0,
    'Livestock':0,
    'Low Tech':-1,
    'Luxury':2,
    'Maltech':4,
    'Medical':2,
    'Military':1,
    'Mineral':-1,
    'Postech':0,
    'Pretech':3,
    'Religious':0,
    'Sentient':2,
    'Survival':0,
    'Tool':1,
    'Vehicle':1,
    'Compact':0,
    'Bulky':0,
    'Common':-1,
    "Rare":1
}

troubles = [
    '1d4 x 10% of the goods are stolen/ruined/lost',
    'Add 1 friction to this deal, and stuck for 1 week',
    'Add 2 friction to this deal',
    'Add 1d4 friction to this deal',
    'Stuck 1d4 weeks before deal is complete',
    'Stuck for 1d6+1 weeks before the deal is complete',
    'Stuck for 2 weeks before deal is complete',
    'Half of the goods are taken by someone in power',
    '1d6 x 10% of the goods are stolen/ruined/lost',
    'Add 1d6 friction to this deal'
]