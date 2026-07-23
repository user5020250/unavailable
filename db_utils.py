import time
import aiosqlite

from config import DATABASE_PATH, STARTING_BALANCE


# -------------------------------------------------------------
# Connection
# -------------------------------------------------------------

async def connect():
    db = await aiosqlite.connect(DATABASE_PATH)
    db.row_factory = aiosqlite.Row
    return db


# -------------------------------------------------------------
# User
# -------------------------------------------------------------

async def create_user(user_id: int):
    async with await connect() as db:
        await db.execute(
            """
            INSERT OR IGNORE INTO users (
                id,
                balance,
                created_at
            )
            VALUES (?, ?, ?)
            """,
            (
                str(user_id),
                STARTING_BALANCE,
                int(time.time())
            )
        )

        await db.commit()


async def get_user(user_id: int):
    await create_user(user_id)

    async with await connect() as db:
        cursor = await db.execute(
            """
            SELECT *
            FROM users
            WHERE id = ?
            """,
            (str(user_id),)
        )

        return await cursor.fetchone()


# -------------------------------------------------------------
# Balance
# -------------------------------------------------------------

async def get_balance(user_id: int) -> int:
    user = await get_user(user_id)
    return user["balance"]


async def add_balance(user_id: int, amount: int):
    await create_user(user_id)

    async with await connect() as db:
        await db.execute(
            """
            UPDATE users
            SET balance = balance + ?
            WHERE id = ?
            """,
            (amount, str(user_id))
        )

        await db.commit()


async def remove_balance(user_id: int, amount: int):
    await create_user(user_id)

    async with await connect() as db:
        await db.execute(
            """
            UPDATE users
            SET balance = MAX(balance - ?, 0)
            WHERE id = ?
            """,
            (amount, str(user_id))
        )

        await db.commit()


# -------------------------------------------------------------
# Bank
# -------------------------------------------------------------

async def deposit(user_id: int, amount: int):
    async with await connect() as db:
        await db.execute(
            """
            UPDATE users
            SET
                balance = balance - ?,
                bank = bank + ?
            WHERE id = ?
            """,
            (amount, amount, str(user_id))
        )

        await db.commit()


async def withdraw(user_id: int, amount: int):
    async with await connect() as db:
        await db.execute(
            """
            UPDATE users
            SET
                bank = bank - ?,
                balance = balance + ?
            WHERE id = ?
            """,
            (amount, amount, str(user_id))
        )

        await db.commit()


# -------------------------------------------------------------
# Experience
# -------------------------------------------------------------

async def add_exp(user_id: int, amount: int):
    async with await connect() as db:
        await db.execute(
            """
            UPDATE users
            SET exp = exp + ?
            WHERE id = ?
            """,
            (amount, str(user_id))
        )

        await db.commit()


# -------------------------------------------------------------
# Commands Used
# -------------------------------------------------------------

async def increment_commands(user_id: int):
    async with await connect() as db:
        await db.execute(
            """
            UPDATE users
            SET commands_used = commands_used + 1
            WHERE id = ?
            """,
            (str(user_id),)
        )

        await db.commit()


# -------------------------------------------------------------
# Cooldowns
# -------------------------------------------------------------

async def set_cooldown(
    user_id: int,
    command: str,
    expires_at: int
):
    async with await connect() as db:
        await db.execute(
            """
            INSERT INTO cooldowns (
                user_id,
                command,
                expires_at
            )
            VALUES (?, ?, ?)

            ON CONFLICT(user_id, command)

            DO UPDATE SET
                expires_at = excluded.expires_at
            """,
            (
                str(user_id),
                command,
                expires_at
            )
        )

        await db.commit()


async def get_cooldown(
    user_id: int,
    command: str
):
    async with await connect() as db:
        cursor = await db.execute(
            """
            SELECT expires_at
            FROM cooldowns
            WHERE user_id = ?
            AND command = ?
            """,
            (
                str(user_id),
                command
            )
        )

        row = await cursor.fetchone()

        if row is None:
            return 0

        return row["expires_at"]
