from dotenv import load_dotenv
import os, sys, traceback
import discord
from discord.ext import commands
import asyncio


#Make sure you have an .env file in the root folder with your discord bot's token in it. You ain't havin' mine.
load_dotenv()
TOKEN = os.getenv("TOKEN")


client = commands.Bot(command_prefix=".")
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
        print(message.created_at, "-- Messaged by:", message.author, "-- Guild:", message.guild,
              "-- Message Channel:", message.channel, "-- Message content:", message.content)

#TODO Slur deleter and reporter

async def moderator(message):
    banned_words = ['banana']
    if any(x in message.content for x in banned_words):
        print(f"-=-=-NAUGHTY WORD DETECTED-=-=- by: {message.author} in server:{message.guild} channel:{message.channel} - - Message with bad words - {message.content}")

client.add_listener(print_action, 'on_message')

client.add_listener(moderator, 'on_message')


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    # print("DO NOT PUSH WITH THIS VISIBLE - TOKEN: ", TOKEN)
    print('Discord version: ' + str(discord.__version__))
    print('------')
    await client.change_presence(status=discord.Status.online, activity=discord.Game(name='#bot-commands | !help'))


client.run(TOKEN)
