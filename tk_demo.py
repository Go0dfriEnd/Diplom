from tkinter import *
from tkinter.ttk import *
import json

def allname():
    op=open("city.list.json")
    lst = []
    for line in op:
        lol=json.loads(line)
        name=lol.get('name')
        lst.append(lol.get('name'))
    return lst



root = Tk()
root.geometry("400x470")
combobox = Combobox(root, values=allname(), font="Arial 12")
# frame - задает родительский виджет, на его территории будет располагаться Combobox
# values - задает набор значений, которые будут содержаться в Combobox изначально
# height - задает высоту выпадающего списка. Если число элементов списка меньше 11, то можно не задавать.
# Если не задано при колличестве элементов больше 10, то с правой стороны появится полоса прокрутки.
# Если в нашем примере задать значение height меньше трех, то с правой стороны появится полоса прокрутки,
# но она будет недоступна, а все элементы будут отображаться одновременно.
combobox.set(u"Выберите город")  # спомощью этой строчки мы установим Combobox в значение ОДИН изначально
combobox.grid(column=0, row=0)  # Позиционируем Combobox на форме




label1 = Label(root, text="Температура \n осадки ", font="Arial 12")
label2 = Label(root, text="Направление ветра \n  скорость", font="Arial 12")
label3 = Label(root, text="Тут \n будет \n картинка", font="Arial 12")
label = Label(text="Дата", font="Arial 12")
# button.bind(, on_click)
# but.grid(row=0,column=0)
label.grid(row=0, column=2)
label1.grid(row=2, column=0)
label2.grid(row=2, column=2)
label3.grid(row=1, column=1)


root.mainloop()
