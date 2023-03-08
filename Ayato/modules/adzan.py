import json

import requests

from pyrogram import Client, filters
from pyrogram.types import Message

from Ayato import CMD_HANDLER as cmd
from Ayato.helpers.SQL.globals import gvarstatus
from Ayato.utils import edit_delete, edit_or_reply
from Ayato.modules.help import add_command_help


@Client.on_message(filters.me & filters.command("adzan", cmd))
async def get_adzan(adzan):
    "Shows you the Islamic prayer times of the given city name"
    input_str = adzan.pattern_match.group(1)
    LOKASI = gvarstatus("WEATHER_DEFCITY") or "Jakarta" if not input_str else input_str
    url = f"http://muslimsalat.com/{LOKASI}.json?key=bd099c5825cbedb9aa934e255a81a5fc"
    request = requests.get(url)
    if request.status_code != 200:
        return await edit_delete(
            adzan, f"**Tidak Dapat Menemukan Kota** `{LOCATION}`", 120
        )
    result = json.loads(request.text)
    catresult = f"<b>Jadwal Shalat Hari Ini:</b>\
            \n<b>📆 Tanggal </b><code>{result['items'][0]['date_for']}</code>\
            \n<b>📍 Kota</b> <code>{result['query']}</code> | <code>{result['country']}</code>\
            \n\n<b>Terbit  : </b><code>{result['items'][0]['shurooq']}</code>\
            \n<b>Subuh : </b><code>{result['items'][0]['fajr']}</code>\
            \n<b>Zuhur  : </b><code>{result['items'][0]['dhuhr']}</code>\
            \n<b>Ashar  : </b><code>{result['items'][0]['asr']}</code>\
            \n<b>Maghrib : </b><code>{result['items'][0]['maghrib']}</code>\
            \n<b>Isya : </b><code>{result['items'][0]['isha']}</code>\
    "
    await edit_or_reply(adzan, catresult, "html")


add_command_help(
  "adzan",
    [
        [
            "adzan <nama kota>",
            "Menunjukkan waktu jadwal sholat dari kota yang diberikan",
        ],
    ],
)
