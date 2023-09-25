from time import strftime
from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title('Clock')


def time():
  string = strftime('%H:%M:%S %p')
  lbl.config(text=string)
  lbl.after(1000, time)


lbl = Label(root,
            font=('calibri', 40, 'bold'),
            background='purple',
            foreground='white')
lbl.pack(anchor='center')
time()

mainloop()
