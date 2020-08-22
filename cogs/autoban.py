import discord
from discord.ext import commands
import __main__

# STILL A WIP, NOTHING IS FUNCTIONAL

class Autoban(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    # MAIN BOT FUNCTION, AUTO KICKS OFFENDERS
    async def on_member_join(self, member):
        offense = __main__.serv.retrieveban(member.id)
        if offense:
            #if perhaps you wanted to send something to them, you'd do it here await member.send('...')
            await member.ban(reason=offense['reason'])
            embed = discord.Embed(title="`OFFENDER JOINED`", description=f"**{member.name}** has attempted to join the server, but was blocked by Diablo.\n**Reason**: {offense['reason']}", color=0xf7f7f7)
            await member.guild.channels[0].send(embed=embed) 
            """you should probably use client.get_channel(id) or 
            discord.utils.get(member.guild.channels, name='the channel name here')
            this just sends the message to the first channel is see's in the guild"""

    @commands.command()
    # report system, temp
    async def report(self, ctx):
        embed = discord.Embed(title="`REPORT`", description="Please use this link for temporary reporting purposes", url='FORM', color=0xf7f7f7)
        await ctx.author.send(embed=embed)

def setup(client):
    client.add_cog(Autoban(client))
