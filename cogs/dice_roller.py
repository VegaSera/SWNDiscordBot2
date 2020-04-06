from discord.ext import commands
import discord
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
    async def roll(self, ctx, *message):
        """Parses a dice string, and rolls it."""
        sent_help_message=False
        if len(message) > 0:  # Message is not empty.
            if message[0].lower() == "help":
                x = self.client.command_prefix
                embed = discord.Embed(title=f"{self.client.command_prefix}roll Help",
                                      color=self.client.embed_color,
                                      description="Currently the bot only accepts simple dice input, keep/drop, and modifiers.\n"
                                                  "Examples:\n"
                                                  f"`{x}roll 2d6` - Rolls two six-sided dice.\n"
                                                  f"`{x}roll 3d6d1` - Rolls three six-sided dice, and drops the lowest result from the total.\n"
                                                  f"`{x}roll 4d6k2` - Rolls four six-sided dice, and keeps only the highest two results for the total.\n"
                                                  f"`{x}roll 5d4+3` - Rolls five four-sided dice, and then adds three as a static modifier to that total.\n\n"
                                                  f"Example:`{x}roll 4d6d1+2d8-1d4+10-3` - Or any combination of dice and static modifiers.\n"
                                                  f"Fractions of dice, extradimensional or non-euclidian dice with a non-integer amount of sides will never be supported.(Use whole numbers only)\n"
                                                  f"Currently the bot only supports addition and subtraction as valid operators.")
                await ctx.channel.send(embed=embed)
                sent_help_message = True
            elif message[0].lower() == "character":  # !roll character should be !rollcharacter - Trolling the user.
                embed = discord.Embed(title=f"{self.client.command_prefix}roll Help",
                                      color=self.client.embed_color,
                                      description="**Error - Cannot roll a character as dice**\n"
                                                  "People are entirely too lumpy. They're like an inefficient d2.\n"
                                                  f"You're likely looking for `{self.client.command_prefix}rollcharacter` and typoed.")
                await ctx.channel.send(embed=embed)
                sent_help_message = True
            elif message[0].lower() == "planet":  # !roll character should be !rollcharacter - Trolling the user.
                embed = discord.Embed(title=f"{self.client.command_prefix}roll Help",
                                      color=self.client.embed_color,
                                      description="**Error - Cannot roll a planet as dice**\n"
                                                  "Have you ever actually used a physical d100? Damn thing never stops rolling. Imagine that but a billion times worse.\n"
                                                  f"You're likely looking for `{self.client.command_prefix}rollplanet` and typoed.")
                await ctx.channel.send(embed=embed)
                sent_help_message = True
            elif message[0].lower() == "race":  # !roll character should be !rollcharacter - Trolling the user.
                embed = discord.Embed(title=f"{self.client.command_prefix}roll Help",
                                      color=self.client.embed_color,
                                      description="**Error - Cannot roll a race as dice**\n"
                                                  "This could be considered a warcrime and thus is not allowed.\n"
                                                  f"You're likely looking for `{self.client.command_prefix}rollrace` and typoed.")
                await ctx.channel.send(embed=embed)
                sent_help_message = True
            elif message[0].lower() == "ship":  # !roll character should be !rollcharacter - Trolling the user.
                embed = discord.Embed(title=f"{self.client.command_prefix}roll Help",
                                      color=self.client.embed_color,
                                      description="**Error - Cannot roll a ship as dice**\n"
                                                  "You pick up the ship and attempt to roll it. It ignites its thrusters and vanishes into the void.\n"
                                                  f"You're likely looking for `{self.client.command_prefix}rollship` and typoed.")
                await ctx.channel.send(embed=embed)
                sent_help_message = True
            elif message[0].lower() == "npc":  # !roll character should be !rollcharacter - Trolling the user.
                embed = discord.Embed(title=f"{self.client.command_prefix}roll Help",
                                      color=self.client.embed_color,
                                      description="**Error - Cannot roll an NPC as dice**\n"
                                                  "You attempt to pick up and roll an NPC named Megajim. He gives you a scornful look and shakes his head in disappointment.\n"
                                                  f"You're likely looking for `{self.client.command_prefix}quick npc` and typoed.")
                await ctx.channel.send(embed=embed)
                sent_help_message = True
        elif len(message) == 0:
            embed = discord.Embed(title=f"Error",
                                  color=self.client.embed_color,
                                  description="You must specify the dice you want to roll.\n"
                                              f"Use `{self.client.command_prefix}roll help` if you need help in using this command.")
            await ctx.channel.send(embed=embed)
            sent_help_message = True


        if not sent_help_message:
            verbose = False
            if 'verbose' in message:
                message = str(message).replace('verbose', "")
                verbose = True


            bad_characters = [" ", "'", "(", ")", ","]
            for i in bad_characters:
                message = str(message).replace(i, "")  # Certain characters will break the parser
            result, result_string = parse_dice_string(str(message), verbose=verbose)

            rollresult = discord.Embed(color=self.client.embed_color)
            rollresult.add_field(name="Roll Result", value=f"{result_string} = **{result}**")
            await ctx.channel.send(embed=rollresult)





def setup(client):
    client.add_cog(Dice(client))