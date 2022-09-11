import discord
import os


# pull these environment variables
DISCORD_TOKEN = os.environ['DISCORD_TOKEN']
SERVER_ID = os.environ['SERVER_ID']
TEXT = os.environ['TEXT']

# configure the discord library
intents = discord.Intents.default()
intents.typing = False
intents.presences = False

# initialize the client
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    channels = {str(channel): channel for channel in client.get_all_channels()}
    channel = channels['general']

    await channel.send(TEXT)

    # kill the discord bot, exit the code, and don't raise an error - hacky I know, but it works
    os._exit(0)


if __name__ == "__main__":
    client.run(DISCORD_TOKEN)