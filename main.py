from dotenv import load_dotenv
import os, sys, traceback
import discord
from discord.ext import commands


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

print(TOKEN)
client.run(TOKEN)