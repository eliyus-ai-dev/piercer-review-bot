from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🌟 Оставить отзыв"), KeyboardButton(text="📢 Отзывы")],
    ],
    resize_keyboard=True
)