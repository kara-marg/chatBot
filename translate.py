from libraries import Translator, LANGUAGES
from libraries import bot, types, dp
from libraries import json
from libraries import detect


# Создаем переводчик
translator = Translator()

# Переменная для хранения целевого языка
dest = None
@dp.message_handler(commands='language')
async def translate_language(message):

    # Перевірка, чи є введена мова підтримуваною
    if len(message.text.split()) > 1:
        target_language = message.text.split()[1].lower()
        if target_language in LANGUAGES:
            # Встановлюємо цільову мову
            global dest
            dest = target_language
            await message.answer(f'Your language is {dest}', parse_mode="HTML")
        else:
            await message.answer('Invalid destination language.')
    else:
        await message.answer('Please specify the target language.')
# @dp.message_handler(commands='text')
# async def translate_text(message):
#     # Перевіряємо, чи введена команда /text разом з текстом
#     if len(message.text.split()) > 1:
#         if message.text.split()[1] == '/text':
#             await message.answer("Vedit text")
#             await message.answer('Please enter the text you want to translate.')
#     else:
#         await message.answer("Invalid command format. Use /text command followed by your text.")

# @dp.message_handler(commands='exit')
# async def exit_message(message):
#     await message.answer('Exiting translation mode.')
#     await dp.bot.send_message(message.chat.id, '/start')
#     await dp.current_handler.stop()
@dp.message_handler(commands='text')
async def handle_message(message):
    if dest is None:
        await message.answer('Please specify the target language.')
    else:
        # Перекладаємо отриманий текст
        src = detect(message.text)
        print(src + "1")
        translated_text = translator.translate(message.text, src=src, dest=dest).text
        await message.answer(translated_text, parse_mode="HTML")

