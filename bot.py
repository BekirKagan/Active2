import os
import discord
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('TOKEN')
intents = discord.Intents.default()
intents.message_content = True

CHANNEL_ID = 1008394768994283521
VOICE_CHANNEL_ID = 1008394768994283525
COMMAND_PREFIX = '!'


if __name__ == '__main__':
    client = discord.Client(intents=intents)


    @client.event
    async def on_ready():
        print('{} is running.'.format(client.user))


    @client.event
    async def on_message(ctx):
        if ctx.author == client.user:
            return
        
        if COMMAND_PREFIX in ctx.content:
            content = ctx.content[1:].lower()
            print("Content: {}".format(content))

            channel = ctx.channel
            print("Channel: {}".format(channel))

            if content == 'merhaba':
                await channel.send('Merhabalar!')

            elif content == 'kodları_ver':
                await ctx.author.send("Gönderdim kodları, geldi mi?")


    client.run(TOKEN)
