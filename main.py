import telebot
from prediction import get_prediction
from weather_photo import create_image
from time import gmtime, strftime

API = 'YOU_API_KEY'
bot = telebot.TeleBot(API, parse_mode=None)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.from_user.id, '🤖Привет, рад тебя видеть!👋')
    bot.send_message(message.from_user.id, 'Чтобы узнать погоду - введи название города или страны')


def message_send_photo(message):
    bot.send_chat_action(message.chat.id, 'upload_photo')
    img = open('image.png', 'rb')
    bot.send_photo(message.chat.id, img, reply_to_message_id=message.message_id)
    img.close()


admins = [815021893]  # 815021893 my id
@bot.message_handler(commands=['admin'])
def helper(message):
    user_id = message.from_user.id
    user_name = message.from_user.username
    if message.from_user.id in admins:
        print(strftime("%Y-%m-%d %H:%M:%S", gmtime()), user_id, user_name, 'воспользовался командой "admin" ')
        bot.send_message(message.from_user.id, '🔐Аутентификация прошла успешно!🔓')

    else:
        print(strftime("%Y-%m-%d %H:%M:%S", gmtime()), user_id, user_name, 'пытался использовать команду "admin" ')
        bot.send_message(message.from_user.id, '❌Такой команды не существует❌')


@bot.message_handler(content_types='text')
def weather_reply(message):
    city_name = message.text
    if get_prediction(city_name) == None:
        user_id = message.from_user.id
        user_name = message.from_user.username
        print(strftime("%Y-%m-%d %H:%M:%S", gmtime()), user_id, user_name, message.text, 'error in main.py')
        bot.send_message(message.chat.id, f'Такого города или страны не существует🌎')
    else:
        for_image = get_prediction(city_name)
        create_image(city_name, for_image[0], for_image[1], for_image[2])
        bot.send_message(message.chat.id, f'Погода {city_name} | {get_prediction(city_name)[1]} ℃ ',
                         message_send_photo(message))


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
