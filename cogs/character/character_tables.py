

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