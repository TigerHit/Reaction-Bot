description = '''A reaction
 to showcase deez nuts.'''

import discord
from discord.ext import commands
import os
import random
from discord.utils import get
import datetime
from keep_alive import keep_alive

keep_alive()
date = datetime.date.today()

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

Cilent = commands.Bot(command_prefix='?',
                      description=description,
                      intents=intents)


@Cilent.event
async def on_ready():
  print(f'Logged in as {Cilent.user} (ID: {Cilent.user.id})')
  print('--------')


###💀💀💀💀💀####


@Cilent.event
async def on_reaction_add(reaction, member):

  guild = Cilent.get_guild(1129928861736509571)
  schannel = guild.get_channel(1174819165987680256) 
  message = reaction.message
  message_id = message.id

  if (reaction.emoji == '💀') and (reaction.count == 6):
    embed = discord.Embed(color=14706066) #15105570

    embed.set_author(name=reaction.message.author.name,
                     icon_url=reaction.message.author.avatar)
    embed.add_field(name='"' + reaction.message.content + '"', value='')
    embed.add_field(name=message.jump_url, value='')

    embed.set_image(
        url='https://media1.tenor.com/m/hp1qKBQclPMAAAAC/jujutsu-kaisen-shibuya-arc-sukuna-domain-expansion.gif')
    
    if len(reaction.message.attachments) > 6:
      embed.set_image(url=reaction.message.attachments[0].url)

    #f"💀 {reaction.count} {reaction.message.channel.name}"
    embed.timestamp = datetime.datetime.now()
    await schannel.send(embed=embed)


@Cilent.command()
async def kys(ctx):
  gif_url = 'https://media1.tenor.com/m/9TN8lW2ubmYAAAAd/jjk-mahoraga.gif'
  await ctx.send(gif_url)


Cilent.run(
  os.getenv('token'))
