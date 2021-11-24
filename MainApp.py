import discord
from discord.ext import commands
import Jokes, Memes

client = discord.Client()
bot = commands.Bot(command_prefix= "lc!")

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    game = discord.Game('母單19年發功中')
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

@bot.command()
async def venom(ctx):
    await ctx.channel.send("假猛毒")
    vid = Memes.venom()
    await ctx.channel.send(file=discord.File(vid))

@bot.command()
async def memes(ctx):
    pic = Memes.get()
    await ctx.channel.send(file=discord.File(pic))

@bot.command()
async def jokes(ctx):
    joke_question, joke_answer = Jokes.tell()
    await ctx.reply("{}\n\n{}".format(joke_question, joke_answer))

@bot.command()
async def about(ctx):
    await ctx.channel.send('https://www.instagram.com/iamleocheng/')
    await ctx.channel.send("""以lc!作為開頭呼叫
jokes：隨機產生一個笑話
memes：隨機傳一張梗圖
更多功能日後上線（當然，如果我有空的話）""")

@bot.command()
async def hello(ctx):
    mention = ctx.author.mention
    await ctx.channel.send("Hello, {}".format(mention))

@bot.command()
@commands.has_role("Admin")
async def ban(ctx, member : discord.Member, *, reason = None):
    if member == None or member == ctx.message.author:
        await ctx.channel.send("You cannot ban yourself")
        return
    if reason == None:
        reason = "過於智障"
    message = f"You have been banned from {ctx.guild.name} for {reason}"
    await member.send(message)
    await ctx.channel.send(f"{member}已被relaxing234永久禁言")
    await member.ban(reason = reason)

@bot.command()
@commands.has_role("Admin")
async def unban(ctx, *, member : discord.Member):
    await member.unban(reason= None)
    await ctx.channel.send(f"機器人大軍已決定赦免{member}")

bot.run('OTAwNzI2NTkzOTQ3ODQ0NjU5.YXFhAg.-wJ99DG_2l0sV4AcmT8kjz8zBFA')
