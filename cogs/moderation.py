import discord
from discord.ext import commands
from pymongo import MongoClient

cluster = MongoClient('lol')
db = cluster["lol"]
collection = db["lol"]

class Moderation(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.warnings_delete.start()

    # mute
    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    async def mute(self, ctx, member : discord.Member):
        if not (discord.utils.get(ctx.guild.roles, name="Muted")):
            await ctx.guild.create_role(name="Muted")
        muted_role = discord.utils.get(ctx.guild.roles, name='Muted')
        await member.add_roles(muted_role)
        embed = discord.Embed(description=f"{member.name} has been muted.", color=0x7289da)
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
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    async def unmute(self, ctx, member : discord.Member):
        muted_role = discord.utils.get(ctx.guild.roles, name='Muted')
        if muted_role not in member.roles:
            embed = discord.Embed(description="User is not muted", color=0xCD1F1F)
            await ctx.send(embed=embed)
        else:
            await member.remove_roles(muted_role)
            embed = discord.Embed(description=f"{member.name} has been unmuted.", color=0x7289da)
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
    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)
        embed=discord.Embed(title=f":boot: {member.name} Kicked", description=f"{member} was kicked for {reason}", color=0x7289da)
        await ctx.send(embed=embed)
    @kick.error
    async def kick_error(self, ctx, error):
            if isinstance(error, commands.MissingRequiredArgument):
                embed=discord.Embed(description=":octagonal_sign: Please specify a user to kick.", color=0xCD1F1F)
                await ctx.send(embed=embed)
            elif isinstance(error, commands.BadArgument):
                embed=discord.Embed(description=":octagonal_sign: Either tag the user you want to kick or be sure to check you wrote their name correctly.", color=0xCD1F1F)
                await ctx.send(embed=embed)

    # Warn
    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def warn(self, ctx, member : discord.Member, *, reason=None):
        if reason is None:
            embed = discord.Embed(description=f":octagonal_sign: Please provide a reason.", color=0xCD1F1F)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title=f":warning: Warning",
                description=f"You have been warned in **{ctx.guild.name}**\n`Reason:` **{reason}**",
                color=0x7289da
            )
            await member.send(embed=embed)
            warning = {"userid":member.id}
            collection.insert_one(warning)
    @warn.error
    async def warn_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(description=":octagonal_sign: Please specify a user to warn.", color=0xCD1F1F)
            await ctx.send(embed=embed)
        elif isinstance(error, commands.BadArgument):
            embed = discord.Embed(description=":octagonal_sign: Either tag the user you want to warn or be sure to check you wrote their name correctly.", color=0xCD1F1F)
            await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def warnings(self, ctx, member : discord.Member):
        infractions = collection.count_documents({"userid":member.id})
        if infractions > 1:
            embed = discord.Embed(title=f":warning: Infractions:", description=f"**{member.name}** has **{infractions} warnings**", color=0x7289da)
            embed.add_field(name="NOTE:", value="Currently Diablo does NOT have a server-specific warnings count. The warning you see accounts for all warnings a person has.", inline=False)
            await ctx.send(embed=embed)
        elif infractions == 1:
            embed = discord.Embed(title=f":warning: Infractions:",  description=f"**{member.name}** has **1 warning**", color=0x7289da)
            embed.add_field(name="NOTE:", value="Currently Diablo does NOT have a server-specific warnings count. The warning you see accounts for all warnings a person has.", inline=False)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title=f":warning: Infractions:", description=f"**{member.name}** has **0 warnings** :tada:", color=0x7289da)
            embed.add_field(name="NOTE:", value="Currently Diablo does NOT have a server-specific warnings count. The warning you see accounts for all warnings a person has.", inline=False)
            await ctx.send(embed=embed)

    @tasks.loop(hours=730.001)
    async def warnings_delete(self):
        delete_infractions = collection.delete_many({})

    @warnings.error
    async def warnings_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(description=":octagonal_sign: Please specify a user to check warnings of.", color=0xCD1F1F)
            await ctx.send(embed=embed)
        elif isinstance(error, commands.BadArgument):
            embed = discord.Embed( description=":octagonal_sign: Either tag the user you want to check warnings of or check you wrote their name correctly.", color=0xCD1F1F)
            await ctx.send(embed=embed)

    # Ban
    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *,  reason=None):
        await member.ban(reason=reason)
        embed=discord.Embed(title=f"{member.name} Banned", description=f"{member} was banned for {reason}", color=0x7289da)
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
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                embed=discord.Embed(
                    title=f"{member.name} was unbanned.",
                    description=f"{member.name} was unbanned banned from the server.",
                    color=0x7289da
                )
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

    # Purge (clear) command
    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount=1):
        await ctx.channel.purge(limit=amount)
        embed = discord.Embed(description=f"{amount} messages cleared.", color=0x7289da)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Moderation(client))
