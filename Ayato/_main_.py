import time
import importlib 
from pyrogram import idle
from uvloop import install

from config import BOT_VER, CMD_HANDLER
from Ayato import BOTLOG_CHATID, LOGGER, LOOP, aiosession, bot1, bots, app, ids
from Ayato.split.misc import create_botlog, git, heroku
from Ayato.modules import ALL_MODULES

MSG_ON = """
🔥 **RamPyro-Bot Menyala** 🔥
━───────╯⇕╰───────━
🤖 **Userbot Version -** `{}`
⚜️ prefixes: ? ! , . *
⌨️ **Ketik** `{}rama` **untuk Mengecheck Bot**
━───────╮⇕╭───────━
"""

async def main():
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module(f"rams.modules.{all_module}")
    for bot in bots:
        try:
            await bot.start()
            bot.me = await bot.get_me()
            await bot.join_chat("geezram")
            await bot.join_chat("userbotch")
            await bot.join_chat("GeezSupport")
            ids.append(bot.me.id)
            try:
                await bot.send_message(
                    BOTLOG_CHATID, MSG_ON.format(BOT_VER, CMD_HANDLER)
                )
            except BaseException:
                pass
            LOGGER("Ayato").info(
                f"Logged in as {bot.me.first_name} | [ {bot.me.id} ]"
            )
        except Exception as a:
            LOGGER("main").warning(a)
    LOGGER("Ayato").info(f"RamPyro-Bot v{BOT_VER} [🔥 UDAH AKTIF NGENTOT! 🔥]")
    if not str(BOTLOG_CHATID).startswith("-100"):
        await create_botlog(bot1)
    await idle()
    await aiosession.close()


if __name__ == "__main__":
    LOGGER("Ayato").info("Starting RamPyro-Bot")
    install()
    heroku()
    LOOP.run_until_complete(main())
