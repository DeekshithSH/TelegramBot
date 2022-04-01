from Test.Bot import TelegramBot
from pyrogram import filters

@TelegramBot.on_message(filters.private & filters.text)
async def test(b, m):
    print(m.text)
    await m.reply_text(m.text)