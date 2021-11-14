async def gifspam(e, smex):
    try:
        await e.client(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=sandy.media.document.id,
                    access_hash=smex.media.document.access_hash,
                    file_reference=smex.media.document.file_reference,
                ),
                unsave=True,
            )
        )
    except Exception:
        pass

import asyncio
import base64
import os
from telethon import events
from telethon import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from .. import D3vil, D3vil2, D3vil3, D3vil4, D3vil5, D3vil6, D3vil7, D3vil8, D3vil9, D3vil10, SUDO_USERS

SMEX_USERS = []
for x in SUDO_USERS:
    SMEX_USERS.append(x)



@D3vil.on(events.NewMessage(pattern="/bigspam"))
@D3vil2.on(events.NewMessage(pattern="/bigspam"))
@D3vil3.on(events.NewMessage(pattern="/bigspam"))
@D3vil4.on(events.NewMessage(pattern="/bigspam"))
@D3vil5.on(events.NewMessage(pattern="/bigspam"))
@D3vil6.on(events.NewMessage(pattern="/bigspam"))
@D3vil7.on(events.NewMessage(pattern="/bigspam"))
@D3vil8.on(events.NewMessage(pattern="/bigspam"))
@D3vil9.on(events.NewMessage(pattern="/bigspam"))
@D3vil10.on(events.NewMessage(pattern="/bigspam"))
async def spam(e):
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None)
        Devil = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(Ustad) == 2:
            message = str(Devil[1])
            counter = int(Devil[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.1)
        elif e.reply_to_msg_id and smex.media:
            counter = int(Devil[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex)
                await asyncio.sleep(0.1)
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(Devil[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.1)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)
