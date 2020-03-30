import discord
from discord.ext import commands

#TODO Allow help to be case insensitive, so .help random and .help Random return the same thing

#TODO Change function from working on the docstring to working from the short_desc and full_desc attributes

class Help(commands.Cog):
    """General Help Description"""

    def __init__(self, client):
        self.client = client
        self.hidden = False
        self.short_desc = "A help function"
        self.full_desc = ""
        print(self.client.embed_color)

    @commands.command(aliases='halp')
    # @commands.has_permissions(add_reactions=True,embed_links=True)
    async def help(self, ctx, *cog):
        """Gets all cogs and commands of mine."""
        try:
            if not cog:
                halp = discord.Embed(title='Cog Listing and Uncatergorized Commands',
                                     color=self.client.embed_color,
                                     description=f'Use `{self.client.command_prefix}help *cog*` to find out more '
                                                 f'about them!\n(BTW, the Cog Name Must Be in Title Case, '
                                                 f'Just Like this Sentence.)')
                cogs_desc = ''
                print(cogs_desc)
                for x in self.client.cogs:  # For every cog, we print the docstring
                    if not self.client.cogs[x].hidden:
                        print(f"{x} is not hidden")
                        cogs_desc += f'{x} - {self.client.cogs[x].__doc__}\n'
                    else:
                        print(f"{x} is hidden.")
                print(cogs_desc)
                halp.add_field(name='Modules', value=cogs_desc[0:len(cogs_desc) - 1], inline=False)
                cmds_desc = ''
                for y in self.client.walk_commands():  # For every uncategorized command, prints the docstring
                    if not y.cog_name and not y.hidden:
                        cmds_desc += ('{} - {}'.format(y.name, y.help) + '\n')
                if len(cmds_desc) > 6:
                    halp.add_field(name='Uncategorized Commands', value=cmds_desc[0:len(cmds_desc) - 1], inline=False)
                # await ctx.message.add_reaction(emoji='✉')
                await ctx.message.author.send('', embed=halp)
            else:
                if len(cog) > 1:
                    halp = discord.Embed(title='Error!', description='That is way too many cogs!',
                                         color=discord.Color.red())
                    await ctx.message.author.send('', embed=halp)
                else:
                    found = False
                    for x in self.client.cogs:
                        for y in cog:
                            if x == y:
                                halp = discord.Embed(title=cog[0] + ' Command Listing', color=self.client.embed_color,
                                                     description=self.client.cogs[cog[0]].__doc__)
                                for c in self.client.get_cog(y).get_commands():
                                    if not c.hidden:
                                        halp.add_field(name=c.name, value=c.help, inline=False)
                                found = True
                    if not found:
                        halp = discord.Embed(title='Error!', description='How do you even use "' + cog[0] + '"?',
                                             color=discord.Color.red())
                    else:
                        pass
                        # await ctx.message.add_reaction(emoji='✉')
                    await ctx.message.author.send('', embed=halp)
        except:
            print("SOMETHING MESSED UP IN HELP! HAAALP!")
            #pass


def setup(client):
    client.add_cog(Help(client))
