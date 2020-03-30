import discord
from discord.ext import commands
from cogs.character.character_tables import bgtables
from cogs.character.character_gen import Character
from cogs.utils.ToolUtils import normalize_message

class Random(commands.Cog):
    """A suite of random generators for SWN."""
    def __init__(self, client):
        self.hidden = False
        self.client = client
        self.short_desc = "A suite of random generators for SWN."
        self.full_desc = ""

    @commands.command()
    async def rollcharacter(self, ctx, *message):
        """`!rollcharacter` - Generates a random level 1 SWN Character"""

        #A normalized message in lower case to compare to easier.
        norm = normalize_message(message)

        # In depth help message
        #TODO Rollcharacter Help Message

        # Setting our seed
        #TODO Set character seed

        #Setting up our stat_type
        if "udb" in norm or "4d6d1" in norm:
            stat_type = "4d6d1"
            #TODO This will error out if invoked until we complete a drop dice roller.
        else:
            stat_type = "norm"

        #Finding classes
        class_type = []
        if "warrior" in norm:
            class_type.append("Warrior")
        if "expert" in norm:
            class_type.append("Expert")
        if "psychic" in norm:
            class_type.append("Psychic")
        if "adventurer" in norm:
            class_type.append("Adventurer")
        if len(class_type) == 0:  # Activates if no class has been passed in a message, setting it to a none type for the generator
            class_type = None
        elif len(class_type) > 2:
            # TODO Return an error to the user and tell them to use less classes.
            pass


        #Finding backgrounds
        if any(bgtables.keys.lower()) in norm:
            #TODO Pass BG information to character
            pass





        new_char = Character(stat_roll_type=stat_type, char_class=class_type)

    @commands.command()
    async def rollplanet(self, ctx, *message):
        """Rolls a random planet"""
        # TODO Random Planet
        pass

    @commands.command()
    async def rollship(self, ctx, *message):
        """Rolls a random ship"""
        # TODO Random Ship
        pass

    @commands.command()
    async def shipnames(self, ctx, *message):
        """Rolls a random ship"""
        # TODO Random Ship Names
        pass

    @commands.command()
    async def rollrace(self, ctx, *message):
        """Rolls a random alien race"""
        # TODO Random Race
        pass

    @commands.command()
    async def quick(self, ctx, *message):
        """Rolls a random NPC/Patron/Encounter"""
        # TODO Quick tables
        pass


def setup(client):
    client.add_cog(Random(client))