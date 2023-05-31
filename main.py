# from libraries import Dispatcher, types, Bot, executor, json
# from libraries import dp, bot
# from libraries import FSMContext
# from libraries import State, StatesGroup
# @dp.message_handler(commands=['start'])
# async def start(message: types.Message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     button1 = types.KeyboardButton('ChatAI')
#     button2 = types.KeyboardButton('Translate')
#
#     markup.add(button1, button2)
#
#     await message.answer('Hello, {0.first_name}!'.format(message.from_user), reply_markup=markup)
#
# class MainMenuState(StatesGroup):
#     MENU = State()  # Стан головного меню
#     TRANSLATOR = State()  # Стан перекладача
#     API = State()  # Стан використання Open API
#     # Додайте інші стани, якщо потрібно
#
#
# @dp.message_handler(text='ChatAI')
# async def bot_message(message: types.Message):
#     await message.answer('Привіт! Задай мені питання')
#     import chatgpt
#
#
# @dp.message_handler(text='Translate')
# async def bot_message_translate(message: types.Message, state: FSMContext):
#     await message.answer('Вкажіть на яку мову треба перекласти. От приклади мов:\n'
#                          'aнглійська(en)\n'
#                          'українська(uk)\n'
#                          'іспанська(es)\n'
#                          'французька(fr)\n'
#                          'німецька(de)\n'
#                          'італійська(it)\n'
#                          'вірменська(hy)\n')
#     await MainMenuState.TRANSLATOR.set()
#     import translate
#
#
# executor.start_polling(dp, skip_updates=True)
#
from libraries import Dispatcher, types, Bot, executor, json
from libraries import dp, bot
from libraries import FSMContext
from libraries import State, StatesGroup
from libraries import Translator, LANGUAGES
from libraries import bot, types, dp
from libraries import json
from libraries import detect
from libraries import FSMContext
from libraries import Dispatcher, types, Bot, executor, json
from libraries import dp, bot
from libraries import FSMContext
from libraries import Dispatcher, types, Bot, executor, json
from libraries import dp, bot
from libraries import FSMContext
from libraries import State, StatesGroup
from libraries import Translator, LANGUAGES

translator = Translator()
dest = None


class MainMenuState(StatesGroup):
    MENU = State()  # Стан головного меню
    TRANSLATOR = State()  # Стан перекладача
    API = State()  # Стан використання Open API
    # Додайте інші стани, якщо потрібно


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('ChatAI')
    button2 = types.KeyboardButton('Translate')

    markup.add(button1, button2)

    await message.answer('Hello, {0.first_name}!'.format(message.from_user), reply_markup=markup)


@dp.message_handler(text='ChatAI')
async def bot_message(message: types.Message):
    await message.answer('Привіт! Задай мені питання')
    import chat_ai


@dp.message_handler(text='Translate')
async def bot_message_translate(message: types.Message, state: FSMContext):
    await message.answer('Вкажіть на яку мову треба перекласти. От приклади мов:\n'
                         'англійська(en)\n'
                         'українська(uk)\n'
                         'іспанська(es)\n'
                         'французька(fr)\n'
                         'німецька(de)\n'
                         'італійська(it)\n'
                         'вірменська(hy)\n')
    # await translate_language(message)


@dp.message_handler(commands='language')
async def translate_language(message: types.Message):
    if len(message.text.split()) > 1:
        target_language = message.text.split()[1].lower()
        if target_language in LANGUAGES:
            global dest
            dest = target_language
            await message.answer(f'Your language is {dest}', parse_mode="HTML")
        else:
            await message.answer('Invalid destination language.')
    else:
        await message.answer('Please specify the target language1.')


# @dp.message_handler(state=MainMenuState.TRANSLATOR)
@dp.message_handler(commands='translate')
async def handle_translation(message: types.Message):
    await message.answer('start of translation')
    message_txt = message.text.split(' ', 1)[1]
    if dest is None:
        await message.answer('Please specify the target language.')
    else:
        src = detect(message_txt)
        translated_text = translator.translate(message_txt, src=src, dest=dest).text
        await message.answer(translated_text, parse_mode="HTML")


@dp.message_handler(commands='exit')
async def exit_translation(message: types.Message, state: FSMContext):
    await state.finish()
    await MainMenuState.MAIN_MENU.set()
    await message.answer('You have exited the translation mode. Back to the main menu.')

executor.start_polling(dp, skip_updates=True)
