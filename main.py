from aiogram import Bot, Dispatcher, executor, types
import logging
from downloader import YouTubeDownloader
import os

bot = Bot("5904607271:AAH-edy50mxak7BhgfeCB-9oLnlrK5QMPiM")
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(f"Salom {message.from_user.full_name}")

@dp.message_handler()
async def start(message: types.Message):
    if message.text.startswith("https://youtube.com/") or message.text.startswith("https://youtu.be/"):
        await message.answer("Video yuklanmoqda...")
        downloaded = YouTubeDownloader(message.text)
        with open("video.mp4", "rb") as video:
            info = f"Video nomi: {downloaded['title']}\nvideoni yuklagan foydalanuvchi: https://youtube.com/@{downloaded['uploader']}\nvideoni yuklangan sanasi: {downloaded['upload_date']}"
            info2 = f"videodagi ko'rishlar soni: {downloaded['view_count']}\nvideodagi likelar soni: {downloaded['like_count']}\nvideoni tavsifi: {downloaded['description']}"
            await message.answer_video(video=video, caption=f"{info}")
            await message.answer(info2)
    else:
        await message.answer(message.text)
    os.remove("video.mp4")


if __name__=='__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=False)