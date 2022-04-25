import uvloop
import asyncio, sys
uvloop.install()
from pyrogram import idle
from Test.Bot import TelegramBot


if sys.version_info[1] > 9:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
else:
    loop = asyncio.get_event_loop()

async def main():
    await TelegramBot.start()
    print('Bot Started')
    await idle()

loop.run_until_complete(main())