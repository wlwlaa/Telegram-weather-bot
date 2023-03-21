import requests
import telebot


API_TOKEN = '6270576083:AAFdxIygi53Ba0fVBqTAFX6WItHM_crCWpE'
bot = telebot.TeleBot(API_TOKEN)

def weather_ip(city):
    START_URL = 'http://api.openweathermap.org/data/2.5/forecast?id=524901&appid=c308c34844dc547a013d1f330c5a58c7'

    url = START_URL + '&q=' + city

    response = requests.get(url).json()

    current_inf = response['list'][0]['main']
    temp = round(current_inf['temp'] - 273)
    temp_feels_like = round(current_inf['feels_like'] - 273)
    pressure = round(current_inf['pressure'] // 10 * 7.537)
    humidity = current_inf['humidity']

    ans = f'\U0001F9ED Погода в городе {city} сейчас:\n'
    ans += f"\U0001F321 Температура: {temp} \U00002103, ощущается как {temp_feels_like} \U00002103\n"
    ans += f"Давление: {pressure} мм. рт. ст.\n"
    ans += f"Влажность: {humidity}%\n"

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
    current_inf = response['list'][4]['main']
    temp = round(current_inf['temp'] - 273)
    weather_inf = response['list'][4]['weather'][0]['description']
    time = response['list'][4]['dt_txt']
    ans += f"\U000025BB {time[8:10]}.{time[5:7]} {time[11:16]}: {temp} \U00002103, {weather_state[weather_inf]}\n"

    current_inf = response['list'][6]['main']
    temp = round(current_inf['temp'] - 273)
    weather_inf = response['list'][6]['weather'][0]['description']
    time = response['list'][6]['dt_txt']
    ans += f"\U000025BB {time[8:10]}.{time[5:7]} {time[11:16]}: {temp} \U00002103, {weather_state[weather_inf]}\n"

    current_inf = response['list'][8]['main']
    temp = round(current_inf['temp'] - 273)
    weather_inf = response['list'][8]['weather'][0]['description']
    time = response['list'][8]['dt_txt']
    ans += f"\U000025BB {time[8:10]}.{time[5:7]} {time[11:16]}: {temp} \U00002103, {weather_state[weather_inf]}\n"

    current_inf = response['list'][10]['main']
    temp = round(current_inf['temp'] - 273)
    weather_inf = response['list'][10]['weather'][0]['description']
    time = response['list'][10]['dt_txt']
    ans += f"\U000025BB {time[8:10]}.{time[5:7]} {time[11:16]}: {temp} \U00002103, {weather_state[weather_inf]}\n"

    current_inf = response['list'][12]['main']
    temp = round(current_inf['temp'] - 273)
    weather_inf = response['list'][12]['weather'][0]['description']
    time = response['list'][12]['dt_txt']
    ans += f"\U000025BB {time[8:10]}.{time[5:7]} {time[11:16]}: {temp} \U00002103, {weather_state[weather_inf]}\n"

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
    print(message.from_user.id)
        
    bot.send_message(message.chat.id, response)
        
bot.infinity_polling()
