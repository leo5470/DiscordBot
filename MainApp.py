import discord
import Jokes, Memes

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
    mention = message.author.mention
    if message.content.startswith('lc!hello'):
        await message.channel.send("{} Hello!".format(mention))
    elif message.content.startswith('lc!about'):
        await message.channel.send('https://www.instagram.com/iamleocheng/')
    elif message.content.startswith('lc!jokes'):
        joke_question, joke_answer = Jokes.tell()
        await message.channel.send("{}\n\n{}".format(joke_question, joke_answer))
    elif message.content.startswith('lc!memes'):
        pic = Memes.get()
        await message.channel.send(file=discord.File(pic))
    elif message.content.startswith('lc!venom'):
        await message.channel.send("假猛毒")
        vid = Memes.venom()
        await message.channel.send(file=discord.File(vid))
client.run('OTAwNzI2NTkzOTQ3ODQ0NjU5.YXFhAg.-wJ99DG_2l0sV4AcmT8kjz8zBFA')
