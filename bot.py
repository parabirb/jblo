"""
    DIABLO - A bot that bans pedos and zoos
    (C) 2020 incipious. All rights reserved.
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
# DIABLO: Database Influenced Automated Ban List of Offenders

import discord
import os
from libdiablo import diabloserv
from discord.ext import commands

client = commands.Bot(command_prefix = 'd.')


@client.event
async def on_command_error(self, ctx, error):
    # CommandNotFound
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(title="This command does not exist", description="Use `d.help` to get a full list of commands", color=0xCD1F1F)
        await ctx.send(embed=embed)
    # Missing Permissions Error
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(description="You do not have the right permissions to run this command.", color=0xCD1F1F)
        await ctx.send(embed=embed)
    
@client.command()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    client.load_extension(f"cogs.{extension}")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

client.run('TOKEN')
