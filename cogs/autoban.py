import discord
from discord.ext import commands
from pymongo import MongoClient

cluster = MongoClient('nice try')
db = cluster["DIABLO"]
collection = db["Offender List"]

class Autoban(commands.Cog):

    def __init__(self, client):
        self.client = client

    # specify a channel where you want diablo log messages
    @commands.command()
    @commands.has_permissions(administrator=True)
    @commands.guild_only()
    async def diablobans(self, ctx):
        bans_channel = discord.utils.get(ctx.guild.text_channels, name='diablobans')
        if not bans_channel:
            overwrites = {
                ctx.guild.default_role: discord.PermissionOverwrite(send_messages=False)
            }
            await ctx.guild.create_text_channel(name="diablobans", topic="Lists the offenders that join the server. :warning: MIGHT BE NSFW, DISABLE AT OWN RISK.", overwrites=overwrites, nsfw=True)
            embed = discord.Embed(
                description=":thumbsup: Channel successfully created. The server will be notified if an offender joins.",
                color=0xFFC900)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                description=':octagonal_sign:  A diablobans channel already exists.',
                color=0xCD1F1F)
            await ctx.send(embed=embed)

    @commands.Cog.listener()
     # MAIN BOT FUNCTION, AUTO KICKS OFFENDERS
    async def on_member_join(self, member : discord.Member):
        offense = collection.find_one({"userid":member.id})
        if offense is not None:
            await member.ban(reason=offense["reason"])
            bans_channel = discord.utils.get(member.guild.text_channels, name='diablobans')
            if not bans_channel:
                overwrites = {
                    member.guild.default_role: discord.PermissionOverwrite(send_messages=False)
                }
                bans_channel = await member.guild.create_text_channel(name="diablobans", topic="Lists the offenders that join the server. :warning: MIGHT BE NSFW, DISABLE AT OWN RISK.", overwrites=overwrites, nsfw=True)
            embed = discord.Embed(title=":axe: `OFFENDER JOINED`", description=f'**{member.name}** has attempted to join the server, but was blocked by Diablo.\n`Reason`: **{offense["reason"]}**', color=0xf7f7f7)
            await bans_channel.send(embed=embed)

    @commands.command()
    # report system, temp
    async def report(self, ctx):
        embed = discord.Embed(title="`REPORT`", description="Please use this link for temporary reporting purposes", url='not posting url', color=0xf7f7f7)
        await ctx.author.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def offenders(self, ctx):
        offenders = collection.count_documents({})
        embed = discord.Embed(title=":axe: Offenders", description=f'There are exactly **{offenders} offenders** on Diablo.', color=0xf7f7f7)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Autoban(client))
