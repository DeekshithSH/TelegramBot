from Test.Bot import TelegramBot
from pyrogram import filters

@TelegramBot.on_message(filters.private)
async def test(b, m):
    print(m.text)
    await m.reply_text("Use @tgxlinkbot insted of this bot\nby @DeekshithSH")
