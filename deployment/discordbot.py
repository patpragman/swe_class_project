import discord
import os
import sys

DISCORD_TOKEN = os.environ['DISCORD_TOKEN']
SERVER_ID = os.environ['SERVER_ID']
USER = os.environ['USER']

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    channels = {str(channel): channel for channel in client.get_all_channels()}
    channel = channels['general']

    await channel.send(f"Recent push to develop branch by {USER}")

    # kill the discord bot, exit the code, and don't raise an error - hacky I know, but it works
    os._exit(0)

client.run(DISCORD_TOKEN)