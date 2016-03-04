# Установка requests: sudo pip3 install requests
# Если не установлен pip3: sudo apt-get install python3-pip
# requests - модуль для удобной работы с запросами и ответами
import requests
import settings
from datetime import datetime, date

# id городов с названиями и координатами тут: http://bulk.openweathermap.org/sample/city.list.json.gz
# - Это обычный .json  в архиве

city_id = '473537'

# TODO:(Сделаль) если отправить несуществующий id, то вернется json  с ошибкой. Доделать обарботку таких ошибок.
params = {'id':city_id , 'APPID': settings.APPID}

response = requests.get(settings.url, params=params)

print('full_result = ', response.json())
print('all_keys = ', response.json().keys())
print('Страна = ', response.json()['sys']['country'])
print('Город = ', response.json()['name'])
print('Уровень моря = ', response.json()['main']['sea_level'],'Метров над уровнем моря')
print('Скорость ветра = ', response.json()['wind']['speed'],'Метров в секунду')
a=response.json()['wind']['deg']
if 89>a<=0 :
    print('Напрваление', a,'на север')
if 179>a<90:
    print('Напрваление', a,'на запад')
if 270>a<180:
    print('Напрваление', a,'на юг')
if 359>a<271:
    print('Напрваление', a,'на восток')
if 360<a:
    print('Напрваление', a,'на север')

print('Температура = ', response.json()['main']['temp_max']-274,'°C')
date_mc = response.json()['dt']  # Дата в микросекундах
print('Дата и время последнего запроса = ', datetime.fromtimestamp(date_mc))
# Подробнее про HTTP запросы тут: http://ruseller.com/lessons.php?rub=28&id=1726
# request - запрос, response - ответ


