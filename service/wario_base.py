import discord
from discord.ext import commands
import json
import random
import argparse

parser = argparse.ArgumentParser(description='Bot around.')
parser.add_argument('--client_id')
args = parser.parse_args()

description = '''Wah?'''
bot = commands.Bot(command_prefix='war?', description=description)

RESPONSES = {}


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    for channel in bot.get_all_channels():
        if 'wario' in channel.name.lower():
            voice = await bot.join_voice_channel(channel)


@bot.listen()
async def on_message(message):
    for keyword in RESPONSES:
        if keyword.lower() in message.content.lower():
            await bot.send_message(message.channel, RESPONSES[keyword])
    if 'wario' in message.content.lower():
        await bot.send_message(message.channel, 'Wah\nWah\nWA' + 'H'*int(random.uniform(1,1000)))

    if 'mario' in message.content.lower():
        new_message = message.content.replace('mario', 'red wario').replace('Mario', 'Red Wario')
        if new_message != message.content:
            await bot.send_message(message.channel, new_message)


@bot.command()
async def update():
    await bot.say('Updated')


@bot.command()
async def add(keyword: str, response: str):
    RESPONSES[keyword] = response
    await bot.say('Wah-dded response for \"%s\"' % keyword)

bot.run(args.client_id)
