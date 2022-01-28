from logging import raiseExceptions
from discord import channel, client
from discord.ext.commands import errors
from discord.ext.commands.core import command
import functions
import matplotlib.pyplot as plt

from discord.ext import commands
import discord

TOKEN = 'OTE4NTU0MDAxMTY1OTI2NDQx.YbI8Ew.o9UZ9xnmbPrEA-FkNUkv3de4AdY'

bot = commands.Bot(command_prefix='@')

client = discord.Client()

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

    await bot.get_channel(918793874485444628).send("Hello and welcome to Tutu and Danee\'s bot! \n Type @hi to get started")

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to Tutu and Danee\'s bot! \n Type @hi to get started.'
    )

@bot.command(name='hi', help=
        "Welcome to Tutu and Danee\'s bot!. \n Type @hi to get started",   
    )
async def about_bot(ctx):
    bot_info = [
        "Glad you are here!. \n",
        'Kindly enter the following commands: \n',
        '1. Type @season Fall, Summer, Winter or Spring to know the most loved fashion for a specific season. i.e @season Fall\n',
        '2. Type @top_selling "gender" to know the highest sales by gender. i.e @top_selling Men. The gender I can tell you about are Boys, Girls, Women, Men and Unisex\n',
        '3. Type @article_type "year" to know the top 5 loved fashion wears in a year. i.e @article_type 2010.\n',
        '4. Type @colour "gender" to know the favourite fashion colour by gender. i.e @colour Men.\n'
    ]
 
    await ctx.send("\n".join(bot_info))

@bot.command(name='article_type', help='The top 5 loved fashion wears in a year.')
async def articles(ctx, year:int):
    functions.article_type_freq(year)
    await ctx.send('This shows the top 5 loved fashion wears in ' + str(year),file=discord.File('images/articleType.png'))
    plt.clf

@bot.command(name='season', help='This shows the most loved fashion usage by season')
async def seasonal_wear(ctx, season):
    functions.season_wears(season)
    await ctx.send('This shows the most loved fashion usage in ' + season ,file=discord.File('images/Fashion_usage.png'))
    plt.clf

@bot.command(name='top_selling', help='This shows the top selling wears')
async def topSales(ctx, gender):
    functions.top_selling(gender)
    await ctx.send('This shows the top selling wears of the ' + gender,file=discord.File('images/Top_selling.png'))
    plt.clf

@bot.command(name='colour', help='This shows the favourite fashion colour by gender')
async def colour(ctx, gender):
    functions.best_colour(gender)
    await ctx.send('This shows the favourite fashion colour of the ' + gender ,file=discord.File('images/Colour.png'))
    plt.clf

#error handling

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.MissingRequiredArgument):
        await ctx.send('Kindly enter all the required parameters. Type @hi for guidance')

    elif isinstance(error,commands.CommandNotFound):
        await ctx.send('Sorry I do not understand. Type @hi to understand the commands to use')

    elif isinstance(error,commands.TooManyArguments):
        await ctx.send('Kindly enter all the required parameters. Type @hi for guidance')
    
    elif isinstance(error,commands.BadArgument):
        await ctx.send('Kindly ensure that you typed the correct parameters. Type @hi for guidance')

    elif isinstance(error,commands.CommandInvokeError):
        await ctx.send('Kindly check the spelling of the parameter. Type @hi for guidance')

    raise error

bot.run(TOKEN)