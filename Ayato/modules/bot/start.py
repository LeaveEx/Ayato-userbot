from Ayato import app
from pyrogram import filters


@app.on_message(filters.command("start") & filters.private)
async def start(client, message):
   await message.reply_text("INI UDH HIDUP KONTOLLL")
