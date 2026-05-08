# 🤖 Telegram-бот для отзывов с модерацией и рейтингом

<div align="center">

### ⭐ Удобный сбор отзывов для мастеров и небольших студий

Клиенты оставляют отзывы с оценкой и фото,  
администратор модерирует их,  
а бот автоматически публикует всё в Telegram-канал.

<br>

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![Aiogram](https://img.shields.io/badge/Aiogram-3.x-2CA5E0?style=for-the-badge&logo=telegram)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker)
![Amvera](https://img.shields.io/badge/Deploy-Amvera-black?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</div>

---

# ✨ Возможности

## 👤 Для клиентов

- Удобное главное меню с кнопками
- Пошаговое создание отзыва:
  - текст
  - рейтинг ⭐ от 1 до 5
  - фотография (по желанию)
- Кнопка «Назад» на каждом шаге
- Возможность отменить отправку
- После отправки — ссылка на канал с отзывами

---

## 🛡️ Для администратора

- Мгновенные уведомления о новых отзывах
- Инлайн-модерация прямо в Telegram
- Кнопки:
  - ✅ Одобрить
  - ❌ Отклонить
- Автоматическая публикация одобренных отзывов
- Отклонённые отзывы не публикуются

---

## 📢 Канал с отзывами

Бот автоматически красиво оформляет публикации:

- ⭐ рейтинг звёздами
- 👤 имя пользователя
- 📝 текст отзыва
- 📷 фотография

Отзывы выглядят аккуратно и профессионально.

---

# 🛠️ Технологии

<div align="center">

| Технология | Описание |
|---|---|
| Python 3.12 | Основной язык |
| Aiogram 3.x | Telegram Bot Framework |
| FSM | Машина состояний |
| SQLite | База данных |
| Docker | Контейнеризация |
| Amvera | Облачный деплой |
| Git | Контроль версий |

</div>

---

# ⚙️ Установка и запуск

## 1️⃣ Клонирование репозитория

```bash
git clone https://github.com/ТВОЙ_ЛОГИН/piercer-review-bot.git
cd piercer-review-bot
```

---

## 2️⃣ Установка зависимостей

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Настройка `.env`

Создайте файл `.env` и заполните его:

```env
BOT_TOKEN=your_bot_token

ADMIN_CHAT_ID=your_admin_id

CHANNEL_ID=your_channel_id
```

---

## 4️⃣ Запуск бота

```bash
python main.py
```

---

# ☁️ Деплой на Amvera

Проект полностью готов к запуску через **Amvera**.

Конфигурация находится в файле:

```bash
amvera.yaml
```

Для обновления проекта достаточно выполнить:

```bash
git push
```

Все переменные окружения задаются через панель управления Amvera.

---

# 📸 Скриншоты

![](screenshots/1.png)

![](screenshots/2.png)

![](screenshots/3.png)

![](screenshots/4.png)

![](screenshots/5.png)

![](screenshots/6.png)

![](screenshots/7.png)

![](screenshots/8.png)

![](screenshots/9.png)

---

# 🚀 Преимущества проекта

- Простая установка
- Готов к продакшену
- Удобная модерация
- Красивое оформление отзывов
- Работа 24/7 в облаке
- Подходит для:
  - пирсеров
  - тату-мастеров
  - барберов
  - салонов
  - косметологов
  - любых услуг с отзывами

---

# 📞 Контакты

## 👨‍💻 Разработчик

Telegram: **@eliyusvl**

Email: **overmuf24@gmail.com**

---

# 📄 Лицензия

Проект распространяется по лицензии **MIT**.

Вы можете свободно:
- использовать
- изменять
- распространять проект

При сохранении упоминания автора.

---

<div align="center">

### ⭐ Если проект понравился — поставьте звезду репозиторию

</div>