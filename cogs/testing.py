import discord
from discord.ext import commands

class Test(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.hidden = True
        self.short_desc = "Assortment of testing functions"
        self.full_desc = "TODO Full Description"

    @commands.command()
    async def test(self, ctx):
        await ctx.send("test")

def setup(client):
    client.add_cog(Test(client))

if __name__ == '__main__':
    print(True, True, True == True, True, True)
