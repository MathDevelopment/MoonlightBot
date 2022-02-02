import discord
import asyncio
from discord.ext import commands
from discord import DMChannel

bot = commands.Bot(command_prefix=['m!'])

@bot.event
async def on_ready():
    print('Moonlight Bot ({0.user}) is active.'.format(bot))
    print(' ')
    print('Made by obvMath#0289')
    await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name='the moon...'))

@bot.command()
async def ping(ctx):
    embed=discord.Embed(description=f'Pong! My ping is **{round(bot.latency * 1000)}**ms.', color=0x252B69)
    await ctx.reply(embed=embed)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def embed(ctx, *, message):
    embed=discord.Embed(description=message, color=0x252B69)
    await ctx.message.delete()
    await ctx.send(embed=embed)


@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user : discord.Member, *, reason=None):
    if reason == None:
        embed=discord.Embed(description=f'**{user.mention}** has been *kicked* from the server.', color=0x252B69)
        dmEmbed=discord.Embed(description=f'You have been *kicked* from the **Moonlight SMP Discord server**.', color=0x252B69)
        await ctx.send(embed=embed)
        await user.send(embed=dmEmbed)
    else:
        embed=discord.Embed(description=f'**{user.mention}** has been *kicked* from the server for __{reason}__.', color=0x252B69)
        dmEmbed=discord.Embed(description=f'You have been *kicked* from the **Moonlight SMP Discord server** for __{reason}__.', color=0x252B69)
        await ctx.send(embed=embed)
        await user.send(embed=dmEmbed)
    await user.kick(reason=reason)

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    if reason == None:
        embed=discord.Embed(description=f'{member.mention} has been *banned* from the server.', color=0x252B69)
        dmEmbed=discord.Embed(description=f'You have been *banned* from the **Moonlight SMP Discord server**.', color=0x252B69)
        await member.send(embed=dmEmbed)
        await ctx.send(embed=embed)
    else:
        embed=discord.Embed(description=f'{member.mention} has been *banned* from the server for __{reason}__.', color=0x252B69)
        dmEmbed=discord.Embed(description=f'You have been *banned* from the **Moonlight SMP Discord server** for __{reason}__.', color=0x252B69)
        await ctx.send(embed=embed)
        await member.send(embed=dmEmbed)
    await member.ban(reason=reason)

@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    embed=discord.Embed(description=f'**{member}** has been *unbanned* from the server.', color=0x252B69)
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if(user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def warn(ctx, user : discord.Member, *, reason=None):
    if reason == None:
        embed=discord.Embed(description=f'{user.mention} has been *warned*.', color=0x252B69)
        dmEmbed=discord.Embed(description=f'You have been warned on the **Moonlight SMP Discord server**.', color=0x252B69)
        await ctx.send(embed=embed)
        await user.send(embed=dmEmbed)
    else:
        embed=discord.Embed(description=f'{user.mention} has been *warned* for __{reason}__.', color=0x252B69)
        dmEmbed=discord.Embed(description=f'You have been warned on the **Moonlight SMP Discord server** for __{reason}__.', color=0x252B69)
        await ctx.send(embed=embed)
        await user.send(embed=dmEmbed)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member : discord.Member):
    MutedRole=discord.utils.get(ctx.guild.roles, name='Muted')
    embed=discord.Embed(description=f'{member.mention} was *muted*.', color=0x252B69)
    dmEmbed=discord.Embed(description=f'You were *muted* on the **Moonlight SMP Discord server**.', color=0x252B69)
    await member.add_roles(MutedRole)
    await ctx.send(embed=embed)
    await member.send(embed=dmEmbed)

@bot.command(aliases = ['purge', 'clean'])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount : int = 999999999):
    await ctx.channel.purge(limit = amount + 1)
    await asyncio.sleep(0.2)
    if amount == 999999999:
        embed = discord.Embed(description = f'Cleared {ctx.message.channel.mention}.', color = 0x00FF00)
        await ctx.send(embed=embed, delete_after=5)
    else:
        embed = discord.Embed(description = f'Cleared **{amount}** messages in {ctx.message.channel.mention}.', color = 0x00FF00)
        await ctx.send(embed=embed, delete_after=5)

