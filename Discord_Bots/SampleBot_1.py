#Simple discord bot
from os import link
import discord
from discord.ext import commands
from discord import Embed
import random
import requests
import aiohttp
import string
import json

# client = discord.Client()

bot = commands.Bot(command_prefix='$')
#client = discord.Client()

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
        4.rimage\n''')
    else:
        await bot.process_commands(msg)

# @bot.command()
# async def test(ctx, arg):
#     for i in range (0, 10):
#         await ctx.send(arg)

# @bot.command()
# async def Help(ctx):
#     await ctx.send('''The available commands are (prefix is $):
#     1.hello
#     2.life
#     3.choose\n''')

@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")

@bot.command()
async def life(ctx):
    await ctx.send("Yes this life :(\n")

@bot.command()
async def choose(ctx, *args):
    await ctx.send("Its better to {0}".format(random.choice(args)))

#link_var = "".join(random.choices(string.ascii_uppercase + string.digits, k = 7))
# link_var = "random"
# link = f"https://source.unsplash.com/1600x900/?{link_var}"

@bot.command()
async def rimage(ctx):
    # response = requests.get("https://source.unsplash.com/random/800x600")
    # data = response.json()
    #using unsplash opensource API
    async with aiohttp.ClientSession() as session:
        request = await session.get("https://source.unsplash.com/random")
        #print(request)
        #randomjson = await request.json(content_type="image/jpeg")
        #url = json.loads(request)[0]["url"]
    request = str(request)
    #print(request)
    #Extracting the image url from GET response
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
    # link_var = "random"
    # link = f"https://source.unsplash.com/1600x900/?{link_var}"
    #image.set_image(url = randomjson["link"])
    image.set_image(url = url)
    image.set_footer(text = "")
    await ctx.send(embed = image)
    

bot.run('token')
