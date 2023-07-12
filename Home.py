from Algorithme import *
from tkinter import *

def password():
    pswrd.delete(0,"end")
    a = genPassword(length.get())
    pswrd.insert(0,a)

menu = Tk()
menu.title("Password Generator")
menu.geometry("500x500")

length_label = Label(menu,text="Entrer la longuere :",width=20)
length_label.grid(row=0,column=0)

l = IntVar()
length = Entry(menu,width=20,textvariable=l)
length.grid(row= 0, column= 1)

a = StringVar()
a.set("")
pswrd_label = Label(menu,text="Votre mot de passe :",width=20)
pswrd_label.grid(row=4,column=0)
pswrd = Entry(menu,textvariable=a,width=20)
pswrd.grid(row=4,column=1)

btn = Button(menu,text="Generate",width=30,command=password)
btn.grid(row=8,column=1)

menu.mainloop()