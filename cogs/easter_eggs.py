from discord.ext import commands
import discord
from cogs.utils.word_tables import SillyAdjTable
import random

class Easter_Eggs(commands.Cog):
    """Congratulations, you looked at the source code and found some easter
    eggs that don't show up in typical !help messages. Do with them as you please."""
    def __init__(self, client):
        self.hidden = True  # Easter eggs are meant to be hidden. If you unhide this, it will unhide everything here.
        self.client = client
        self.short_desc = "A number of hidden easter egg functions"
        self.full_desc = "A number of hidden easter egg functions that dont make sense to clutter the normal groups with."

    @commands.command()
    async def rollplant(self, ctx):
        """Typo of !rollplanet. Redirecting."""
        plant = discord.Embed(title="Random Plant",
                              color=self.client.embed_color,
                              description=f"{random.choice(SillyAdjTable)} Ficus")
        plant.add_field(name=f"Plant History:",
                        value=f"{random.choice(['Exceptionally', 'Extremely', 'Immensely', 'Particularly', 'Abnormally'])}"
                              f" Boring\n\n"
                              f"You are probably looking for `{self.client.command_prefix}rollplanet` and typo'd.")
        await ctx.channel.send(embed=plant)

    @commands.command()
    async def rollplane(self, ctx):
        """Typo of !rollplanet. Redirecting."""
        plane = discord.Embed(title="Random Plane",
                              color=self.client.embed_color,
                              description=f"{random.choice(SillyAdjTable)} Glider")
        plane.add_field(name=f"Plane History:",
                        value=f"Engineer gave a {random.randint(77,101)}% chance of crashing.\n\n"
                              f"You are probably looking for `{self.client.command_prefix}rollplanet` and typo'd.")
        await ctx.channel.send(embed=plane)

    @commands.command()
    async def rollplan(self, ctx):
        """Typo of !rollplanet. Redirecting."""
        plan = discord.Embed(title="Random Plan",
                              color=self.client.embed_color,
                              description=f"{random.choice(SillyAdjTable)} Pincer Attack")
        plan.add_field(name=f"Plan History:",
                        value=f"{random.choice(['Disasterous', 'Catastrophic', 'Horrific', 'Surprisingly well at first, then the mouth of hell opened up.'])}\n\n"
                              f"You are probably looking for `{self.client.command_prefix}rollplanet` and typo'd.")
        await ctx.channel.send(embed=plan)

    @commands.command()
    async def smack(self, ctx):
        """Bot will smack the tagged person"""
        mess = ctx.content.split(' ', 1)[1]
        smack = discord.Embed(color=self.client.embed_color)
        smack.add_field(name="You have made someone very upset...",
                        value=f"*{mess} has been smacked by a robot hand!*")
        await ctx.channel.send(embed=smack)


def setup(client):
    client.add_cog(Easter_Eggs(client))

