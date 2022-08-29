import tkinter as tk
#import csv
import sqlite3
import datetime
import os
import mod as m
from tkinter import ttk
from tkinter import *
from tkinter import Menu
from tkinter import messagebox as mb
#import main.py as ma

#Окно
window = Tk()
window.title("Години")
window.geometry("1280x720")
window.resizable(width=False, height=False)

#Блоки
frame_add_form = tk.Frame(window, width = 640, height = 350)
frame_add_statistics = tk.Frame(window, width = 640, height = 350)
frame_add_list = tk.Frame(window, width = 1280, height = 600)

frame_add_form.pack()
frame_add_form.place(x = 0, y = 0)
frame_add_statistics.pack()
frame_add_statistics.place(x = 640, y = 0)
frame_add_list.pack()
frame_add_list.place(x = 0, y = 350)

#Выход з приложения
def endProgram():
    raise SystemExit
    sys.exit()

def refresh():
    window.destroy()
    os.popen("Godziny.py")

def refresh_bi(event):
    window.destroy()
    os.popen("Godziny.py")

#Меню сверху
menu = Menu(window)
new_info = Menu(menu, tearoff = 0)
new_info.add_command(label = 'Info')
new_info.add_separator()
new_info.add_command(label = 'Refresh', command = refresh)
window.bind('<F5>', refresh_bi)
new_info.add_separator()
new_info.add_command(label = 'Export')
new_info.add_separator()
new_info.add_command(label = "Exit", command = endProgram)
menu.add_cascade(label = 'File', menu = new_info)

new_comand = Menu(menu, tearoff = 0)
new_comand.add_command(label = 'Alt + F4                     Exit')
new_comand.add_command(label ='F5                              Refresh')
new_comand.add_command(label = 'Ctrl + E                     Export')
menu.add_cascade(label = 'Commands', menu = new_comand)
window.config(menu = menu)

#Данные ввода
form = Label(window, text = 'Дата:', font = ("Sylfaen", 12))
form.pack()
form.place(x = 30, y = 30)
mb_form = Entry()
mb_form.pack()
mb_form.place(x = 400, y = 30)

form = Label(window, text = 'Початок робочого дня:', font = ("Sylfaen", 12))
form.pack()
form.place(x = 30, y = 70)
mb_form = Entry()
mb_form.pack()
mb_form.place(x = 400, y = 70)

form = Label(window, text = 'Кінець робочого дня:', font = ("Sylfaen", 12))
form.pack()
form.place(x = 30, y = 110)
mb_form = Entry()
mb_form.pack()
mb_form.place(x = 400, y = 110)

form = Label(window, text = 'Премія:', font = ("Sylfaen", 12))
form.pack()
form.place(x = 30, y = 180)
mb_form = Entry()
mb_form.pack()
mb_form.place(x = 400, y = 180)

form = Button(window, text = "Записати", font = ("Sylfaen", 12))
form.pack()
form.place(x = 1040, y = 280)

#Данные статистики
form_statistics = Label(window, text = 'Зароблена сума:', font = ("Sylfaen", 12))
form_statistics.pack()
form_statistics.place(x = 670, y = 70)
form_value = tk.Label(window, text = 12)
form_value.pack()
form_value.place(x = 1040, y = 70)

form_statistics = Label(window, text = 'За цілий місяць годин:', font = ("Sylfaen", 12))
form_statistics.pack()
form_statistics.place(x = 670, y = 30)
form_statistics = tk.Label(window, text = m.get_statistic_houer())
form_statistics.pack()
form_statistics.place(x = 1040, y = 30)
#form_value = tk.Label(window, text = get_statistic_data(), font = ("Sylfaen", 12))
#form_value.pack()
#form_value.place(x = 1040, y = 30)

#БД
lst = [(1, '24.08.2022', '06:00', '18:00', '12', '272.40'),
       (1, '24.08.2022', '06:00', '18:00', '12', '272.40'),
       (2, '24.08.2022', '06:00', '18:00', '12', '272.40'),
       (1, '24.08.2022', '06:00', '18:00', '12', '272.40'),
       (1, '24.08.2022', '06:00', '18:00', '12', '272.40'),
       (1, '24.08.2022', '06:00', '18:00', '12', '272.40'),
       (1, '24.08.2022', '06:00', '18:00', '12', '272.40'),
       (1, '24.08.2022', '06:00', '18:00', '12', '272.40'),
       (3, '24.08.2022', '06:00', '18:00', '12', '272.40'),
       (4, '24.08.2022', '06:00', '18:00', '12', '272.40'),
       (5, '24.08.2022', '06:00', '18:00', '12', '272.40'),
       (1, '24.08.2022', '06:00', '18:00', '12', '272.40'),
       (1, '24.08.2022', '06:00', '18:00', '12', '272.40'),
       (1, '24.08.2022', '06:00', '18:00', '12', '272.40'),
       (1, '24.08.2022', '06:00', '18:00', '12', '272.40'),
       (1, '24.08.2022', '06:00', '18:00', '12', '272.40'),
       (1, '24.08.2022', '06:00', '18:00', '12', '272.40'),
       (1, '24.08.2022', '06:00', '18:00', '12', '272.40')]
#lst.place(x = 10, y = 10)
#lst.pack()

heads = ['id', 'data', 'start', 'finish', 'houer', 'selery']
table = ttk.Treeview(frame_add_list, show = 'headings')
table['columns'] = heads

for header in heads:
    table.heading(header, text = header, anchor = 'w')
    table.column(header, anchor = 'w', width = 210)
    #table.column('id', anchor = 'w', width = 50)
    #table.column('data', anchor = 'w', width = 350)
    #table.column('start', anchor = 'w', width = 350)
    #table.column('finish', anchor = 'w', width = 350)
    #table.column('houer', anchor = 'w', width = 350)
    #table.column('selery', anchor = 'w', width = 350)

for row in lst:
    table.insert('', tk.END, values = row)

scroll_pane = ttk.Scrollbar(frame_add_list, command = table.yview)
table.configure(yscrollcommand = scroll_pane.set)
scroll_pane.pack(side = tk.RIGHT, fill = tk.Y)
table.pack(expand = tk.YES, fill = tk.BOTH)


window.mainloop()