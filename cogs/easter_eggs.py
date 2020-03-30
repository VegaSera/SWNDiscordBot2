from discord.ext import commands

class Easter_Eggs(commands.Cog):
    """Congratulations, you looked at the source code and found some easter
    eggs that don't show up in typical !help messages. Do with them as you please."""
    def __init__(self, client):
        self.hidden = True  # Easter eggs are meant to be hidden. If you unhide this, it will unhide everything here.
        self.client = client
        self.short_desc = "A number of hidden easter egg functions"
        self.full_desc = ""

    @commands.command()
    async def rollplant(self, ctx):
        """Typo of !rollplanet. Redirecting."""
        # TODO Rollplant troll response
        pass

    @commands.command()
    async def rollplane(self, ctx):
        """Typo of !rollplanet. Redirecting."""
        # TODO Rollplane troll response
        pass

    @commands.command()
    async def rollplan(self, ctx):
        """Typo of !rollplanet. Redirecting."""
        # TODO Rollplan troll response
        pass

    @commands.command()
    async def smack(self, ctx, *message):
        """Bot will smack the tagged person"""
        # TODO Smack a hoe
        pass


def setup(client):
    client.add_cog(Easter_Eggs(client))

