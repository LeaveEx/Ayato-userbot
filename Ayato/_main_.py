import importlib
from pyrogram import idle
from uvloop import install


from Ayato.modules import ALL_MODULES
from Ayato import BOTLOG_CHATID, LOGGER, LOOP, aiosession, app, bots, ids
from Ayato.modules.basic import join

BOT_VER = "0.1.0"
CMD_HANDLER = ["." "," "?" "!"]
MSG_ON = """
🐻‍❄️ **PyroKar Telah Hidup** 🐻‍❄️
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
❍▹ **Userbot Version -** `{}`
❍▹ **Ketik** `{}alive` **untuk Mengecek Bot**
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
"""


async def main():
    await app.start()
    LOGGER("Geez").info("Memulai Geez Pyro..")
    LOGGER("Geez").info("Loading Everything.")
    for all_module in ALL_MODULES:
        importlib.import_module("Geez.modules" + all_module)
    for bot in bots:
        try:
            await bot.start()
            ex = await bot.get_me()
            await logging(bot)
            try:
                await bot.send_message(BOTLOG_CHATID, MSG_ON.format(BOT_VER, gver, CMD_HNDLR))
            except BaseException as a:
                LOGGER("Geez").warning(f"{a}")
            LOGGER("Geez").info("Startup Completed")
            LOGGER("Geez").info(f"Started as {ex.first_name} | {ex.id} ")
            ids.append(ex.id)
        except Exception as e:
            LOGGER("Geez").info(f"{e}")
    await idle()
    await aiosession.close()


if __name__ == "__main__":
    LOGGER("Geez").info("Starting Geez Pyro Userbot")
    install()
    LOOP.run_until_complete(main())
