from tkinter import *

def button_click(num):
    global equation_text

    equation_text = equation_text + str(num)
    equation_label.set(equation_text)

def equals():
    global equation_text

    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text=total
    except ZeroDivisionError:
        equation_label.set("Arithmetic Error")
        equation_text=""

    except SyntaxError:
        equation_label.set("Syntax Error")
        equation_text=""

def clear():
    global equation_text
    equation_label.set("")
    equation_text=""


window = Tk()
window.title("Calculator program by SV")
window.geometry("480x520")

equation_text = ""

equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=('Arial', 16), bg='white', width=33, height=2)
label.pack()

frame = Frame(window)
frame.pack()

button1 = Button(frame, text=1, height=3, width=9, font=25, command= lambda:button_click(1))
button1.grid(row=0,column=0)

button2 = Button(frame, text=2, height=3, width=9, font=25, command= lambda:button_click(2))
button2.grid(row=0,column=1)

button3 = Button(frame, text=3, height=3, width=9, font=25, command= lambda:button_click(3))
button3.grid(row=0,column=2)

button4 = Button(frame, text=4, height=3, width=9, font=25, command= lambda:button_click(4))
button4.grid(row=1,column=0)

button5 = Button(frame, text=5, height=3, width=9, font=25, command= lambda:button_click(5))
button5.grid(row=1,column=1)

button6 = Button(frame, text=6, height=3, width=9, font=25, command= lambda:button_click(6))
button6.grid(row=1,column=2)

button7 = Button(frame, text=7, height=3, width=9, font=25, command= lambda:button_click(7))
button7.grid(row=2,column=0)

button8 = Button(frame, text=8, height=3, width=9, font=25, command= lambda:button_click(8))
button8.grid(row=2,column=1)

button9 = Button(frame, text=9, height=3, width=9, font=25, command= lambda:button_click(9))
button9.grid(row=2,column=2)

button0 = Button(frame, text=0, height=3, width=9, font=25, command= lambda:button_click(0))
button0.grid(row=3,column=1)

plus = Button(frame, text="+", height=3, width=6, font=25, command= lambda:button_click("+"))
plus.grid(row=0,column=3)

minus = Button(frame, text="-", height=3, width=6, font=25, command= lambda:button_click("-"))
minus.grid(row=1,column=3)

mul = Button(frame, text="*", height=3, width=6, font=25, command= lambda:button_click("*"))
mul.grid(row=2,column=3)

div = Button(frame, text="/", height=3, width=6, font=25, command= lambda:button_click("/"))
div.grid(row=3,column=3)

equal = Button(frame, text="=", height=3, width=9, font=25, command=equals)
equal.grid(row=4,column=1)

clears = Button(frame, text="clear", height=3, width=9, font=25, command= clear)
clears.grid(row=4,column=0)

decimal = Button(frame, text=".", height=3, width=9, font=25, command= lambda:button_click("."))
decimal.grid(row=4,column=2)

left_parenthesis = Button(frame, text=")", height=3, width=9, font=25, command= lambda:button_click(")"))
left_parenthesis.grid(row=3,column=2)

right_parenthesis = Button(frame, text="(", height=3, width=9, font=25, command= lambda:button_click("("))
right_parenthesis.grid(row=3,column=0)

modulus = Button(frame, text="%", height=3, width=6, font=25, command= lambda:button_click("%"))
modulus.grid(row=4,column=3)

window.mainloop()