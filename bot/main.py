import discord
import os

COMMAND_SYMBOL = '.'

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(COMMAND_SYMBOL + 'ping'):
        await message.channel.send('pong')


client.run(os.getenv('BOT_TOKEN'))
