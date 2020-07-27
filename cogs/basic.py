import discord
import random
from discord.ext import commands

class Basic(commands.Cog):

    def __init__(self, client):
        self.client = client

    #Events
    @commands.Cog.listener()
    # activation procedure
    async def on_ready(self):
        await self.client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game("WIP"))
        print('Activated!')

    # user join
    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f'{member} has joined the server.')
        await ctx.send(f'{member} has joined the server.')

    # user leave
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f'{member} has left the server.')
        await ctx.send(f'{member} has left the server.')

    # pingy schmingy
    @commands.command()
    async def ping(self, ctx):
        embed=discord.Embed(title="Pong!", description=f'**Returned at:** {round(self.client.latency * 1000)}ms', color=000000)
        await ctx.send(embed=embed)

    # ID (find the ID of an individual)
    @commands.command()
    async def userid(self, ctx, member : discord.Member):
        embed=discord.Embed(title=f"{member.name}'s ID:", description=f"{member.id}", color=000000)
        await ctx.send(embed=embed)

    # about
    @commands.command()
    async def about(self, ctx):
        embed=discord.Embed(title="About", description="**DIABLO** is an acronym that stands for **Database Influenced Automated Ban List of Offenders.** Its purpose is to prevent predators such as zoophiles and pedophiles from joining servers with Diablo, preventing any potential harm to people who may be at risk. Diablo also serves as data collection, so we can create one of the most extensive ban lists on Discord to prevent as many predatory incidents as possible. Think of it as this way- what would be more efficient: curing an illness or preventing an illness? We believe prevention is the right course of action, because we can stop many incidents from occuring.", color=000000)
        embed.add_field(name="DIABLO", value="A project by incipious", inline=False)
        await ctx.send(None, embed=embed)

    # Source Link
    @commands.command()
    async def source(self, ctx):
        embed=discord.Embed(title="Source", url="https://github.com/incipious/DIABLO", description="Here's the source link for Diablo.", color=000000)
        await ctx.send(embed=embed)

    # fun command I made because I got bored
    @commands.command()
    async def randomoffender(self, ctx):
        responses = ['Quantum_Kitty',
                    'Apaloosa',
                    'changed_mikey',
                    'Belladonna (shithead)_Zetta',
                    'chocobo13',
                    'DearestDoggie',
                    'paintedlykon',
                    'seby the fuckhead',
                    'the entire cast of zooier than thou',
                    'elle, stella, or whatever her bitchass name is',
                    'Jeffrey Epstein',
                    'Mickey Mouse',
                    'Forest Fire',
                    'ZooStories.farm',
                    'Lycaon',
                    'MilkyBella',
                    'Sweetest Sweets',
                    'Gitchep',
                    'Dario Fulminante']
        embed=discord.Embed(title="Random Offender", description=f'A random offender is: **{random.choice(responses)}**', color=000000)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Basic(client))
