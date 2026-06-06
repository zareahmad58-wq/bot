import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# ================== TOKEN ==================
TOKEN = os.getenv("TOKEN")

# ================== ادکلن‌ها ==================
perfumes = {
    "blue by ahmad": """🌿 Blue by Ahmad
🏷 برند: Ahmed Al Maghribi
👤 جنسیت: زنانه، مردانه
❄️ طبع: خنک
🌸 رایحه: چوبی، مرکباتی، تازه
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
🌿 رایحه: سیب، اسطوخودوس، چرم، وانیل، مشک
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

# ================== /start ==================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "به فروشگاه خوش آمدید 👋\nادکلن یا لوازم آرایشی؟",
        reply_markup=main_menu
    )

# ================== پیام‌ها ==================
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()

    # فقط ادکلن‌ها بدون حساسیت به بزرگ/کوچیک
    normalized_text = text.lower()

    perfumes_normalized = {k.lower(): v for k, v in perfumes.items()}
    cosmetics_normalized = {k.lower(): v for k, v in cosmetics.items()}

    # منوی اصلی
    if text == "ادکلن":
        buttons = [[name] for name in perfumes.keys()]
        keyboard = ReplyKeyboardMarkup(buttons, resize_keyboard=True)

        await update.message.reply_text(
            "📋 لیست ادکلن‌ها",
            reply_markup=keyboard
        )

    elif text == "لوازم آرایشی":
        buttons = [[name] for name in cosmetics.keys()]
        keyboard = ReplyKeyboardMarkup(buttons, resize_keyboard=True)

        await update.message.reply_text(
            "💄 لوازم آرایشی",
            reply_markup=keyboard
        )

    # ادکلن‌ها (case-insensitive)
    elif normalized_text in perfumes_normalized:
        await update.message.reply_text(
            perfumes_normalized[normalized_text],
            reply_markup=main_menu
        )

    # آرایشی
    elif text in cosmetics:
        await update.message.reply_text(
            cosmetics[text],
            reply_markup=main_menu
        )

    else:
        await update.message.reply_text(
            "❌ متوجه نشدم",
            reply_markup=main_menu
        )

# ================== main ==================
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
