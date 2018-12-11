from tkinter import *
from tkinter.ttk import *
from tkinter import scrolledtext
from phpserialize import *


window = Tk()
 
window.title("Welcome to Iman app")
 
window.geometry('500x400')
 
lbl = Label(window, text="Hello")
 
lbl.grid(column=0, row=0)
 
txt = Entry(window,width=10)
 
txt.grid(column=1, row=0)

txt.focus()
 
def clicked():
 
    res = txt.get()

    print(res)

    #str_byte = str.encode(res)
    
    #print(str_byte)

    temp = dumps(res)

    lbl.configure(text= temp)
 
btn = Button(window, text="Click Me", command=clicked)
 
btn.grid(column=2, row=0)

combo = Combobox(window)

combo['values']= ("Object", "String", "Integer",)

combo.current(1) #set the selected item

combo.grid(column=1, row=1)
 
window.mainloop()
