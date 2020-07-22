import discord
import os


client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.game("관리중")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("사과 안녕"):
        await message.channel.send("그래")
    if message.content.startswith("사과 안녕"):
        await message.channel.send("방가워!")
    if message.content.startswith("사과 안녕"):
        await message.channel.send("나도!")
    if message.content.startswith("사과 뭐해"):
        await message.channel.send("사과 먹는중")
    if message.content.startswith("사과 뭐해"):
        await message.channel.send("게임하고 있어")
    if message.content.startswith("사과 바보"):
        await message.channel.send("너?")
    if message.content.startswith("사과 바보"):
        await message.channel.send("나빠")
    if message.content.startswith("사과 바보"):
        await message.channel.send("너 싫어")
    if message.content.startswith("사과 바보"):
        await message.channel.send("힝...")
    if message.content.startswith("사과 심심해"):
        await message.channel.send("나도..")
    if message.content.startswith("사과 심심해"):
        await message.channel.send("그래서")
    if message.content.startswith("사과 놀자"):
        await message.channel.send("너 혼자 놀아")
    if message.content.startswith("사과 놀자"):
        await message.channel.send("뭐하고?")
    if message.content.startswith("사과 놀자"):
        await message.channel.send("그래서?")
    if message.content.startswith("사과 놀자"):
        await message.channel.send("난 잘거야")
    if message.content.startswith("사과 나빠"):
        await message.channel.send("퉤")
    if message.content.startswith("사과 관리자"):
        await message.channel.send("https://jjalbot.com/media/2016/10/ryOAU6U0/20160813_57ae9599dd25b.jpg")



access_token = os.environ["BOT_TOKEN"]
client.run(access_token)



