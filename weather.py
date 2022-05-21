import datetime
import requests
from config import token_weather


def get_weather(city):
    global message
    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B"
    }

    r = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={token_weather}&units=metric'
    )
    data = r.json()
    print(data)

    try:
        city = data["name"]
        cur_weather = data["main"]["temp"]

        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Посмотри в окно, не пойму что там за погода!"

        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
            data["sys"]["sunrise"])

        message = f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n" \
                  f"Погода в городе: {city}\nТемпература: {cur_weather}C° {wd}\n" \
                  f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind} м/с\n" \
                  f"Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\nПродолжительность дня: {length_of_the_day}\n" \
                  f"***Хорошего дня!***"

    except KeyError:
        message = "\U00002620 РџСЂРѕРІРµСЂСЊС‚Рµ РЅР°Р·РІР°РЅРёРµ РіРѕСЂРѕРґР° \U00002620"
    return message
