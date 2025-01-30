import os
import sys
from typing import Optional

from dotenv import load_dotenv
from loguru import logger


class Config:
    def load_settings(self, mode: Optional[str] = None):
        if mode is not None:
            env = mode
        else:
            env = os.getenv("MODE")

        if env is None:
            env = "production"
            load_dotenv()
        else:
            load_dotenv(f".env.{env}".lower())
        logger.info(f"Running* {env}")

    def setup_logging(self, lvl: str = "INFO"):
        logger.add("logs/error_{time:YYYY-MM-DD}.log", level="ERROR", rotation="5MB")
        logger.remove()
        logger.add(sys.stdout, level=lvl)


cfg = Config()


def initialize_app(mode: Optional[str] = None):
    cfg.load_settings(mode)
    cfg.setup_logging()


def initialize_app_testing():
    initialize_app("testing")
