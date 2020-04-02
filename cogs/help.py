import discord
from discord.ext import commands


#TODO Help function fails silently too often

class Help(commands.Cog):
    """General Help Description"""

    def __init__(self, client):
        self.client = client
        self.hidden = False
        self.short_desc = "This help function"
        self.full_desc = "Longer help description with stuff!"

    @commands.command(aliases=['halp'])
    # @commands.has_permissions(add_reactions=True,embed_links=True)
    async def help(self, ctx, *cog):
        """Gets all cogs and commands that have been registered by the bot, and returns their short help files."""
        try:
            if not cog:
                halp = discord.Embed(title='Cog Listing and Uncatergorized Commands',
                                     color=self.client.embed_color,
                                     description=f'Use `{self.client.command_prefix}help *category*` to find out more '
                                                 f'about them!\nThink of these like folders '
                                                 f'for commands, to avoid clutter.')
                cogs_desc = ''
                print(cogs_desc)
                for x in self.client.cogs:  # For every cog, we print short_desc
                    if not self.client.cogs[x].hidden:
                        # print(f"{x} is not hidden")
                        cogs_desc += f'{x} - {self.client.cogs[x].short_desc}\n'
                    else:
                        pass
                        # print(f"{x} is hidden.")
                # print(cogs_desc)
                halp.add_field(name='Modules', value=cogs_desc[0:len(cogs_desc) - 1], inline=False)
                cmds_desc = ''
                for y in self.client.walk_commands():  # For every uncategorized command, prints the docstring
                    if not y.cog_name and not y.hidden:
                        cmds_desc += ('{} - {}'.format(y.name, y.help) + '\n')
                if len(cmds_desc) > 6:
                    halp.add_field(name='Uncategorized Commands', value=cmds_desc[0:len(cmds_desc) - 1], inline=False)
                # await ctx.message.add_reaction(emoji='✉')
                await ctx.message.channel.send('', embed=halp)
            else:
                if len(cog) > 1:
                    halp = discord.Embed(title='Error!',
                                         description="You specified too many help parameters.\n"
                                                     "If you're looking for help with a specific command, "
                                                     "it likely has it's own help modifier, for instance: "
                                                     f"`{self.client.command_prefix}rollcharacter help`",
                                         color=discord.Color.red())
                    await ctx.message.channel.send('', embed=halp)
                else:
                    found = False
                    for x in self.client.cogs:
                        for y in cog:
                            if x.lower() == y.lower():
                                print(cog[0].capitalize(), "cog help command invoked")
                                halp = discord.Embed(title=cog[0].capitalize() + ' Command Listing',
                                                     color=self.client.embed_color,
                                                     description=self.client.cogs[cog[0].capitalize()].full_desc)
                                for c in self.client.get_cog(y.capitalize()).get_commands():
                                    if not c.hidden:
                                        # Adds the docstring as the help.
                                        # Allows our docstrings to have a dynamic prefix
                                        c.help = c.help.format(prefix=self.client.command_prefix)
                                        halp.add_field(name=c.name, value=c.help, inline=False)
                                found = True
                    if not found:
                        halp = discord.Embed(title='Error!',
                                             description='If you are trying to access specific help for a command '
                                                         'called .' + cog[0] + ', you may want to try `.' + cog[0] +
                                                         ' help`\nOtherwise you may have simply misspelled what '
                                                         'you\'re looking for',
                                             color=discord.Color.red())
                    else:
                        pass
                        # await ctx.message.add_reaction(emoji='✉')
                    await ctx.message.channel.send('', embed=halp)
        except:
            # This is uninformative and fails silently. Need to fix this.
            print("SOMETHING MESSED UP IN HELP! HAAALP!")
            # pass

    @commands.command()
    async def bugreport(self, ctx):
        """`{prefix}bugreport` - Files a bug report. Be descriptive"""

        # Maybe have better handling in the future than writing to a text file.
        with open("logging/bugreport.txt", "a") as my_file:
            my_file.write(f"Bug Report created at {ctx.message.created_at}\n -- Author: {ctx.author}\n"
                          f" -- Guild: {ctx.guild}\n -- Channel: {ctx.channel}\n -- Bug: {ctx.message.content}\n"
                          f" -- Status: NEW\n -- Developer Comments: [] \n\n")
        bugrep = discord.Embed(name="Bug report received", color=self.client.embed_color)
        bugrep.set_footer(text="Bug Report Received")
        print("-=BUG REPORT RECEIVED=-")
        await ctx.channel.send(embed=bugrep)


def setup(client):
    client.add_cog(Help(client))
