from libraries import Dispatcher, types, Bot, executor, json
from libraries import dp, bot
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('ChatAI')
    button2 = types.KeyboardButton('Translate')

    markup.add(button1, button2)

    await message.answer('Hello, {0.first_name}!'.format(message.from_user), reply_markup=markup)

@dp.message_handler(text='ChatAI')
async def bot_message(message: types.Message):

    import chatgpt
@dp.message_handler(text='Translate')
async def bot_message_translate(message: types.Message):
    import translate


executor.start_polling(dp, skip_updates=True)