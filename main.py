import telebot as tl
import foto

bot = tl.TeleBot('1175544967:AAFcw45HBVds-fSr1CbBWW30QeA2PSV9fiE')

keyboard1 = tl.types.ReplyKeyboardMarkup()
keyboard1.row('/Surtysti', '/Negative', '/Jarygyraq', '/Aq_qara', '/Sepia')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Salem, Qosh qeldiniz! Photonyzdy qaldyrynyz!')


@bot.message_handler(content_types=['photo'])
def handle_docs_photo(message):
    try:
        chat_id = message.chat.id
        file_info = bot.get_file(message.photo[len(message.photo)-1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        src = 'downloaded_photos/' + file_info.file_path
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)
        global name_photo
        name_photo = str(file_info.file_path)
        bot.reply_to(message, "Kyte turynyz, juktelude ...")
    except Exception as e:
        bot.reply_to(message, e)
    send_photo(message)
@bot.message_handler(content_types=['photo'])
def send_photo(message):
    chat_id = message.chat.id
    a = foto.s(name_photo)
    if a == "yes":
        same_photo = foto.linn(name_photo)
        photo = open('completed_photos/{}'.format(same_photo), 'rb')
        bot.send_photo(chat_id, photo, reply_markup=keyboard1)

@bot.message_handler(commands=['Surtysti'])
def a1(message):
    chat_id = message.chat.id
    a = foto.a1(name_photo)
    if a == "yes":
        same_photo = foto.linn(name_photo)
        photo = open('completed_photos/{}'.format(same_photo), 'rb')
        bot.send_photo(chat_id, photo, reply_markup=keyboard1)

@bot.message_handler(commands=['Negative'])
def a2(message):
    chat_id = message.chat.id
    a = foto.a2(name_photo)
    if a == "yes":
        same_photo = foto.linn(name_photo)
        photo = open('completed_photos/{}'.format(same_photo), 'rb')
        bot.send_photo(chat_id, photo, reply_markup=keyboard1)

@bot.message_handler(commands=['Jarygyraq'])
def a3(message):
    chat_id = message.chat.id
    a = foto.a3(name_photo)
    if a == "yes":
        same_photo = foto.linn(name_photo)
        photo = open('completed_photos/{}'.format(same_photo), 'rb')
        bot.send_photo(chat_id, photo, reply_markup=keyboard1)

@bot.message_handler(commands=['Aq_qara'])
def a4(message):
    chat_id = message.chat.id
    a = foto.a4(name_photo)
    if a == "yes":
        same_photo = foto.linn(name_photo)
        photo = open('completed_photos/{}'.format(same_photo), 'rb')
        bot.send_photo(chat_id, photo, reply_markup=keyboard1)

@bot.message_handler(commands=['Sepia'])
def a5(message):
    chat_id = message.chat.id
    a = foto.a5(name_photo)
    if a == "yes":
        same_photo = foto.linn(name_photo)
        photo = open('completed_photos/{}'.format(same_photo), 'rb')
        bot.send_photo(chat_id, photo, reply_markup=keyboard1)

bot.polling()