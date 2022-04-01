from pyrogram import Client
from Test.vars import Var

TelegramBot=Client(session_name=":memory:",
    api_id=Var.API_ID,
    api_hash=Var.API_HASH,
    bot_token=Var.BOT_TOKEN,
    workdir="Test",
    plugins={"root": "Test/plugins"},
)
