import discord
from misc import list_data,save_data,clear_data
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
      return
    elif message.content.startswith('$bookmarks'):
      result = list_data(message)
      if result:
        await message.channel.send(result)
      else:
        await message.channel.send('I am having a headache. I cannot save that right now :sob:')
    elif message.content.startswith('$bookmark'):
      result = save_data(message)
      if result:
        await message.channel.send('Okay okay, I saved that :smirk:')
      else:
        await message.channel.send('I am having a headache. I cannot save that right now :sob:')
    elif message.content.startswith('$clear'):
      channel_id = message.channel.id
      clear_data(channel_id)
      await message.channel.send(':x: I cleared every single bookmark for this text channel. :x:')
    elif message.content.startswith('$help'):
      output = 'You can command me with the following:.\n'
      output += '$bookmark {message}: I save the message.\n'
      output += '$bookmarks: I show you all my bookmarks for this text channel.\n'
      output += '\n Made By Stavros Tsompanidis'
      await message.channel.send(output)



client.run(os.getenv('TOKEN'))
