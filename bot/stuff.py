#    This file is part of the CompressorQueue distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/1Danish-00/CompressorQueue/blob/main/License> .

from .worker import *


async def up(event):
    if not event.is_private:
        return
    stt = dt.now()
    ed = dt.now()
    v = ts(int((ed - uptime).seconds) * 1000)
    ms = (ed - stt).microseconds / 1000
    p = f"🌋Pɪɴɢ = {ms}ms"
    await event.reply(v + "\n" + p)


async def start(event):
    await event.reply(
        f"Hi `{event.sender.first_name}`\nHi, I am Dark's Bot Which Can Encode Videos.\nI an using an official ffmpeg code used by dark for @Animes_Encoded , So pls dont try to encode any anime episode\\This Bot Was Hosted On Railways and On Qovery.",
        buttons=[
            [Button.inline("What Code Is Used In FFMPEG", data="ihelp")],
            [
                Button.url("Channel", url="t.me/animes_encoded"),
                Button.url("Boss", url="t.me/Bro_isDarkal"),
            ],
        ],
    )


async def help(event):
    await event.reply(
        "**Dont Read My Bio {Moron}**\n\n+I Encode  Videos With Negligible Quality {480p} Change.\n+Generate Sample Compressed Video To check quality\n+Easy to Use\n-Due to Quality Settings Bot Takes Time To Compress , So join @Animes_encoded.\nSo, Spam me me me.\nDont{ignore this} Spam Bot.\n\nJust Forward Video To Get Options"
    )


async def ihelp(event):
    await event.edit(
        "**⏳ ffmpeg -i  -c:v libx265 -metadata  title=DarkEncodes -s 1280x720 -crf 29.5 -c:a libopus -b:a 32k -c:s copy  -map 0 -ac 2  -ab 36k -pix_fmt yuv420p -preset faster  -vbr 2 '''{}''' -y **\n\n+This Bot Uses Thia code to encode  Videos With Negligible Quality Change.\n+Its a 720p code\n+It Has Queue Features also\n+Easy to Use\n-Due to The use of bot for @Animes_encoded, this bot is not for public use.\nSo, Ask me first before using.\nDont Spam Bot.\n\nThanka for reading it",
        buttons=[Button.inline("BACK", data="beck")],
    )


async def beck(event):
    await event.edit(
        f"Hi `{event.sender.first_name}`\nThis is A Bot  Which Can Encode Videos.",
        buttons=[
            [Button.inline("What code Is used in FFMPEG", data="ihelp")],
            [
                Button.url("Channel", url="t.me/animes_encoded"),
                Button.url("Boss", url="t.me/Bro_isDarkal"),
            ],
        ],
    )
