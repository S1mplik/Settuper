
from discord.ext import commands
import datetime
import random
import re

client = commands.Bot(command_prefix='.')
Token = 'YOUR DISCORD BOT TOKEN'
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="na příkaz .help"))
    print('Bot je úspěšne zapnul')

@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name='welcome' )
    await channel.send(f'Vítej ***{member.mention}**,na **{member.guild.name}** discord serveru')

@client.command()
async def ping(ctx):
    await ctx.send(f'Tvůj ping je: **{round(client.latency * 1000)}ms**' )
@client.command()
async def Ping(ctx):
    await ctx.send(f'Tvůj ping je: **{round(client.latency * 1000)}ms**' )

@client.command()
async def serverinfo(ctx):
    embed = discord.Embed(title=f" Název Serveru: {ctx.guild.name}\n", description="Informace", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Vytvoření Serveru", value=f"{ctx.guild.created_at}\n")
    embed.add_field(name="Majitel Serveru", value=f"{ctx.guild.owner}\n")
    embed.add_field(name="Oblast", value=f"{ctx.guild.region}\n")
    embed.add_field(name="ID Serveru", value=f"{ctx.guild.id}\n")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail(url="https://upload.hicoria.com/files/Tc2qBXx1.png")

    await ctx.send(embed=embed)



@client.command()
async def userinfo(ctx):
    embed = discord.Embed(color=discord.Color.blue(), timestamp=datetime.datetime.utcnow())
    embed.add_field(name=f"Informace o uživateli - {member}")
    embed.add_field(name="ID", value=member.id)
    emebd.add_field(name="Název guild:", value=member.display_name)
    embed.set_thubmail(url=member.avatar_url)
    await ctx.send(embed=embed)
@client.command()
async def si(ctx):
    embed = discord.Embed(title=f" Název Serveru: {ctx.guild.name}\n", description="Informace", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Vytvoření Serveru", value=f"{ctx.guild.created_at}\n")
    embed.add_field(name="Majitel Serveru", value=f"{ctx.guild.owner}\n")
    embed.add_field(name="Oblast", value=f"{ctx.guild.region}\n")
    embed.add_field(name="ID Serveru", value=f"{ctx.guild.id}\n")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail(url="https://upload.hicoria.com/files/Tc2qBXx1.png")

    await ctx.send(embed=embed)
@client.command()
async def Serverinfo(ctx):
    embed = discord.Embed(title=f" Název Serveru: {ctx.guild.name}\n", description="Informace", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Vytvoření Serveru", value=f"{ctx.guild.created_at}\n")
    embed.add_field(name="Majitel Serveru", value=f"{ctx.guild.owner}\n")
    embed.add_field(name="Oblast", value=f"{ctx.guild.region}\n")
    embed.add_field(name="ID Serveru", value=f"{ctx.guild.id}\n")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail(url="https://upload.hicoria.com/files/Tc2qBXx1.png")

    await ctx.send(embed=embed)
@client.command()
async def info(ctx):
    embed = discord.Embed(title=f" Název Serveru: {ctx.guild.name}\n", description="Informace", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Vytvoření Serveru", value=f"{ctx.guild.created_at}\n")
    embed.add_field(name="Majitel Serveru", value=f"{ctx.guild.owner}\n")
    embed.add_field(name="Oblast", value=f"{ctx.guild.region}\n")
    embed.add_field(name="ID Serveru", value=f"{ctx.guild.id}\n\n")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail(url="https://upload.hicoria.com/files/Tc2qBXx1.png")

    await ctx.send(embed=embed)
@client.command()
async def Info(ctx):
    embed = discord.Embed(title=f" Název Serveru: {ctx.guild.name}\n", description="Informace", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Vytvoření Serveru", value=f"{ctx.guild.created_at}\n")
    embed.add_field(name="Majitel Serveru", value=f"{ctx.guild.owner}\n")
    embed.add_field(name="Oblast", value=f"{ctx.guild.region}\n")
    embed.add_field(name="ID Serveru", value=f"{ctx.guild.id}\n")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail(url="https://upload.hicoria.com/files/Tc2qBXx1.png")

    await ctx.send(embed=embed)
@client.command()
async def ServerInfo(ctx):
    embed = discord.Embed(title=f" Název Serveru: {ctx.guild.name}\n", description="Informace", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Vytvoření Serveru", value=f"{ctx.guild.created_at}\n")
    embed.add_field(name="Majitel Serveru", value=f"{ctx.guild.owner}\n")
    embed.add_field(name="Oblast", value=f"{ctx.guild.region}\n")
    embed.add_field(name="ID Serveru", value=f"{ctx.guild.id}\n")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail(url="https://upload.hicoria.com/files/Tc2qBXx1.png")

    await ctx.send(embed=embed)
@client.command()
async def serverInfo(ctx):
    embed = discord.Embed(title=f" Název Serveru: {ctx.guild.name}\n", description="Informace", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Vytvoření Serveru", value=f"{ctx.guild.created_at}\n")
    embed.add_field(name="Majitel Serveru", value=f"{ctx.guild.owner}\n")
    embed.add_field(name="Oblast", value=f"{ctx.guild.region}\n")
    embed.add_field(name="ID Serveru", value=f"{ctx.guild.id}\n")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail(url="https://upload.hicoria.com/files/Tc2qBXx1.png")

    await ctx.send(embed=embed)

@client.command()
async def help(ctx):
    embed = discord.Embed(title=f"Seznam příkazů", description="Tyto příkazy jsou speciálně děkané pro lidi co se v tomto botovy nevyznají", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Seznam změn:", value="Changelog\n")
    embed.add_field(name="Hry:", value="flip, roll, ball\n")
    embed.add_field(name="Pokročilé:", value="ping\n")
    embed.add_field(name="A-Team:", value="clear\n")
    embed.set_thumbnail(url="https://upload.hicoria.com/files/Tc2qBXx1.png")
    await ctx.send(embed=embed)

@client.command()
async def flip(ctx):
    choices = ('PANA','OREL')
    rancoin = random.choice(choices)
    await ctx.send(f'Padlo ti: **{rancoin}**')
@client.command()
async def Flip(ctx):
    choices = ('PANA','OREL')
    rancoin = random.choice(choices)
    await ctx.send(f'Padlo ti: **{rancoin}**')


@client.command()
async def invite(ctx):
    await ctx.send('Zde je odkaz pro pozvání dalších **kamarádů nebo hráčů** https://discord.gg/UrUz8sH')
@client.command()
async def Invite(ctx):
    await ctx.send('Zde je odkaz pro pozvání dalších **kamarádů nebo hráčů** https://discord.gg/UrUz8sH')


@client.command()
@has_permissions(manage_roles=True, ban_members=True)
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f"Chat byl smazán: **Členem A-Teamu**")
@client.command()
@has_permissions(manage_roles=True, ban_members=True)
async def Clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f"Chat byl smazán: **Členem A-Teamu**")
@client.command()
async def a (ctx):
    embed = discord.Embed(title=f"Rules\n", description="Information", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.set_thumbnail(url="https://upload.hicoria.com/files/Tc2qBXx1.png")
    await ctx.send(embed=embed)
@client.command()
async def rules(ctx):
    embed = discord.Embed(color=discord.Color.blue())
    embed.add_field(name="\n**1. Be respectful**", value=f"\nYou must respect all users, regardless of your liking towards them. Treat others the way you want to be treated.\n")
    embed.add_field(name="\n**2. No Inappropriate Language**", value=f"\nThe use of profanity should be kept to a minimum. However, any derogatory language towards any user is prohibited.\n")
    embed.add_field(name="\n**3. No spamming**", value=f"\nDon't send a lot of small messages right after each other. Do not disrupt chat by spamming.\n")
    embed.add_field(name="\n**4. No pornographic/adult/other NSFW material**", value=f"\nThis is a community server and not meant to share this kind of material.\n")
    embed.add_field(name="\n**5. No advertisements**", value=f"\nWe do not tolerate any kind of advertisements, whether it be for other communities or streams. You can post your content in the media channel if it is relevant and provides actual value (Video/Art)\n")
    embed.add_field(name="\n**6. No offensive names and profile pictures**", value=f"\nYou will be asked to change your name or picture if the staff deems them inappropriate.\n")
    embed.add_field(name="\n**7. Server Raiding**", value=f"\nRaiding or mentions of raiding are not allowed.\n")
    embed.add_field(name="\n**8. Direct & Indirect Threats**", value=f"\nThreats to other users of DDoS, Death, DoX, abuse, and other malicious threats are absolutely prohibited and disallowed.\n")
    embed.add_field(name="\n**9. Follow the Discord Community Guidelines**", value=f"\nYou can find them here: https://discordapp.com/guidelines\n")
    embed.add_field(name="\n**10. Do not join voice chat channels without permission of the people already in there**", value=f"\nIf you see that they have a free spot it is alright to join and ask whether they have an open spot, but leave if your presence is not wanted by whoever was there first.\n")
    embed.add_field(name="\n**The Admins and Mods will Mute/Kick/Ban per discretion. If you feel mistreated dm an Admin and we will resolve the issue.**", value=f"\n")
    embed.add_field(name="\nAll Channels will have pinned messages explaining what they are there for and how everything works. If you don't understand something, feel free to ask!", value=f"\n")
    embed.add_field(name="\n**Your presence in this server implies accepting these rules, including all further changes. These changes might be done at any time without notice, it is your responsibility to check for them.**", value=f"\n")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail(url="https://upload.hicoria.com/files/Tc2qBXx1.png")

    await ctx.send(embed=embed)

@client.command()
async def roll(ctx):
    n = random.randrange(1, 101)
    await ctx.send(f"Padlo ti číslo: **{n}**")
@client.command()
async def Roll(ctx):
    n = random.randrange(1, 101)
    await ctx.send(f"Padlo ti číslo: **{n}**")


@client.command()
async def changelog(ctx):
    await ctx.send ('Sem se nechávají zaznamenávat všechny změny na serveru Majitel serveru se dohodne s vlastníkem bota co se do těchto příkazu dá popřípadě se změní vizualizace bota')
@client.command()
async def Changelog(ctx):
    await ctx.send ('Sem se nechávají zaznamenávat všechny změny na serveru Majitel serveru se dohodne s vlastníkem bota co se do těchto příkazu dá popřípadě se změní vizualizace bota')

@client.command()
async def Otazky(ctx, *, question):
    responses = ['Máš pravdu', 'Na 100%', 'Nejsem si jistý', 'Ne', 'Ani náhodou', 'To je vtip', 'Jako vážně']
    await ctx.send(f'Otázka: {question}\nOtázka: {random.choice(responses)}')
@client.command()
async def ball(ctx, *, question):
    responses = ['Máš pravdu', 'Na 100%', 'Nejsem si jistý', 'Ne', 'Ani náhodou', 'To je vtip', 'Jako vážně']
    await ctx.send(f'Otázka: {question}\nOtázka: {random.choice(responses)}')
@client.command()
async def Ball(ctx, *, question):
    responses = ['Máš pravdu', 'Na 100%', 'Nejsem si jistý', 'Ne', 'Ani náhodou', 'To je vtip', 'Jako vážně']
    await ctx.send(f'Otázka: {question}\nOtázka: {random.choice(responses)}')
@client.command()
async def otázky(ctx, *, question):
    responses = ['Máš pravdu', 'Na 100%', 'Nejsem si jistý', 'Ne', 'Ani náhodou', 'To je vtip', 'Jako vážně']
    await ctx.send(f'Otázka: {question}\nOdpověď: {random.choice(responses)}')



client.run(Token)
