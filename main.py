import telebot
from telebot import types
import requests

bot = telebot.TeleBot('توكنك')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text="اضفني لمجموعتك ™", url="http://t.me/hmaihbot?startgroup=new")
    item2 = types.InlineKeyboardButton(text="مبرمج البوت", url="http://t.me/s_00v")
    item3 = types.InlineKeyboardButton(text="اسئله سوئال", callback_data="questions")

    markup.add(item1, item2, item3)

    welcome_message = '''
   ↯︙اهلا بك عزيزي !
↯︙انا بوت اسمي ( MAX )
↯︙وضيفتي الاساسية هي ان اعطيك جواب لأي سؤال
↯︙قم بأضافتي لمجموعتك واستمتع
↯︙ايضا يمكنك ارسال سؤالك هنا

------------------------------------------------
↯︙اتمنى ان تقوم بأستخدامي بشكل جيد !
    '''
    
    bot.reply_to(message, welcome_message, reply_markup=markup)

@bot.message_handler(content_types=['text'])
def handle_buttons(message):
    if message.text == 'اسئله سوئال':
        bot.reply_to(message, 'أنا بوت للتحدث مع الذكاء الاصطناعي، أي أنني نموذج لغوي آلي كبير تم تدريبه باستخدام تقنية الذكاء الاصطناعي لتوفير الإجابات والمحادثات للمستخدمين في مختلف المواضيع والمجالات. فهل يمكنني مساعدتك في شيء معين؟')
    elif message.text == 'questions':
        # هنا يجب وضع الإجراءات التي تريد تنفيذها عند الضغط على زر "اسئله سوئال"
        # مثال: bot.reply_to(message, 'تم الضغط على زر "اسئله سوئال"')
        pass

bot.infinity_polling()