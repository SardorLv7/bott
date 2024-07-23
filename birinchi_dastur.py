import telebot
from telebot import types

API_TOKEN = '7235447998:AAEWnCu4t30IkLaeOuyv2zjvT8tHzdeoXok'  # Bu yerga sizning bot tokeningizni kiriting

bot = telebot.TeleBot(API_TOKEN)

# Inline tugmalar yaratish
def create_inline_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    button_names = [
        "Katta guruh mashg'ulotlar ishlanmasi",
        "Taqdimot",
        "Muqobil modellarni qo'llash",
        "Loyiha ishi"
    ]
    for i, name in enumerate(button_names, start=1):
        button = types.InlineKeyboardButton(name, callback_data=f"doc_{i}")
        keyboard.add(button)
    return keyboard

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Salom! Bizning ishlarimizni ko'rish uchun /work tugmasini tanlang.")

@bot.message_handler(commands=['work'])
def send_work(message):
    bot.send_message(message.chat.id, "Quyidagi tugmalardan birini tanlang:", reply_markup=create_inline_keyboard())

@bot.callback_query_handler(func=lambda call: call.data.startswith('doc_'))
def handle_query(call):
    doc_number = call.data.split('_')[1]
    if doc_number == '1':
        doc_path = r"C:\Users\sardo\OneDrive\Desktop\Python\muqobil-modellar.docx"
    elif doc_number == '2':
        doc_path = r"C:\Users\sardo\OneDrive\Desktop\Python\taqdimot.pptx"
    elif doc_number == '3':
        doc_path = r"C:\Users\sardo\OneDrive\Desktop\Python\muqobil-modellar.docx"
    elif doc_number == '4':
        doc_path = r"C:\Users\sardo\OneDrive\Desktop\Python\loyiha.docx"
    else:
        doc_path = f"docs/document_{doc_number}.pdf"
    
    try:
        with open(doc_path, 'rb') as doc:
            bot.send_document(call.message.chat.id, doc)
    except FileNotFoundError:
        bot.send_message(call.message.chat.id, f"Hujjat topilmadi: {doc_path}")

bot.polling()
