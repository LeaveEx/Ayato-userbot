import os
import sys
from pyrogram import Client



def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "Ayato"])

async def join(client):
    try:
        await client.join_chat("senzusupp")
        await client.join_chat("idealizerd")
        await client.join_chat("stereoproject")
        await client.join_chat("themusicLD")
    except BaseException:
        pass
