import discord

client = discord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    game = discord.Game('尋找戀愛學分中')
    await client.change_presence(status=discord.Status.online, activity=game)
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    elif message.content.startswith('$about'):
        await message.channel.send('https://www.instagram.com/iamleocheng/')
client.run('OTAwNzI2NTkzOTQ3ODQ0NjU5.YXFhAg.-wJ99DG_2l0sV4AcmT8kjz8zBFA')
