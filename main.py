# bot.py
import os
import keep_alive
from discord import Embed



import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
SERVER = os.getenv('DISCORD_SERVER')
trigger = '&'

isAdmin = False
bot = commands.Bot(command_prefix='&')

@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name == SERVER:
            break

    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@bot.command()
async def say(ctx, args):
  await ctx.send(args)

@bot.command() #StarWars Wiki Lookup
async def info(ctx, *args):
    await ctx.send('https://starwars.fandom.com/wiki/'+ '_'.join(args))

@bot.command() #RWL Lookup
async def lookup(ctx, *args):
    await ctx.send('https://rwldiscord.fandom.com/wiki/'+ '_'.join(args))

@bot.command()
async def thegame(ctx):
    await ctx.send('https://en.wikipedia.org/wiki/The_Game_(mind_game)')

@bot.command()
async def google(ctx, *args):
      await ctx.send("https://www.google.com/search?q=" + '+'.join(args))

@bot.command()
async def HuntersBannedCommand(ctx, user: discord.User):
  themessage = "https://i.pinimg.com/originals/88/82/bc/8882bcf327896ab79fb97e85ae63a002.gif"

  if ctx.author.id != 415710538178232333:
    await ctx.message.delete()
    await user.send(themessage)
    await ctx.send(":thumbsup:")
  else:
    sendToHunter = await bot.fetch_user(415710538178232333)
    await sendToHunter.send(themessage)
    await ctx.send("Hunter, Really?")

@bot.command()
async def rr(ctx, *args):
  await ctx.message.delete()
  await ctx.send("https://tenor.com/view/roger-roger-roger-star-wars-the-phantom-menace-droids-gif-4890643")

@bot.command() #embed testing
async def embedtest(ctx, *args):
  if ctx.author.id ==634176167351681045: #My userID
    t = "Sample Embed"
    desc = "Click the link to go to Nasa.gov"
    embed = discord.Embed(title = t, description = desc, color = 0xFF5733)
    await ctx.send(embed = embed)

@bot.command() #Roger's polling function
async def poll(ctx, *args):
      await ctx.message.delete()
      name = args[0]
      answers = []
      for i in range(1, len(args)):
        answers.append(args[i])
      embed = discord.Embed(title = name, color = discord.Color.red())

      creator = ctx.author.name
      member = ctx.message.author
      userAvatar = member.avatar_url
      embed.set_author(name = creator, icon_url = userAvatar)
      
      char = 1
      for i in answers:
        embed.add_field(name = i, value = getemoji(char), inline = False)
        char = char + 1
      msg = await ctx.send(embed = embed)

      char = 1

      for i in answers:
        await msg.add_reaction(getNumber(char))
        char = char + 1


def getemoji(int):
  if int==1:
    return ":one:"
  elif int==2:
    return ":two:"
  elif int ==3:
    return ":three:"
  elif int ==4:
    return ":four:"
  elif int == 5:
    return ":five:"
  elif int == 6:
    return ":six:"
  elif int == 7:
    return ":seven:"

def getNumber(int):
  if int==1:
    return "1️⃣"
  elif int==2:
    return "2️⃣"
  elif int ==3:
    return "3️⃣"
  elif int ==4:
    return "4️⃣"
  elif int == 5:
    return "5️⃣"
  elif int == 6:
    return "6️⃣"
  elif int == 7:
    return "7️⃣"


keep_alive.keep_alive()                       
bot.run(TOKEN)
