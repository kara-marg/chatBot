from libraries import detect
from libraries import Dispatcher, types, Bot, executor, json
from libraries import dp, bot
from libraries import FSMContext
from libraries import State, StatesGroup
from libraries import Translator, LANGUAGES

translator = Translator()
dest = None


class MainMenuState(StatesGroup):
    MENU = State()
    TRANSLATOR = State()
    API = State()



@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('ChatAI')
    button2 = types.KeyboardButton('Translate')

    markup.add(button1, button2)

    await message.answer('Привіт, {0.first_name}!'.format(message.from_user), reply_markup=markup)


@dp.message_handler(text='ChatAI')
async def bot_message(message: types.Message):
    await message.answer('Привіт! Задай мені питання')
    import chat_ai


@dp.message_handler(text='Translate')
async def bot_message_translate(message: types.Message, state: FSMContext):
    await message.answer('Вкажіть на яку мову треба перекласти. Для того, щоб ввести мову, треба написати "/language (код мови)" От приклади кодів деяких мов мов:\n'
                         'англійська(en)\n'
                         'українська(uk)\n'
                         'іспанська(es)\n'
                         'французька(fr)\n'
                         'німецька(de)\n'
                         'італійська(it)\n'
                         'вірменська(hy)\n')
@dp.message_handler(commands='language')
async def translate_language(message: types.Message):
    if len(message.text.split()) > 1:
        target_language = message.text.split()[1].lower()
        if target_language in LANGUAGES:
            global dest
            dest = target_language
            await message.answer(f'Ваша мова {dest}', parse_mode="HTML")
            await message.answer('Вкажіть через "/translate (текст перекладу)" текст, який требе перекласти')
        else:
            await message.answer('Недійсна цільова мова.')
    else:
        await message.answer('Будь ласка, вкажіть цільову мову.')

@dp.message_handler(commands='translate')
async def handle_translation(message: types.Message):
    await message.answer('Запуск перекладу')
    message_txt = message.text.split(' ', 1)[1]
    if dest is None:
        await message.answer('Будь ласка, вкажіть цільову мову.')
    else:
        src = detect(message_txt)
        translated_text = translator.translate(message_txt, src=src, dest=dest).text
        await message.answer(translated_text, parse_mode="HTML")

executor.start_polling(dp, skip_updates=True)
