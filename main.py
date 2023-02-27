from aiogram import Bot, types, Dispatcher
import time
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

bot = Bot(os.getenv("TOKEN"))