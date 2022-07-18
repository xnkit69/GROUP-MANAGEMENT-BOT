import os
import re
import random
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from Ankit.events import register
from Ankit import telethn as tbot


PHOTO = [
    "https://telegra.ph/file/6b1d7cb290d37f4bc25f6.jpg",
]

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**ʜᴇʏ​ [{event.sender.first_name}](tg://user?id={event.sender.id}),ɪ ᴀᴍ ᴀɴᴋɪᴛ 🇮🇳 **\n━━━━━━━━━━━━━━━━━━━\n"
  TEXT += f"» **ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ : [ᴀɴᴋɪᴛ 🇮🇳](https://t.me/XnKiTKuMaR)** \n"
  TEXT += f"» **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{tlhver}` \n"
  TEXT += f"» **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{pyrover}` \n━━━━━━━━━━━━━━━━━\n\n"
  BUTTON = [[Button.url("🔹ʜᴇʟᴘ🔹", "https://t.me/XNKITKBOT?start=help"), Button.url("⭐ᴅᴇᴠᴇʟᴏᴘᴇʀ⭐", "https://t.me/XnKiTKuMaR")]]
  ran = random.choice(PHOTO)
  await tbot.send_file(event.chat_id, ran, caption=TEXT,  buttons=BUTTON)

## Alive mod
