import discord
from discord.ext import commands
import json
import random
import argparse

parser = argparse.ArgumentParser(description='Bot around.')
parser.add_argument('--client_id')
args = parser.parse_args()

description = '''Wah?'''
client = discord.Client()
bot = commands.Bot(command_prefix='war?', description=description)

RESPONSES = {}

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    
@client.event
async def on_message(message):
    for keyword in RESPONSES:
        if keyword.lower() in message.content.lower():
            await client.send_message(message.channel, RESPONSES[keyword])
    if 'wario' in message.content.lower():
        await client.send_message(message.channel, 'Wah, wah, WA' + 'H'*int(random.uniform(1,1000)))

@bot.command()
async def update():
    global RESPONSES
    with open('wario.txt') as resource_file:
      RESPONSES = json.load(resource_file)
    await bot.say('Updated')

@bot.command()
async def add(keyword: str, response: str):
    RESPONSES[keyword] = response
    with open('data.txt', 'w') as resource_file:
        json.dump(RESPONSES, resource_file)
    await bot.say('Wah-dded response for ' + keyword)

client.run(args.client_id)
bot.run(args.client_id)
