from discord.ext import commands, tasks
from discord import Interaction
from dotenv import load_dotenv
import os
import discord
load_dotenv()
PREFIX = "."
client = commands.Bot(command_prefix=PREFIX, intents=discord.Intents.all())
@client.event
async def on_ready():
    print(f"bot logged in with {client.user}")
    try: 
        synced = await client.tree.sync()
        print(f"Synced {len(synced)} cmd(s).")
    except Exception as e:
        print(e)
@client.tree.command(name="ping")
async def ping(ctx):
    await ctx.response.send_message(f"i love you \n`{round(client.latency,1)}ms`")
client.run(os.getenv("TOKEN"))

