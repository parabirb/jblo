import discord
import random
from discord.ext import commands
import datetime

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

    # Message sent when Diablo joins.
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        embed=discord.Embed(
            title="Thanks for adding Diablo!",
            description=f"Thanks for adding Diablo to {guild.name}, here's some information on Diablo:",
            color=0x7289da,
            timestamp=datetime.datetime.utcnow()
        )
        embed.add_field(
            name='About Diablo',
            value='Diablo is an open-source public discord ban bot. '
                  'In simpler terms: Diablo uses data submitted by users to create a safer environment for all discord users in servers that have Diablo installed.'
                  'This means the average user can report certain users which they believe are breaking our guidelines (and Discord TOS) '
                  'and we will potentially add them to our global database of offenders. '
                  'If you want an exact number of offenders on Diablo, you can run `d.offenders` to get an exact number.',
            inline=False
        )
        embed.add_field(
            name='Diablo Reporting',
            value="You can run the command `d.report` and you will receive a DM from the bot asking you to fill out a form. "
                  "Once you fill out the submission, our mods will be right at work to determine if the person you reported breaks our guidelines and/or Discord TOS.",
            inline=False
        )
        embed.add_field(
            name='Bot Prefix',
            value="The bot prefix is: `d.`",
            inline=False
        )
        embed.set_image(url='https://i.imgur.com/Z6swN2y.png')
        send_channel = guild.text_channels[0]
        await send_channel.send(embed=embed)

    # pingy schmingy
    @commands.command()
    @commands.guild_only()
    async def ping(self, ctx):
        embed=discord.Embed(title="Pong!", description=f'**Returned at:** {round(self.client.latency * 1000)}ms', color=0x7289da)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def whois(self, ctx, member : discord.Member):
        embed=discord.Embed(title=f"{member}'s Information",
                            color=0x7289da)
        embed.set_thumbnail(
            url=member.avatar_url
        )
        embed.add_field(name='User ID:', value=member.id, inline=False)
        embed.add_field(name='Nickname:', value=member.display_name, inline=False)
        embed.add_field(name='Joined server at:', value=member.joined_at, inline=False)
        embed.add_field(name='Created at:', value=member.created_at, inline=False)
        await ctx.send(embed=embed)
    @whois.error
    async def whois_error(self, ctx, error):
            if isinstance(error, commands.MissingRequiredArgument):
                embed = discord.Embed(title=f"{ctx.author}'s Information",
                                      color=0xFBFBFB)
                embed.set_thumbnail(
                    url=ctx.author.avatar_url
                )
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
        embed=discord.Embed(
            title="About",
            description="**DIABLO** is an acronym that stands for **Database Influenced Automated Ban List of Offenders.** Its purpose is to prevent predators such as zoophiles and pedophiles from joining servers with Diablo, preventing any potential harm to people who may be at risk. Diablo also serves as data collection, so we can create one of the most extensive ban lists on Discord to prevent as many predatory incidents as possible. Think of it as this way- what would be more efficient: curing an illness or preventing an illness? We believe prevention is the right course of action, because we can stop many incidents from occuring.",
            color=0x7289da
        )
        embed.add_field(name="DIABLO", value="A project by incipious", inline=False)
        await ctx.send(None, embed=embed)

    # Source Link
    @commands.command()
    @commands.guild_only()
    async def source(self, ctx):
        embed=discord.Embed(title="Source", url="https://github.com/incipious/DIABLO", description="Here's the source link for Diablo.", color=0x7289da)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Basic(client))
