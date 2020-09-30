import tkinter
from tkinter import *
from tkinter import messagebox

val = ""
A = 0
operator = ""


def btn1_clicked():
    global val
    val = val + "1"
    data.set(val)


def btn2_clicked():
    global val
    val = val + "2"
    data.set(val)


def btn3_clicked():
    global val
    val = val + "3"
    data.set(val)


def btn4_clicked():
    global val
    val = val + "4"
    data.set(val)


def btn5_clicked():
    global val
    val = val + "5"
    data.set(val)


def btn6_clicked():
    global val
    val = val + "6"
    data.set(val)


def btn7_clicked():
    global val
    val = val + "7"
    data.set(val)


def btn8_clicked():
    global val
    val = val + "8"
    data.set(val)


def btn9_clicked():
    global val
    val = val + "9"
    data.set(val)


def btn0_clicked():
    global val
    val = val + "0"
    data.set(val)


def btn_plus():
    global A
    global operator
    global val
    A = int(val)
    operator = "+"
    val = val + "+"
    data.set(val)


def btn_sub():
    global A
    global operator
    global val
    A = int(val)
    operator = "-"
    val = val + "-"
    data.set(val)


def btn_malti():
    global A
    global operator
    global val
    A = int(val)
    operator = "*"
    val = val + "*"
    data.set(val)


def btn_div():
    global A
    global operator
    global val
    A = int(val)
    operator = "/"
    val = val + "/"
    data.set(val)


def c_presed():
    global A
    global operator
    global val
    val = ""
    A = 0
    operator = ""
    data.set(val)


def eaual():
    global A
    global operator
    global val
    val2 = val
    if operator == "+":
        x = int((val2.split("+")[1]))
        C = A + x
        data.set(C)
        val = str(C)

    elif operator == "-":
        x = int((val2.split("-")[1]))
        C = A - x
        data.set(C)
        val = str(C)

    elif operator == "*":
        x = int((val2.split("*")[1]))
        C = A * x
        data.set(C)
        val = str(C)

    elif operator == "/":
        x = int((val2.split("/")[1]))
        if x == 0:
            messagebox.showerror("ERROR", "DIVISION OF 0 IS NOT ALLOW")
            A = ""
            val = ""
            data.set(val)
        else:
            C = int(A / x)
            data.set(C)
            val = str(C)


root = tkinter.Tk()
root.geometry("250x400+300+300")
root.resizable(0, 0)
root.title("CALCULATOR")

data = StringVar()
lab = Label(
    root,
    text="0",
    font=("verdana", 25),
    anchor=SE,
    textvariable=data,
    background="#565656",
    fg="#000000",
)
lab.pack(expand=True, fill="both", )

btnrow1 = Frame(root, bg="#808080")
btnrow1.pack(expand=True, fill="both", )

btnrow2 = Frame(root, bg="#808080")
btnrow2.pack(expand=True, fill="both", )

btnrow3 = Frame(root, bg="#808080")
btnrow3.pack(expand=True, fill="both", )

btnrow4 = Frame(root, bg="#808080")
btnrow4.pack(expand=True, fill="both", )

btn1 = Button(
    btnrow1,
    text="1",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    bg="#3a3a3c",
    command=btn1_clicked,
)
btn1.pack(side=LEFT, expand=True, fill="both", )

btn2 = Button(
    btnrow1,
    text="2",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    bg="#3a3a3c",
    command=btn2_clicked
)

btn2.pack(side=LEFT, expand=True, fill="both", )

btn3 = Button(
    btnrow1,
    text="3",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    bg="#3a3a3c",
    command=btn3_clicked,
)

btn3.pack(side=LEFT, expand=True, fill="both", )

btnplus = Button(
    btnrow1,
    text="+",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    bg="#3a3a3c",
    command=btn_plus,
)

btnplus.pack(side=LEFT, expand=True, fill="both", )

btn4 = Button(
    btnrow2,
    text="4",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    bg="#3a3a3c",
    command=btn4_clicked,
)
btn4.pack(side=LEFT, expand=True, fill="both", )

btn5 = Button(
    btnrow2,
    text="5",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    bg="#3a3a3c",
    command=btn5_clicked,
)
btn5.pack(side=LEFT, expand=True, fill="both", )

btn6 = Button(
    btnrow2,
    text="6",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    bg="#3a3a3c",
    command=btn6_clicked,
)
btn6.pack(side=LEFT, expand=True, fill="both", )

btnsub = Button(
    btnrow2,
    text="_",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    bg="#3a3a3c",
    command=btn_sub,
)
btnsub.pack(side=LEFT, expand=True, fill="both", )

btn7 = Button(
    btnrow3,
    text="7",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    bg="#3a3a3c",
    command=btn7_clicked,
)
btn7.pack(side=LEFT, expand=True, fill="both", )

btn8 = Button(
    btnrow3,
    text="8",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    bg="#3a3a3c",
    command=btn8_clicked,
)
btn8.pack(side=LEFT, expand=True, fill="both", )

btn9 = Button(
    btnrow3,
    text="9",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    bg="#3a3a3c",
    command=btn9_clicked,
)
btn9.pack(side=LEFT, expand=True, fill="both", )

btnmalti = Button(
    btnrow3,
    text="x",
    font=("verdana", 20),
    relief=GROOVE,
    border=0,
    bg="#3a3a3c",
    command=btn_malti,
)
btnmalti.pack(side=LEFT, expand=True, fill="both", )

btnc = Button(
    btnrow4,
    text="C",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    bg="#ff6e00",
    command=c_presed,
)
btnc.pack(side=LEFT, expand=True, fill="both", )

btn0 = Button(
    btnrow4,
    text="0",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    bg="#3a3a3c",
    command=btn0_clicked,
)
btn0.pack(side=LEFT, expand=True, fill="both", )

btnequal = Button(
    btnrow4,
    text="=",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    bg="#3a3a3c",
    command=eaual,
)
btnequal.pack(side=LEFT, expand=True, fill="both", )

btndiv = Button(
    btnrow4,
    text="/",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    bg="#3a3a3c",
    command=btn_div,
)
btndiv.pack(side=LEFT, expand=True, fill="both", )

root.mainloop()
