#gui based user interactive calculator app using tkinter "this is from my personal projects"

from tkinter import *


def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                print(e)
                value = "Error"
        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


root = Tk()
root.geometry("480x790")
root.maxsize(480, 790)
root.minsize(480, 790)
root.title("GUI Calculator by Himanshu")
# root.wm_iconbitmap("icon.ico")
root.configure(background="SpringGreen")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="manrope 40", background="azure3")
screen.pack()

f1 = Frame(root, bg="SpringGreen")
b = Button(f1, text="9", padx=10, pady=10, font="manrope 30 bold", bg="grey85")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=15, pady=15)

b = Button(f1, text="8", padx=10, pady=10, font="manrope 30 bold", bg="grey85")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=15, pady=15)

b = Button(f1, text="7", padx=10, pady=10, font="manrope 30 bold", bg="grey85")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=15, pady=15)

b = Button(f1, text="C", padx=10, pady=10, font="manrope 30 bold", bg="grey85")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=15, pady=15)

f1.pack()

f1 = Frame(root, bg="SpringGreen")
b = Button(f1, text="6", padx=10, pady=10, font="manrope 30 bold", bg="grey85")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=15, pady=15)

b = Button(f1, text="5", padx=10, pady=10, font="manrope 30 bold", bg="grey85")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=15, pady=15)

b = Button(f1, text="4", padx=10, pady=10, font="manrope 30 bold", bg="grey85")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=15, pady=15)

b = Button(f1, text="*", padx=10, pady=10, font="manrope 30 bold", bg="grey85")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=15, pady=15)

f1.pack()

f1 = Frame(root, bg="SpringGreen")
b = Button(f1, text="3", padx=10, pady=10, font="manrope 30 bold", bg="grey85")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=15, pady=15)

b = Button(f1, text="2", padx=10, pady=10, font="manrope 30 bold", bg="grey85")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=15, pady=15)

b = Button(f1, text="1", padx=10, pady=10, font="manrope 30 bold", bg="grey85")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=15, pady=15)

b = Button(f1, text="/", padx=10, pady=10, font="manrope 30 bold", bg="grey85")
b.config(width=2, height=1)
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=15, pady=15)

f1.pack()

f1 = Frame(root, bg="SpringGreen")

b = Button(f1, text=".", padx=10, pady=10, font="manrope 30 bold", bg="grey85")
b.config(width=2, height=1)
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=15, pady=15)
b = Button(f1, text="0", padx=10, pady=10, font="manrope 30 bold", bg="grey85")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=15, pady=15)

b = Button(f1, text="-", padx=10, pady=10, font="manrope 30 bold", bg="grey85")
b.config(width=2, height=1)
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=15, pady=15)

b = Button(f1, text="+", padx=10, pady=10, font="manrope 30 bold", bg="grey85")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=15, pady=15)

f1.pack()

f1.pack()

f1 = Frame(root, bg="SpringGreen")
b = Button(f1, text="%", padx=10, pady=10, font="manrope 30 bold", bg="grey85")
b.config(width=2, height=1)
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=15, pady=15)

b = Button(f1, text="=", padx=10, pady=10, font="manrope 30 bold", bg="grey85")
b.config(width=10, height=1)
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=15, pady=15)

f1.pack()

# b.config( width=4,height=1)


root.mainloop()