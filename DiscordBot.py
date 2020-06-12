#Discord server bot that responds to messages containing 'Dota' or 'Dodo' with random Dota 2 quotes 
import os
import random 
import discord 
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

#Printing out a message to let me know that the bot has connected successfully 
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


#Checking through incoming messages and replying with a quote if 'Dota' or 'Dodo' are found 
@client.event
async def on_message(message):
    if message.author == client.user:
        return
        
    dota_quotes = [
         '<:dota:1234>',
         'What if they get me?',
         'Time is the cruelest cut!',
         'SLITHERING!',
         'Can\'t sell while dead!',
         'Ooohhh yaahhh - look at it GO!',
         'For the CUBS!'
    ]
    
    if 'dota' in message.content.lower() or 'dodo' in message.content.lower():
        response = random.choice(dota_quotes)
        await message.channel.send(response)
        
client.run(TOKEN)