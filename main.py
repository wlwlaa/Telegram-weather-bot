import requests
import telebot
from telebot import types


API_TOKEN = '6270576083:AAFdxIygi53Ba0fVBqTAFX6WItHM_crCWpE'
bot = telebot.TeleBot(API_TOKEN)


def wind_convert(wind_dir):
    if wind_dir >= 338 or wind_dir < 23:
        return 'северный\U00002B07'
    elif 23 <= wind_dir < 68:
        return 'северо-восточный\U00002199'
    elif 68 <= wind_dir < 113:
        return 'восточный\U00002B05'
    elif 113 <= wind_dir < 158:
        return 'юго-восточный\U00002196'
    elif 158 <= wind_dir < 203:
        return 'южный\U00002B06'
    elif 203 <= wind_dir < 248:
        return 'юго-западный\U00002197'
    elif 248 <= wind_dir < 293:
        return 'западный\U000027A1'
    elif 293 <= wind_dir < 338:
        return 'северо-западный\U00002198'


def weather_ip(city):
    API_KEY = 'c308c34844dc547a013d1f330c5a58c7'

    url = 'http://api.openweathermap.org/data/2.5/forecast?id=524901&appid=' + API_KEY + '&q=' + city

    response = requests.get(url).json()

    current_inf = response['list'][0]['main']
    temp = round(current_inf['temp'] - 273)
    temp_feels_like = round(current_inf['feels_like'] - 273)
    pressure = round(current_inf['pressure'] // 10 * 7.537)
    humidity = current_inf['humidity']
    wind_velocity = round(response['list'][0]['wind']['speed'])
    wind_dir = response['list'][0]['wind']['deg']
    

    ans = f'\U0001F9ED Погода в городе {city} сейчас:\n'
    ans += f"\U0001F321 Температура: {temp} \U00002103, ощущается как {temp_feels_like} \U00002103\n"
    ans += f"Давление: {pressure} мм. рт. ст.\n"
    ans += f"Влажность: {humidity}%\n"
    ans += f"\U0001F4A8 Ветер {wind_convert(wind_dir)}, скорость {wind_velocity} м/с\n"

    weather_inf = response['list'][0]['weather'][0]['description']
    weather_state = {
        'clear sky': 'ясно\U00002600', 
        'fog': 'туман\U0001F32B', 
        'scattered clouds': 'переменная облачность\U0001F324', 
        'light rain': 'легкий дождь\U0001F327', 
        'few clouds': 'облачно\U00002601', 
        'moderate rain': 'дождь\U0001F327', 
        'heavy intensity rain': 'сильный дождь\U0001F4A7', 
        'rain and snow': 'дождь со снегом\U0001F328', 
        'snow': 'снег\U00002744', 
        'light snow': 'легкий снег\U0001F328', 
        'overcast clouds': 'пасмурно\U00002601', 
        'broken clouds': 'малооблачно\U000026C5'
    }
    
    if weather_inf in weather_state:
        ans += f"Состояние неба: {weather_state[weather_inf]}\n"
    else:
        ans += f"Состояние неба: {weather_inf}\n"

    ans += '\n'

    ans += "Прогноз на следующие часы:\n"

    current_inf = response['list'][3]['main']
    temp = round(current_inf['temp'] - 273)
    weather_inf = response['list'][3]['weather'][0]['description']
    time = response['list'][3]['dt_txt']
    ans += f"\U000025BB {time[8:10]}.{time[5:7]} {time[11:16]}: {temp} \U00002103, {weather_state[weather_inf]}\n"

    current_inf = response['list'][4]['main']
    temp = round(current_inf['temp'] - 273)
    weather_inf = response['list'][4]['weather'][0]['description']
    time = response['list'][4]['dt_txt']
    ans += f"\U000025BB {time[8:10]}.{time[5:7]} {time[11:16]}: {temp} \U00002103, {weather_state[weather_inf]}\n"
    
    current_inf = response['list'][5]['main']
    temp = round(current_inf['temp'] - 273)
    weather_inf = response['list'][5]['weather'][0]['description']
    time = response['list'][5]['dt_txt']
    ans += f"\U000025BB {time[8:10]}.{time[5:7]} {time[11:16]}: {temp} \U00002103, {weather_state[weather_inf]}\n"

    current_inf = response['list'][6]['main']
    temp = round(current_inf['temp'] - 273)
    weather_inf = response['list'][6]['weather'][0]['description']
    time = response['list'][6]['dt_txt']
    ans += f"\U000025BB {time[8:10]}.{time[5:7]} {time[11:16]}: {temp} \U00002103, {weather_state[weather_inf]}\n"

    current_inf = response['list'][7]['main']
    temp = round(current_inf['temp'] - 273)
    weather_inf = response['list'][7]['weather'][0]['description']
    time = response['list'][7]['dt_txt']
    ans += f"\U000025BB {time[8:10]}.{time[5:7]} {time[11:16]}: {temp} \U00002103, {weather_state[weather_inf]}\n\n"

    ans += "Прогноз на следующие дни:\n"

    temp = str(round(response['list'][10]['main']['temp']) - 273) + ' - ' + str(round(response['list'][13]['main']['temp']) - 273)
    weather_inf = response['list'][13]['weather'][0]['description']
    wind_dir = wind_convert(response['list'][13]['wind']['deg'])
    time = response['list'][13]['dt_txt']
    ans += f"\U000025BB {time[8:10]}.{time[5:7]}: {temp} \U00002103, {weather_state[weather_inf]}, ветер {wind_dir}\n"

    temp = str(round(response['list'][18]['main']['temp']) - 273) + ' - ' + str(round(response['list'][21]['main']['temp']) - 273)
    weather_inf = response['list'][21]['weather'][0]['description']
    wind_dir = wind_convert(response['list'][21]['wind']['deg'])
    time = response['list'][21]['dt_txt']
    ans += f"\U000025BB {time[8:10]}.{time[5:7]}: {temp} \U00002103, {weather_state[weather_inf]}, ветер {wind_dir}\n"

    temp = str(round(response['list'][26]['main']['temp']) - 273) + ' - ' + str(round(response['list'][29]['main']['temp']) - 273)
    weather_inf = response['list'][29]['weather'][0]['description']
    wind_dir = wind_convert(response['list'][29]['wind']['deg'])
    time = response['list'][29]['dt_txt']
    ans += f"\U000025BB {time[8:10]}.{time[5:7]}: {temp} \U00002103, {weather_state[weather_inf]}, ветер {wind_dir}\n"

    temp = str(round(response['list'][34]['main']['temp']) - 273) + ' - ' + str(round(response['list'][37]['main']['temp']) - 273)
    weather_inf = response['list'][37]['weather'][0]['description']
    wind_dir = wind_convert(response['list'][37]['wind']['deg'])
    time = response['list'][37]['dt_txt']
    ans += f"\U000025BB {time[8:10]}.{time[5:7]}: {temp} \U00002103, {weather_state[weather_inf]}, ветер {wind_dir}\n"

    return ans


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Напиши название города ниже:')

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, "Этот бот дает точную информацию о погоде сайчас и на ближайшее время.\nНапиши город в формате: 'Москва' или 'Moscow'.")

@bot.message_handler(content_types=['text'])
def get_cityname(message):
    try:
        response = weather_ip(message.text)
    except KeyError:
        response = 'Населенный пункт не найден'
    print(message.from_user.username)
        
    bot.send_message(message.chat.id, response)
        
bot.infinity_polling()
