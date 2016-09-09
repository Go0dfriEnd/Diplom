from tkinter import *
from tkinter.ttk import *
import json
import requests
import settings
from datetime import datetime, date

def allname():
    op = open("city.list.json", encoding='UTF-8')
    lst = []
    for line in op:
        lol = json.loads(line)
        name = lol.get('name')
        lst.append(lol.get('name'))
    return lst


city_id=519188

params = {'id': city_id, 'APPID': settings.APPID}

response = requests.get(settings.url, params=params)


root = Tk()
root.geometry("450x470")
combobox = Combobox(root, values=allname(), font="Arial 12")

combobox.set(u"Выберите город")  # спомощью этой строчки мы установим Combobox в значение ОДИН изначально
combobox.grid(column=0, row=0)  # Позиционируем Combobox на форме

temp=response.json()['main']['temp_max'] - 273
temp=round(temp)

# print(temp)
tex = Text(root, width=5,height=3,font="Arial 12")
label1 = Label(root,text=temp, font="Arial 18")
label2 = Label(root, text=response.json()['wind']['speed'], font="Arial 12")
label3=Label(text= '°C',font="Arial 14")
label4=Label(root,text='Cкорость ветра в м\с',font="Arial 14")
label5=Label(root,font="Arial 14")
label = Label(text=datetime.fromtimestamp(response.json()['dt']), font="Arial 12")
label6=Label(font='Arial 18')
# button.bind(, on_click)
# but.grid(row=0,column=0)
tex.grid(row=2,column=2)
label.grid(row=0, column=3)
label1.grid(row=4, column=2)
label2.grid(row=5, column=0)
label3.grid(row=5,column=2)
label4.grid(row=6,column=0)
label5.grid(row=1,column=3)
label6.grid(row=3,column=2)
root.mainloop()