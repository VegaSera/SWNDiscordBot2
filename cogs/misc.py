from discord.ext import commands
import discord
import platform



class Misc(commands.Cog):
    """Commands related to the Dice rolling function"""
    def __init__(self, client):
        self.client = client
        self.hidden = False
        self.short_desc = "Miscellaneous bot commands that don't fit anywhere else"
        self.full_desc = "A resting place for commands that don't fit anywhere else."


    @commands.command(aliases=['avionics'])
    async def about(self, ctx):
        """About this bot"""
        embed = discord.Embed(title="About This Bot",
                              color=self.client.embed_color,
                              description="This bot is the second iteration of a discord bot written by Vega Sera. "
                                          "Below you'll find a number of frequently asked questions.")
        embed.add_field(
            name='What is the bot written in?',
            value=f"Currently running on:\nPython version: {platform.python_version()}\nDiscord Version: {str(discord.__version__)}",
            inline=False)
        embed.add_field(
            name='Why AVIONICS? What does that mean?',
            value='This stands for Awesome Virtual Intelligence Of Nothing Important, Carrying-on, and Senselessness.\n'
                  "It's a horrific backronym, and the only reason I chose it is because of the letters 'VI' in it.",
            inline=False)
        embed.add_field(
            name='Who the hell is Mega Jim?',
            value=f"Type `{self.client.command_prefix}megajim` and enjoy having your entire life changed forever.",
            inline=False)
        embed.add_field(
            name='Is your code up on Github or somewhere else that I can look at it?',
            value=f"Yes it is. Type `{self.client.command_prefix}github` and try not to judge me too hard.",
            inline=False)


        await ctx.channel.send(embed=embed)

    @commands.command()
    async def megajim(self, ctx):
        """Gives an easy way to search for the Ballad of Mega Jim"""
        # TODO Make a check to see if it's on the SWN discord. If not, return a different message.
        embed = discord.Embed(title="The Ballad of Mega Jim",
                              color=self.client.embed_color,
                              description='If you want to read the Ballad of Mega Jim, copy and paste this into '
                                          'the Discord Search Bar:')
        embed.add_field(
            name='`during: 2018-01-16 hydraulic`',
            value=' \nThe search phrase does not have to make sense, but rest assured it will lead you there.\n ')
        embed.set_footer(text='Keep in mind this only works on the Stars Without Number community Discord.')

        await ctx.channel.send(embed=embed)

    @commands.command(hidden=True)
    async def github(self, ctx):
        """Gives a link to view the bot's source code on Github"""
        # TODO Link to this bots repo on Github
        pass




def setup(client):
    client.add_cog(Misc(client))