import discord
import random
from discord.ext import commands

class Basic(commands.Cog):

    def __init__(self, client):
        self.client = client

    #Events
    @commands.Cog.listener()
    @commands.guild_only()
    # activation procedure
    async def on_ready(self):
        await self.client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game("September 19"))
        print('Activated!')

    # pingy schmingy
    @commands.command()
    @commands.guild_only()
    async def ping(self, ctx):
        embed=discord.Embed(title="Pong!", description=f'**Returned at:** {round(self.client.latency * 1000)}ms', color=0xf7f7f7)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    @commands.bot_has_guild_permissions()
    async def important(self, ctx):
        if ctx.author.id == 747964541664755762:
            embed = discord.Embed(title="`Important Announcement`", description="@everyone This is an important announcement from the bot developer, **incipious**. My main account (incipious#7492, ID: 179696307470991360) was deactivated. I am not revealing the terms of my ban, but I have a few issues at hand here. 1) Diablo is registered on my main account, but that shouldn't be an issue considering that I can always port over Diablo to a new token on a new account. I have filed an appeal with Discord but I am not expecting to regain access to my account anytime soon, so in the scenario that I don't get reinstated, we will have to remake the Diablo on my new account plus a new token. Don't worry, I have all the code saved on my computer so no progress will be lost. I will fill you in more once I get more information.",color=0xf7f7f7)
            await ctx.send(embed=embed)

    # ID (find the ID of an individual)
    @commands.command()
    @commands.guild_only()
    async def userid(self, ctx, member : discord.Member):
        embed=discord.Embed(title=f"{member.name}'s ID:", description=f"{member.id}", color=0xf7f7f7)
        await ctx.send(embed=embed)
    @userid.error
    async def userid_error(self, ctx, error):
            if isinstance(error, commands.MissingRequiredArgument):
                embed=discord.Embed(title=f"{ctx.author.name}'s ID:", description=f"{ctx.author.id}", color=0xf7f7f7)
                await ctx.send(embed=embed)
            if isinstance(error, commands.BadArgument):
                embed=discord.Embed(description="Be sure check that you wrote out the name correctly.", color=0xCD1F1F)
                await ctx.send(embed=embed)

    # about
    @commands.command()
    @commands.guild_only()
    async def about(self, ctx):
        embed=discord.Embed(title="About", description="**DIABLO** is an acronym that stands for **Database Influenced Automated Ban List of Offenders.** Its purpose is to prevent predators such as zoophiles and pedophiles from joining servers with Diablo, preventing any potential harm to people who may be at risk. Diablo also serves as data collection, so we can create one of the most extensive ban lists on Discord to prevent as many predatory incidents as possible. Think of it as this way- what would be more efficient: curing an illness or preventing an illness? We believe prevention is the right course of action, because we can stop many incidents from occuring.", color=000000)
        embed.add_field(name="DIABLO", value="A project by incipious", inline=False)
        await ctx.send(None, embed=embed)

    # Source Link
    @commands.command()
    @commands.guild_only()
    async def source(self, ctx):
        embed=discord.Embed(title="Source", url="https://github.com/incipious/DIABLO", description="Here's the source link for Diablo.", color=0xf7f7f7)
        await ctx.send(embed=embed)

    # fun command I made because I got bored
    @commands.command()
    @commands.guild_only()
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
        embed=discord.Embed(title="Random Offender", description=f'A random offender is: **{random.choice(responses)}**', color=0xf7f7f7)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Basic(client))
