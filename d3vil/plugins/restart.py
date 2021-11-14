from .. import D3vil, D3vil2, D3vil3, D3vil4, D3vil5, D3vil6, D3vil7, D3vil8, D3vil9, D3vil10, SUDO_USERS
from telethon import events
import os
import random
import sys

SMEX_USERS = []
for x in SUDO_USERS:
    SMEX_USERS.append(x)

@D3vil.on(events.NewMessage(pattern="/restart"))
@D3vil2.on(events.NewMessage(pattern="/restart"))
@D3vil3.on(events.NewMessage(pattern="/restart"))
@D3vil4.on(events.NewMessage(pattern="/restart"))
@D3vil5.on(events.NewMessage(pattern="/restart"))
@D3vil6.on(events.NewMessage(pattern="/restart"))
@D3vil7.on(events.NewMessage(pattern="/restart"))
@D3vil8.on(events.NewMessage(pattern="/restart"))
@D3vil9.on(events.NewMessage(pattern="/restart"))
@D3vil10.on(events.NewMessage(pattern="/restart"))
async def restart(e):
    if e.sender_id in SMEX_USERS:
        text = " 🤖𝐑𝐄𝐒𝐓𝐀𝐑𝐓𝐄𝐃🤖\n🔰𝐏𝐋𝐄𝐀𝐒𝐄 𝐖𝐀𝐈𝐓 𝐓𝐈𝐋𝐋 𝐈𝐓 𝐑𝐄𝐁𝐎𝐎𝐓𝐒...."
        await e.reply(text, parse_mode=None, link_preview=None)
        try:
            await D3vil.disconnect()
        except Exception:
            pass
        try:
            await D3vil2.disconnect()
        except Exception:
            pass
        try:
            await D3vil3.disconnect()
        except Exception:
            pass
        try:
            await D3vil4.disconnect()
        except Exception:
            pass
        try:
            await D3vil5.disconnect()
        except Exception:
            pass
        try:
            await D3vil6.disconnect()
        except Exception:
            pass
        try:
            await D3vil7.disconnect()
        except Exception:
            pass
        try:
            await D3vil8.disconnect()
        except Exception:
            pass
        try:
            await D3vil9.disconnect()
        except Exception:
            pass
        try:
            await D3vil10.disconnect()
        except Exception:
            pass
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()
