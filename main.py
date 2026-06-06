import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# ================== TOKEN از Environment ==================
TOKEN = os.getenv("8651339116:AAGRRBUEv6upYLtdtFLJBvHcKRkkdXSNmvU")

# ================== ادکلن‌ها ==================
perfumes = {
    "blue by ahmad": """🌿 Blue by Ahmad
🏷 برند: Ahmed Al Maghribi
👤 جنسیت: زنانه، مردانه
❄️ طبع: خنک
🌸 رایحه: چوبی، مرکباتی، تازه
☀️ مناسب: فصل‌های گرم
""",

    "whitetiger": """🐯 White Tiger
🏷 برند: Ahmed Al Maghribi
👤 جنسیت: زنانه، مردانه
❄️ طبع: خنک و معتدل
""",

    "aghra": """🌹 Aghra
🏷 برند: احمد المغربی
👤 جنسیت: زنانه، مردانه
🌡 طبع: معتدل
""",

    "oclock": """⏰ Oclock
🏷 برند: احمد المغربی
👤 جنسیت: زنانه، مردانه
""",

    "peach peach": """🍑 Peach Peach
👩 جنسیت: زنانه
🌡 طبع: ملایم
""",

    "royal wood": """🌳 Royal Wood
🔥 طبع: گرم
""",

    "frost ice": """❄️ Frost Ice
❄️ طبع: خنک
""",

    "fusion intense": """🔥 Fusion Intense
🔥 طبع: گرم
""",

    "leader": """👑 Leader
🔥 طبع: گرم
"""
}

# ================== آرایشی ==================
cosmetics = {
    "در حال ساخت 🚧": "✅ بخش لوازم آرایشی به زودی تکمیل خواهد شد."
}

# ================== منو ==================
main_menu = ReplyKeyboardMarkup(
    [["ادکلن", "لوازم آرایشی"]],
    resize_keyboard=True
)

# ================== start ==================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "به فروشگاه خوش آمدید 👋\nادکلن یا لوازم آرایشی؟",
        reply_markup=main_menu
    )

# ================== پیام‌ها ==================
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()

    if text == "ادکلن":
        buttons = [[name] for name in perfumes.keys()]
        keyboard = ReplyKeyboardMarkup(buttons, resize_keyboard=True)

        await update.message.reply_text(
            "📋 لیست ادکلن‌ها",
            reply_markup=keyboard
        )

    elif text == "