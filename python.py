import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print("I'm in")
    print(client.user)
    
@client.event  
async def on_message(message):
     if "bad" in message.content:
           await client.send_message(message.channel, 'no u')


        



client.run(os.getenv('TOKEN'))
