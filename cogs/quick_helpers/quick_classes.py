import cogs.utils.namer as namer
import random


class NPC():
    def __init__(self, gender):
        self.name = namer.random_name(gender=gender)
        self.age = self.get_age()
        self.background = self.get_background()
        self.role = self.get_role()
        self.problem = self.get_problem()
        self.desire = self.get_desire()
        self.trait = self.get_trait()

    def get_age(self):
        age_table = ['Unusually young or old for their role', 'Young Adult', 'Mature Prime', 'Middle-Aged or Elderly']
        return random.choice(age_table)

    def get_background(self):
        bg_table = ['The local underclass or poorest natives', 'Common laborers or cube workers',
                    'Aspiring bourgeoise or upper class', 'The elite of this society', 'Minority or foreigners',
                    'Offworlders or exotics']
        return random.choice(bg_table)

    def get_role(self):
        role_table = ['Criminal, Thug, Thief, Swindler', 'Menial, cleaner, retail worker, servant',
                      'Unskilled heavy labor, porter, construction', 'Skilled trade, electrician, mechanic, pilot',
                      'Idea worker, programmer, writer', 'Merchant, business owner, trader, banker',
                      'Official, bureaucrat, courtier, clerk', 'Military, soldier, enforcer, law officer']
        return random.choice(role_table)

    def get_problem(self):
        prob_table = ['They have a significant debt or money woes', 'A loved one is in trouble',
                      'Romantic failure with desired person', 'Drug or behavioral addiction',
                      'Their superior dislikes or resents them', 'They have a persistent sickness',
                      'They hate their job or life situation', 'Someone dangerous is targeting them',
                      'They\'re pursuing a dangerous purpose', 'They have no problems worth mentioning']
        return random.choice(prob_table)

    def get_desire(self):
        desire_table = ['They want a particular romantic partner', 'They want money for them or a loved one',
                        'They want a promotion in their job',
                        'They want answers about a past trauma', 'They want revenge on an enemy',
                        'They want to help a beleaguered friend',
                        'They want an entirely different job', 'They want protection from an enemy',
                        'They want to leave their current life',
                        'They want fame and glory', 'They want power over those around them',
                        'They have everything they want from life']
        return random.choice(desire_table)

    def get_trait(self):
        trait_table = ['Ambition', 'Avarice', 'Bitterness', 'Courage', 'Cowardice', 'Curiosity', 'Deceitfulness',
                       'Determination', 'Devotion to a cause',
                       'Filiality', 'Hatred', 'Honesty', 'Hopefulness', 'Love of a person', 'Nihilism', 'Paternalism',
                       'Pessimism', 'Protectiveness',
                       'Resentment', 'Shame']
        return random.choice(trait_table)


