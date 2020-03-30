from discord.ext import commands



class Misc(commands.Cog):
    """Commands related to the Dice rolling function"""
    def __init__(self, client):
        self.client = client
        self.hidden = False


    @commands.command()
    async def about(self, string):
        """About this bot"""
        #TODO Tell a bit about the bot
        pass

    @commands.command()
    async def megajim(self, string):
        """Gives an easy way to search for the Ballad of Mega Jim"""
        # TODO Give a link to the Ballad of Megajim
        pass

    @commands.command(hidden=True)
    async def github(self, string):
        """Gives a link to view the bot's source code on Github"""
        # TODO Link to this bots repo on Github
        pass



def setup(client):
    client.add_cog(Misc(client))