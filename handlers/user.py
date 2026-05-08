from aiogram import Router, F, Bot
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
import os
from dotenv import load_dotenv
from keyboards.main_menu import main_kb
from keyboards.inline import get_moderation_keyboard, get_skip_keyboard, get_rating_keyboard
from db import add_review

load_dotenv()
router = Router()
ADMIN_CHAT_ID = int(os.getenv("ADMIN_CHAT_ID"))
CHANNEL_ID = os.getenv("CHANNEL_ID")

class ReviewForm(StatesGroup):
    waiting_for_text = State()
    waiting_for_rating = State()
    waiting_for_photo = State()

@router.message(F.text == "/start")
async def start(message: Message):
    await message.answer(
        "🌟 Привет! Здесь ты можешь оставить отзыв об оказанной услуге.\n"
        "Просто нажми кнопку ниже и следуй инструкциям.",
        reply_markup=main_kb
    )

@router.message(F.text == "📢 Отзывы")
async def show_channel(message: Message):
    channel_url = f"https://t.me/reviewdeaddoll"
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔥 Перейти в канал", url=channel_url)]
    ])
    await message.answer("📸 Здесь ты можешь увидеть работы и отзывы клиентов:", reply_markup=kb)

@router.message(F.text.in_(["🌟 Оставить отзыв", "/review"]))
async def start_review(message: Message, state: FSMContext):
    await state.set_state(ReviewForm.waiting_for_text)
    await message.answer(
        "✍️ Напиши текст отзыва (можно развёрнуто, можно коротко):",
        reply_markup=ReplyKeyboardRemove()
    )

@router.message(ReviewForm.waiting_for_text, F.text)
async def process_text(message: Message, state: FSMContext):
    await state.update_data(text=message.text)
    await state.set_state(ReviewForm.waiting_for_rating)
    await message.answer(
        "⭐ Оцените мастера от 1 до 5 звёзд:",
        reply_markup=get_rating_keyboard()
    )

@router.callback_query(F.data.startswith("rate_"), ReviewForm.waiting_for_rating)
async def rate_handler(callback: CallbackQuery, state: FSMContext):
    rating = int(callback.data.split("_")[1])
    await state.update_data(rating=rating)
    await state.set_state(ReviewForm.waiting_for_photo)
    await callback.message.edit_text(
        f"Вы выбрали оценку: {'⭐'*rating}\nТеперь пришлите фото или нажмите «Пропустить».",
        reply_markup=get_skip_keyboard()
    )
    await callback.answer()

@router.callback_query(F.data == "back_to_text", ReviewForm.waiting_for_rating)
async def back_to_text(callback: CallbackQuery, state: FSMContext):
    await state.set_state(ReviewForm.waiting_for_text)
    await callback.message.edit_text("✍️ Введите новый текст отзыва:")
    await callback.answer()

@router.callback_query(F.data == "back_to_rating", ReviewForm.waiting_for_photo)
async def back_to_rating(callback: CallbackQuery, state: FSMContext):
    await state.set_state(ReviewForm.waiting_for_rating)
    await callback.message.edit_text(
        "⭐ Оцените мастера от 1 до 5 звёзд:",
        reply_markup=get_rating_keyboard()
    )
    await callback.answer()

@router.message(ReviewForm.waiting_for_photo, F.photo)
async def process_photo(message: Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    text = data.get("text")
    rating = data.get("rating", 0)
    photo_id = message.photo[-1].file_id

    user_id = message.from_user.id
    username = message.from_user.username or message.from_user.full_name
    review_id = add_review(user_id, username, text, photo_id, rating)

    try:
        await bot.send_photo(
            ADMIN_CHAT_ID,
            photo_id,
            caption=f"📩 Отзыв от @{username}:\n{'⭐'*rating}\n{text}\nID: {review_id}",
            reply_markup=get_moderation_keyboard(review_id)
        )
    except Exception as e:
        print(f"Ошибка отправки админу: {e}")
        await message.answer("⚠️ Не удалось отправить отзыв. Попробуйте позже.")
        await state.clear()
        return

    await message.answer(
        "✅ Отзыв отправлен на модерацию!",
        reply_markup=main_kb
    )
    await state.clear()

@router.callback_query(F.data == "skip_photo", ReviewForm.waiting_for_photo)
async def skip_photo_callback(callback: CallbackQuery, state: FSMContext, bot: Bot):
    data = await state.get_data()
    text = data.get("text")
    rating = data.get("rating", 0)
    user_id = callback.from_user.id
    username = callback.from_user.username or callback.from_user.full_name
    review_id = add_review(user_id, username, text, None, rating)

    try:
        await bot.send_message(
            ADMIN_CHAT_ID,
            f"📩 Новый отзыв от @{username} (без фото):\n{'⭐'*rating}\n{text}\nID: {review_id}",
            reply_markup=get_moderation_keyboard(review_id)
        )
    except Exception as e:
        print(f"Ошибка отправки админу: {e}")
        await callback.message.answer("⚠️ Не удалось отправить отзыв.")
        await state.clear()
        await callback.answer()
        return

    await callback.message.answer(
        "✅ Отзыв отправлен на модерацию!",
        reply_markup=main_kb
    )
    await state.clear()
    await callback.answer()

@router.message(F.text == "❌ Отменить")
async def cancel_action(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.clear()
        await message.answer("🚫 Действие отменено.", reply_markup=main_kb)
    else:
        await message.answer("Вы не находитесь в процессе отзыва.", reply_markup=main_kb)