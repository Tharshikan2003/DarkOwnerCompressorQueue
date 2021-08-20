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
            [Button.inline("HELP", data="ihelp")],
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
        "**🐠 A Quality CompressorQueue**\n\n+This Bot Compress Videos With Negligible Quality Change.\n+Generate Sample Compressed Video\n+Screenshots Too\n+Easy to Use\n-Due to Quality Settings Bot Takes Time To Compress.\nSo Be patience Nd Send videos One By One After Completing.\nDont Spam Bot.\n\nJust Forward Video To Get Options",
        buttons=[Button.inline("BACK", data="beck")],
    )


async def beck(event):
    await event.edit(
        f"Hi `{event.sender.first_name}`\nThis is A Bot  Which Can Encode Videos.",
        buttons=[
            [Button.inline("HELP", data="ihelp")],
            [
                Button.url("Channel", url="t.me/animes_encoded"),
                Button.url("Boss", url="t.me/Bro_isDarkal"),
            ],
        ],
    )
