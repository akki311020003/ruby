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
        
@client.event  
async def on_message(message):
     if "good" in message.content:
           await client.send_message(message.channel, 'My nature is based on your behaviour ;P') 
        
@client.event  
async def on_message(message):
     if "UCA is Crazy" in message.content:
           await client.send_message(message.channel, 'UCA is a crazy boiman')
        
 @client.event  
async def on_message(message):
     if "r!" in message.content:
           await client.send_message(message.channel, 'This is the Ruby Bot. Developed by Akshit, we are still in Beta Testing. Please DM Max Planck to provide suggestions in making the bot better. Mic drop.')       


        



client.run(os.getenv('TOKEN'))
