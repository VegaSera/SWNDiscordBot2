from discord.ext import commands
from cogs.dice.dice_utils import parse_dice_string
from cogs.utils.ToolUtils import diceroller


class Dice(commands.Cog):
    """Commands related to the Dice rolling function"""
    def __init__(self, client):
        self.client = client
        self.hidden = False
        self.short_desc = "Commands related to Dice Rolling Functions"
        self.full_desc = ""


    @commands.command()
    async def roll(self, string):
        """Parses a dice string, and rolls it."""
        pass



def setup(client):
    client.add_cog(Dice(client))