class Patron():
    def __init__(self, gender):
        self.name = namer.random_name(gender=gender)
        self.eagerness = self.get_eager()
        self.trust = self.get_trust()
        self.challenge = self.get_challenge()
        self.counter = self.get_counter()
        self.reward = self.get_reward()
        self.complication = self.get_complication()

    def get_eager(self):
        PATD4 = ["Cautious, but can be convinced to hire", "Willing to promise standard rates",
                 "Eager, willing to offer a bonus", "Desperate, might offer what they can't pay"]
        return random.choice(PATD4)

    def get_trust(self):
        PATD6 = ["They intend to totally screw the PCs", "They wont pay unless forced to",
                 "They'll pay slowly or reluctantly", "They'll pay, but discount for mistakes",
                 "They'll pay without quibbling", "They'll pay more than they promised"]
        return random.choice(PATD6)

    def get_challenge(self):
        PATD8 = ["Kill someone who might deserve it", "Kidnap someone dangerous", "Steal a well-guarded object",
                 "Arson or sabotage on a place", "Get proof of some misdeed",
                 "Protect someone from an immediate threat",
                 "Transport someone through danger", "Guard an object being transported"]
        return random.choice(PATD8)

    def get_counter(self):
        PATD10 = ["A treacherous employer or subordinate", "An open and known enemy of the patron",
                  "Official governmental meddling", "An unknown rival of the patron",
                  "The macguffin itself opposes them", "Very short timeframe allowed",
                  "This job is spectacularly illegal", "A participant would profit by their failure",
                  "The patron is badly wrong about a thing", "The locals are against the patron"]
        return random.choice(PATD10)

    def get_reward(self):
        PATD12 = ["Government official favors owed", "Property in the area", "An item very valuable on another world",
                  "Pretech mod components", "Useful pretech artifact", "Information the PCs need",
                  "Membership in a powerful group", "Black market access", "Use of restricted facilities or shipyards",
                  "Shares in a profitable business", "Maps to a hidden or guarded treasure",
                  "Illegal but valuable weapons or gear"]
        return random.choice(PATD12)

    def get_complication(self):
        PATD20 = ["An ambush is laid somewhere", "PC involvement is leaked to the enemy",
                  "The patron gives faulty aid somehow", "Failing would be extremely unhealthy",
                  "The job IDs them as allies of a local faction", "The macguffin is physically dangerous",
                  "An important location is hard to get into", "Succeeding would be morally distasteful",
                  "A supposed ally is very unhelpful or stupid",
                  "The patron badly misunderstood the PCs", "The job changes suddenly partway through",
                  "An unexpected troublemaker is involved", "Critical gear will fail partway through",
                  "An unrelated accident complicates things", "Payment comes in a hard to handle form",
                  "Someone is turning traitor on the patron", "A critical element has suddenly moved",
                  "Payment is in avidly pursued hot goods", "The true goal is a subsidiary part of the job",
                  "No complications, it's just as it seems to be"]
        return random.choice(PATD20)

class Urban():
    def __init__(self):
        self.conflict = self.get_conflict()
        self.venue = self.get_venue()
        self.pc_involve = self.get_pc_involvement()
        self.nature = self.get_nature()
        self.antag_involve = self.get_antag_involve()
        self.features = self.get_features()

    def get_conflict(self):
        UENCD4 = ['Money, Extortion, Payment due, Debts', 'Respect, Submission to social authority',
                  'Grudges, Ethnic resentment, gang payback', 'Politics, Religion, or other ideology']
        return random.choice(UENCD4)

    def get_venue(self):
        UENCD6 = ['In the middle of the street', 'In a public plaza', "Down a side alley", "Inside a local business",
                  'Next to or in a public park', "At a mass transit station"]
        return random.choice(UENCD6)

    def get_pc_involvement(self):
        UENCD8 = ['A sympathetic participant appeals to them', "Ways around it are all dangerous/blocked",
                  "It happens immediately around them",
                  "A valuable thing looks snatchable amid it", "A participant offers a reward for help",
                  "Someone mistakenly involves the PCs in it",
                  "The seeming way out just leads deeper in", "Responsibility is somehow pinned on them"]
        return random.choice(UENCD8)

    def get_nature(self):
        UENCD10 = ["A parade or festival is being disrupted", "Innocents are being assaulted",
                   "An establishment is being robbed",
                   "A disturbance over local politics happens", "Someone is being blamed for something",
                   "Fires or building collapses are happening",
                   "A medical emergency is happening", "Someone is trying to cheat the PCs",
                   "A vehicle accident is happening", "A religious ceremony is being disrupted"]
        return random.choice(UENCD10)

    def get_antag_involve(self):
        UENCD12 = ["A local bully and their thugs", "A ruthless political boss and their zealots", "Violent Criminals",
                   "Religious fanatics", "A blisteringly obnoxious offworlder",
                   "Corrupt or over-strict government official",
                   "A mob of intoxicated locals", "A ranting demagogue and their followers",
                   "A stupidly bull-headed local grandee",
                   "A very capable assassin or strong-arm", "A self centered local scion of power",
                   "A confused foreigner or backwoodsman"]
        return random.choice(UENCD12)

    def get_features(self):
        UENCD20 = ["Heavy traffic running through the place", "Music blaring at deafening volumes",
                   "Two groups present that detest each other",
                   "Large delivery taking place right there", "Swarm of schoolkids or feral youth",
                   "Insistent soapbox preacher here",
                   "Several pickpockets working the crowd", "A kiosk is tipping over and spilling things",
                   "Streetlights are out or visibility is low",
                   "A cop patrol is here and reluctant to act", "PC-hostile reporters are recording here",
                   "Someone's trying to sell something to the PCs",
                   "Feral dogs or other animals crowd here", "Unrelated activists are protesting here",
                   "Street kids are trying to steal from the PCs",
                   "GPS maps are dangerously wrong here", "Downed power lines are a danger here",
                   "Numerous open manholes and utility holes",
                   "The street is blockaded by something", "Crowds so thick one can barely move"]
        return random.choice(UENCD20)


