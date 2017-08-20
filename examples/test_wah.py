import discord
from discord.ext import commands
import random
import argparse

parser = argparse.ArgumentParser(description='Bot around.')
parser.add_argument('--client_id')
args = parser.parse_args()

description = '''Wah?'''
client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    
@client.event
async def on_message(message):
    if 'justice' in message.content.lower():
        await client.send_message(message.channel, 'http://www.nintendoworldreport.com/media/18935/4/1.jpg')
    if 'wario' in message.content.lower():
        await client.send_message(message.channel, 'Wah, wah, wa' + 'h'*int(random.uniform(1,1000)))

client.run(args.client_id)
