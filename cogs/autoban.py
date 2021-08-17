import discord
from discord.ext import commands, tasks
from pymongo import MongoClient
from datetime import datetime
import asyncio

cluster = MongoClient('Redacted')
db = cluster["Redacted"]
collection = db["Redacted"]

diablocolor = 0x1551b3

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
            await ctx.guild.create_text_channel(
                name="diablobans",
                topic="Lists the offenders that join the server. :warning: MIGHT BE NSFW, DISABLE AT OWN RISK.",
                overwrites=overwrites,
                nsfw=True
            )
            embed = discord.Embed(
                description=":thumbsup: Channel successfully created. The server will be notified if an offender joins.",
                color=diablocolor,
                timestamp=datetime.utcnow()
            )
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                description=':octagonal_sign:  A diablobans channel already exists.',
                color=0xCD1F1F)
            await ctx.send(embed=embed)

    # Automatic ban on database offenders, triggered by user join.
    @commands.Cog.listener()
    async def on_member_join(self, member : discord.Member):
        offense = collection.find_one({"userid":member.id})

        if offense is not None:
            await member.ban(reason=offense["reason"])
            bans_channel = discord.utils.get(member.guild.text_channels, name='diablobans')
            if bans_channel is None:
                overwrites = {
                    member.guild.default_role: discord.PermissionOverwrite(send_messages=False)
                }
                bans_channel = await member.guild.create_text_channel(
                    name="diablobans",
                    topic="Lists the offenders that join the server. :warning: MIGHT BE NSFW, DISABLE AT OWN RISK.",
                    overwrites=overwrites,
                    nsfw=True
                )

            embed = discord.Embed(
                description=f'**{member}** has attempted to join the server, but was blocked by Diablo.',
                timestamp=member.joined_at,
                color=diablocolor
            )
            embed.set_thumbnail(url=member.avatar_url)
            embed.set_author(name='OFFENDER JOINED', icon_url=member.avatar_url)
            embed.add_field(name='Reason', value=str(offense["reason"]), inline=False)
            await bans_channel.send(embed=embed)
            
    # Total number of Diablo offenders
    @commands.command()
    @commands.guild_only()
    async def offenders(self, ctx):
        embed = discord.Embed(
            title=":axe: Offenders",
            description=f'There are exactly **{collection.count_documents({})} offenders** on Diablo.',
            color=diablocolor,
            timestamp=datetime.utcnow()
        )
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Autoban(client))
