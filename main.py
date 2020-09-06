from dotenv import load_dotenv
import os
import discord
from discord.ext import commands

print(str(discord.__version__))

#Make sure you have an .env file in the root folder with your discord bot's token in it. You ain't havin' mine.
load_dotenv()
TOKEN = os.getenv("TOKEN")


client = commands.Bot(command_prefix="!")
client.embed_color = discord.Color.blue()


@client.command(hidden=True)
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")

@client.command(hidden=True)
async def unload(ctx, extension):
    """Unloads a function from the bot"""
    client.unload_extension(f"cogs.{extension}")

@client.command(hidden=True)
async def reload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    client.load_extension(f"cogs.{extension}")

client.remove_command('help')

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")


async def print_action(message):
    """Listener function to print useful information to us as people are using the bot, even in whispers"""
    if message.author == client.user:
        pass
    else:
        # TODO Make it so we're not getting EVERY message on the servers being printed.
        print(message.created_at, "-- Messaged by:", message.author, "-- Guild:", message.guild,
              "-- Message Channel:", message.channel, "-- Message content:", message.content)


async def moderator(message):
    banned_words = [] #Banned words to be added later
    admin_channel = None
    for banned in banned_words:
        if banned in message.content:
            for i in message.guild.channels:  # Gets an admin channel to post a report
                if str(i).startswith('admin'):
                    admin_channel = i.id
                    break
            if admin_channel is not None:
                channel = client.get_channel(admin_channel)
                embed = discord.Embed(title="Message automatically deleted and reported",
                                      color=discord.Color.red(),
                                      description=f"A message has automatically deleted by moderation tools at {message.created_at}. Details below.")
                embed.add_field(name="Offending User:", value=message.author)
                embed.add_field(name="In channel:", value=message.channel)
                embed.add_field(name="Reason", value=f"Particularly Offensive Language - {banned}")
                embed.add_field(name="Offending Message", value=message.content, inline=False)
                await channel.send(embed=embed)
                await message.author.send(embed=embed)
            await message.delete()

client.add_listener(print_action, 'on_message')

client.add_listener(moderator, 'on_message')





@client.event
async def on_ready():

    #Getting user count
    num_users = 0
    for server in client.guilds:
        num_users += len(server.members)

    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('Discord version: ' + str(discord.__version__))
    print(f'Connected to {len(client.guilds)} server{"s" if len(client.guilds) > 1 else ""} servicing {num_users} users')
    print('------')
    await client.change_presence(status=discord.Status.online,
                                 activity=discord.Game(name=f'#bot-commands | {client.command_prefix}help'))


client.run(TOKEN)
