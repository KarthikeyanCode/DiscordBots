#API using python for discord bot
import asyncio
import os
from os import link, path
import discord
import time
from discord import file
from discord import message
from discord.ext import commands
from discord.ext import tasks
from discord import Embed
import random
import requests
import aiohttp
import string
import json
from PIL import Image

bot = commands.Bot(command_prefix='$')
client = discord.Client()

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.event
async def on_message(msg):
    if msg.author == bot.user:
        pass
    elif msg.content.startswith("$help"):
        await msg.channel.send('''The available commands are (prefix is $):
        1.hello
        2.life
        3.choose
        4.rimage
        5.rgif
        6.roll_die
        7.flip_coin\n''')
    else:
        await bot.process_commands(msg)

@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")

@bot.command()
async def life(ctx):
    await ctx.send("Yes this life :(\n")

@bot.command()
async def choose(ctx, *args):
    await ctx.send("Its better to {0}".format(random.choice(args)))

@bot.command()
async def cool(ctx, arg):
    list_1 = ["Cool", "Not Cool"]
    await ctx.send("{0} is {1}".format(arg, random.choice(list_1)))

@bot.command()
async def rimage(ctx):
    async with aiohttp.ClientSession() as session:
        request = await session.get("https://source.unsplash.com/random")
    request = str(request)
    url = ""
    key = 0
    for var in request:
        if(var == '('):
            key = 1
            continue
        elif(var == ')'):
            break
        elif(key==1):
            url = url + var
        else: 
            continue
    #print(url)
    image = discord.Embed(
        title = "Random Image",
        description = "",
        colour = discord.Colour.purple()
    )
    image.set_image(url = url)
    image.set_footer(text = "")
    await ctx.send(embed = image)

@bot.command()
async def rgif(ctx):
    gif_list = ["https://tenor.com/view/monke-monkey-monke-army-monke-swag-buy-gif-20219369", 
                "https://tenor.com/view/cool-monkey-gangster-shades-on-swag-gif-15768048",
                "https://tenor.com/view/david-monke-david-gaming-gaming-monke-gaming-gif-19468007",
                "https://tenor.com/view/monke-monkey-discord-pfp-pfp-monkeys-gif-21010625",
                "https://tenor.com/view/monkey-funny-monke-funny-monkey-monke-gif-22117277",
                "https://tenor.com/view/swag-monkey-gang-gif-19286871"]
    await ctx.send(random.choice(gif_list))

@bot.command()
async def roll_die(ctx):
    command_user = ctx.author.mention
    async with ctx.typing():
        await ctx.send("Rolling a die.. :game_die:")
        await ctx.send("Result of your roll {0}: {1}".format(command_user,random.randint(1,6)))

@bot.command()
async def flip_coin(ctx):
    command_user = ctx.author.mention
    sample_space_coin = ["Head", "Tail"]
    async with ctx.typing():
        await ctx.send("Flipping a coin.. :coin:")
        await ctx.send("Result of your flip {0}: {1}".format(command_user, random.choice(sample_space_coin)))

@bot.command()
async def ping(ctx):
    before = time.monotonic()
    message = await ctx.send("My heart beat is ...")
    latency = int((time.monotonic()-before)*1000)
    await message.edit(content="My heart beat is ... `{0}ms`".format(latency))

if __name__ == "__main__":

    bot.run('token')
