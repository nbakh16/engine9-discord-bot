import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = 'en ')
client.remove_command('help')

@client.event
async def on_ready():
    activity = discord.Game(name=" en help")
    await client.change_presence(status=discord.Status.online, activity=activity)
    #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="en help"))
    print('engine9 ready to rock!')

#write message on console when a member send message
@client.event
async def on_message(message):
    author = message.author
    global authorGlobal
    authorGlobal = author
    print('{} has sent a message.' .format(author)) #to write a msg on console
    await client.process_commands(message) #to check & execute if it's a command

@client.event
async def on_message(message):
    if message.content.startswith('ho'):
        await message.channel.send('Okay')
    await client.process_commands(message)

#greetings to newly joined member and assing a role
@client.event
async def on_member_join(member):
    mention = member.mention
    guild = member.guild
    role= discord.utils.get(member.guild.roles, name = 'Jonogon')
    await member.add_roles(role)

    embed = discord.Embed(title=str('***New member joined***'), colour=0x6BFF33,
        description=str('{} joined the server.').format(mention))
    embed.set_thumbnail(url=f"{member.avatar_url}")
    embed.set_author(name=f'{member.name}', icon_url=f'{member.avatar_url}')
    embed.set_footer(text=f'{member.guild}', icon_url=f'{member.guild.icon_url}')


    channel = discord.utils.get(member.guild.channels, id = int (631485176534532118))
    await channel.send(embed=embed)

    await channel.send('Role **{}** given to **{}**.' .format(role, member.name))

#embed on leaving member
@client.event
async def on_member_remove(member):
    mention = member.mention
    guild = member.guild

    embed = discord.Embed(title=str('***Member left***'), colour=0x6BFF33,
        description=str("{} left the server!\n Who cares!!").format(mention))
    embed.set_thumbnail(url=f"{member.avatar_url}")
    embed.set_author(name=f'{member.name}', icon_url=f'{member.avatar_url}')
    embed.set_footer(text=f'{member.guild}', icon_url=f'{member.guild.icon_url}')

    channel = discord.utils.get(member.guild.channels, id = int (631485176534532118))
    await channel.send(embed=embed)

#test command "en ping"
@client.command()
async def ping(ctx):
    await ctx.send("Yeah! I'm alive. <:pubgchickn:719923687410761769>")

#sent embeded invite link when type "en invite"
@client.command()
async def invite(ctx):
    embed = discord.Embed(title=str('Server invite link'), colour=0xf6f5f5, description = str('https://discord.gg/DqxrcGW'))
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/702494150012174356/741326802718425128/Logopit_1521240538242.jpg")
    embed.set_footer(text="Everyone's cordially welcome")
    await ctx.send(embed=embed)

#get username of self or other's
@client.command(pass_context=True)
async def name(ctx, *, user: discord.User=None):

    if user is None:
        await ctx.send(f"Your discord username {ctx.author}")
    else:
        await ctx.send(f"Discord username {user}")

#delete specific amount of messages
@client.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=10): #10 is default amount
    channel = ctx.message.channel
    messages = []
    async for message in channel.history(limit=(amount+1)):
              messages.append(message)
    await channel.delete_messages(messages)
    await ctx.send('{} Messages deleted.' .format(amount))

#help command
@client.command()
async def help(ctx):
    embed=discord.Embed(title="Commands", description="`en` is my prefix. Type `en` before every commands", color=0xe8e8e8)
    embed.set_author(name="Engine#9", url="https://facebook.com/nbakh99")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/702494150012174356/741326802718425128/Logopit_1521240538242.jpg?width=702&height=702")
    embed.add_field(name="ping", value="to test the bot", inline=False)
    embed.add_field(name="invite", value="get server invite link", inline=False)
    embed.add_field(name="name", value="know username", inline=False)
    embed.add_field(name="name *@user*", value="know @'s username", inline=False)
    embed.add_field(name="clear", value="clears 10 messages", inline=False)
    embed.add_field(name="clear *amount*", value="clears specific amounts of messages", inline=False)
    embed.set_footer(text="Soon will be added more commands. Stay tuned! Facing any problem or got suggestion about new commands? Feel free to contact with @Nabil16#3777")
    #await self.bot.say(embed=embed)
    await ctx.send(embed=embed)


#errors handling

@client.event
async def on_command_error(ctx, error):
    print(ctx.command.name + " was invoked incorrectly")
    #await ctx.send(ctx.command.name + " was invoked incorrectly")
    await ctx.send(error)

#client.run(TOKEN)
client.run(os.environ['token'])
