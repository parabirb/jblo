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
    async def whois(self, ctx, member : discord.Member):
        embed=discord.Embed(title=f"{member}'s Information",
                            set_image=member.avatar_url,
                            color=0xFBFBFB)
        embed.add_field(name='User ID:', value=member.id, inline=False)
        embed.add_field(name='Nickname:', value=member.display_name, inline=False)
        embed.add_field(name='Joined server at:', value=member.joined_at, inline=False)
        embed.add_field(name='Created at:', value=member.created_at, inline=False)
        await ctx.send(embed=embed)
    @whois.error
    async def whois_error(self, ctx, error):
            if isinstance(error, commands.MissingRequiredArgument):
                embed = discord.Embed(title=f"{ctx.author}'s Information",
                                      set_image=ctx.author.avatar_url,
                                      color=0xFBFBFB)
                embed.add_field(name='User ID:', value=ctx.author.id, inline=False)
                embed.add_field(name='Nickname:', value=ctx.author.display_name, inline=False)
                embed.add_field(name='Joined server at:', value=ctx.author.joined_at, inline=False)
                embed.add_field(name='Created at:', value=ctx.author.created_at, inline=False)
                await ctx.send(embed=embed)
            if isinstance(error, commands.BadArgument):
                embed=discord.Embed(description=":octagonal_sign: Be sure check that you wrote out the name correctly.", color=0xCD1F1F)
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
