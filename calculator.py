from tkinter import *

root = Tk()

e = Entry(root, width=35, border=5, font=10)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)


def button_sub():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)


def button_mul():
    first_number = e.get()
    global f_num
    global math
    math = "multiply"
    f_num = int(first_number)
    e.delete(0, END)


def button_div():
    first_number = e.get()
    global f_num
    global math
    math = "divide"
    f_num = int(first_number)
    e.delete(0, END)


def button_clear():
    e.delete(0, END)
    

def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + int(second_number))
    elif math == "subtraction":
        e.insert(0, f_num - int(second_number))
    elif math == "multiply":
        e.insert(0, f_num * int(second_number))
    elif math == "divide":
        e.insert(0, f_num / int(second_number))


# define button


button_1 = Button(root, text="1", font=10, padx=40, pady=20, bg="black", fg="white", border=5, command=lambda: button_click(1))
button_2 = Button(root, text="2", font=10, padx=40, pady=20, bg="black", fg="white", border=5, command=lambda: button_click(2))
button_3 = Button(root, text="3", font=10, padx=40, pady=20, bg="black", fg="white", border=5, command=lambda: button_click(3))
button_4 = Button(root, text="4", font=10, padx=40, pady=20, bg="black", fg="white", border=5, command=lambda: button_click(4))
button_5 = Button(root, text="5", font=10, padx=40, pady=20, bg="black", fg="white", border=5, command=lambda: button_click(5))
button_6 = Button(root, text="6", font=10, padx=40, pady=20, bg="black", fg="white", border=5, command=lambda: button_click(6))
button_7 = Button(root, text="7", font=10, padx=40, pady=20, bg="black", fg="white", border=5, command=lambda: button_click(7))
button_8 = Button(root, text="8", font=10, padx=40, pady=20, bg="black", fg="white", border=5, command=lambda: button_click(8))
button_9 = Button(root, text="9", font=10, padx=40, pady=20, bg="black", fg="white", border=5, command=lambda: button_click(9))
button_0 = Button(root, text="0", font=10, padx=40, pady=20, bg="black", fg="white", border=5, command=lambda: button_click(0))
button_add = Button(root, text="+", font=10, padx=39, pady=20, bg="black", fg="white", border=5, command=button_add)
button_sub = Button(root, text="-", font=10, padx=41, pady=20, bg="black", fg="white", border=5, command=button_sub)
button_mul = Button(root, text="*", font=10, padx=40, pady=20, bg="black", fg="white", border=5, command=button_mul)
button_div = Button(root, text="/", font=10, padx=41, pady=20, bg="black", fg="white", border=5, command=button_div)
button_clear = Button(root, text="c", font=10, padx=94, pady=20, bg="black", fg="white", border=5, command=button_clear)
button_equal = Button(root, text="=", font=10, padx=93, pady=20, bg="black", fg="white", border=5, command=button_equal)


# put the button on the screen

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)

button_add.grid(row=2, column=3)
button_sub.grid(row=3, column=3)
button_mul.grid(row=4, column=3)
button_div.grid(row=5, column=3)

button_0.grid(row=5, column=1)

button_clear.grid(row=1, column=0, columnspan=2)
button_equal.grid(row=1, column=2, columnspan=2)


root.mainloop()
