import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# ================== TOKEN از Environment ==================
TOKEN = os.getenv("8651339116:AAGRRBUEv6upYLtdtFLJBvHcKRkkdXSNmvU")

# ================== ادکلن‌ها ==================
perfumes = {
    "blue by ahmad": "🌿 Blue by Ahmad\n🏷 برند: Ahmed Al Maghribi",
    "whitetiger": "🐯 White Tiger",
    "aghra": "🌹 Aghra",
    "oclock": "⏰ Oclock",
    "peach peach": "🍑 Peach Peach",
    "royal wood": "🌳 Royal Wood",
    "frost ice": "❄️ Frost Ice",
    "fusion intense": "🔥 Fusion Intense",
    "leader": "👑 Leader"
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

    elif text in perfumes:
        await update.message.reply_text(perfumes[text], reply_markup=main_menu)

    elif text in cosmetics:
        await update.message.reply_text(cosmetics[text], reply_markup=main_menu)

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
