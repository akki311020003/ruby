import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print("I'm in")
    print(client.user)


        
@client.event        
async def on_message(message):
     if "not" in message.content:
           await client.send_message(message.channel, 'yes' + message.content)


client.run(os.getenv('TOKEN'))
