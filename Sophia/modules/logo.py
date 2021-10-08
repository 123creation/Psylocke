from Sophia.events import register
from Sophia import OWNER_ID
from Sophia import telethn as tbot

import os 
from PIL import Image, ImageDraw, ImageFont
import shutil 
import random, re
import glob
import time

from telethon.tl.types import InputMessagesFilterPhotos


FONT_FILE_TO_USE = "/usr/share/fonts/truetype/Dashdemo-ozJA.ttf"


TELEGRAPH_MEDIA_LINKS = ["https://telegra.ph/file/e354ce72d5cc6a1d27c4d.jpg",
                         "https://telegra.ph/file/424d845531192b9279162.jpg"
                         ]

@register(pattern="^/logo ?(.*)")
async def lego(event):
 quew = event.pattern_match.group(1)
 if event.sender_id == OWNER_ID:
     pass
 else:
     
    if not quew:
       await event.reply('Provide Some Text To Draw!')
       return
    else:
       pass
 await event.reply('Creating your logo...')
 try:
    text = event.pattern_match.group(1)
    img = Image.open('./Sophia/etc/large-2967829.jpg')
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    pointsize = 500
    fillcolor = "white"
    shadowcolor = "blue"
    font = ImageFont.truetype("./Sophia/etc/Dashdemo-ozJA.ttf", 250)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    image_width, image_height = img.size
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
    x = (image_widthz-w)/2
    y= ((image_heightz-h)/2+6)
    draw.text((x, y), text, font=font, fill="black", stroke_width=0, stroke_fill="black")
    fname2 = "SophiaLogo.png"
    img.save(fname2, "png")
    await tbot.send_file(event.chat_id, fname2, caption="Made By @Psylocke_robot 💞")
    if os.path.exists(fname2):
            os.remove(fname2)
 except Exception as e:
   await event.reply(f'Error Go to Help From  @pigasusSupport, {e}')




@register(pattern="^/wlogo ?(.*)")
async def lego(event):
 quew = event.pattern_match.group(1)
 if event.sender_id == OWNER_ID:
     pass
 else:
     
    if not quew:
       await event.reply('Provide Some Text To Draw!')
       return
    else:
       pass
 await event.reply('Creating your logo...')
 try:
    text = event.pattern_match.group(1)
    img = Image.open('./Sophia/etc/images (1) (8).jpeg')
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    pointsize = 500
    fillcolor = "white"
    shadowcolor = "blue"
    font = ImageFont.truetype("./Sophia/etc/Dashdemo-ozJA.ttf", 125)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    image_width, image_height = img.size
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
    x = (image_widthz-w)/2
    y= ((image_heightz-h)/2+6)
    draw.text((x, y), text, font=font, fill="white", stroke_width=0, stroke_fill="black")
    fname2 = "SophiaLogo.png"
    img.save(fname2, "png")
    await tbot.send_file(event.chat_id, fname2, caption="Made By @Psylocke_robot")
    if os.path.exists(fname2):
            os.remove(fname2)
 except Exception as e:
   await event.reply(f'Error Go to Help From  @pigasusSupport, {e}')




@register(pattern="^/rlogo ?(.*)")
async def lego(event):
 quew = event.pattern_match.group(1)
 if event.sender_id == OWNER_ID:
     pass
 else:
     
    if not quew:
       await event.reply('Provide Some Text To Draw!')
       return
    else:
       pass
 await event.reply('Creating your logo...')
 try:
    text = event.pattern_match.group(1)
    img = Image.open('./Sophia/etc/large-2967829.jpg')
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    pointsize = 500
    fillcolor = "white"
    shadowcolor = "black"
    font = ImageFont.truetype("./Sophia/etc/Dashdemo-ozJA.ttf", 250)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    image_width, image_height = img.size
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
    x = (image_widthz-w)/2
    y= ((image_heightz-h)/2+6)
    draw.text((x, y), text, font=font, fill="white", stroke_width=0, stroke_fill="black")
    fname2 = "SophiaLogo.png"
    img.save(fname2, "png")
    await tbot.send_file(event.chat_id, fname2, caption="Made By @Psylocke_robot")
    if os.path.exists(fname2):
            os.remove(fname2)
 except Exception as e:
   await event.reply(f'Error Go to Help From  @pigasusSupport, {e}')





file_help = os.path.basename(__file__)
file_help = file_help.replace(".py", "")
file_helpo = file_help.replace("_", " ")


__help__ = """
 ~ /logo {text} :  Create your Yello logo with your name
 ~ /wlogo {text} :  Create your White Logo with your name
 ~ /rlogo {text} :  Create your Red logo with your name
 """
__mod_name__ = "💞Logo💞"
