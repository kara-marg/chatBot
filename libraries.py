import openai
import googletrans
import langdetect
import json
from aiogram import Bot, Dispatcher, types, executor
from googletrans import Translator, LANGUAGES
from langdetect import detect
file = open('config.json', 'r')
config = json.load(file)

bot = Bot(config['token'])
dp = Dispatcher(bot)
