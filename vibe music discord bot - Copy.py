import discord
import os


client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('v/vibe'):
        await message.channel.send('How is the vibe')

client.run(os.getenv('TOKEN'))        
        