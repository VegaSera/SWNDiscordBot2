from discord.ext import commands
import discord
from cogs.server_helpers import server_utils


class Server(commands.Cog):
    """A collection of discord server management tools"""

    def __init__(self, client):
        self.hidden = False
        self.client = client
        self.short_desc = "A collection of discord server management tools and role settings"
        self.full_desc = "A collection of various discord server management tools and role management tools."

    @commands.command()
    async def lfg(self, ctx, *message):
        """Either assigns or removes the LFG role, based on whether or not you have it already"""

        result = await server_utils.toggle_group("lfg", ctx)

        if result == 'whisper': # Role has not been found on the server
            embed = discord.Embed(title="Could not add/remove the LFG role", color=discord.Color.red(),
                                  description="You are DMing this bot right now. Roles do not exist in DMs. Use this command on a server.")
            await ctx.channel.send(embed=embed)
        elif result == 'role not found': # Role has not been found on the server
            embed = discord.Embed(title="Could not add/remove the LFG role", color=discord.Color.red(),
                                  description="AVIONICS did not recognize any roles named 'LFG' on this server.")
            await ctx.channel.send(embed=embed)
        elif result == 'removed':  # Role has been found, will remove it from the user
            embed = discord.Embed(title=f"LFG Role removed from {ctx.author}", color=self.client.embed_color,
                                  description="You will no longer receive notifications when someone is looking for players")
            await ctx.channel.send(embed=embed)
        elif result == 'added':  # Role has been found on the server, but not on the user. Adding it.
            embed = discord.Embed(title=f"LFG Role added to {ctx.author}", color=self.client.embed_color,
                                  description="You will be notified when someone is looking for players.")
            await ctx.channel.send(embed=embed)


    @commands.command()
    async def udb(self, ctx, *message):
        """Either assigns or removes the Community Player role, based on whether or not you have it already"""
        if len(message) == 0:
            embed = discord.Embed(title="United Discord Backdrop Community Games", color=self.client.embed_color,
                                  description="UDB, or United Discord Backdrop, is a drop-in, drop-out campaign in the "
                                              "style of West Marches, set in an expanding sector. Anyone who is "
                                              "interested is eligible to GM for a UDB session. See pinned messages in "
                                              "#udb-players on the Stars Without Number Community Discord for Roll20 "
                                              "links and resources, ping Helpers for becoming a UDB GM.\n\n\n"
                                              "If you wish to be notified when a UDB game is coming up, or if you no"
                                              "longer wish to receive notifications as a Community Player, use the"
                                              f"`{self.client.command_prefix}udb role` command to toggle your role status.")
            await ctx.channel.send(embed=embed)

        elif message[0] == 'role':
            result = await server_utils.toggle_group("Community Player", ctx)
            if result == 'whisper':  # Role has not been found on the server
                embed = discord.Embed(title="Could not add/remove the Community Player role", color=discord.Color.red(),
                                      description="You are DMing this bot right now. Roles do not exist in DMs. Use this command on a server.")
                await ctx.channel.send(embed=embed)
            elif result == 'role not found':  # Role has not been found on the server
                embed = discord.Embed(title="Could not add/remove the Community Player role", color=discord.Color.red(),
                                      description="AVIONICS did not recognize any roles named 'Community Player' on this server.")
                await ctx.channel.send(embed=embed)
            elif result == 'removed':  # Role has been found, will remove it from the user
                embed = discord.Embed(title=f"Community Player Role removed from {ctx.author}", color=self.client.embed_color,
                                      description="You will no longer receive notifications about UDB games.")
                await ctx.channel.send(embed=embed)
            elif result == 'added':  # Role has been found on the server, but not on the user. Adding it.
                embed = discord.Embed(title=f"Community Player Role added to {ctx.author}", color=self.client.embed_color,
                                      description="You will be notified when there are updates about UDB games.")
                await ctx.channel.send(embed=embed)

    @commands.command()
    async def followroll20(self, ctx, *message):
        """Either assigns or removes the Roll20 Sheet Follower role, based on whether or not you have it already"""
        result = await server_utils.toggle_group("roll20 sheet follower", ctx)

        if result == 'whisper':  # Role has not been found on the server
            embed = discord.Embed(title="Could not add/remove the Roll20 Sheet Follower role", color=discord.Color.red(),
                                  description="You are DMing this bot right now. Roles do not exist in DMs. Use this command on a server.")
            await ctx.channel.send(embed=embed)
        elif result == 'role not found':  # Role has not been found on the server
            embed = discord.Embed(title="Could not add/remove the Roll20 Sheet Follower role", color=discord.Color.red(),
                                  description="AVIONICS did not recognize any roles named 'Roll20 Sheet Follower' on this server.")
            await ctx.channel.send(embed=embed)
        elif result == 'removed':  # Role has been found, will remove it from the user
            embed = discord.Embed(title=f"Roll20 Sheet Follower Role removed from {ctx.author}", color=self.client.embed_color,
                                  description="You will no longer receive notifications when there are updates to the Roll20 Sheet")
            await ctx.channel.send(embed=embed)
        elif result == 'added':  # Role has been found on the server, but not on the user. Adding it.
            embed = discord.Embed(title=f"Roll20 Sheet Follower Role added to {ctx.author}", color=self.client.embed_color,
                                  description="You will be notified when there are updates to the Roll20 Sheet")
            await ctx.channel.send(embed=embed)

    @commands.command()
    async def followfoundry(self, ctx, *message):
        """Either assigns or removes the Roll20 Sheet Follower role, based on whether or not you have it already"""
        result = await server_utils.toggle_group("foundry sheet follower", ctx)

        if result == 'whisper':  # Role has not been found on the server
            embed = discord.Embed(title="Could not add/remove the Foundry Sheet Follower role",
                                  color=discord.Color.red(),
                                  description="You are DMing this bot right now. Roles do not exist in DMs. Use this command on a server.")
            await ctx.channel.send(embed=embed)
        elif result == 'role not found':  # Role has not been found on the server
            embed = discord.Embed(title="Could not add/remove the Foundry Sheet Follower role",
                                  color=discord.Color.red(),
                                  description="AVIONICS did not recognize any roles named 'Foundry Sheet Follower' on this server.")
            await ctx.channel.send(embed=embed)
        elif result == 'removed':  # Role has been found, will remove it from the user
            embed = discord.Embed(title=f"Foundry Sheet Follower Role removed from {ctx.author}",
                                  color=self.client.embed_color,
                                  description="You will no longer receive notifications when there are updates to the Roll20 Sheet")
            await ctx.channel.send(embed=embed)
        elif result == 'added':  # Role has been found on the server, but not on the user. Adding it.
            embed = discord.Embed(title=f"Foundry Sheet Follower Role added to {ctx.author}",
                                  color=self.client.embed_color,
                                  description="You will be notified when there are updates to the Roll20 Sheet")
            await ctx.channel.send(embed=embed)

    @commands.command()
    async def playtest(self, ctx, *message):
        """Either assigns or removes the Roll20 Sheet Follower role, based on whether or not you have it already"""
        result = await server_utils.toggle_group("playtester", ctx)

        if result == 'whisper':  # Role has not been found on the server
            embed = discord.Embed(title="Could not add/remove the Playtester role",
                                  color=discord.Color.red(),
                                  description="You are DMing this bot right now. Roles do not exist in DMs. Use this command on a server.")
            await ctx.channel.send(embed=embed)
        elif result == 'role not found':  # Role has not been found on the server
            embed = discord.Embed(title="Could not add/remove the Playtester role",
                                  color=discord.Color.red(),
                                  description="AVIONICS did not recognize any roles named 'Playtester' on this server.")
            await ctx.channel.send(embed=embed)
        elif result == 'removed':  # Role has been found, will remove it from the user
            embed = discord.Embed(title=f"Playtester Role removed from {ctx.author}",
                                  color=self.client.embed_color,
                                  description="You will no longer receive notifications when there are things to playtest.")
            await ctx.channel.send(embed=embed)
        elif result == 'added':  # Role has been found on the server, but not on the user. Adding it.
            embed = discord.Embed(title=f"Playtester Role added to {ctx.author}",
                                  color=self.client.embed_color,
                                  description="You will be notified when someone has a something they would like to playtest.")
            await ctx.channel.send(embed=embed)

    @commands.command()
    async def getavionics(self, ctx, *message):
        embed = discord.Embed(title="Add this bot to your own server!",
                              color=self.client.embed_color,
                              description='https://discordapp.com/oauth2/authorize?client_id=434493327279259648&permissions=268445760&scope=bot')
        await ctx.channel.send(embed=embed)

def setup(client):
    client.add_cog(Server(client))
