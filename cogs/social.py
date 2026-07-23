import discord
from discord import app_commands
from discord.ext import commands

import db_utils as db
from utils.embed import create_embed, add_field


class Social(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(
        name="balance",
        description="View your balance."
    )
    async def balance(
        self,
        interaction: discord.Interaction
    ):
        user = await db.get_user(interaction.user.id)

        embed = create_embed("Balance")

        add_field(
            embed,
            "Cash",
            f"₱{user['balance']:,}"
        )

        add_field(
            embed,
            "Bank",
            f"₱{user['bank']:,}"
        )

        add_field(
            embed,
            "Total",
            f"₱{user['balance'] + user['bank']:,}"
        )

        await interaction.response.send_message(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(Social(bot))
