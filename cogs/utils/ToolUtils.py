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
    randomseed = ""
    random.seed()  # Makes sure we dont have another seed influencing this.
    for i in range(random.randint(5, 15)):
        randomseed += random.choice(tables.SeedDigits)
    return randomseed

def normalize_message(message):
    """Takes in a tuple message and converts it to a list, then lowercases it."""

    message = list(message)
    for index, i in enumerate(message):
        i = i.lower()
        message[index] = i
        print(i)
    return message