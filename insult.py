from os import environ
import discord
from dotenv import load_dotenv
import random

load_dotenv()
TOKEN = environ['DISCORD']

client = discord.Client()

insultFile = open('static/insults.txt')
insults = list(insultFile)
insultFile.close()

@client.event
async def on_ready():
    print(f'{client.user} has connected')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    insultToSend = random.choice(insults).strip()
    if message.content.startswith('!insult'):
        name = message.content.split(' ')[1]
        response = "Hey "+name+", "+insultToSend
        await message.channel.send(response)

client.run(TOKEN)