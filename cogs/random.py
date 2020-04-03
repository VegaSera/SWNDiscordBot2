import discord
from discord.ext import commands
from cogs.character.character_tables import bgtables
from cogs.character.character_gen import Character
from cogs.utils.ToolUtils import normalize_message, random_seed_setter
from cogs.utils.word_tables import nountable, NormalAdjTable, SillyAdjTable
import random


class Random(commands.Cog):
    """A suite of random generators for SWN."""

    def __init__(self, client):
        self.hidden = False
        self.client = client
        self.short_desc = "A suite of random generators for SWN."
        self.full_desc = "The majority of these random generators come directly from the book. Commands such as " \
                         f"{self.client.command_prefix}rollship and {self.client.command_prefix}rollrace were taken " \
                         f"from the book as well and adapted for bot use.\n\n" \
                         "Invoke `help` after any command to access more detailed help and information about it.\n" \
                         f"Example - `{self.client.command_prefix}rollcharacter help`"

    @commands.command()
    async def rollcharacter(self, ctx, *message):
        """`{prefix}rollcharacter` - Generates a random level 1 SWN Character"""

        # A normalized message in lower case to compare to easier.
        norm = normalize_message(message)

        # In depth help message
        sent_help_message=False
        if len(message) > 0:  # Message is not empty. Empty messages should just use default settings.
            if message[0].lower() == "help":
                print("INVOKED ROLLCHARACTER HELP")
                # TODO Rollcharacter Help Message
                sent_help_message = True


        if not sent_help_message: # If a help message gets sent, we dont want to generate a character.

            # If we get a bad message at any point, throw an error and prevent the character from generating.
            error_in_message = False

            # Setting our seed
            seed = random_seed_setter()
            for i in message:  # Not using our normalized message because capitalization matters.
                if i.lower().startswith('seed='):
                    seed = i.split('=')[1]
            random.seed(seed)

            # Setting up our stat_type
            if "udb" in norm or "4d6d1" in norm:
                stat_type = "4d6d1"
                # TODO This will error out if invoked until we complete a drop dice roller.
            else:
                stat_type = "norm"

            # Finding classes
            class_type = []
            if "warrior" in norm:
                class_type.append("Warrior")
            if "expert" in norm:
                class_type.append("Expert")
            if "psychic" in norm:
                class_type.append("Psychic")
            if "adventurer" in norm:
                class_type.append("Adventurer")

            if len(class_type) > 2:
                print(f"Too many classes passed. User passed {len(class_type)} classes.")
                error_in_message = True
                # TODO Return an error to the user and tell them to use less classes.
                pass

            # Finding backgrounds
            bgs = [i.lower() for i in bgtables.keys()]
            background = []
            for i in norm:
                if i in bgs:
                    print("Found specified background", i)
                    background.append(i.capitalize())
            if len(background) > 1:
                error_in_message = True
                print(f"Too many backgrounds passed. Found {len(background)} backgrounds in the message.")
                pass
                #TODO Throw error and break

            if not error_in_message: # No errors have been thrown by initial handling.
                print(f"Passing this information to the character.\nStat type:{stat_type}\nClass={class_type}\nBackground={background}")

                #Generating new character
                new_char = Character(stat_roll_type=stat_type, char_class=class_type, char_background=background)
                print("Seed = ", seed)
                print("Classes = ", new_char.char_class)
                print("Stat mods", new_char.str_mod, new_char.dex_mod, new_char.con_mod, new_char.int_mod, new_char.wis_mod, new_char.cha_mod )
                print("Skills", new_char.skills)
                print("--Verbose Log--")
                print(new_char.verbose_log)

    @commands.command()
    async def rollplanet(self, ctx, *message):
        """`{prefix}rollplanet` - Generates a random planet via the rules as written"""
        # TODO Random Planet
        pass

    @commands.command()
    async def rollship(self, ctx, *message):
        """`{prefix}rollship` - Generates a random ship with fittings"""
        # TODO Random Ship
        pass

    @commands.command()
    async def shipnames(self, ctx, *message):
        """`{prefix}shipnames` - Generates a list of possible ship names`"""
        default = 10
        limit = 20  # Max number of ships to return. Single variable for easy tuning.
        sent_help_message = False
        if len(message) > 0:  # Message is not empty. Empty messages should just use default settings.
            if message[0].lower() == "help":
                rand_ship_names = discord.Embed(color=self.client.embed_color, title="Random Ship Names Help")
                rand_ship_names.add_field(name="General Information",
                                          value="Generates a set of potential ship names of questionable quality from a "
                                                "long list of almost 2000 nouns.",
                                          inline=False)
                rand_ship_names.add_field(name="Usage Examples",
                                          value=f"`{self.client.command_prefix}shipnames` - Generates ship names. {default} by default.\n"
                                                f"`{self.client.command_prefix}shipnames 15` - Generates 15 ship names."
                                                f" You can change the `15` to be any integer from 1 to {limit}.\n"
                                                f"`{self.client.command_prefix}shipnames help` - Displays this help message.",
                                          inline=False)
                await ctx.message.channel.send(embed=rand_ship_names)
                sent_help_message = True

        if not sent_help_message:
            ship_names = []
            sent_error = False
            try:
                if limit >= int(message[0]) > 0:
                    j = int(message[0])
                elif int(message[0]) > limit:
                    rand_ship_names = discord.Embed(color=self.client.embed_color)
                    rand_ship_names.add_field(name="Error - Specified a number that is too large",
                                              value=f"Be respectful of everyone else's screen space and limit the "
                                                    f"amount of ship names you generate to {limit} or less")
                    await ctx.message.channel.send(embed=rand_ship_names)
                    sent_error = True
                else:
                    j = default
            except:  # Throws an exception if no number was given, we'll default it.
                j = default

            if not sent_error:
                for i in range(j):
                    k = random.randint(1, 10000)
                    if k % 4 == 0:
                        ship_names.append(("The " + random.choice(nountable) + " " + random.choice(nountable)))
                    if k % 4 == 1:
                        ship_names.append(("The " + random.choice(NormalAdjTable + SillyAdjTable) + " " +
                                           random.choice(nountable)))
                    if k % 4 == 2:
                        ship_names.append(
                            (random.choice(NormalAdjTable + SillyAdjTable) + random.choice(nountable).lower() + ", the "
                             + random.choice(nountable) + " of " + random.choice(nountable) + "s"))
                    else:
                        ship_names.append(("The " + random.choice(nountable) + f" of {random.choice(nountable)}s"))
                ship_name_string = ""
                for i in ship_names:
                    ship_name_string += str(i) + "\n"
                rand_ship_names = discord.Embed(color=self.client.embed_color)
                rand_ship_names.add_field(name="Your random ship names", value=ship_name_string)
                await ctx.message.channel.send(embed=rand_ship_names)

    @commands.command()
    async def rollrace(self, ctx, *message):
        """`{prefix}rollrace` - Generates an alien race with features and lenses. Basically combines aliens and beasts from the book"""
        # TODO Random Race
        pass

    @commands.command()
    async def quick(self, ctx, *message):
        """`{prefix}quick npc` - Generates a quick roll NPC via the RAW. `npc` can be replaced with `patron`, `urban`, and `wilderness`"""
        # TODO Quick tables
        pass


def setup(client):
    client.add_cog(Random(client))
