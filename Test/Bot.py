from pyrogram import Client

TelegramBot=Client(session_name=":memory:",
    api_id=<api_id>,
    api_hash='<api_hash>',
    bot_token="<Bot Token>",
    workdir="Test",
    plugins={"root": "Test/plugins"},
)
