from tkinter import *
from tkinter.ttk import *
import json
import requests
import settings
from datetime import datetime, date


# Запрашивает данные о погоде у сайта и показывает их в консоли
# TODO: В функции нет ни единой строчки с запросом к сайту.(response)
# TODO: Если ты делаешь графическую программу, то зачем она что-то показывает в консоли?
# TODO: В функции есть алгоритм определения направления ветра, его нужно вынести в отдельную функцию
# TODO: Для улучшения читабельности кода - функции должны отдельяться друг от друга двумя пустыми строками(я добавил)
def conclusionweather():
    """
    !!!Комментарии к функции делают не перед ней,
    а в виде многострочного комметария в начале функции
    """
    if response.json().get('cod') == '404':
        print("Неверно задан город")
    else:
        print('id=  ', response.json()['id'])
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


def wind():#Алгоритм определения направления ветра
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

# Выводит в консоль города которые есть в файле city.list.json
# TODO: Куда она их пишет? (В консоль)
def allname():
    op = open("city.list.json", encoding='UTF-8')
    lst = []
    for line in op:
        lol = json.loads(line)
        name = lol.get('name')
        lst.append(lol.get('name'))
    return lst


# Выполняет  любое действие которые вы пропишите внутри этой функиции при выборе города в списке в граф часте
# TODO: Какое действие она выполняет?
# TODO: Зачем внутри вызывается функция run(), если этой функции вообще нет?(Функция была переименованна,щас я ее убрал)
def newselection(event):
    event = combobox.get()
    print(event)
    op = open('city.list.json')
    # conclusionweather()
    city_name = event
    return city_name


# Находит id выбранного города
# TODO: И что она с ним делает после того как найдет?
# TODO: Почитай что такое локальные и глобальные переменные...
# TODO: Все объявления функций должны находиться в начале файла(я переместил эту функцию выше)

def find_id(city_name):
    """
    Принимает название города, возвращает его id
    """
    # Открываем файл с городами на чтение
    f_cities = open('city.list.json', encoding='UTF-8')
    for line in f_cities:
        # Преобразуем формат JSON к словарю Python
        city = json.loads(line)
        # Для каждого города в файле city.list.json сравниваем название с искомым
        if city_name == city['name']:
            # Если нашли город в файле с нужным именем, возвращаем его id
            return city["_id"]

# Начало программы! Все объявления функций должны быть выше.
root = Tk()
root.geometry("450x470")
combobox = Combobox(root, values=allname(), font="Arial 12")
# frame - задает родительский виджет, на его территории будет располагаться Combobox
# values - задает набор значений, которые будут содержаться в Combobox изначально
# height - задает высоту выпадающего списка. Если число элементов списка меньше 11, то можно не задавать.
# Если не задано при колличестве элементов больше 10, то с правой стороны появится полоса прокрутки.
# Если в нашем примере задать значение height меньше трех, то с правой стороны появится полоса прокрутки,
# но она будет недоступна, а все элементы будут отображаться одновременно.
combobox.set(u"Выберите город")  # спомощью этой строчки мы установим Combobox в значение ОДИН изначально
combobox.grid(column=0, row=0)  # Позиционируем Combobox на форме

# TODO: Для чего ты вызвал эту функцию в этом месте программы?(Чтобы пользователь знал какие города есть в списке)
#allname()

# TODO: Если ты делаешь графическую программу, то зачем название города запрашиваешь в консоли?
#city_name = input('Введите город :  ')

find_id()

combobox.bind("<<ComboboxSelected>>", newselection)
# TODO: Тебе же подчеркнули переменную city_id красной чертой - это значит переменная не объявлена.
params = {'id': city_id, 'APPID': settings.APPID}

# TODO: Что делает эта строчка кода?
response = requests.get(settings.url, params=params)

# combobox.bind("<<ComboboxSelected>>",newselection)
# TODO: Какой результат возвращает выражение: response.json()['main']['temp_max'] - 273 ?
#Запрашивает у сайта температуру по Фаренгейту а я ее преобразовываю в Цельсий
label1 = Label(root, text=response.json()['main']['temp_max'] - 273, font="Arial 12")
label2 = Label(root, text=response.json()['wind']['speed'], font="Arial 12")
label = Label(text=datetime.fromtimestamp(response.json()['dt']), font="Arial 12")
# button.bind(, on_click)
# but.grid(row=0,column=0)
label.grid(row=0, column=2)
label1.grid(row=2, column=0)
label2.grid(row=2, column=2)

try:  # Перехватывает сетевую ошибку
    # TODO: Зачем ты снова написал это? Тоже самое написано чуть выше!(Убрал)
    # TODO: Для чео ты вызвал тут эту функцию?
    #Щас такая штука возникла если я уберу эту строку или кину ее в коментарий то ваше TODO будет выдавать ошибку
    conclusionweather()
except requests.exceptions.ConnectionError:
    print("Нет соединения с сервером")

root.mainloop()