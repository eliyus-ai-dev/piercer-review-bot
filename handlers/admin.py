from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery
from db import get_review, update_review_status
import os
from dotenv import load_dotenv

load_dotenv()
router = Router()
CHANNEL_ID = os.getenv("CHANNEL_ID")

@router.callback_query(F.data.startswith("approve_"))
async def approve(callback: CallbackQuery, bot: Bot):
    review_id = int(callback.data.split("_")[1])
    review = get_review(review_id)
    if review is None:
        await callback.answer("Отзыв не найден", show_alert=True)
        return

    text = review["text"]
    photo_id = review["photo_id"]
    username = review["username"]
    rating_val = review["rating"] or 0
    rating = int(rating_val) if rating_val else 0
    stars = "⭐" * rating if rating else ""

    # Убрали "@" перед username, чтобы не было ссылки на профиль
    try:
        if photo_id:
            await bot.send_photo(
                CHANNEL_ID,
                photo_id,
                caption=f"{stars}\nОтзыв от {username}:\n\n{text}"   # <-- тут исправлено
            )
        else:
            await bot.send_message(
                CHANNEL_ID,
                f"{stars}\nОтзыв от {username}:\n\n{text}"           # <-- и тут
            )
        update_review_status(review_id, "approved")
        await callback.message.edit_reply_markup(reply_markup=None)
        await callback.message.reply("✅ Отзыв опубликован в канале!")
    except Exception as e:
        await callback.answer(f"Ошибка публикации: {e}", show_alert=True)
        return
    await callback.answer()

@router.callback_query(F.data.startswith("reject_"))
async def reject(callback: CallbackQuery):
    review_id = int(callback.data.split("_")[1])
    update_review_status(review_id, "rejected")
    await callback.message.edit_reply_markup(reply_markup=None)
    await callback.message.reply("❌ Отзыв отклонён.")
    await callback.answer("Отклонено")