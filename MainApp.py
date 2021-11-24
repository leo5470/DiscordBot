import discord
from discord.ext import commands
import Jokes, Memes

bot = commands.Bot(command_prefix= "lc!")

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    game = discord.Game('母單19年發功中')
    await bot.change_presence(status=discord.Status.online, activity=game)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

@bot.command()
async def hello(ctx):
    mention = ctx.author.mention
    await ctx.send("Hello, {}".format(mention))

@bot.command()
async def about(ctx):
    await ctx.send('Author: https://www.instagram.com/iamleocheng/')
    await ctx.send("""以lc!作為開頭呼叫
jokes：隨機產生一個笑話
memes：隨機傳一張梗圖
更多功能日後上線（當然，如果我有空的話）""")

@bot.command()
async def jokes(ctx):
    joke_question, joke_answer = Jokes.tell()
    await ctx.reply("{}\n\n{}".format(joke_question, joke_answer))

@bot.command()
async def memes(ctx):
    pic = Memes.get()
    await ctx.send(file=discord.File(pic))

@bot.command()
async def venom(ctx):
    await ctx.channel.send("假猛毒")
    vid = Memes.venom()
    await ctx.send(file=discord.File(vid))

@bot.command()
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
    

bot.run('OTAwNzI2NTkzOTQ3ODQ0NjU5.YXFhAg.-wJ99DG_2l0sV4AcmT8kjz8zBFA')
