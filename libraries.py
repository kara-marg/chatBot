import openai
import json
from aiogram import Bot, Dispatcher, types, executor
file = open('config.json', 'r')
config = json.load(file)

bot = Bot(config['token'])
dp = Dispatcher(bot)
