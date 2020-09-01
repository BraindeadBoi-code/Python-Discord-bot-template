import discord
from discord.ext import commands

Discord_Token = 'Placeholder_Token'

client = commands.Bot(command_prefix= 'Placeholder_Prefix')
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('France? France'))
    print('Placeholder_Message')
#--Welcome and Leave messages--
@client.event
async def on_member_join(member):
    await member.send(f'Thank you for joining the discord Server {member}')
    print(f'{member} has joined the server')
@client.event
async def on_member_leave(member):
    await member.send(f'{member} has left the discord Server')
    print(f'{member} has left the server')
#--Help--
@client.command()
async def help(member):
    await member.send('Commands\n Prefix is Placeholder_Prefix \n .kick kicks users\n .ban bans users\n .unban unbans users \n .purge amount (default is 10) deletes specified amount of messages')
#--Unban--
@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_cunts = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    for ban_entry in banned_cunts:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'{user} has been unbanned')
            print(f'{user} Has been unbanned')
#--Kick--
@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.send(f'you have been kick from the server for {reason}')
    await member.kick(reason=reason)
    await ctx.channel.purge(limit=1)
    await ctx.send(f'{member} has been kicked from the server for {reason}')
    print(f'{member} Has been kicked from the server for {reason}')
#--Ban--
@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.send(f'you have been ban from the server for {reason}')
    await member.ban(reason=reason)
    await ctx.channel.purge(limit=1)
    await ctx.send(f'{member} has been ban from the server for {reason}')
    print(f'{member} Has been ban from the server for {reason}')
#--Purge--
@client.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount=11):
    await ctx.channel.purge(limit=amount)
#--Error_Hooks--

#--Mute--

#--Phrog--
@client.command(pass_context=True)
async def phrog(ctx, member : discord.Member):
    embed = discord.Embed()
    embed.colour = discord.Colour.dark_purple()
    embed.set_author(name=member)
    embed.set_image(url='https://i.redd.it/blaegizarda41.jpg')
    await member.send(embed=embed)
#--Stepbro--

client.run(Discord_Token)