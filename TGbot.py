from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def long_inp1(message: types.Message):
    await message.answer('Введите долготу и широту\n(ЧЕРЕЗ ПРОБЕЛ)\n(В ПОРЯДКЕ "долгота широта")')

@dp.message_handler()
async def lati_inp(message: types.Message):
    try:
        listik = message.text.split(' ')
        long = listik[0]
        lati = listik[1]
        if long != None and lati != None:
            await bot.send_location(chat_id=message.chat.id, longitude=int(long), latitude=int(lati))
    except:
        await message.answer('НЕДОПУСТИМЫЕ ПАРАМЕТРЫ')


if __name__ == '__main__':
    executor.start_polling(dp)