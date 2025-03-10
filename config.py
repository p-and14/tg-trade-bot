import os
from dotenv import load_dotenv
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

env_path = BASE_DIR.joinpath(".env")
if env_path.exists():
    load_dotenv(env_path)

# DB
DB_NAME = os.environ.get("DB_NAME", "postgres")
DB_USER = os.environ.get("DB_USER", "postgres")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "postgres")
DB_HOST = os.environ.get("DB_HOST", "0.0.0.0")
DB_PORT = os.environ.get("DB_PORT", "5432")

# TG
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN")
