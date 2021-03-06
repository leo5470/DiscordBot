import discord
from discord.ext import commands
import Jokes, Memes

key = 'OTAwNzI2NTkzOTQ3ODQ0NjU5.YXFhAg.-wJ99DG_2l0sV4AcmT8kjz8zBFA'
client = discord.Client()
bot = commands.Bot(command_prefix= "lc!")

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    game = discord.Game('母單19年發功中')
    await bot.change_presence(status=discord.Status.online, activity=game)

@bot.command()
async def venom(ctx):
    await ctx.channel.send("假猛毒")
    vid = Memes.venom()
    await ctx.channel.send(file=discord.File(vid))
    print("Venom called")
@bot.command()
async def memes(ctx):
    pic = Memes.get()
    await ctx.channel.send(file=discord.File(pic))
    print("Memes called")

@bot.command()
async def jokes(ctx):
    joke_question, joke_answer = Jokes.tell()
    await ctx.reply("{}\n\n{}".format(joke_question, joke_answer))
    print("Jokes called")

@bot.command()
async def about(ctx):
    await ctx.channel.send('https://www.instagram.com/iamleocheng/')
    await ctx.channel.send("""以lc!作為開頭呼叫
jokes：隨機產生一個笑話
memes：隨機傳一張梗圖
更多功能日後上線（當然，如果我有空的話）""")
    print("About called")

@bot.command()
async def hello(ctx):
    mention = ctx.author.mention
    await ctx.channel.send("Hello, {}".format(mention))
    print("Hello Called")

@bot.command()
@commands.has_role("Admin")
async def ban(ctx, member : discord.Member, *, reason = None):
    if member == None or member == ctx.message.author:
        await ctx.channel.send("You cannot ban yourself")
        return
    if reason == None:
        reason = "過於智障"
    message = f"您已從{ctx.guild.name}被ban出，原因為{reason}"
    await member.send(message)
    await member.ban(reason = reason)
    await ctx.channel.send(f"{member}已被relaxing234永久禁言")
    print("Ban called")

@bot.command()
@commands.has_role("Admin")
async def unban(ctx, user : discord.User):
    await ctx.guild.unban(user)
    await ctx.channel.send(f"機器人大軍已決定赦免{user}")
    print("Unban called")

bot.run(key)
