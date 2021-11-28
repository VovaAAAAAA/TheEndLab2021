from tkinter import *
from prettytable import PrettyTable
from grafic import showplot
from table import openTabble
from toJSON import convertToJSON
from toJSON import convertInJSON
from table_txt import opentabble_2
from table_cvs import opentabble_1

root = Tk()
root.title("Графік росту ціни")
root.geometry("300x300")
root.resizable(False, False)
root.configure(bg = "gray22")

def openPlot():
    showplot()

def openTable():
    openTabble()
    root_2 = Tk()
    root_2.geometry('200x100')
    root_2.title("ТАблиця")
    lbl = Label(root_2)
    lbl.configure(font = (7), text = "Таблиця в консолі")
    lbl.place(x = 0, y = 0)
    root_2.mainloop()


def createJSON():
    convertToJSON()
    root_3 = Tk()
    root_3.geometry('356x70')
    root_3.resizable(False, False)
    root_3.title('файл ')
    lbl = Label(root_3)
    lbl.configure(font = (8), text = 'Файл у форматі JSON сформовано')
    lbl.place(x = 4, y = 2)
    root_3.mainloop()

def create_JSON():
    convertInJSON()
    root_4 = Tk()
    root_4.geometry('356x50')
    root_4.resizable(False, False)
    root_4.title('повідомлення')
    lbl = Label(root_4)
    lbl.configure(font = (10), text = 'Файл у форматі JSON сформовано')
    lbl.place(x = 4, y = 2)
    root_4.mainloop()

def openTable_1():
    opentabble_1()
    root_5 = Tk()
    root_5.geometry('356x50')
    root_5.resizable(False, False)
    root_5.title('Повідомлення')
    lbl = Label(root_5)
    lbl.configure(font = (10), text = 'Таблиця сформована в .csv')
    lbl.place(x = 4, y = 2)
    root_5.mainloop

def openTable_2():
    opentabble_2()
    root_6 = Tk()
    root_6.geometry('356x50')
    root_6.resizable(False, False)
    root_6.title('Повідомлення')
    lbl = Label(root_6)
    lbl.configure(font = (10), text = "Таблиця сформована в .txt")
    lbl.place(x = 4, y = 2)
    root_6.mainloop



btn1 = Button(root)
btn1.configure(bg = 'gray', fg = 'white', text = 'Відкрити графік', command=openPlot)
btn1.place(x = 55, y = 20, width=200, height=30)

btn2 = Button(root)
btn2.configure(bg='gray', fg='white', text='Відкрити таблицю', command=openTable)
btn2.place(x = 55, y = 50, width=200, height=30)

btn3 = Button(root)
btn3.configure(bg = 'gray', fg = 'white', text = 'відкрити список товарів(JSON)', command = createJSON)
btn3.place(x = 25, y = 80, width = 250, height = 30)

btn4 = Button(root)
btn4.configure(bg = 'gray', fg = 'white', text = 'відкрити  ціну(JSON)', command = create_JSON)
btn4.place(x = 55, y = 110, width = 200, height = 30)

btn5 = Button(root)
btn5.configure(bg = 'gray', fg = 'white', text = 'Cформувати таблицю в exel', command = openTable_1)
btn5.place(x = 55, y = 140, width = 200, height = 30)

btn6 = Button(root)
btn6.configure(bg = 'gray', fg = 'white', text = 'Cтворити текстовий файл', command = openTable_2)
btn6.place(x = 55, y = 170, width = 200, height = 30)

root.mainloop()