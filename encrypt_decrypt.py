from tkinter import messagebox, simpledialog,Tk
#from random import choice

root=Tk()

def get_task():
    task=simpledialog.askstring('Task','Do you want to encrypt or decrypt?')
    return task

def get_message():
    message=simpledialog.askstring('Message','Enter the secret message: ')
    return message

while True:
    task=get_task()
    if task=='encrypt':
        message=get_message()
        messagebox.showinfo('Message to encrypt is: ',message)
    elif task=='decrypt':
        message=get_message()
        messagebox.showinfo('Message to decrypt is: ',message)
    else:
        break

def is_even(num):
    return num%2==0

def get_even_letter(message):
    even_letters=[]
    for counter in range(0,len(message)):
        if is_even(counter):
            even_letters.append(message[counter])
    return even_letters

def get_odd_letter(message):
    odd_letters=[]
    for counter in range(0,len(message)):
        if not is_even(counter):
            odd_letters.append(message[counter])
    return odd_letters

def swap_letters(message):
    letter_list=[]
    if not is_even(len(message)):
        message=message+'*'
    even_letter=get_even_letter(message)
    odd_letter=get_odd_letter(message)
    for counter in range(0,int(len(message/2))):
        letter_list.append(odd_letter[counter])
        letter_list.append(even_letter[counter])
    new_message=' '.join(letter_list)
    return new_message

root.mainloop()

