from pathlib import Path
from dotenv import load_dotenv
import os

# -------------------------------------------------------------
# Load Environment Variables
# -------------------------------------------------------------

load_dotenv()

TOKEN = os.getenv("TOKEN")

if not TOKEN:
    raise RuntimeError(
        "Discord bot token not found. Create a .env file with TOKEN=YOUR_BOT_TOKEN"
    )

# -------------------------------------------------------------
# Project Directories
# -------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

ASSETS_DIR = BASE_DIR / "assets"
ASSETS_DIR.mkdir(parents=True, exist_ok=True)

DATABASE_PATH = DATA_DIR / "economy.db"

# -------------------------------------------------------------
# Bot Appearance
# -------------------------------------------------------------

EMBED_COLOR = 0x000000

# -------------------------------------------------------------
# Economy Settings
# -------------------------------------------------------------

STARTING_BALANCE = 5_000
STARTING_BANK = 0

MAX_PRESTIGE = 10
MAX_PETS = 5

# -------------------------------------------------------------
# Experience
# -------------------------------------------------------------

BASE_EXP_PER_LEVEL = 100

# -------------------------------------------------------------
# Background Tasks
# -------------------------------------------------------------

JOB_REFRESH_SECONDS = 30 * 60      # 30 minutes
EVENT_INTERVAL_SECONDS = 15 * 60   # 15 minutes

# -------------------------------------------------------------
# Reward Cooldowns
# -------------------------------------------------------------

DAILY_COOLDOWN = 24 * 60 * 60
WEEKLY_COOLDOWN = 7 * 24 * 60 * 60
MONTHLY_COOLDOWN = 30 * 24 * 60 * 60
YEARLY_COOLDOWN = 365 * 24 * 60 * 60

# -------------------------------------------------------------
# Activity Cooldowns
# -------------------------------------------------------------

WORK_COOLDOWN = 2 * 60
OVERTIME_COOLDOWN = 10 * 60

BEG_COOLDOWN = 2 * 60
COOK_COOLDOWN = 2 * 60
FISH_COOLDOWN = 2 * 60
FARM_COOLDOWN = 2 * 60
HARVEST_COOLDOWN = 2 * 60

ROB_COOLDOWN = 60 * 60

PET_FEED_COOLDOWN = 10 * 60

BANK_INTEREST_COOLDOWN = 24 * 60 * 60

# -------------------------------------------------------------
# Economy Rewards
# -------------------------------------------------------------

WORK_REWARD = (1_000, 5_000)
OVERTIME_REWARD = (5_000, 10_000)

BEG_REWARD = (1_000, 5_000)
COOK_REWARD = (1_000, 5_000)
FISH_REWARD = (1_000, 5_000)
FARM_REWARD = (1_000, 5_000)
HARVEST_REWARD = (1_000, 5_000)

# -------------------------------------------------------------
# Event Rewards
# -------------------------------------------------------------

LOST_WALLET_REWARD = (10_000, 30_000)
TREASURE_CHEST_REWARD = (10_000, 100_000)
CASH_RAIN_REWARD = (5_000, 10_000)
ATM_GLITCH_REWARD = (10_000, 10_000)
JACKPOT_REWARD = (100_000, 2_000_000)
