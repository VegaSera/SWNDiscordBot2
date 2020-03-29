import discord
from discord.ext import commands

class Example(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.hidden = True

    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("AVIONICS BOT LOADED AND READY TO BEGIN THE FUCKMAKING")

    #Commands
    @commands.command()
    async def ping(self, ctx, *message):
        message = list(message)
        for index, i in enumerate(message):
            i = i.lower()
            message[index] = i
            print(i)
        if not message:
            await ctx.send("Pong.")
        if message:
            await ctx.send(message)



def setup(client):
    client.add_cog(Example(client))