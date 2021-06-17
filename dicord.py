import discord
import requests
import json

client = discord.Client()


def get_quotes():
    response = re


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("inspire"):
        await message.channel.send(get_quotes())


client.run("ODQ4OTU2NDA2OTQxMDg5ODI0.YLUKRA.QR4257VZMn5PY6dGyGBFprxHT-o")
