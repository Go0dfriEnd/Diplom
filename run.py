from tkinter import *
from tkinter.ttk import *
import json
import requests
import settings
from datetime import datetime, date

city_id=519188

params = {'id': city_id, 'APPID': settings.APPID}

response = requests.get(settings.url, params=params)


def allname():
    op = open("city.list.json", encoding='UTF-8')
    lst = []
    for line in op:
        lol = json.loads(line)
        name = lol.get('name')
        lst.append(lol.get('name'))
    return lst


root = Tk()
root.geometry("450x470")
combobox = Combobox(root, values=allname(), font="Arial 12")

combobox.set(u"Выберите город")  # спомощью этой строчки мы установим Combobox в значение ОДИН изначально
combobox.grid(column=0, row=0)  # Позиционируем Combobox на форме



label1 = Label(root, text=response.json()['main']['temp_max'] - 273, font="Arial 12")
label2 = Label(root, text=response.json()['wind']['speed'], font="Arial 12")
label = Label(text=datetime.fromtimestamp(response.json()['dt']), font="Arial 12")
# button.bind(, on_click)
# but.grid(row=0,column=0)
label.grid(row=0, column=2)
label1.grid(row=2, column=0)
label2.grid(row=2, column=2)


root.mainloop()