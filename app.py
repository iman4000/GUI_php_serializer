from tkinter import *
from tkinter.ttk import *
from tkinter import scrolledtext
from phpserialize import *


#Test class for make obj_box
class graphic_obj_basic:
        def __init__(self, master):
        '''
        self.master = master
        self.frame = tk.Frame(self.master)
        self.button1 = tk.Button(self.frame, text = 'New Window', width = 25, command = self.new_window)
        self.button1.pack()
        self.frame.pack()
        '''    
        #second way

        w = Label(root, text="red", bg="red", fg="white")
        w.pack(padx=5, pady=10, side=LEFT)
        w = Label(root, text="green", bg="green", fg="black")
        w.pack(padx=5, pady=20, side=LEFT)
        w = Label(root, text="blue", bg="blue", fg="white")
        w.pack(padx=5, pady=20, side=LEFT)

    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo2(self.newWindow)
        

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
