from tkinter import *
from tkinter.ttk import *
import json
import requests
import settings
from datetime import datetime, date

# Запрашивает данные о погоде у сайта и показывает их в консоли
def conclusionweather():
     if response.json().get('cod') == '404':
         print("Неверно задан город")
     else:
        print('id=  ',response.json()['id'])
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
     #request - запрос, response - ответ
#Пишет все имена городов которые есть в файле city.list.json
def allname():
    op=open("city.list.json",encoding='UTF-8')
    lst = []
    for line in op:
        lol=json.loads(line)
        name=lol.get('name')
        lst.append(lol.get('name'))
    return lst
#Выполняет действие при выборе города в списке в граф часте
def newselection(event):
    event = combobox.get()
    print(event)
    op=open('city.list.json')
    run()
    city_name=event

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


allname()

city_name=input('Введите город :  ')

#Находит id выбранного города
def find_id():
    op = open('city.list.json',encoding='UTF-8')
    city_id = None
    for line in op:
        city = json.loads(line)
        if city_name == city['name']:
            city_id = city["_id"]
            break
find_id()

combobox.bind("<<ComboboxSelected>>",newselection)
params = {'id': city_id, 'APPID': settings.APPID}

response = requests.get(settings.url, params=params)


#combobox.bind("<<ComboboxSelected>>",newselection)
label1 = Label(root, text=response.json()['main']['temp_max'] - 273, font="Arial 12")
label2 = Label(root, text=response.json()['wind']['speed'], font="Arial 12")
label = Label(text= datetime.fromtimestamp(response.json()['dt']), font="Arial 12")
# button.bind(, on_click)
# but.grid(row=0,column=0)
label.grid(row=0, column=2)
label1.grid(row=2, column=0)
label2.grid(row=2, column=2)




try:#Перехватывает сетевую ошибку
     response = requests.get(settings.url, params=params)
     conclusionweather()
except requests.exceptions.ConnectionError:
     print("Нет соединения с сервером")

root.mainloop()
