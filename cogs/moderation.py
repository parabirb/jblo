import discord
from discord.ext import commands

class Moderation(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Kick command
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *,  reason=None):
        await member.kick(reason=reason)
        embed=discord.Embed(title=f"{member} Kicked", description=f"{member} was kicked for {reason}", color=000000)
        embed.add_field(name="DIABLO", value="Moderation", inline=False)
        await ctx.send(embed=embed)
    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send("Please indicate a user.")

    # Ban
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *,  reason=None):
        await member.ban(reason=reason)
        embed=discord.Embed(title=f"{member} Banned", description=f"{member} was banned for {reason}", color=000000)
        embed.add_field(name="DIABLO", value="Moderation", inline=False)
        await ctx.send(embed=embed)
    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send("Please indicate a user.")

    # unban
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                embed=discord.Embed(title=f"{member} was unbanned.", description=f"{member} was unbanned banned from the server.", color=000000)
                embed.add_field(name="DIABLO", value="Moderation", inline=False)
                await ctx.send(embed=embed)
                return

    # mute
#    @commands.command()
#    @command.has_permissions(mute_members=True)
#    async def mute(self, ctx, member : discord.Member, *, time : discord.time):
#        role = self.discord.utils.get(member.server.roles, name='Muted')
#        await member.mute(time=time)
#        await ctx.send(f"**{member}** was muted for {time}")

def setup(client):
    client.add_cog(Moderation(client))
