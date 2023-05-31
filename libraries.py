import openai
import googletrans
import langdetect
import json
from aiogram import Bot, Dispatcher, types, executor
from googletrans import Translator, LANGUAGES
from langdetect import detect
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
file = open('config.json', 'r')
config = json.load(file)

bot = Bot(config['token'])
dp = Dispatcher(bot)
