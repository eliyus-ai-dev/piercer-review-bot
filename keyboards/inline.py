from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_moderation_keyboard(review_id):
    buttons = [
        [
            InlineKeyboardButton(text="✅ Одобрить", callback_data=f"approve_{review_id}"),
            InlineKeyboardButton(text="❌ Отклонить", callback_data=f"reject_{review_id}")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def get_skip_keyboard():
    buttons = [
        [InlineKeyboardButton(text="Пропустить ➡️", callback_data="skip_photo")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def get_rating_keyboard():
    buttons = [
        [
            InlineKeyboardButton(text="⭐", callback_data="rate_1"),
            InlineKeyboardButton(text="⭐(2)", callback_data="rate_2"),
            InlineKeyboardButton(text="⭐(3)", callback_data="rate_3"),
            InlineKeyboardButton(text="⭐(4)", callback_data="rate_4"),
            InlineKeyboardButton(text="⭐(5)", callback_data="rate_5")
        ],
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="back_to_text")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)