class Wilderness():
    def __init__(self):
        self.range = self.get_range()
        self.weather = self.get_weather()
        self.nature = self.get_nature()
        self.friendly = self.get_friendly()
        self.hostile = self.get_hostile()
        self.features = self.get_features()

    def get_range(self):
        WENCD4 = ["Visible from a long distance away", "Noticed 1d4*100 meters away",
                  "Noticed only within 1d6*10 meters", "Noticed only when adjacent to the event."]
        return random.choice(WENCD4)

    def get_weather(self):
        WENCD6 = ["Takes place in daylight and clear weather", "Daylight, but fog, mist, rain or the like",
         "Daylight, but harsh seasonal weather",
         "Night encounter, but clear weather", "Night, with rain or other obscuring effects",
         "Night, with terrible weather and wind"]
        return random.choice(WENCD6)

    def get_nature(self):
        WENCD8 = ["Attack by pack of hostiles", "Ambush by a single lone hostile",
                  "Meet people who dont want to be met", "Encounter people in need of aid",
                  "Encounter hostile creatures", "Nearby feature is somehow dangerous",
                  "Nearby feature promises useful loot", "Meet hostiles that aren't immediately so"]
        return random.choice(WENCD8)

    def get_friendly(self):
        WENCD10 = ["Affable but reclusive hermit", "Local herd animal let loose to graze",
                   "Government ranger or circuit judge", "Curious local animal",
                   "Remote homesteader and family", "Working trapper or hunter", "Back country villager or native",
                   "Hiker or wilderness tourist",
                   "Religious recluse or holy person", "Impoverished social exile"]
        return random.choice(WENCD10)

    def get_hostile(self):
        WENCD12 = ["Bandits in their wilderness hideout", "Dangerous locals looking for an easy mark",
                   "Rabid or diseased large predator",
                   "Pack of hungry beasts", "Herd of potentially dangerous prey animals", "Swarm of dangerous vermin",
                   "Criminal seeking to evade the law",
                   "Brutal local landowner and their men", "Crazed hermit seeking enforced solitude",
                   "Friendly seeming guide into lethal danger",
                   "Harmless-looking but dangerous beast", "Confidence man seeking to gull the PCs"]
        return random.choice(WENCD12)

    def get_features(self):
        WENCD20 = ["Overgrown homestead", "Stream prone to flash flooding", "Narrow bridge or beam over deep cleft",
                   "Box canyon with steep sides",
                   "Unstable hillside that slides if disturbed", "Long lost crash site of the gravflyer",
                   "Once inhabited cave or tunnel",
                   "Steep and dangerous cliff", "Quicksand-laden swamp or dust pit",
                   "Ruins of a ghost town or lost hamlet",
                   "Hunting cabin with necessities", "Ill-tended graveyard of a lost family stead",
                   "Narrow pass that's easily blocked",
                   "Dilapidated resort building", "Remote government monitoring outpost",
                   "Illicit substance farm or processing center",
                   "Old and forgotten battleground", "Zone overrun with dangerous plants",
                   "Thick growth that lights up at a spark", "Abandoned vehicle"]
        return random.choice(WENCD20)

