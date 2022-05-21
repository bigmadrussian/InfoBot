import telebot
import weather
import json
import datetime
from telebot import types
from config import token_bot
from news import check_news_update

bot = telebot.TeleBot(token_bot)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    item1 = types.KeyboardButton('⛅Погода')
    item2 = types.KeyboardButton('📰Лента новостей')
    item3 = types.KeyboardButton('🎬Кинопоиск')

    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id, 'Привет, {0.first_name}! Выбери в меню, то что тебя интересует'
                     .format(message.from_user), reply_markup=markup)


def end_operation(message):
    if message.text == '⬅Назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        item1 = types.KeyboardButton('⛅Погода')
        item2 = types.KeyboardButton('📰Лента новостей')
        item3 = types.KeyboardButton('🎬Кинопоиск')

        markup.add(item1, item2, item3)

        bot.send_message(message.chat.id, '⬅Назад'.format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def bot_send_message(message):
    if message.text == '⛅Погода':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('⬅Назад')
        markup.add(back)
        bot.send_message(message.chat.id, '⛅Погода'.format(message.from_user), reply_markup=markup)

        insert_city_name(message)

    elif message.text == '📰Лента новостей':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        item1 = types.KeyboardButton("Все новости")
        item2 = types.KeyboardButton("Последние 5 новостей")
        item3 = types.KeyboardButton("Свежие новости")
        back = types.KeyboardButton('⬅Назад')
        markup.add(item1, item2, item3, back)

        bot.send_message(message.chat.id, '📰Лента новостей'.format(message.from_user), reply_markup=markup)

    elif message.text == "Все новости":
        with open("news_dict.json") as file:
            news_dict = json.load(file)

        for k, v in sorted(news_dict.items()):
            news = f"{datetime.datetime.fromtimestamp(v['article_date_timestamp'])}\n" \
                   f"{v['article_title']}\n" \
                   f"{v['article_desc']}\n" \
                   f"{v['article_url']}"

            bot.send_message(message.chat.id, news)

    elif message.text == "Последние 5 новостей":
        with open("news_dict.json") as file:
            news_dict = json.load(file)

        for k, v in sorted(news_dict.items())[-5:]:
            news = f"{datetime.datetime.fromtimestamp(v['article_date_timestamp'])}\n" \
                   f"{v['article_title'], v['article_url']}"

            bot.send_message(message.chat.id, news)

    elif message.text == "Свежие новости":
        fresh_news = check_news_update()

        if len(fresh_news) >= 1:
            for k, v in sorted(fresh_news.items()):
                news = f"{datetime.datetime.fromtimestamp(v['article_date_timestamp'])}\n" \
                       f"{v['article_title'], v['article_url']}"

                bot.send_message(message.chat.id, news)

        else:
            bot.send_message(message.chat.id, "Пока нет   свежих новостей...")

    elif message.text == '🎬Кинопоиск':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        item1 = types.KeyboardButton('Комедии')
        item2 = types.KeyboardButton('Боевики')
        item3 = types.KeyboardButton('Ужасы')
        item4 = types.KeyboardButton('Драмы')
        item5 = types.KeyboardButton('Триллеры')
        item6 = types.KeyboardButton('Фантастика')
        item7 = types.KeyboardButton('Военные')
        item8 = types.KeyboardButton('Детективы')
        back = types.KeyboardButton('⬅Назад')
        markup.add(item1, item2, item3, item4, item5, item6, item7, item8, back)

        bot.send_message(message.chat.id, "Выбери жанр кино, которое хочешьь посмотреть".format(message.from_user),
                         reply_markup=markup)

    elif message.text == 'Комедии':
        with open("kom_film.json") as file:
            kom_film = json.load(file)

        for k, v in sorted(kom_film.items()):
            news = f"{(v['article_year'])}\n" \
                   f"{(v['article_name_film'])}\n" \
                   f"{v['article_url'], v['article_desc']}"

            bot.send_message(message.chat.id, news)

    elif message.text == 'Боевики':
        with open("action_film.json") as file:
            kom_film = json.load(file)

        for k, v in sorted(kom_film.items()):
            news = f"{(v['article_year'])}\n" \
                   f"{(v['article_name_film'])}\n" \
                   f"{v['article_url'], v['article_desc']}"

            bot.send_message(message.chat.id, news)

    elif message.text == 'Ужасы':
        with open("horor_film.json") as file:
            kom_film = json.load(file)

        for k, v in sorted(kom_film.items()):
            news = f"{(v['article_year'])}\n" \
                   f"{(v['article_name_film'])}\n" \
                   f"{v['article_url'], v['article_desc']}"

            bot.send_message(message.chat.id, news)

    elif message.text == 'Драмы':
        with open("dram_film.json") as file:
            kom_film = json.load(file)

        for k, v in sorted(kom_film.items()):
            news = f"{(v['article_year'])}\n" \
                   f"{(v['article_name_film'])}\n" \
                   f"{v['article_url'], v['article_desc']}"

            bot.send_message(message.chat.id, news)

    elif message.text == 'Триллеры':
        with open("th_film.json") as file:
            kom_film = json.load(file)

        for k, v in sorted(kom_film.items()):
            news = f"{(v['article_year'])}\n" \
                   f"{(v['article_name_film'])}\n" \
                   f"{v['article_url'], v['article_desc']}"

            bot.send_message(message.chat.id, news)

    elif message.text == 'Фантастика':
        with open("fantasy_film.json") as file:
            kom_film = json.load(file)

        for k, v in sorted(kom_film.items()):
            news = f"{(v['article_year'])}\n" \
                   f"{(v['article_name_film'])}\n" \
                   f"{v['article_url'], v['article_desc']}"

            bot.send_message(message.chat.id, news)

    elif message.text == 'Военные':
        with open("mil_film.json") as file:
            kom_film = json.load(file)

        for k, v in sorted(kom_film.items()):
            news = f"{(v['article_year'])}\n" \
                   f"{(v['article_name_film'])}\n" \
                   f"{v['article_url'], v['article_desc']}"

            bot.send_message(message.chat.id, news)

    elif message.text == 'Детективы':
        with open("det_film.json") as file:
            kom_film = json.load(file)

        for k, v in sorted(kom_film.items()):
            news = f"{(v['article_year'])}\n" \
                   f"{(v['article_name_film'])}\n" \
                   f"{v['article_url'], v['article_desc']}"

            bot.send_message(message.chat.id, news)

    else:
        end_operation(message)


def insert_city_name(message):
    msg = bot.send_message(message.chat.id, text='Введите название города: ')
    bot.register_next_step_handler(msg, reply_to_user)


def reply_to_user(message):
    if message.text == '⬅Назад':
        end_operation(message)
        return
    message_to_user = weather.get_weather(message.text)
    msg = bot.reply_to(message, message_to_user)
    bot.register_next_step_handler(msg, reply_to_user)


if __name__ == '__main__':
    bot.polling(none_stop=True, )
