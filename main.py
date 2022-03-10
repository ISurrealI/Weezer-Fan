import discord
import random
import os

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

client = discord.Client()

token = ''
command = '=w='

# string stuff
split = "/"

weezergif = [
    'https://tenor.com/view/weezer-donut-weezer-gif-19177822',
    'https://media.discordapp.net/attachments/727276444962783236/949748707937615942/dumpy949716585579417611.gif',
    'https://tenor.com/view/weezer-weezer-green-album-green-album-gif-22961198',
    'https://tenor.com/view/weezer-gif-21192793',
    'https://tenor.com/view/weez-nuts-weezer-weezer-cube-cube-gif-22382503',
    'https://tenor.com/view/weezer-blue-album-shuffle-band-meme-gif-21447356',
    'https://tenor.com/view/weezer-weezer-green-album-green-album-gif-22961200',
    'https://tenor.com/view/i-love-weezer-weezer-is-the-best-band-weezer-weezer-fan-epic-gif-20452259',
    'https://tenor.com/view/weezer-gif-21274022'
]

mewhenweezer = [
    'I LOVE WEEZR!!',
    'WEEZER:bangbang:',
    'Weezeeeeer, yeeeeaaah! WEEZEEEEEEER!!!',
    ':weary:'
]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    quoteChance = 85

    if message.author.id == 656962312565030963:
        await message.channel.send(reference=discord.Union())
    
    if message.author.id == 401762887980417045:
        quoteChance - random.randint(25, 40)

    if message.content.startswith(command + 'weezerquote'):
        await message.channel.send(file=discord.File('./quotes/' + random.choice(os.listdir('./quotes'))))

    if random.randint(0, quoteChance) == 0:
        await message.channel.send(file=discord.File('./quotes/' + random.choice(os.listdir('./quotes'))))

    if message.content.startswith(command + 'hello'):
        await message.channel.send('hello i\\\'m the weezer fan')

    if message.content.startswith(command + 'weezergif'):
        await message.channel.send(random.choice(weezergif))

    if message.content.startswith(command + 'mewhenweezer'):
        await message.channel.send(random.choice(mewhenweezer))
    
    if message.content.startswith(command + 'weezerhelp'):
        await message.channel.send('commands:\nweezerquote = creates quote\nhello = hello weezer\nweezergif = posts random weezer gif\nmewhenweezer = i love weezr!!\nweezerhelp = helps weezer\nweezercard (to/from) = creates card')

    if message.content.startswith(command + 'weezercard'):
        toDraw = message.content.replace(command + 'weezercard ', '')

        if (split in toDraw):
            to = toDraw.split(split)[0]
            frm = toDraw.split(split)[1]

            xTo = 832
            yTo = 415

            xFrom = 907
            yFrom = 521

            fontName = "comic"
            fontColor = [0, 0, 0]
            fontSize = 56
            fontShadow=None

            imgName = random.choice(os.listdir('./cards'))

            img = Image.open('./cards/' + imgName)
            draw = ImageDraw.Draw(img)

            if (imgName.startswith("red_album")):
                xTo = 780
                yTo = 468

                xFrom = 777
                yFrom = 546

                fontName = "araboto_black_400"
                fontSize = 46
                fontColor = [169, 212, 254]
                fontShadow="black"

            if (imgName.startswith("raditude")):
                xTo = 560
                yTo = 530

                xFrom = 610
                yFrom = 604

                fontSize = 43

            font = ImageFont.truetype("./fonts/" + fontName + ".ttf", int(fontSize - min(fontSize-1, (len(to) / 2))))

            draw.text((int(xTo), int(yTo + (len(to) / 2))), to, (fontColor[0], fontColor[1], fontColor[2]), font=font)

            font = ImageFont.truetype("./fonts/" + fontName + ".ttf", int(fontSize - min(fontSize-1, len(frm) / 2)))
            draw.text((int(xFrom), int(yFrom + (len(frm) / 2))), frm, (fontColor[0], fontColor[1], fontColor[2]), font=font)
            img.save('card-out.jpg')

            await message.channel.send(file=discord.File('./card-out.jpg'))
            os.remove('./card-out.jpg')
        else: 
            await message.channel.send('wrong input! (ex. =w=weezercard Mary Tyler Moore/Buddy Holly)')

client.run(token)
