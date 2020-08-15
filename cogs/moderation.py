import discord
from discord.ext import commands

class Moderation(commands.Cog):

    def __init__(self, client):
        self.client = client

    # mute
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def mute(self, ctx, member : discord.Member):
        for roles in ctx.guild.roles:
            if discord.utils.get(ctx.guild.roles, name='Muted'):
                break
            else:
                await ctx.guild.create_role(name="Muted")
        muted_role = discord.utils.get(ctx.guild.roles, name='Muted')
        await member.add_roles(muted_role)
        embed = discord.Embed(description=f"{member.name} has been muted.", color=0xf7f7f7)
        await ctx.send(embed=embed)
    @mute.error
    async def mute_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed=discord.Embed(description="Please specify a user to mute.", color=0xCD1F1F)
            await ctx.send(embed=embed)
        elif isinstance(error, commands.BadArgument):
            embed=discord.Embed(description="Either tag the user you want to mute or be sure to check you wrote their name correctly.", color=0xCD1F1F)
            await ctx.send(embed=embed)

    # unmute
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def unmute(self, ctx, member : discord.Member):
        muted_role = discord.utils.get(ctx.guild.roles, name='Muted')
        if muted_role not in member.roles:
            embed = discord.Embed(description="User is not muted", color=0xCD1F1F)
            await ctx.send(embed=embed)
        else:
            await member.remove_roles(muted_role)
            embed = discord.Embed(description=f"{member.name} has been unmuted.", color=0xf7f7f7)
            await ctx.send(embed=embed)
    @unmute.error
    async def unmute_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed=discord.Embed(description="Please specify a user to unmute.", color=0xCD1F1F)
            await ctx.send(embed=embed)
        elif isinstance(error, commands.BadArgument):
            embed=discord.Embed(description="Either tag the user you want to mute or be sure to check you wrote their name correctly.", color=0xCD1F1F)
            await ctx.send(embed=embed)

    # Kick command
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *,  reason=None):
        await member.kick(reason=reason)
        embed=discord.Embed(title=f"{member.name} Kicked", description=f"{member} was kicked for {reason}", color=0xf7f7f7)
        await ctx.send(embed=embed)
    @kick.error
    async def kick_error(self, ctx, error):
            if isinstance(error, commands.MissingRequiredArgument):
                embed=discord.Embed(description="Please specify a user to kick.", color=0xCD1F1F)
                await ctx.send(embed=embed)
            elif isinstance(error, commands.BadArgument):
                embed=discord.Embed(description="Either tag the user you want to kick or be sure to check you wrote their name correctly.", color=0xCD1F1F)
                await ctx.send(embed=embed)

    # Ban
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *,  reason=None):
        await member.ban(reason=reason)
        embed=discord.Embed(title=f"{member.name} Banned", description=f"{member} was banned for {reason}", color=0xf7f7f7)
        await ctx.send(embed=embed)
    @ban.error
    async def ban_error(self, ctx, error):
            if isinstance(error, commands.MissingRequiredArgument):
                embed=discord.Embed(description="Please specify a user to ban.", color=0xCD1F1F)
                await ctx.send(embed=embed)
            elif isinstance(error, commands.BadArgument):
                embed=discord.Embed(description="Either tag the user you want to ban or be sure to check you wrote their name correctly.", color=0xCD1F1F)
                await ctx.send(embed=embed)

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
                embed=discord.Embed(title=f"{member.name} was unbanned.", description=f"{member.name} was unbanned banned from the server.", color=0xf7f7f7)
                await ctx.send(embed=embed)
                return
    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed=discord.Embed(description="Please specify a user to unban.", color=0xCD1F1F)
            await ctx.send(embed=embed)
        elif isinstance(error, commands.BadArgument):
            embed=discord.Embed(description="Make sure you wrote the user name and discriminator (tagline) correctly.", color=0xCD1F1F)
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Moderation(client))
