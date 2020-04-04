

#Dictionary to translate Stats to their corresponding modifier
stat_mod_dict = {3:-2, 4:-1, 5:-1, 6:-1, 7:-1, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0, 14:1, 15:1, 16:1, 17:1, 18:2}

char_classes = ["Warrior", "Expert", "Psychic", "Adventurer"]

bgtables = {'Barbarian': ('Survive', ('+1 Any Stat', '+2 Physical', '+2 Physical', '+2 Mental', 'Exert', 'Any Skill'),
                          ('Any Combat', 'Connect', 'Exert', 'Lead', 'Notice', 'Punch', 'Sneak', 'Survive')),
            'Clergy': ('Talk', ('+1 Any Stat', '+2 Mental', '+2 Physical', '+2 Mental', 'Connect', 'Any Skill'),
                       ('Administer', 'Connect', 'Know', 'Lead', 'Notice', 'Perform', 'Talk', 'Talk')),
            'Courtesan': ('Perform', ('+1 Any Stat', '+2 Mental', '+2 Mental', '+2 Physical', 'Connect', 'Any Skill'),
                          ('Any Combat', 'Connect', 'Exert', 'Notice', 'Perform', 'Survive', 'Talk', 'Trade')),
            'Criminal': ('Sneak', ('+1 Any Stat', '+2 Mental', '+2 Physical', '+2 Mental', 'Connect', 'Any Skill'),
                         ('Administer', 'Any Combat', 'Connect', 'Notice', 'Program', 'Sneak', 'Talk', 'Trade')),
            'Dilettante': (
            'Connect', ('+1 Any Stat', '+1 Any Stat', '+1 Any Stat', '+1 Any Stat', 'Connect', 'Any Skill'),
            ('Any Skill', 'Any Skill', 'Connect', 'Know', 'Perform', 'Pilot', 'Talk', 'Trade')),
            'Entertainer': ('Perform', ('+1 Any Stat', '+2 Mental', '+2 Mental', '+2 Physical', 'Connect', 'Any Skill'),
                            ('Any Combat', 'Connect', 'Exert', 'Notice', 'Perform', 'Perform', 'Sneak', 'Talk')),
            'Merchant': ('Trade', ('+1 Any Stat', '+2 Mental', '+2 Mental', '+2 Mental', 'Connect', 'Any Skill'),
                         ('Administer', 'Any Combat', 'Connect', 'Fix', 'Know', 'Notice', 'Trade', 'Talk')),
            'Noble': ('Lead', ('+1 Any Stat', '+2 Mental', '+2 Mental', '+2 Mental', 'Connect', 'Any Skill'),
                      ('Administer', 'Any Combat', 'Connect', 'Know', 'Lead', 'Notice', 'Pilot', 'Talk')),
            'Official': ('Administer', ('+1 Any Stat', '+2 Mental', '+2 Mental', '+2 Mental', 'Connect', 'Any Skill'),
                         ('Administer', 'Any Skill', 'Connect', 'Know', 'Lead', 'Notice', 'Talk', 'Trade')),
            'Peasant': ('Exert', ('+1 Any Stat', '+2 Physical', '+2 Physical', '+2 Physical', 'Exert', 'Any Skill'),
                        ('Connect', 'Exert', 'Fix', 'Notice', 'Sneak', 'Survive', 'Trade', 'Work')),
            'Physician': ('Heal', ('+1 Any Stat', '+2 Physical', '+2 Mental', '+2 Mental', 'Connect', 'Any Skill'),
                          ('Administer', 'Connect', 'Fix', 'Heal', 'Know', 'Notice', 'Talk', 'Trade')),
            'Pilot': ('Pilot', ('+1 Any Stat', '+2 Physical', '+2 Physical', '+2 Mental', 'Connect', 'Any Skill'),
                      ('Connect', 'Exert', 'Fix', 'Notice', 'Pilot', 'Pilot', 'Shoot', 'Trade')),
            'Politician': ('Talk', ('+1 Any Stat', '+2 Mental', '+2 Mental', '+2 Mental', 'Connect', 'Any Skill'),
                           ('Administer', 'Connect', 'Connect', 'Lead', 'Notice', 'Perform', 'Talk', 'Talk')),
            'Scholar': ('Know', ('+1 Any Stat', '+2 Mental', '+2 Mental', '+2 Mental', 'Connect', 'Any Skill'),
                        ('Administer', 'Connect', 'Fix', 'Know', 'Notice', 'Perform', 'Program', 'Talk')),
            'Soldier': (
            'Any Combat', ('+1 Any Stat', '+2 Physical', '+2 Physical', '+2 Physical', 'Exert', 'Any Skill'),
            ('Administer', 'Any Combat', 'Exert', 'Fix', 'Lead', 'Notice', 'Sneak', 'Survive')),
            'Spacer': ('Fix', ('+1 Any Stat', '+2 Physical', '+2 Physical', '+2 Mental', 'Exert', 'Any Skill'),
                       ('Administer', 'Connect', 'Exert', 'Fix', 'Know', 'Pilot', 'Program', 'Talk')),
            'Technician': ('Fix', ('+1 Any Stat', '+2 Physical', '+2 Mental', '+2 Mental', 'Connect', 'Any Skill'),
                           ('Administer', 'Connect', 'Exert', 'Fix', 'Fix', 'Know', 'Notice', 'Pilot')),
            'Thug': ('Any Combat', ('+1 Any Stat', '+2 Mental', '+2 Physical', '+2 Physical', 'Connect', 'Any Skill'),
                     ('Any Combat', 'Connect', 'Exert', 'Notice', 'Sneak', 'Stab', 'Shoot', 'Survive', 'Talk')),
            'Vagabond': ('Survive', ('+1 Any Stat', '+2 Physical', '+2 Physical', '+2 Mental', 'Exert', 'Any Skill'),
                         ('Any Combat', 'Connect', 'Notice', 'Perform', 'Pilot', 'Sneak', 'Survive', 'Work')),
            'Worker': ('Work', ('+1 Any Stat', '+1 Any Stat', '+1 Any Stat', '+1 Any Stat', 'Exert', 'Any Skill'),
                       ('Administer', 'Any Skill', 'Connect', 'Exert', 'Fix', 'Pilot', 'Program', 'Work'))
            }

