import discord
from discord.ext import commands
import Jokes, Memes

bot = commands.Bot(command_prefix= "lc!")

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    game = discord.Game('母單19年發功中')
    await bot.change_presence(status=discord.Status.online, activity=game)
    return
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
<<<<<<< HEAD

@bot.command()
async def hello(ctx):
    mention = ctx.author.mention
    await ctx.send("Hello, {}".format(mention))
    return

@bot.command()
async def about(ctx):
    await ctx.send('Author: https://www.instagram.com/iamleocheng/')
    await ctx.send("""以lc!作為開頭呼叫
=======
    mention = message.author.mention
    if message.content.startswith('lc!hello'):
        await message.reply("Hello, {}!".format(mention))
    elif message.content.startswith('lc!about'):
        await message.channel.send('https://www.instagram.com/iamleocheng/')
    elif message.content.startswith('lc!jokes'):
        joke_question, joke_answer = Jokes.tell()
        await message.reply("{}\n\n{}".format(joke_question, joke_answer))
    elif message.content.startswith('lc!memes'):
        pic = Memes.get()
        await message.channel.send(file=discord.File(pic))
    elif message.content.startswith('lc!venom'):
        await message.channel.send("假猛毒")
        vid = Memes.venom()
        await message.channel.send(file=discord.File(vid))
    elif message.content.startswith('lc!help'):
        await message.channel.send("""以lc!作為開頭呼叫
>>>>>>> parent of c9a11db (Update MainApp.py)
jokes：隨機產生一個笑話
memes：隨機傳一張梗圖
更多功能日後上線（當然，如果我有空的話）""")
    return

@bot.command()
<<<<<<< HEAD
async def jokes(ctx):
    joke_question, joke_answer = Jokes.tell()
    await ctx.reply("{}\n\n{}".format(joke_question, joke_answer))
    return

@bot.command()
async def memes(ctx):
    pic = Memes.get()
    await ctx.send(file=discord.File(pic))
    return

@bot.command()
async def venom(ctx):
    await ctx.channel.send("假猛毒")
    vid = Memes.venom()
    await ctx.send(file=discord.File(vid))
    return

@bot.command()
=======
>>>>>>> parent of c9a11db (Update MainApp.py)
@commands.has_role("Admin")
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)
    if member is None or member == ctx.message.author:
        await ctx.send("You cannot ban yourself")
        return
    if reason is None:
        reason = "過於智障"
    message = f"You have been banned from {ctx.guild.name} for {reason}"
    await member.send(message)
    await ctx.send(f"{member}已被Relaxing234永久禁言")
    return
    

bot.run('OTAwNzI2NTkzOTQ3ODQ0NjU5.YXFhAg.-wJ99DG_2l0sV4AcmT8kjz8zBFA')
