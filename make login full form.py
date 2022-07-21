from tkinter import *


root = Tk()
root.geometry("425x280")
root.title("Form")
#root.configure(f1,background="black")
def log():
    f2 = Frame()
    f2.place(x=0, y=0, width=425, height=280)
########################################################################################################################
    f2.configure(background="black")
########################################################################################################################
    Label(f2,text="Welcome To Login Form:",font="Arial 15",bg="black",fg="red").place(x=100,y=3)

    Label(f2,text="Enter Name",font="Arial 17",bg="black",fg="red").place(x=70,y=40)
    e1=Entry(f2,font="Arial 10",bg="white",fg="red")
    e1.place(x=220,y=45)

    Label(f2, text="Enter Pass.", font="Arial 17", bg="black", fg="red").place(x=70, y=90)
    e2=Entry(f2,font="Arial 10",bg="White",fg="red")
    e2.place(x=220,y=95)

    b3=Button(f2,text="Login!!!",font="Arial 15",bg="black",fg="red")
    b3.place(x=180,y=150)

    b2=Button(f2,text="Back!!!",font="Arial 12",bg="black",fg="red",command=home)
    b2.place(x=0,y=245)

def reg():
    f3 = Frame()
    f3.place(x=0, y=0, width=425, height=280)
    f3.configure(background="black")

    Label(f3, text="Welcome To Registration Form:", font="Arial 15", bg="black", fg="red").place(x=80, y=3)

    Label(f3, text="Enter Name:", font="Arial 17", bg="black", fg="red").place(x=70, y=50)
    e1 = Entry(f3, font="Arial 10", bg="white", fg="red")
    e1.place(x=250, y=55)

    Label(f3, text="Enter PhoneNo.:", font="Arial 17", bg="black", fg="red").place(x=70, y=90)
    e2 = Entry(f3, font="Arial 10", bg="white", fg="red")
    e2.place(x=250, y=95)

    Label(f3, text="Enter Email:", font="Arial 17", bg="black", fg="red").place(x=70, y=130)
    e3 = Entry(f3, font="Arial 10", bg="white", fg="red")
    e3.place(x=250, y=135)

    Label(f3, text="Enter Address:", font="Arial 17", bg="black", fg="red").place(x=70, y=170)
    e4 = Entry(f3, font="Arial 10", bg="white", fg="red")
    e4.place(x=250, y=176)

    b3 = Button(f3, text="Submit!!!", font="Arial 12", bg="black", fg="red")
    b3.place(x=185, y=210)

    b4 = Button(f3, text="Back!!!", font="Arial 12", bg="black", fg="red",command=home)
    b4.place(x=0, y=247)



def home():

    f1=Frame()
    f1.place(x=0,y=0,width=425,height=280)
    f1.configure(background="black")
    Label(f1,text="Welcome To Form!!!",font="Arial  20 ",bg="black",fg="red").place(x=100,y=3)
    Label(f1, text="---------------------------", font="Arial  20 ", bg="black", fg="red").place(x=100, y=35)
    b1=Button(f1,text="Login!!",font="Arial 15",fg="red",bg="black",command=log)
    b1.place(x=105,y=110)

    b2=Button(f1,text="Regis.!!",font="Arial 15",fg="red",bg="black",command=reg)
    b2.place(x=250,y=110)

home()
root.mainloop()