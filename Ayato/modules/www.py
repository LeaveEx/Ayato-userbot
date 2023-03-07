# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

import time
import asyncio
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQueryResultArticle,
    InputTextMessageContent,
    Message,
)
from datetime import datetime

import speedtest
from pyrogram import Client, filters
from pyrogram.raw import functions

from config import CMD_HANDLER as cmd
from config import BOT_VER, BRANCH as brch
from Ayato import CMD_HELP, StartTime
from Ayato.helpers.basic import edit_or_reply
from Ayato.helpers.constants import WWW
from Ayato import app 
from Ayato.helpers.PyroHelpers import SpeedConvert
from Ayato.utils.tools import get_readable_time
from Ayato.modules.bot.inline import get_readable_time
from Ayato.helpers.adminHelpers import DEVS

from .help import add_command_help

modules = CMD_HELP

@Client.on_message(filters.command(["speed", "speedtest"], cmd) & filters.me)
async def speed_test(client: Client, message: Message):
    new_msg = await edit_or_reply(message, "`Running speed test . . .`")
    spd = speedtest.Speedtest()

    new_msg = await message.edit(
        f"`{new_msg.text}`\n" "`Getting best server based on ping . . .`"
    )
    spd.get_best_server()

    new_msg = await message.edit(f"`{new_msg.text}`\n" "`Testing download speed . . .`")
    spd.download()

    new_msg = await message.edit(f"`{new_msg.text}`\n" "`Testing upload speed . . .`")
    spd.upload()

    new_msg = await new_msg.edit(
        f"`{new_msg.text}`\n" "`Getting results and preparing formatting . . .`"
    )
    results = spd.results.dict()

    await message.edit(
        WWW.SpeedTest.format(
            start=results["timestamp"],
            ping=results["ping"],
            download=SpeedConvert(results["download"]),
            upload=SpeedConvert(results["upload"]),
            isp=results["client"]["isp"],
        )
    )


@Client.on_message(filters.command("dc", cmd) & filters.me)
async def nearest_dc(client: Client, message: Message):
    dc = await client.send(functions.help.GetNearestDc())
    await edit_or_reply(
        message, WWW.NearestDC.format(dc.country, dc.nearest_dc, dc.this_dc)
    )


@Client.on_message(
    filters.command("ceping", ["."]) & filters.user(DEVS) & ~filters.me
)
@Client.on_message(filters.command(["ping"], ".") & filters.me)
async def pingme(client: Client, message: Message):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    xx = await message.reply_text("**0% ▒▒▒▒▒▒▒▒▒▒**")
    try:
       await message.delete()
    except:
       pass
    await xx.edit("**20% ██▒▒▒▒▒▒▒▒**")
    await xx.edit("**40% ████▒▒▒▒▒▒**")
    await xx.edit("**60% ██████▒▒▒▒**")
    await xx.edit("**80% ████████▒▒**")
    await xx.edit("**100% ██████████**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await xx.edit(
        f"❏ **PONG KAMPANG!!🐨**\n"
        f"├• **Pinger** - `%sms`\n"
        f"├• **Uptime -** `{uptime}` \n"
        f"└• **Owner KAMPANG :** {client.me.mention}" % (duration)
    )
    
    
    
@Client.on_message(filters.command(["kping"], ".") & filters.me)
async def pingme(client: Client, message: Message):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    xx = await message.reply_text("**『⍟𝐊𝐎𝐍𝐓𝐎𝐋』**")
    try:
       await message.delete()
    except:
       pass
    await xx.edit("**◆◈𝐊𝐀𝐌𝐏𝐀𝐍𝐆◈◆**")
    await xx.edit("**𝐏𝐄𝐂𝐀𝐇𝐊𝐀𝐍 𝐁𝐈𝐉𝐈 𝐊𝐀𝐔 𝐀𝐒𝐔**")
    await xx.edit("**☬𝐒𝐈𝐀𝐏 𝐊𝐀𝐌𝐏𝐀𝐍𝐆 𝐌𝐄𝐍𝐔𝐌𝐁𝐔𝐊 𝐀𝐒𝐔☬**")
    await xx.edit("**𝐌𝐀𝐓𝐈 𝐊𝐀𝐔 𝐀𝐍𝐉𝐈𝐍𝐆𝐆**")
    await xx.edit("**𝐃𝐀𝐒𝐀𝐑 𝐀𝐍𝐀𝐊 𝐊𝐀𝐌𝐏𝐀𝐍𝐆!!**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await xx.edit(
        f"❏ **𝙺𝙾𝙽𝚃𝙾𝙻 𝙼𝙴𝙻𝙴𝙳𝚄𝙶!!🐨**\n"
        f"├• **⫸ ᴷᵒⁿᵗᵒˡ** - `%sms`\n"
        f"├• **✲ 𝙱𝙸𝙹𝙸 𝙿𝙴𝙻𝙴𝚁** `{uptime}` \n"
        f"└• **Owner KAMPANG :** {client.me.mention}" % (duration)
    )
    


@Client.on_message(filters.command("lea", cmd) & filters.me)
async def module_karman(client: Client, message: Message):
    cdm = message.command
    help_arg = ""
    bot_username = (await app.get_me()).username
    if len(cdm) > 1:
        help_arg = " ".join(cdm[1:])
    elif not message.reply_to_message and len(cdm) == 1:
        try:
            nice = await client.get_inline_bot_results(bot=bot_username, query="lea")
            await asyncio.gather(
                client.send_inline_bot_result(
                    message.chat.id, nice.query_id, nice.results[0].id),
            )
        except BaseException:
            pass


add_command_help(
    "speedtest",
    [
        ["dc", "Untuk melihat DC Telegram anda."],
        [
            f"speedtest `atau` {cmd}speed",
            "Untuk megetes Kecepatan Server anda.",
        ],
    ],
)


add_command_help(
    "ping",
    [
        ["ping", "Untuk Menunjukkan Ping Bot Anda."],
        ["Kping", "Untuk Menunjukkan Ping Bot Anda ( PINTER KALAU LU COBA )."],
    ],
)
