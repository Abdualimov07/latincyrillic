from aiogram import Bot,Dispatcher,executor,types
from config import API_TOKEN
import logging
from texts import *




logging.basicConfig(level=logging.INFO)

bot=Bot(token=API_TOKEN, parse_mode=None)
dp=Dispatcher(bot)

@dp.message_handler(commands="start")
async def start(message:types.message):
    await message.answer("Hello, welcome to our bot,\n\n please type in Latin or Cyrillic")

@dp.message_handler()
async def echo(message:types.message):
    msg = message.text
    if msg.isascii():
        javob = to_cyrillic(msg)
    else:
        javob = to_latin(msg)    
    await message.answer(javob)




        

    
    
    




executor.start_polling(dp, skip_updates=True)