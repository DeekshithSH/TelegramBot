import asyncio, sys
from pyrogram import idle
from Test.Bot import TelegramBot



# loop = asyncio.new_event_loop()
# asyncio.set_event_loop(loop)

loop = asyncio.get_event_loop()

async def main():
    await TelegramBot.start()
    print('Bot Started')
    await idle()

loop.run_until_complete(main())
loop.close
