import aiosqlite

from config import DATABASE_PATH


CREATE_TABLES = [
    """
    CREATE TABLE IF NOT EXISTS users (
        id TEXT PRIMARY KEY,

        balance INTEGER NOT NULL DEFAULT 5000,
        bank INTEGER NOT NULL DEFAULT 0,

        level INTEGER NOT NULL DEFAULT 1,
        exp INTEGER NOT NULL DEFAULT 0,

        job TEXT,

        prestige INTEGER NOT NULL DEFAULT 0,

        title TEXT NOT NULL DEFAULT 'None',

        commands_used INTEGER NOT NULL DEFAULT 0,

        gambling_won INTEGER NOT NULL DEFAULT 0,
        gambling_lost INTEGER NOT NULL DEFAULT 0,
        gambling_used INTEGER NOT NULL DEFAULT 0,

        created_at INTEGER NOT NULL
    );
    """,

    """
    CREATE TABLE IF NOT EXISTS cooldowns (
        user_id TEXT NOT NULL,
        command TEXT NOT NULL,
        expires_at INTEGER NOT NULL,

        PRIMARY KEY (user_id, command)
    );
    """,

    """
    CREATE TABLE IF NOT EXISTS achievements (
        id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        description TEXT NOT NULL,
        secret INTEGER NOT NULL DEFAULT 0,
        reward_type TEXT NOT NULL,
        reward_value TEXT NOT NULL
    );
    """,

    """
    CREATE TABLE IF NOT EXISTS user_achievements (
        user_id TEXT NOT NULL,
        achievement_id TEXT NOT NULL,
        unlocked_at INTEGER NOT NULL,

        PRIMARY KEY (user_id, achievement_id)
    );
    """,

    """
    CREATE TABLE IF NOT EXISTS pets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,

        owner_id TEXT NOT NULL,

        species TEXT NOT NULL,
        name TEXT NOT NULL,

        health INTEGER NOT NULL DEFAULT 100,
        hunger INTEGER NOT NULL DEFAULT 100,
        happiness INTEGER NOT NULL DEFAULT 100,

        level INTEGER NOT NULL DEFAULT 1,
        exp INTEGER NOT NULL DEFAULT 0,

        alive INTEGER NOT NULL DEFAULT 1,

        last_feed INTEGER NOT NULL,
        last_play INTEGER NOT NULL
    );
    """,

    """
    CREATE TABLE IF NOT EXISTS jobs (
        name TEXT PRIMARY KEY,

        salary_min INTEGER NOT NULL,
        salary_max INTEGER NOT NULL,

        stock INTEGER NOT NULL,

        updated_at INTEGER NOT NULL
    );
    """,

    """
    CREATE TABLE IF NOT EXISTS events (
        id INTEGER PRIMARY KEY AUTOINCREMENT,

        event_type TEXT NOT NULL,
        rarity TEXT NOT NULL,

        reward INTEGER NOT NULL,

        claimed INTEGER NOT NULL DEFAULT 0,
        claimed_by TEXT,

        spawned_at INTEGER NOT NULL
    );
    """
]


async def initialize_database():
    """
    Creates every database table if it doesn't exist.
    """

    async with aiosqlite.connect(DATABASE_PATH) as db:
        await db.execute("PRAGMA foreign_keys = ON;")

        for query in CREATE_TABLES:
            await db.execute(query)

        await db.commit()
