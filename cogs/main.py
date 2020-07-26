import discord
from discord.ext import commands, tasks
from itertools import cycle

# STILL A WIP, NOTHING IS FUNCTIONAL

class Main(commands.Cog):

    def __init__(self, client):
        self.client = client

#    offenders = cycle(libdiablo.webcheckban)

    #@tasks.loop(seconds=15)
    #async def main(self):


def setup(client):
    client.add_cog(Main(client))
