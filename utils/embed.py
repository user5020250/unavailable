import discord

from config import EMBED_COLOR


def create_embed(
    title: str,
    description: str | None = None
) -> discord.Embed:
    """
    Creates a standardized embed for the bot.
    """

    embed = discord.Embed(
        title=f"**{title}**",
        description=description,
        color=EMBED_COLOR
    )

    return embed


def add_field(
    embed: discord.Embed,
    name: str,
    value,
    inline: bool = False
):
    """
    Adds a formatted field using backticks.
    """

    embed.add_field(
        name=f"**{name}**",
        value=f"`{value}`",
        inline=inline
    )

    return embed


def success_embed(
    title: str,
    message: str
) -> discord.Embed:
    embed = create_embed(title)
    add_field(embed, "Success", message)
    return embed


def error_embed(
    title: str,
    message: str
) -> discord.Embed:
    embed = create_embed(title)
    add_field(embed, "Error", message)
    return embed
