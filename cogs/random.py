import discord
from discord.ext import commands
from cogs.character.character_tables import bgtables
from cogs.character.character_gen import Character
import cogs.utils.ToolUtils as ToolUtil
from cogs.utils.word_tables import nountable, NormalAdjTable, SillyAdjTable
import cogs.utils.namer as namer
import cogs.quick_helpers.quick_classes as quickc
from cogs.random_race.race_gen import Race
from cogs.planets.raw_planet import Raw_Planet
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
        norm = ToolUtil.normalize_message(message)

        # In depth help message
        sent_help_message = False
        if len(message) > 0:  # Message is not empty. Empty messages should just use default settings.
            if message[0].lower() == "help":
                print("INVOKED ROLLCHARACTER HELP")
                char_embed = discord.Embed(title=f"{self.client.command_prefix}rollcharacter Help",
                                           color=self.client.embed_color,
                                           description="Generates a level 1 character based on various criteria.")
                x = self.client.command_prefix  # So we dont have to write it out several times
                char_embed.add_field(name="Command Modifiers",
                                     value=f"`{x}rollcharacter` - Generates a random character with a random class and background.\n"
                                           f"`{x}rollcharacter help` - Displays this message\n"
                                           f"`{x}rollcharacter (class)` - Generates a random character with the "
                                           f"specified class(es). Up to two classes in [Warrior, Expert, Psychic, "
                                           f"Adventurer] - Adventurer will always generate partial classes.\n"
                                           f"`{x}rollcharacter (background)` - Generates a random character with a specified background. "
                                           f"Only one background can be specified.\n"
                                           f"`{x}rollcharacter verbose` - Gives a more detailed log of what happens during character creation.\n"
                                           f"`{x}rollcharacter seed=XXXX` - Replace XXXX with anything you want to specify the random seed. "
                                           f"If not specified, it will generate a random seed.\n\n"
                                           f"Command modifiers can also be combined.\n"
                                           f"Example: `{x}rollcharacter warrior adventurer noble verbose seed=Potato`\n"
                                           f"This will generate a random partial Warrior with either Psychic or "
                                           f"Expert, with the noble background, give a detailed log of character "
                                           f"creation, and will generate the same every time with the seed Potato"
                                     , inline=False)
                char_embed.add_field(name="Technical Stuff",
                                     value=f"This command goes through the entirety of character generation, but because"
                                           f" it is random by it's nature, some choices are 'suboptimal'. However it "
                                           f"behaves smartly in most cases. \nIf Growth provides a +2 Physical Attribute "
                                           f"bonus, it will first look to raise modifiers before assigning randomly. "
                                           f"If it sees that it can raise a stat with +1 out of a +2, it will do so "
                                           f"and use the other +1 somewhere else.\n"
                                           f"Equipment is also assigned based on the provided tables and what would be "
                                           f"appropriate for the character's foci and background.\n\nIf it looks like your "
                                           f"character only has one or two skills, that means it has rolled +1 Any Stat "
                                           f"or +2 Physical many times in the Growth/Learning phase. "
                                           f"These are automatically assigned. Use `{x}rollcharacter verbose` to see these."
                                           f"\n\nBe aware, sometimes silly things can happen."
                                     , inline=False)
                char_embed.set_footer(text="Sorry for being excessive :( It's a complex command.")
                await ctx.channel.send(embed=char_embed)
                sent_help_message = True

        if not sent_help_message:  # If a help message gets sent, we dont want to generate a character.

            # If we get a bad message at any point, throw an error and prevent the character from generating.
            error_in_message = False

            # Setting our seed
            seed = ToolUtil.random_seed_setter()
            for i in message:  # Not using our normalized message because capitalization matters.
                if i.lower().startswith('seed='):
                    seed = i.split('=')[1]
            random.seed(seed)

            # Setting up our stat_type
            if "udb" in norm or "4d6d1" in norm:
                stat_type = "4d6d1"
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
            error_embed = discord.Embed(title="Error in Command", color=self.client.embed_color)
            if len(class_type) > 2:
                error_in_message = True
                error_embed.add_field(name="Too many classes passed",
                                      value=f"You passed {len(class_type)} different classes. Use two or less.",
                                      inline=False)
                pass

            # Finding backgrounds
            bgs = [i.lower() for i in bgtables.keys()]
            background = []
            for i in norm:
                if i in bgs:
                    background.append(i.capitalize())
            if len(background) > 1:
                error_in_message = True
                error_embed.add_field(name="Too many backgrounds passed",
                                      value=f"You passed {len(background)} different backgrounds. Use one or none.",
                                      inline=False)

            if error_in_message:  # Got an error
                await ctx.channel.send(embed=error_embed)
            else:
                # Generating new character
                new_char = Character(stat_roll_type=stat_type, char_class=class_type, char_background=background)

                # Sending back to user
                char_embed = discord.Embed(title="Random Character", color=self.client.embed_color)
                char_embed.add_field(name="Seed", value=seed)
                char_embed.add_field(name="Class", value=new_char.class_string)
                char_embed.add_field(name="Background", value=new_char.char_bg)
                char_embed.add_field(name="Attributes",
                                     value=f"Strength: {new_char.str} ({new_char.str_mod})\n"
                                           f"Dexterity: {new_char.dex} ({new_char.dex_mod})\n"
                                           f"Constitution: {new_char.con} ({new_char.con_mod})\n"
                                           f"Intelligence: {new_char.int} ({new_char.int_mod})\n"
                                           f"Wisdom: {new_char.wis} ({new_char.wis_mod})\n"
                                           f"Charisma: {new_char.cha} ({new_char.cha_mod})\n")
                char_embed.add_field(name="HP", value=f"{new_char.hp} ({new_char.max_hp})")
                char_embed.add_field(name="Attack Bonus", value=new_char.ab)
                char_embed.add_field(name="Foci", value=new_char.foci, inline=False)
                char_embed.add_field(name="Skills", value=new_char.skills, inline=False)
                char_embed.add_field(name="Equipment", value=new_char.equipment, inline=False)
                if 'verbose' in norm:
                    char_embed.add_field(name="Verbose Log", value=new_char.verbose_log, inline=False)
                await ctx.channel.send(embed=char_embed)

    @commands.command()
    async def rollplanet(self, ctx, *message):
        """`{prefix}rollplanet` - Generates a random planet via the rules as written"""
        norm = ToolUtil.normalize_message(message)

        # In depth help message
        sent_help_message = False
        if len(message) > 0:  # Message is not empty.
            if message[0].lower() == "help":
                print("INVOKED ROLLPLANET HELP")
                embed = discord.Embed(title=f"{self.client.command_prefix}rollplanet Help",
                                      color=self.client.embed_color,
                                      description="Generates a random planet via the rules as written on page 130")
                await ctx.channel.send(embed=embed)
                sent_help_message = True

        if not sent_help_message:  # If a help message gets sent, we dont want to generate anything.

            # Setting our seed
            seed = ToolUtil.random_seed_setter()
            for i in message:  # Not using our normalized message because capitalization matters.
                if i.lower().startswith('seed='):
                    seed = i.split('=')[1]
            random.seed(seed)


            #TODO Generate different type of planet that makes more sense.
            new_planet = Raw_Planet(num_tags=3)


            embed = discord.Embed(title="Random Planet", color=self.client.embed_color)
            embed.add_field(name="Planet Name", value=ToolUtil.random_namer(2,4), inline=False)
            embed.add_field(name="Seed", value=seed, inline=False)
            embed.add_field(name="Atmosphere", value=new_planet.atmo)
            embed.add_field(name="Temperature", value=new_planet.temp)
            embed.add_field(name="Biosphere", value=new_planet.bio)
            embed.add_field(name="Population", value=new_planet.pop)
            embed.add_field(name="Tech Level", value=new_planet.tl)
            embed.add_field(name="World Tags", value=new_planet.world_tags, inline=False)

            await ctx.channel.send(embed=embed)

    @commands.command(hidden=True)
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

        # A normalized message in lower case to compare to easier.
        norm = ToolUtil.normalize_message(message)  # Not currently used, but may be in the future when modifiers need parsed.

        # In depth help message
        sent_help_message = False
        if len(message) > 0:  # Message is not empty.
            if message[0].lower() == "help":
                embed = discord.Embed(title=f"{self.client.command_prefix}rollrace Help",
                                      color=self.client.embed_color,
                                      description="Generates a random alien race using a combination of Alien Race rules"
                                                  " and beast rules.\n\n Currently this command does not support any "
                                                  "modifiers other than `seed=XXXX`, but in the future you will be "
                                                  "able to specify various parts.")
                await ctx.channel.send(embed=embed)
                sent_help_message = True

        if not sent_help_message:  # If a help message gets sent, we dont want to generate anything.

            # Setting our seed
            seed = ToolUtil.random_seed_setter()
            for i in message:  # Not using our normalized message because capitalization matters.
                if i.lower().startswith('seed='):
                    seed = i.split('=')[1]
            random.seed(seed)

            new_race = Race()
            race_embed = discord.Embed(title="Random Race", color=self.client.embed_color)
            race_embed.add_field(name="Race Name", value=ToolUtil.random_namer(2, 5), inline=False)
            race_embed.add_field(name="Seed", value=seed, inline=False)
            race_embed.add_field(name="Basic Features", value=new_race.base)
            race_embed.add_field(name="Body Plan", value=new_race.body)
            race_embed.add_field(name="Size", value=new_race.size)
            race_embed.add_field(name="Lens/Psychology", value=new_race.lens, inline=False)
            race_embed.add_field(name="Social Structure", value=new_race.social, inline=False)
            race_embed.add_field(name="Racial Perks", value=new_race.perk, inline=False)

            await ctx.channel.send(embed=race_embed)

    @commands.command()
    async def quick(self, ctx, *message):
        """`{prefix}quick npc` - Generates a quick roll NPC via the RAW. `npc` can be replaced with `patron`, `urban`, and `wilderness`"""
        norm = ToolUtil.normalize_message(message)
        x = self.client.command_prefix
        sent_help_message = False
        if len(message) == 0 or message[0].lower() == "help":
            print("INVOKED QUICK HELP")
            npc_embed = discord.Embed(title=f"{self.client.command_prefix}quick Help",
                                  color=self.client.embed_color,
                                  description="One-roll stuff based on the tables on pages 244-247")
            npc_embed.add_field(name=f"`{x}quick npc`", value = "Generates an NPC", inline=False)
            npc_embed.add_field(name=f"`{x}quick patron`",
                                value=f"Generates a Patron, a job contact.\n\nFor both NPCs and Patrons, you can "
                                      f"specify a gender by using a modifier like `{x}quick npc female` and such.", inline=False)
            npc_embed.add_field(name=f"`{x}quick urban`", value="Generates an Urban Encounter", inline=False)
            npc_embed.add_field(name=f"`{x}quick wilderness`", value="Generates a Wilderness Encounter", inline=False)
            await ctx.channel.send(embed=npc_embed)
            sent_help_message = True

        if not sent_help_message:
            seed = ToolUtil.random_seed_setter()
            for i in message:  # Not using our normalized message because capitalization matters.
                if i.lower().startswith('seed='):
                    seed = i.split('=')[1]
            random.seed(seed)

            if message[0].lower() == 'npc':
                if 'female' in norm:
                    gender = 'f'
                elif 'male' in norm:
                    gender = 'm'
                else:
                    gender = None

                npc = quickc.NPC(gender=gender)
                npc_embed = discord.Embed(title="Random Quick-Roll NPC", color=self.client.embed_color)
                npc_embed.add_field(name="Seed", value=seed)
                npc_embed.add_field(name="Name", value=npc.name)
                npc_embed.add_field(name="Age", value=npc.age, inline=False)
                npc_embed.add_field(name="Background", value=npc.background, inline=False)
                npc_embed.add_field(name="Their Role in Society", value=npc.role, inline=False)
                npc_embed.add_field(name="Their Biggest Problem", value=npc.problem, inline=False)
                npc_embed.add_field(name="Their Greatest Desire", value=npc.desire, inline=False)
                npc_embed.add_field(name="Most Obvious Character Trait", value=npc.trait, inline=False)
                await ctx.channel.send(embed=npc_embed)

            elif message[0].lower() == 'patron':
                if 'female' in norm:
                    gender = 'f'
                elif 'male' in norm:
                    gender = 'm'
                else:
                    gender = None

                patron = quickc.Patron(gender=gender)
                patron_embed = discord.Embed(title="Random Quick-Roll Patron", color=self.client.embed_color)
                patron_embed.add_field(name="Seed", value=seed)
                patron_embed.add_field(name="Name", value=patron.name)
                patron_embed.add_field(name="Eagerness to Hire", value=patron.eagerness, inline=False)
                patron_embed.add_field(name="Trustworthiness", value=patron.trust, inline=False)
                patron_embed.add_field(name="Basic challenge of the job", value=patron.challenge, inline=False)
                patron_embed.add_field(name="Main Countervaling force", value=patron.counter, inline=False)
                patron_embed.add_field(name="Potential Non-cash Rewards", value=patron.reward, inline=False)
                patron_embed.add_field(name="Complication to the Job", value=patron.complication, inline=False)
                await ctx.channel.send(embed=patron_embed)

            elif message[0].lower() == 'urban':

                urban = quickc.Urban()
                urban_embed = discord.Embed(title="Random Quick-Roll Urban Encounter", color=self.client.embed_color)
                urban_embed.add_field(name="Seed", value=seed)
                urban_embed.add_field(name="What is the conflict about?", value=urban.conflict, inline=False)
                urban_embed.add_field(name="General Venue of the Event", value=urban.venue, inline=False)
                urban_embed.add_field(name="Why are PCs involved?", value=urban.pc_involve, inline=False)
                urban_embed.add_field(name="What is the nature of the event?", value=urban.nature, inline=False)
                urban_embed.add_field(name="What antagonists are involved?", value=urban.antag_involve, inline=False)
                urban_embed.add_field(name="Relevant Urban Features", value=urban.features, inline=False)
                await ctx.channel.send(embed=urban_embed)

            elif message[0].lower() == 'wilderness':
                wild = quickc.Wilderness()
                wild_embed = discord.Embed(title="Random Quick-Roll Wilderness Encounter", color=self.client.embed_color)
                wild_embed.add_field(name="Seed", value=seed)
                wild_embed.add_field(name="Initial Encounter Range", value=wild.range, inline=False)
                wild_embed.add_field(name="Weather and Lighting", value=wild.weather, inline=False)
                wild_embed.add_field(name="Basic Nature of the Encounter", value=wild.nature, inline=False)
                wild_embed.add_field(name="Types of Friendly Creatures", value=wild.friendly, inline=False)
                wild_embed.add_field(name="Types of Hostile Creatures", value=wild.hostile, inline=False)
                wild_embed.add_field(name="Specific Nearby Features of Relevance", value=wild.features, inline=False)
                await ctx.channel.send(embed=wild_embed)






def setup(client):
    client.add_cog(Random(client))
