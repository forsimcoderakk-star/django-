
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import executor
import random
API_TOKEN ="8429117299:AAH0HsrRTxdiv1sYRRw1fhs5_0c2qgEILpA"
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
### toq va juft bot
@dp.message_handler()
async def check_number(message: types.Message):
    try:
        number = int(message.text)
        if number % 2 == 0:
            await message.answer(f"{number} Bu son Juft son")
        else:
            await message.answer(f"{number} Bu son Toq son")
    except ValueError:
        await message.answer("Raqam kiriting!")


#karra
answers = {}
@dp.message_handler(commands=['karra'])
async def karra(message: types.Message):
    imkoniyat = 3
    async def ask_question():
        nonlocal imkoniyat
        son1 = random.randint(1, 9)
        son2 = random.randint(1, 9)
        javob = son1 * son2
        answers[message.chat.id] = javob
        print(son1)
        print(son2)
        print(javob)
        
        await message.reply(f"{son1} * {son2} = ?")
        
        async def handle_answer(inner_message: types.Message):
            nonlocal imkoniyat
            user_answer = inner_message.text.strip()
            user_answer = int(user_answer)
            javob = answers.get(message.chat.id)
            if user_answer == javob:    
                await message.reply("To'g'ri!")
            else:
                await message.reply(f"Noto'g'ri! To'g'ri javob {javob}.")
                imkoniyat -= 1
            if imkoniyat == 0:
                await message.reply("Sizda 3 ta noto'g'ri urinish bor. Test tugadi.")
                return
            dp.edited_message_handler(handle_answer)
            await ask_question()
            
        dp.register_message_handler(handle_answer, content_types=types.ContentType.TEXT)
    await ask_question()
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)