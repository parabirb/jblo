import discord
from discord.ext import commands
from libdiablo import diabloserv

# STILL A WIP, NOTHING IS FUNCTIONAL

class Autoban(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    # MAIN BOT FUNCTION, AUTO KICKS OFFENDERS
    async def on_member_join(self, ctx, member : discord.Member, reason : diabloserv.retrieveban):
        if diabloserv.checkban():
            await member.ban(reason=reason)
            embed = discord.Embed(title="`OFFENDER JOINED`", description=f"**{member.name}** has attempted to join the server, but was blocked by Diablo.\n**Reason**: {reason}", color=0xf7f7f7)
            await ctx.send(embed=embed)

    @commands.command()
    # report system, temp
    async def report(self, ctx):
        embed = discord.Embed(title="`REPORT`", description="Please use this link for temporary reporting purposes", url='FORM', color=0xf7f7f7)
        await ctx.author.send(embed=embed)

def setup(client):
    client.add_cog(Autoban(client))
