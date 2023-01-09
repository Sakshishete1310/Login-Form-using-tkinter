from tkinter import *
top = Tk()
top.geometry("500x500")
top.title("My second GUI App")

label1 = Label(top,text="Login Form").place(x=200,y=50)

label2 = Label(top,text="Enter your Email id").place(x=100,y=100)
entry1 = Entry(top).place(x=100,y=130)

label3 = Label(top,text="Password").place(x=100,y=160)
entry2 = Entry(top).place(x=100,y=190)

button = Button(top, text="Login").place(x=120,y=230)
button = Button(top, text="Cancel").place(x=200,y=230)

top.mainloop()
