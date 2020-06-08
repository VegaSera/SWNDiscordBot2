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
        """`{prefix}about` - About this bot"""
        embed = discord.Embed(title="About This Bot",
                              color=self.client.embed_color,
                              description="This bot is the second iteration of a discord bot written by Vega Sera. "
                                          "Below you'll find a number of frequently asked questions.")
        embed.add_field(
            name='What is the bot written in?',
            value=f"Currently running on:\nPython version: {platform.python_version()}\n"
                  f"Discord Version: {str(discord.__version__)}",
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
        """`{prefix}megajim` - Gives an easy way to search for the Ballad of Mega Jim"""
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
        embed = discord.Embed(title="This Bot on Github",
                              color=self.client.embed_color,
                              description='https://github.com/VegaSera/SWNDiscordBot2/')
        embed.set_footer(text="Please do not judge me too hard. I'm just a boy. A 3X year old boy.")
        await ctx.channel.send(embed=embed)

    @commands.command()
    async def abnegation(self, ctx):
        """`{prefix}abnegation` - Gives a link to the Revised version of the Abnegation discipline, adapted by Vega Sera"""
        embed = discord.Embed(title="Abnegation for Revised", color=self.client.embed_color,
                              description="Abnegation was original featured in Cult of the Wraith for Other Dust, "
                                          "which operates on the 1st edition psychic rules.\n\n"
                                          "It has since been adapted to SWN Revised by Vega Sera.\n\n\n"
                                          "https://docs.google.com/document/d/16YrjPPz_tZxZGMnKDr14g8b2Of_7NmLqcuBu5oyd7R0/edit?usp=sharing")
        await ctx.channel.send(embed=embed)

    @commands.command()
    async def teratogenics(self, ctx):
        """`{prefix}teratogenics` - Gives a link to the Revised version of the Teratogenics discipline, adapted by Vengeful"""
        embed = discord.Embed(title="Teratogenics for Revised", color=self.client.embed_color,
                              description="Teratogenics was original featured in Cult of the Still Lady for Other Dust, "
                                          "which operates on the 1st edition psychic rules.\n\n"
                                          "It has since been adapted to SWN Revised by Vengeful.\n\n\n"
                                          "https://docs.google.com/document/d/1qwvqp563CadMU865eg9kzn45bEcdmjht70ZoEU-9f4w/edit?usp=sharing")
        await ctx.channel.send(embed=embed)

    @commands.command(hidden=True)
    async def judication(self, ctx):
        """`{prefix}judication` - Explains why Judication is not adapted for revised despite Teratogenics and Abnegation being adapted"""
        embed = discord.Embed(title="Judication for Revised", color=self.client.embed_color,
                              description="Judication was originally featured in the Mandate Archives 2011: The "
                                          "Judicators.\n\nThis is not a free supplement, and as such, Judication will "
                                          "not be publicly adapted for Revised.")
        await ctx.channel.send(embed=embed)




def setup(client):
    client.add_cog(Misc(client))