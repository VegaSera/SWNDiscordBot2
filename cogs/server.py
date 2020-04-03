from discord.ext import commands


class Server(commands.Cog):
    """A collection of discord server management tools"""

    def __init__(self, client):
        self.hidden = False
        self.client = client
        self.short_desc = "A collection of discord server management tools and role settings"
        self.full_desc = "A collection of various discord server management tools and role management tools."

    @commands.command()
    async def lfg(self):
        """Either assigns or removes the LFG role, based on whether or not you have it already"""
        #TODO LFG Role Handling
        pass

    @commands.command()
    async def udb(self):
        """Either assigns or removes the Community Player role, based on whether or not you have it already"""
        #TODO UDB Role Handling
        pass



def setup(client):
    client.add_cog(Server(client))
