import discord
import Jokes

client = discord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    game = discord.Game('母單19年發功中')
    await client.change_presence(status=discord.Status.online, activity=game)
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    elif message.content.startswith('$about'):
        await message.channel.send('https://www.instagram.com/iamleocheng/')
    elif message.content.startswith('$jokes'):
        joke_question, joke_answer = Jokes.tell()
        await message.channel.send("{}\n\n{}".format(joke_question, joke_answer))
client.run('OTAwNzI2NTkzOTQ3ODQ0NjU5.YXFhAg.-wJ99DG_2l0sV4AcmT8kjz8zBFA')
