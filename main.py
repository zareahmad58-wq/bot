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

🔹 نت آغازی:
گریپ فروت، فلفل صورتی، نعناع، لیمو

🔸 نت میانی:
زنجبیل، جوز هندی، یاس

🔻 نت پایه:
بخور، سدر، چوب صندل، پاچولی، مشک سفید
""",

    "whitetiger": """🐯 White Tiger

🏷 برند: Ahmed Al Maghribi
👤 جنسیت: زنانه، مردانه
❄️ طبع: خنک و معتدل

🔹 نت اولیه:
مرکبات، مشک

🔸 نت میانی:
خاکی، تازه، گلی

🔻 نت پایه:
خزه، خاکی
""",

    "aghra": """🌹 Aghra

🏷 برند: احمد المغربی
👤 جنسیت: زنانه، مردانه
🌡 طبع: معتدل

🌸 گروه بویایی:
شرقی، چوبی، گلی

🔹 نت‌ها:
ترکیب گل‌ها، چوب‌ها و روایح شرقی
""",

    "oclock": """⏰ Oclock

🏷 برند: احمد المغربی
👤 جنسیت: زنانه، مردانه
🌡 طبع: معتدل

🌿 رایحه:
فوژه، معطر

🔹 نت آغازی:
سیب، اسطوخودوس

🔸 نت میانی:
چرم، وانیل

🔻 نت پایه:
مشک، چوب صندل
""",

    "peach peach": """🍑 Peach Peach

🏷 برند: احمد المغربی
👩 جنسیت: زنانه
🌡 طبع: ملایم

🍬 رایحه:
شیرین، میوه‌ای

🔹 نت آغازی:
هلو، پرتقال خونی

🔸 نت میانی:
پاچولی

🔻 نت پایه:
عسل، کنیاک
""",

    "royal wood": """🌳 Royal Wood

🏷 برند: احمد المغربی
👤 جنسیت: زنانه، مردانه
🔥 طبع: گرم

🌿 رایحه:
چوبی، ادویه‌ای

🔹 نت‌ها:
عود، رز، چوب صندل، کهربا
""",

    "frost ice": """❄️ Frost Ice

🏷 برند: احمد المغربی
👤 جنسیت: زنانه، مردانه
❄️ طبع: خنک

🌊 رایحه:
دریایی، میوه‌ای، گلی

🔹 نت آغازی:
هندوانه، گریپ فروت

🔸 نت میانی:
یاس، رزماری

🔻 نت پایه:
روایح گلی
""",

    "fusion intense": """🔥 Fusion Intense

👤 جنسیت: زنانه، مردانه
🔥 طبع: گرم

🧴 رایحه:
چرمی، معطر

🔹 نت‌ها:
اسطوخودوس، چرم، وانیل، دانه تونکا
""",

    "leader": """👑 Leader

🏷 برند: Ahmed Al Maghribi
👤 جنسیت: زنانه، مردانه
🔥 طبع: گرم

🌿 رایحه:
چرمی، زعفرانی

🔹 نت‌ها:
گل‌ها، یاس، چرم، کهربا
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

    normalized = text.lower()
    perfumes_normalized = {k.lower(): v for k, v in perfumes.items()}

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

    elif normalized in perfumes_normalized:
        await update.message.reply_text(
            perfumes_normalized[normalized],
            reply_markup=main_menu
        )

    elif text in cosmetics:
        await update.message.reply_text(
            cosmetics[text],
            reply_markup=main_menu
        )

    else:
        await update.message.reply_text(
            "❌ متوجه نشدم\nلطفاً از دکمه‌ها استفاده کن.",
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
