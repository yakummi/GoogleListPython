from aiogram import types, Dispatcher, Bot, executor

bot = Bot(token='5875660894:AAHTudwp_lcSiD5QSGuX2dPRpnEK_JHQWT0')

dp = Dispatcher(bot=bot)

@dp.message_handler()
async def check_message(message: types.Message):
    text = message.text
    print(text)

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, skip_updates=True)