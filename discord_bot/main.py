import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()


class DocBot(commands.Bot):
    """Doc du bot."""

    def __init__(self) -> None:
        super().__init__(command_prefix="/", intents=discord.Intents.all())

    async def on_ready(self) -> None:
        print(f"INFO: Logged on as {self.user}")  # noqa: T201


token = os.getenv("TOKEN")
doc_bot = DocBot()
if token:
    doc_bot.run(token)
