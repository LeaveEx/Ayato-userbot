import os
import sys
from pyrogram import Client



def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "Ayato"])

async def join(client):
    try:
        await client.join_chat("senzusupp")
        await client.join_chat("idealizerd")
        await client.join_chat("Stereoproject")
        await client.join_chat("themuisicLD")
    except BaseException:
        pass
