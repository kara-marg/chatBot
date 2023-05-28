print('gpt')
from libraries import Dispatcher, types, Bot, executor, json
from libraries import dp, bot
from libraries import openai

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
print('gpt')
file = open('config.json', 'r')
config = json.load(file)

openai.api_key = config['openai']


messages = [
    {"role": "system", "content": "system responds"},
    {"role": "user", "content": "user asks"}]


class MyStates(StatesGroup):
    WAITING_FOR_INPUT = State()



def update(messages, role, content):
    messages.append({"role": role, "content": content})
    return messages
# async def start():
#     await bot.send_message('Привіт! Задай мені питання)')

# @dp.message_handler(commands=['startgpt'])
# async def start_command(message: types.Message):
#     await message.answer('Привіт! Задай мені питання)')

@dp.message_handler(commands=['stopgpt'])
async def start_command(message: types.Message):
    await message.answer('Гарного для! Слава Україні!')


@dp.message_handler(state=MyStates.WAITING_FOR_INPUT, content_types=types.ContentType.TEXT)
async def handle_input(message: types.Message, state: FSMContext):
    # Отримати відповідь від користувача
    response_text = message.text

    # Очистити стан
    await state.finish()

    # Оновити історію повідомлень
    update(messages, "user", response_text)

    # Знайти відповідь за допомогою OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)

    # Надіслати відповідь користувачу
    message.answer(response['choices'][0]['text'])

    # Оновити історію повідомлень
    update(messages, "system", response['choices'][0]['text'])


@dp.message_handler()
async def send(message: types.Message):
    update(messages, "user", message.text)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)

    await message.answer(response['choices'][0]['message']['content'])

    update(messages, "system", response['choices'][0]['message']['content'])


# executor.start_polling(dp, skip_updates=True)