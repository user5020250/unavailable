import os
import discord
from discord.ext import commands

from config import TOKEN
from database import initialize_database


class EconomyBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()

        super().__init__(
            command_prefix="!",
            intents=intents,
            help_command=None
        )

    async def setup_hook(self):
        print("Initializing database...")

        await initialize_database()

        print("Database initialized.")

        # Automatically load every cog
        if os.path.isdir("cogs"):
            for filename in os.listdir("cogs"):
                if filename.endswith(".py"):
                    extension = f"cogs.{filename[:-3]}"

                    try:
                        await self.load_extension(extension)
                        print(f"Loaded {extension}")

                    except Exception as e:
                        print(f"Failed to load {extension}")
                        print(e)

        print("Syncing slash commands...")

        synced = await self.tree.sync()

        print(f"Synced {len(synced)} command(s).")

    async def on_ready(self):
        activity = discord.Game("/help")

        await self.change_presence(activity=activity)

        print("-" * 50)
        print(f"Logged in as {self.user}")
        print(f"ID: {self.user.id}")
        print("-" * 50)


bot = EconomyBot()

bot.run(TOKEN)