foci = ['Alert', 'Armsman', 'Assassin', 'Authority', 'Close Combatant', 'Connected', 'Die Hard', 'Diplomat',
           'Gunslinger', 'Hacker', 'Healer', 'Henchkeeper', 'Ironhide', 'Savage Fray', 'Shocking Assault', 'Sniper',
           'Specialist', 'Star Captain', 'Starfarer', 'Tinker', 'Unarmed Combatant', 'Wanderer']

psyfoci = ['Alert', 'Armsman', 'Assassin', 'Authority', 'Close Combatant', 'Connected', 'Die Hard', 'Diplomat',
           'Gunslinger', 'Hacker', 'Healer', 'Henchkeeper', 'Ironhide', 'Savage Fray', 'Shocking Assault', 'Sniper',
           'Specialist', 'Star Captain', 'Starfarer', 'Tinker', 'Unarmed Combatant', 'Wanderer', 'Psychic Training']

nonpsyfoci = ['Alert', 'Armsman', 'Assassin', 'Authority', 'Close Combatant', 'Connected', 'Die Hard', 'Diplomat',
           'Gunslinger', 'Hacker', 'Healer', 'Henchkeeper', 'Ironhide', 'Savage Fray', 'Shocking Assault', 'Sniper',
           'Specialist', 'Star Captain', 'Starfarer', 'Tinker', 'Unarmed Combatant', 'Wanderer', 'Wild Psychic Talent']

allfoci = ['Alert', 'Armsman', 'Assassin', 'Authority', 'Close Combatant', 'Connected', 'Die Hard', 'Diplomat',
           'Gunslinger', 'Hacker', 'Healer', 'Henchkeeper', 'Ironhide', 'Savage Fray', 'Shocking Assault', 'Sniper',
           'Specialist', 'Star Captain', 'Starfarer', 'Tinker', 'Unarmed Combatant', 'Wanderer', 'Psychic Training',
              'Wild Psychic Talent', 'Unique Gift']

