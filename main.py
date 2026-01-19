import logging
from aiogram import Bot, Dispatcher, executor, types
import wikipedia

# Wikipedia tili
wikipedia.set_lang('uz')

# O'zingizning bot tokeningizni kiriting
API_TOKEN = '8551387673:AAFiYStWEtsfu3pkbnmr_pAVQ7gHmaCiLMc'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Assalomu alaykum! Wikipedia botiga xush kelibsiz.\nQidirmoqchi bo'lgan mavzuingizni yozing.")

@dp.message_handler()
async def wiki_search(message: types.Message):
    try:
        result = wikipedia.summary(message.text)
        await message.answer(result)
    except wikipedia.exceptions.PageError:
        await message.answer("Ma'lumot topilmadi.")
    except Exception:
        await message.answer("Xatolik yuz berdi.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
