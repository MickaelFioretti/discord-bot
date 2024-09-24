import logging
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

client = discord.Client(intents=discord.Intents.all())

bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())


@client.event
async def on_ready() -> None:
    print(f"Logged on as {client.user}")


@client.event
async def on_message(message: discord.Message) -> None:
    if message.content.lower() == "ping":
        await message.channel.send("Pong!")


@bot.command(name="del")
async def delete_messages(ctx: commands.Context, number_of_message: int) -> None:
    print(f"Deleting {number_of_message} messages")
    async for message in ctx.channel.history(limit=number_of_message + 1):
        await message.delete()


token = os.getenv("TOKEN")
if token:
    bot.run(token)
    # client.run(token)
else:
    logging.error("Token not found")
