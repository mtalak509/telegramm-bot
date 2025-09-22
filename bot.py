# 1.Импорт библиотек

import logging
import os
from datetime import datetime

from aiogram import Bot, Dispatcher
from aiogram.types import Message             # ловим все обновления этого типа 
from aiogram.filters.command import Command   # обрабатываем команды /start, /help и другие

transliteration_dict = {'а': 'a',
                        'б': 'b',
                        'в': 'v',
                        'г': 'g',
                        'д': 'd',
                        'е': 'e',
                        'ё': 'e',
                        'ж': 'zh',
                        'з': 'z',
                        'и': 'i',
                        'й': 'i',
                        'к': 'k',
                        'л': 'l',
                        'м': 'm',
                        'н': 'n',
                        'о': 'o',
                        'п': 'p',
                        'р': 'r',
                        'с': 's',
                        'т': 't',
                        'у': 'u',
                        'ф': 'f',
                        'х': 'kh',
                        'ц': 'ts',
                        'ч': 'ch',
                        'ш': 'sh',
                        'щ': 'shch',
                        'ъ': 'ie',
                        'ы': 'y',
                        'ь': '',
                        'э': 'e',
                        'ю': 'iu',
                        'я': 'ia',}

# 2. Инициализация объектов
Token = os.getenv('TOKEN')
bot = Bot(token=Token)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO,
                    filename='logs.log',
                    datefmt='%H:%M:%S')

is_alive = False    # Флаг состояния бота 

# 3. Обработка/Хэндлер на команду /start
@dp.message(Command(commands=['start']))
async def proccess_command_start(message: Message):
    global is_alive

    is_alive = True
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f'Hello, {user_name} {user_id}! This bot is made for name transliteration.'
    logging.info(f'{user_name}, {user_id} activated bot')
    await bot.send_message(chat_id=user_id, text=text)

# 4. Обработка/Хэндлер на команду /stop

@dp.message(Command(commands=['stop']))
async def proccess_command_stop(message: Message):
    global is_alive

    is_alive = False
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f'Stopping name transliteration bot'
    logging.info(f'{user_name}, {user_id} stopped bot')
    await bot.send_message(chat_id=user_id, text=text)
     
# 5. Обработка/Хэндлер на любые сообщения

@dp.message()
async def transliteration(message: Message):
    if is_alive:
        user_name = message.from_user.full_name
        user_id = message.from_user.id
        text = ''.join(transliteration_dict.get(char, char) for char in message.text.lower()).capitalize()
        logging.info(f'{datetime.now()}, {user_name}, {user_id}: {text}')
        await message.answer(text=text)
    else:
        await message.answer(text=f'bot is shutted down. Use a /start command to wake up bot.')

# 6. Запуск процесса пуллинга

if __name__ == '__main__':
    dp.run_polling(bot)
