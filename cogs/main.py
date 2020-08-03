import discord
from discord.ext import commands
from libdiablo import diabloserv
import pymongo
from itertools import cycle

# STILL A WIP, NOTHING IS FUNCTIONAL

class Main(commands.Cog):

    def __init__(self, client):
        self.client = client

   # @commands.Cog.listener()
    # MAIN BOT FUNCTION, AUTO KICKS OFFENDERS
  #  async def on_member_join(self, ctx : discord.ctx, member : discord.Member, reason : diabloserv.reason):
   #     for x in diabloserv.checkban(member.id):
   #         if diabloserv.checkban(member.id) == member.id:
  #              await member.ban(reason=diabloserv.retrieveban(member.id).reason)
   #             await member.ban(reason=reason)
   #             embed = discord.Embed(title=f"Offender Joined", description=f"{member.name} has attempted to join the server, but was blocked by Diablo.\n**Reason**: {reason}", color=000000)
   #             await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Main(client))
