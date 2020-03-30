import random
import cogs.utils.general_tables as tables


def diceroller(num: int, sides: int, mod=0, verbose=False):
    """Rolls a simple die. For easy 1:1 translation from tabletop to program.

    :param num: - Number of dice to roll
    :param sides: - Number of sides on the dice
    :param mod: - Static modifier to add to the result. Default 0 if no modifier is specified.
    :param verbose: - If true, returns a list of individual die results. Default False
    :return: - Returns the result
    """
    die_results = []
    total = 0
    for i in range(num):
        roll_result = random.randint(1, sides)
        die_results.append(roll_result)
        total += roll_result
    if verbose:
        return total+mod, die_results
    else:
        return total+mod


def random_seed_setter():
    """

    :return: - Returns the random seed that is generated
    """
    random_seed = ""
    random.seed()  # Makes sure we don't have another seed influencing this.
    for i in range(random.randint(5, 15)):
        random_seed += random.choice(tables.SeedDigits)
    return random_seed


def normalize_message(message):
    """Takes in a tuple message and converts it to a list, then lower cases it."""

    message = list(message)
    for index, i in enumerate(message):
        i = i.lower()
        message[index] = i
        print(i)
    return message


def random_namer(min_len, max_len, lang="all"):
    """Both Cherokee and Japanese have phonemes that are designed to be combined with each other. Taking an assortment
    and adding them together creates somewhat plausible names.
    Could add other syllablistic languages in the future."""
    cherokeesyllatable = ['a', 'ga', 'ka', 'ha', 'la', 'ma', 'na', 'hna', 'nah', 'qua', 's', 'sa', 'da', 'ta', 'dla',
                          'tla', 'tsa', 'wa', 'ya', 'e', 'ge', 'he', 'le', 'me', 'ne', 'que', 'se', 'de', 'te', 'tle',
                          'tse', 'we', 'ye', 'i', 'gi', 'hi', 'li', 'mi', 'ni', 'qui', 'si', 'di', 'ti', 'tli', 'tsi',
                          'wi', 'yi', 'o', 'go', 'ho', 'lo', 'mo', 'no', 'quo', 'so', 'do', 'tlo', 'tso', 'wo', 'yo']
    japsyllatable = ['a', 'ka', 'sa', 'ta', 'na', 'ha', 'ma', 'ya', 'ra', 'wa', 'i', 'ki', 'shi', 'chi', 'ni', 'hi',
                     'mi', 'ri', 'wi', 'u', 'ku', 'su', 'tsu', 'nu', 'fu', 'mu', 'yu', 'ru', 'e', 'ke', 'se', 'te',
                     'ne', 'he', 'me', 're', 'we', 'o', 'ko', 'so', 'to', 'no', 'ho', 'mo', 'yo', 'ro', 'wo', 'kya',
                     'sha', 'cha', 'nya', 'hya', 'mya', 'rya', 'kyu', 'shu', 'chu', 'nyu', 'hyu', 'myu', 'ryu', 'kyo',
                     'sho', 'cho', 'nyo', 'hyo', 'myo', 'ryo', 'ga', 'za', 'da', 'ba', 'pa', 'gi', 'ji', 'bi', 'pi',
                     'gu', 'zu', 'bu', 'pu', 'ge', 'ze', 'de', 'be', 'pe', 'go', 'zo', 'do', 'bo', 'po', 'gya', 'ja',
                     'bya', 'pya', 'gyu', 'ju', 'byu', 'pyu', 'gyo', 'jo', 'byo', 'pyo']

    # We do the Cherokee table twice to make the tables roughly even length and reduce the japanese-ness of the result.
    combtable = cherokeesyllatable*2 + japsyllatable
    if lang == 'cherokee':
        table = cherokeesyllatable
    elif lang == 'japanese':
        table = japsyllatable
    elif lang == 'all':  # This is the default.
        table = combtable
    else:  # Got an unexpected result. Printing a warning but returning the 'all' table.
        print(f"WARNING - random_namer() got an unexpected language = {lang}. Defaulting to 'all'")
        table = combtable

    name = ''
    for i in range(random.randint(min_len, max_len)):
        name += random.choice(table)
    return name.title()