@bot.command(aliases = ['av', 'pfp', 'profilepicture', 'useravatar'])
async def avatar(ctx, user : discord.Member = None):
    if user == None:
        embed = discord.Embed(color = 0x252B69)
        embed.set_author(name=f"{ctx.author}'s avatar")
        embed.set_image(url=ctx.author.avatar_url)
        await ctx.reply(embed=embed)
    else:
        embed = discord.Embed(color = 0x252B69)
        embed.set_author(name=f"{user}'s avatar")
        embed.set_image(url=user.avatar_url)
        await ctx.reply(embed=embed)

@bot.command(aliases = ['serverip', 'smpip', 'moonlightip', 'ipaddress'])
async def ip(ctx):
    embed = discord.Embed(title = '**Moonlight SMP IP:**', description = '__moonlightsmpreal.apexmc.co__', color = 0x252B69)
    await ctx.reply(embed=embed)

@bot.command(aliases = ['frostitribute', 'tributefrosti', 'tributetofrosti', 'ripfrosti'])
async def frosti(ctx):
    embed = discord.Embed(title = '**A Tribute to Frosti**', description = 'R.I.P. Frosti, an awesome guy. We will miss you. Fly high, see you under the moon.', color = 0x252B69)
    await ctx.reply(embed=embed)

@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandOnCooldown):
		await ctx.send(f'You can use that again in **{round(error.retry_after, 2)}** seconds.')
@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.MissingPermissions):
		await ctx.send('You do not have permission to do that.')
@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send(f'You are missing the argument **{error.param}**')
    
bot.remove_command('help')
@bot.group(invoke_without_command=True)
async def help(ctx):
    embed=discord.Embed(title='**Help**', color=0x252B69)
    embed.add_field(name='Prefix', value='m!')
    embed.add_field(name='Commands', value='ping, embed, warn, mute, kick, ban, unban, help')
    embed2=discord.Embed(description='Type `m!help <command>` for more info on a command.', color=0x252B69)
    await ctx.reply(embed=embed)
    await ctx.send(embed=embed2)
@help.command()
async def ping(ctx):
    embed=discord.Embed(title='**Ping**', description='Pings the bot')
    embed.add_field(name='Usage', value='```m!ping```')
    await ctx.reply(embed=embed)
@help.command()
async def embed(ctx):
    embed=discord.Embed(title='**Embed**', description='Replaces your text with a rich embed (manage messages permission required).')
    embed.add_field(name='Usage', value='```m!embed <message>```')
    await ctx.reply(embed=embed)
@help.command()
async def warn(ctx):
    embed=discord.Embed(title='**Warn**', description='Warns a user (manage message permissions required).')
    embed.add_field(name='Usage', value='```m!warn <Discord user>```')
    await ctx.reply(embed=embed)
@help.command()
async def mute(ctx):
    embed=discord.Embed(title='**Mute**', description='Mutes a user (manage message permissions required).')
    embed.add_field(name='Usage', value='```m!mute <Discord user>```')
    await ctx.reply(embed=embed)
@help.command()
async def kick(ctx):
    embed=discord.Embed(title='**Kick**', description='Kicks a user (kick members permission required).')
    embed.add_field(name='Usage', value='```m!kick <Discord user> [reason]```')
    await ctx.reply(embed=embed)
@help.command()
async def ban(ctx):
    embed=discord.Embed(title='**Ban**', description='Bans a user (ban/unban members permission required).')
    embed.add_field(name='Usage', value='```m!ban <Discord user> [reason]```')
    await ctx.reply(embed=embed)
@help.command()
async def unban(ctx):
    embed=discord.Embed(title='**Unban**', description='Unbans a user (ban/unban members permission required).')
    embed.add_field(name='Usage', value='```m!unban <Discord user>```')
    await ctx.reply(embed=embed)
@help.command()
async def help(ctx):
    embed=discord.Embed(title='**Help**', description='Moonlight Bot help.')
    embed.add_field(name='Usage', value='```m!help [command]```')
    await ctx.reply(embed=embed)

bot.run('TOKEN')