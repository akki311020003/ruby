import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print("I'm in")
    print(client.user)


        
@client.event        
async def on_message(message):
    if message.content.startswith('not')
           await client.send_message(message.channel, 'yes')


client.run(os.getenv('TOKEN'))