combatfoci = ['Armsman', 'Assassin', 'Close Combatant', 'Die Hard', 'Gunslinger', 'Savage Fray', 'Shocking Assault', 'Sniper',
               'Unarmed Combatant']

FociList = {'Alert': 'Notice',
            'Armsman': 'Stab',
            'Assassin': 'Sneak',
            'Authority': 'Lead',
            'Close Combatant': 'Any Combat',
            'Connected': 'Connect',
            'Die Hard': '',
            'Diplomat': 'Talk',
            'Gunslinger': 'Shoot',
            'Hacker': 'Program',
            'Healer': 'Heal',
            'Henchkeeper': 'Lead',
            'Ironhide': '',
            'Savage Fray': 'Stab',
            'Shocking Assault': 'Stab',
            'Sniper': 'Shoot',
            'Specialist': 'Any Skill',
            'Star Captain': 'Lead',
            'Starfarer': 'Pilot',
            'Tinker': 'Fix',
            'Unarmed Combatant': 'Punch',
            'Wanderer': 'Survive',
            'Psychic Training': 'Any Psychic',
            'Wild Psychic Talent': ''}

skillTable = ['Administer', 'Connect', 'Exert', 'Fix', 'Heal', 'Know', 'Lead', 'Notice', 'Perform', 'Pilot',
                  'Program', 'Punch', 'Shoot', 'Sneak', 'Stab', 'Survive', 'Talk', 'Trade', 'Work']

equipmentPackages = {'Barbarian':"Spear(1d6+1 damage), Primitive Hide Armor(AC 13), Primitive Shield(+1 AC),"
                                 " Knife(1d4 damage), Backpack TL0, 7 days rations, 20m Rope, 500 credits",
                     'Blade':"Monoblade Sword(1d8+1 damage), Woven Body Armor(AC 15), Secure Clothing(AC 13),"
                              " Thermal Knife(1d6 damage), Backpack TL0, Compad, Lazarus Patch, 50 Credits",
                     'Thief':"Laser Pistol(1d6 damage), Armored Undersuit(AC 13), Monoblade Knife(1d6 damage)," 
                              " Climbing Harness, Low Light Goggles, 2 Type-A Cells, Backpack TL0",
                     'Hacker':"Laser Pistol(1d6 damage), Secure Clothing(AC 13), Postech Tool Kit,"
                              " 3 units of spare parts, 2 Type-A Cells, Dataslab, Metatool, 2 Line Shunts, 100 Credits",
                     'Gunslinger':"Laser Pistol(1d6 damage), Armored Undersuit(AC 13), Monoblade Knife(1d6 damage),"
                                  " 8 Type-A Cells, Backpack TL0, Compad, 100 Credits",
                     'Soldier':"Combat Rifle(1d12 damage), Woven Body Armor(AC 15), Knife(1d4 damage),"
                               " 80 rounds Ammo, Backpack TL0, Compad, 100 Credits",
                     'Scout':"Laser Rifle(1d10 damage), Armored Vacc Suit(AC 13), Knife(1d4 damage), Survey Scanner, "
                             " Survival Kit, Binoculars TL3, 8 Type-A Cells, Backpack TL0, Compad, 25 Credits",
                     'Medic':"Laser Pistol(1d6 damage), Secure Clothing(AC 13), 4 Lazarus Patches, 2 doses of Lift, "
                             " Backpack TL0, Medkit, Compad, Bioscanner, 25 Credits",
                     'Civilian':"Secure Clothing(AC 13), Compad, 700 Credits",
                     'Technician':"Laser Pistol(1d6 damage), Armored Undersuit(AC 13), Monoblade Knife(1d6 damage) "
                                  " Postech Toolkit, 6 units of spare parts, 4 Type-A Cells, Backpack TL0, Dataslab,"
                                  " Metatool, 200 Credits"}