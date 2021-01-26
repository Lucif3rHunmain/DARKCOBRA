# Author: Shubhendra Kushwaha (@TheShubhendra)
# Email: shubhendrakushwaha94@gmail.com
import requests
import pygita
import os
from userbot.utils import admin_cmd, edit_delete
from userbot import CMD_HELP
from userbot.uniborgConfig import Config

CLIENT_ID = os.environ.get("GITA_CLIENT_ID", None)
CLIENT_SECRET = os.environ.get("GITA_CLIENT_SECRET", None)
""" Get API crendentials from https://bhagavadgita.io . """


@borg.on(admin_cmd(pattern="gita +(.*) +(.*)$"))
async def gita(event):
    """ To get a specific verse from a specific chapter in English. """
    if CLIENT_ID is None or CLIENT_SECRET is None:
        await event.edit_delete(
            event,
            "`Please add required GITA_CLIENT_SECRET and GITA_CLIENT_ID env var`",
            10,
        )
        return
    pygita.auth(CLIENT_ID, CLIENT_SECRET)
    chapter_number = int(event.pattern_match.group(1))
    verse_number = int(event.pattern_match.group(2))
    verse = pygita.get_verse(chapter_number, verse_number, language="en")
    await event.edit(f"**{verse.text}** {verse.meaning}")


@borg.on(admin_cmd(pattern="gita +(.*) +(.*) hi$"))
async def gita(event):
    """ To get a specific verse from a specific chapter in Hindi. """
    if CLIENT_ID is None or CLIENT_SECRET is None:
        await event.edit_delete(
            event,
            "`Please add required GITA_CLIENT_SECRET and GITA_CLIENT_ID env var`",
            10,
        )
        return
    pygita.auth(CLIENT_ID, CLIENT_SECRET)
    chapter_number = int(event.pattern_match.group(1))
    verse_number = int(event.pattern_match.group(2))
    verse = pygita.get_verse(chapter_number, verse_number, language="hi")
    await event.edit(f"**{verse.text}** {verse.meaning}")

CMD_HELP.update(
    {
        "geeta":".gita <chapter_number> <verse_number> "
        "\nUsage: Get a specific verse from a particular chapter \n\n"
        ".gita <chapter_number> <verse_number> hi"
        "\nUsage: Get a specific verse from a particular chapter in hindi.\n\n"
    }
)
