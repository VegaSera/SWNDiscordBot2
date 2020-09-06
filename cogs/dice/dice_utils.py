from cogs.utils.ToolUtils import diceroller
import re


def keep_dice(die, side, keep):
    """Dice in the format of XdYkZ. X is the number of dice to roll, Y is the number of side each die should have. Z is the number of dice to keep."""

    tot, verbose = diceroller(die, side, verbose=True)
    if keep >= die:  # If this is true, we keep all dice and no dice need to be dropped.
        return tot, verbose
    elif keep <= 0:  # All dice get dropped. Total = 0 and all entries in verbose are crossed out.
        crossout = []
        for i in verbose:
            crossout.append("~~" + str(i) + "~~")
        return 0, crossout
    else:  # Keep dice is between 1 and the number of dice.
        kept_list = []
        crossout = verbose
        for i in range(int(keep)):
            kept_list.append(max(crossout))
            crossout.remove(max(crossout))
        total = sum(kept_list)
        for j in crossout:  # The only things remaining in this are values to be crossed out.
            kept_list.append("~~" + str(j) + "~~")
        return total, kept_list

def drop_dice(die, side, drop):
    """Dice in the format of XdYdZ. X is the number of dice to roll, Y is the number of side each die should have. Z is the number of dice to drop."""
    tot, verbose = diceroller(die, side, verbose=True)
    if drop >= die:  # If this is true, we drop all dice and return 0, with all entries crossed out.
        crossout = []
        for i in verbose:
            crossout.append("~~" + str(i) + "~~")
        return 0, crossout
    elif drop <= 0:  # No dice get dropped.
        return tot, verbose
    else:  # Drop dice is between 1 and the number of dice.
        kept_list = []
        newsplit = verbose
        for j in range(int(die) - int(drop)):
            kept_list.append(max(newsplit))
            newsplit.remove(max(newsplit))
        total = sum(kept_list)
        for j in newsplit:
            kept_list.append("~~" + str(j) + "~~")
        return total, kept_list

def is_sensible_roll(dice):
    """Checks the dice results for sensible sizes. Returns a boolean, and an error string if false."""
    if int(dice[1]) > 100:  # Attempted to roll more than 100 dice in a single group.
        return False, "Attempted to roll more than 100 dice in a single group."
    elif int(dice[2]) > 50000: #Attempted to roll a die with more than 50000 sides.
        return False, "Attempted to roll a dice with more than 50000 sides."
    else:
        return True, ""


def parse_dice_string(dicestring, verbose=False):
    """Parses our dice string and does the appropriate math."""
    results = []
    return_string = ''
    simple_dice = re.findall('(\A|[+-])(\d+)d(\d+)(?=[+-]|\Z|\s|\n)', dicestring)
    keepdice = re.findall('(\A|[+-])(\d+)d(\d+)k(\d+)(?=[+-]|\Z|\s|\n)', dicestring)
    dropdice = re.findall('(\A|[+-])(\d+)d(\d+)d(\d+)(?=[+-]|\Z|\s|\n)', dicestring)
    modifier = re.findall('([+-])(\d+)(?=[^d0-9]|[+-]|\s|\Z)', dicestring)

    #Keep Dice
    #Structure of the keep dice - [Sign/Start Of String][Number of Dice][Number of Sides][Number to Keep]
    #Checking for sensibility
    for i in keepdice:
        if not is_sensible_roll(i)[0]:
            return 0, is_sensible_roll(i)[1]

        print(i)
        # If the dice are sensible
        total, kept_list = keep_dice(int(i[1]), int(i[2]), int(i[3]))

        verbose_string = '['
        for x in kept_list:
            verbose_string += (str(x) + ", ")
        verbose_string = verbose_string[:-2]
        verbose_string += ']'

        lst = list(i)
        if i[0] not in ['-', '+']:
            lst[0] = '+'
        else:
            lst[0] = i[0]

        string = (" " + lst[0] + " " + i[1] + 'd' + i[2] + 'k' + i[3] + '(**' + str(total) + '**)')
        if verbose:
            string += str(verbose_string)
        return_string += string

        if i[0] == '-':
            results.append(total*-1)
        else:
            results.append(total)

    for i in dropdice:
        if not is_sensible_roll(i)[0]:
            return 0, is_sensible_roll(i)[1]

        total, keptlist = drop_dice(int(i[1]), int(i[2]), int(i[3]))
        verbosestring = '['
        for x in keptlist:
            verbosestring += (str(x) + ', ')
        verbosestring = verbosestring[:-2]
        verbosestring += ']'
        if i[0] not in ['-', '+']:
            lst = list(i)
            lst[0] = '+'
        else:
            lst = list(i)
            lst[0] = i[0]

        string = (" " + lst[0] + " " + i[1] + 'd' + i[2] + 'd' + i[3] + '(**' + str(total) + '**)')
        if verbose:
            string += str(verbosestring)
        return_string += string

        if i[0] == '-':
            results.append(total * -1)
        else:
            results.append(total)

    for i in simple_dice:
        if not is_sensible_roll(i)[0]:
            return 0, is_sensible_roll(i)[1]

        total, split = diceroller(int(i[1]), int(i[2]), verbose=True)
        verbosestring = '['
        for x in split:
            verbosestring += (str(x) + ', ')
        verbosestring = verbosestring[:-2]
        verbosestring += ']'

        string = (" " + i[0] + " " + i[1] + 'd' + i[2] + '(**' + str(total) + '**)')
        if verbose:
            string += str(verbosestring)
        return_string += string

        if i[0] == '-':
            results.append(total * -1)
        else:
            results.append(total)

    for i in modifier:
        string = " " + str(i[0]) + " **" + str(i[1] + "**")
        return_string += string
        if i[0] == '-':
            results.append(int(i[1]) * -1)
        elif i[0] == '+':
            results.append(int(i[1]))

    return_string = return_string[2:]
    return sum(results), return_string