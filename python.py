import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print("I'm in")
    print(client.user)


        



client.run(os.getenv('TOKEN'))
