import logging
from functions import ids, TvaSQI
from aiogram import Bot, Dispatcher, executor, types
import key

API_TOKEN = key.TOKEN

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)

KA = TvaSQI


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    id = message.from_user.id
    if message.from_user.username:
        info = f"username: @{message.from_user.username} \n ID: {message.from_user.id}"
        await bot.send_message(556841744, info)
    else:
        info = f"full name: {message.from_user.full_name} \n ID: {message.from_user.id}"
        await bot.send_message(556841744, info)
    text = f"Assalomu alaykum <b>{message.from_user.full_name}</b>.\n"
    text += f"Tizim va Signallarni qayta ishlash fanidan ma'lumotlarni olishingiz uchun sizga linklar yuboraman.\n"
    text += f"Linklar nomiga qarab sizga kerakli ma'lumot nomini ko'rgan linkning ustiga bosing "
    text += f" va sizga <b>Google Cloud</b>ga yuklangan maruza matnlarini linkiga beriladi.\n"
    text += f"Bu ishlar sizlarga Oraliq nazoratda foylanishiz uchun qilingan."
    await message.reply(text)
    for ka in KA:
        await bot.send_message(id, text=f"<a href='{ka['link']}'>{ka['name']}</a>")
    await bot.send_message(id, text=f"Noqulayliklar uchun uzr. 🙏🏽🙏🏽🙏🏽")


@dp.message_handler(commands=['admin', 'developer'])
async def admins(message: types.Message):
    if message.from_user.username:
        info = f"<b>username:</b> @{message.from_user.username} \n <b>ID:</b> {message.from_user.id}" \
               f"\n <b>User:</b> Siz bilan Bog'lanmoqchi."
        await bot.send_message(556841744, info)
        await message.reply("Siz bilan admin tez oraqa bog'lanadi.")
    else:
        info = f"<b>full name:</b> {message.from_user.full_name} \n <b>ID:</b> {message.from_user.id}" \
               f"\n <b>User: Siz bilan bog'lanmoqchi.</b>\n Undan nomerini so'radim."
        await bot.send_message(556841744, info)
        await message.reply("Siz bilan admin tez oraqa bog'lanadi. Iloji bo'lsa telefon nomerizni yozivoring. ")


@dp.message_handler()
async def echo(message: types.Message):
    await bot.send_message(556841744, f"<b>ID:</b> {message.from_user.id} \n <b>Messages:</b> {message.text}")
    if message.from_user.id == 556841744:
        if message.text == "TvaSQI":
            text = "Assalomu alaykum <a href='https://t.me/TvaSQIbot'> Tizim va Signallarni qayta ishlash bot </a> shu linkga kiring. \n"
            text += "Bu botda Tizim va Signallarni qayta ishlash bo'yicha ma'lumotlar berilgan.\n"
            text += "Foydasi tegadi deb o'yladim. 😁😁😁 \n"
            # await bot.send_message(1641286382, text)
            for ID in ids:
                try:
                    await bot.send_message(ID, text)
                except:
                    pass

    if "+998" in message.text:
        await message.answer(f"{message.text} \n Nomeringiz yetib bordi.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
