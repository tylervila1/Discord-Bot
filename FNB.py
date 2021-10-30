import os
import discord
from discord.ext import commands
import random as r
import aiohttp

def bot_commands():
    # Make sure you create text files for your Virustotal API key and bot token in this same directory this script runs so it can read it.
    bot = commands.Bot(command_prefix = '!')
    token = open("token.txt","r").read()
    discord_rules = open("rules.txt","r").read()
    dcommands = open("dcommands" , "r").read()


# Ready message for bot client which will output to the terminal showing that its runnning
    @bot.event
    async def on_ready():
        print(f"Remember, with great power comes great responsibility")

    @bot.event
    async def on_member_join(member):
        # channel id Change this and hide the id to read from file
        embed = discord.Embed(colour=0x95efcc,description=f"Welcome!, You are the {len(list(member.guild.members))} member!")
        embed.set_thumbnail(url=f"{member.avatar_url}")
        embed.set_author(name=f"{member.name}", icon_url=f"{member.avatar_url}")
        embed.set_footer(text=f"{member.guild}", icon_url=f"{member.guild.icon_url}")

    @bot.command()
    async def hello(ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://youtu.be/9iA1YWbdAKI") as r:
                await ctx.send(r.url)
    @bot.command()
    async def toasted (ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://media0.giphy.com/media/xUySTIzc2BkMmQ9Zo4/giphy.gif?cid=790b76110cd380c7685c073e055b19996fc300904d83b8b2&rid=giphy.gif&ct=g") as r:
                await ctx.send(r.url)

    @bot.command()
    async def rem (ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://i.imgur.com/afavvqK.jpg") as r:
                await ctx.send(r.url)

    @bot.command()
    async def fuckyou(ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://i.imgur.com/GukszoE.png") as r:
                await ctx.send(r.url)

#ask a random question command.
    @bot.command()
    async def botterman (ctx, *question):
        responses = ['It is certain.',
                     'It is decidedly so.',
                     'Without a doubt.',
                     'Yes – definitely.',
                     'You may rely on it.',
                     'As I see it, yes.',
                     'Most likely.',
                     'Outlook good.',
                     'Yes.',
                     'Signs point to yes.',
                     'Reply hazy, try again.',
                     'Ask again later.',
                     'Better not tell you now.',
                     'Cannot predict now.',
                     'Concentrate and ask again.',
                     'Dont count on it',
                     'My reply is no.',
                     'My sources say no.',
                     'Outlook not so good.',
                     'Very doubtful.']
        await ctx.send(f'``Answer: {r.choice(responses)}``')

    @bot.command()
    async def command (ctx):
        await ctx.send(dcommands)




    @bot.command()
    async def food(ctx, *question):
        responses = ['Mexican Food.',
                     'Italian Cuisine.',
                     'Indian Food.',
                     'Cajun Food.',
                     'Soul Food.',
                     'Thai Food.',
                     'Greek Cuisine.',
                     'Chinese Food.',
                     'Lebanese Cuisine.',
                     'Japanese Cuisine.',
                     'American Food.',
                     'Moroccan Food.',
                     'Mediterranean Cuisine.',
                     'French Food.',
                     'Spanish Cuisine.',
                     'German Food',
                     'Korean Food.',
                     'Vietnamese Food.',
                     'Turkish Cuisine.',
                     'Caribbean Food.']
        await ctx.send(f'``Answer: {r.choice(responses)}``')

    @bot.command()
    async def random(ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://picsum.photos/400/400") as r:
                await ctx.send(r.url)

    bot.run(token)
bot_commands()
