# Установка requests: sudo pip3 install requests
# Если не установлен pip3: sudo apt-get install python3-pip
# requests - модуль для удобной работы с запросами и ответами
import requests
import settings
from datetime import datetime, date

# id городов с названиями и координатами тут: http://bulk.openweathermap.org/sample/city.list.json.gz
# - Это обычный .json  в архиве

city_id = '1496990'

# TODO: если отправить несуществующий id, то вернется json  с ошибкой. Доделать обарботку таких ошибок.
params = {'id': city_id, 'APPID': settings.APPID}


try:#Перехватывает сетевую ошибку
    response = requests.get(settings.url, params=params)
except requests.exceptions.ConnectionError:
    print("Нет соединения с сервером")


if response.json().get('cod') == '404':
    print("Неверно задан город")
else:

    print('full_result = ', response.json())
    print('all_keys = ', response.json().keys())
    print('Страна = ', response.json()['sys']['country'])
    print('Город = ', response.json()['name'])
    print('Скорость ветра = ', response.json()['wind']['speed'], 'Метров в секунду')
    deg = response.json()['wind']['deg']
    print('напр ветра --> ', deg)
    if 30 > deg >= 0:
        print('Направление', 'на Восток')
    if 60 > deg > 31:
        print('Направление', 'на Северо-восток')
    if 119 > deg > 61:
        print('Направление', 'на Север')
    if 149 > deg > 120:
        print('Направление  на Северо-запад')
    if 209 > deg > 150:
        print('Направление на Запад')
    if 239 > deg > 210:
        print('Направление на Юго-запад')
    if 299 > deg > 240:
        print('Направление на Юг')
    if 329 > deg > 300:
        print('Направление на Юго-восток')
    if 360 > deg > 330:
        print('Направление на Восток')

    print('Температура = ', response.json()['main']['temp_max'] - 273, '°C')
    date_mc = response.json()['dt']  # Дата в микросекундах
    print('Дата и время последнего запроса = ', datetime.fromtimestamp(date_mc))
    # Подробнее про HTTP запросы тут: http://ruseller.com/lessons.php?rub=28&id=1726
    # request - запрос, response - ответ