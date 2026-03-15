import asyncio
import logging
import sys
import time

# -------- Logging setup first (avoid circular import issues) --------
logging.basicConfig(
    level=logging.INFO,
    handlers=[
        logging.FileHandler("unzip-bot.log"),
        logging.StreamHandler()
    ],
    format="%(asctime)s - %(levelname)s - %(name)s - %(threadName)s - %(message)s",
)

LOGGER = logging.getLogger("unzipbot")

logging.getLogger("aiohttp").setLevel(logging.WARNING)
logging.getLogger("aiofiles").setLevel(logging.WARNING)
logging.getLogger("GitPython").setLevel(logging.WARNING)
logging.getLogger("motor").setLevel(logging.WARNING)
logging.getLogger("Pillow").setLevel(logging.WARNING)
logging.getLogger("psutil").setLevel(logging.WARNING)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

# -------- Other imports after logger --------
from pyrogram import Client
from .config.config import Config

# -------- Event loop setup --------
if sys.platform.startswith("win32") or sys.platform.startswith("linux-cross"):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
else:
    import uvloop

    uvloop.install()
    loop = uvloop.new_event_loop()
    asyncio.set_event_loop(loop)

boottime = time.time()
plugins = dict(root="modules")

# -------- Pyrogram client --------
unzipbot_client = Client(
    name="unzip-bot",
    bot_token=Config.BOT_TOKEN,
    api_id=Config.APP_ID,
    api_hash=Config.API_HASH,
    plugins=plugins,
    sleep_threshold=7200,
    max_concurrent_transmissions=3,
)
