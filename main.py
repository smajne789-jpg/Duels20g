from __future__ import annotations

import asyncio
import sys
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

try:
    from bot.main import main as run_bot
except ImportError as error:
    raise RuntimeError(
        "Не удалось импортировать bot.main. Убедись, что папка 'bot' загружена рядом с main.py."
    ) from error


if __name__ == "__main__":
    asyncio.run(run_bot())
