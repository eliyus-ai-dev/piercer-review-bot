import asyncio
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from handlers import user, admin
from db import init_db

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

async def main():
    init_db()
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(user.router)
    dp.include_router(admin.router)
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())