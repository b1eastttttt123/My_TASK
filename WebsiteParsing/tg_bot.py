import asyncio
import datetime
import json
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from config import token
from main import check_news_update

logging.basicConfig(level=logging.INFO)

bot = Bot(token=token)
dp = Dispatcher()

@dp.message(Command("all_news"))
async def get_all_news(message: types.Message):
    with open("news_dict.json") as file:
        news_dict = json.load(file)

    for k, v in sorted(news_dict.items()):
        news = f"<b>{datetime.datetime.fromtimestamp(v['article_date_timestamp'])}</b>\n<u>{v['article_title']}</u>\n<code>{v['article_desc']}</code>\n{v['article_url']}"

        await message.answer(news, parse_mode="HTML")

@dp.message(Command("last_five"))
async def get_last_five_news(message: types.Message):
    with open("news_dict.json") as file:
        news_dict = json.load(file)

    for k, v in sorted(news_dict.items())[-5:]:
        news = f"<b>{datetime.datetime.fromtimestamp(v['article_date_timestamp'])}</b>\n<u>{v['article_title']}</u>\n<code>{v['article_desc']}</code>\n{v['article_url']}"

        await message.answer(news, parse_mode="HTML")

@dp.message(Command("fresh_news"))
async def get_fresh_news(message: types.Message):
    fresh_news = check_news_update()

    if len(fresh_news) >= 1:
        for k, v in sorted(fresh_news.items()):
            news = f"<b>{datetime.datetime.fromtimestamp(v['article_date_timestamp'])}</b>\n<u>{v['article_title']}</u>\n<code>{v['article_desc']}</code>\n{v['article_url']}"

            await message.answer(news, parse_mode="HTML")
    else:
        await message.answer("Пока нет новых новостей...")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
