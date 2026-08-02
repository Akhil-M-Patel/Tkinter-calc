from tkinter import *

window = Tk()
window.geometry("300x450")

#Entry box
e = Entry(window, borderwidth=5)
e.place(x=10, y=10, width=280, height=40)

#Buttons

def click(num):
    result = e.get()
    e.delete(0, END)
    e.insert(0, str(result) + str(num))

num = 9

for row in range(3):
    for col in range(3):
        Button(
            window,
            text=str(num),
            width=12,
            command=lambda n=num: click(n)
        ).place(x=10 + col*90, y=80 + row*60)

        num -= 1

Button(
    window,
    text="0",
    width=12,
    command=lambda: click(0)
).place(x=10, y=260)

#Operators
def add():
    n1 = e.get()
    global math
    math = "addition" 
    global i
    i = int(n1)
    e.delete(0, END)
    
b = Button(window, text = "+", width = 12, command = add)
b.place(x=100, y=260)

def sub():
    n1 = e.get()
    global math
    math = "subtraction"
    global i
    i = int(n1)
    e.delete(0, END)
    
b = Button(window, text = "-", width = 12, command = sub)
b.place(x=190, y=260)

def mult():
    n1 = e.get()
    global math
    math = "multiplication"
    global i
    i = int(n1)
    e.delete(0, END)

b = Button(window, text = "*", width = 12, command = mult)
b.place(x=10, y=320)

def div():
    n1 = e.get()
    global math
    math = "division"
    global i
    i = int(n1)
    e.delete(0, END)

b = Button(window, text = "/", width = 12, command = div)
b.place(x=100, y=320)

def equal():
    n2 = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, i + int(n2))
    elif math == "subtraction":
        e.insert(0, i - int(n2))
    elif math == "multiplication":
        e.insert(0, i * int(n2))
    elif math == "division":
        try:
            e.insert(0, i / int(n2))
        except ZeroDivisionError:
            e.insert(0, "Error!! Cannot divide by zero")

b = Button(window, text = "=", width = 12, command = equal)
b.place(x=190, y=320)

def clear():
    e.delete(0, END)

b = Button(window, text = "Clear", width = 12, command = clear)
b.place(x=10, y=380)

mainloop()
