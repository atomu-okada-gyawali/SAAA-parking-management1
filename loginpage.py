from tkinter import *
from PIL import ImageTk, Image
import sqlite3
# import ctypes
from tkinter import messagebox

# ctypes.windll.shcore.setprocessDpiAwareness(1)
win=Tk()
win.configure(bg="white")
win.geometry("1624x962")

# win.maxsize(width=1000,height=800)
# win.minsize(width=500,height=300)

def login():
    try:
        conn = sqlite3.connect('parkingManagement.db')
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM User WHERE UserUName = (?)''',(etn_username.get(),))
        userRecord = cursor.fetchone()

        assert userRecord != None, 'Wrong Username'
        assert userRecord[5] == entry_password.get() , 'Wrong Password'

        with open('currentlyLoggedUser.txt', 'w') as currenUser:
            currenUser.write(str(userRecord[0]))
        conn.close()
        win.destroy()
        import mainpage
    except AssertionError as e:
        messagebox.askretrycancel('Login Error',str(e))

img = Image.open("SAAA-parking-management1\\resources\\icon_loginpage.jpg")
topg = ImageTk.PhotoImage(img)

photoLabel = Label(win, image=topg,bg="white",height="500",width="700")
photoLabel.place(x=20, y=50)


# BACKGROUND IMAGE
img = Image.open("SAAA-parking-management1\\resources\\image_loginpage.jpg")
backg = ImageTk.PhotoImage(img)

photoLabel = Label(win, image=backg,bg="white",height="500",width="700")
photoLabel.place(x=700, y=180)



def show_password():
    if show_password_var.get():
        entry_password.config(show="")
    else:
        entry_password.config(show="*")


# Entry widget for password
entry_password = Entry(win, show="*",width="30")
entry_password.place(x=250, y=540)

# Checkbutton for "Show Password"
show_password_var = BooleanVar() #The BooleanVar in Tkinter is a special type of variable used to store boolean values (True or False). 
#It is commonly used with widgets like Checkbutton to keep track of their state. When the state of the BooleanVar changes, it triggers associated actions, such as invoking a callback function.

check_button = Checkbutton(win, text="Show Password", bg="white",variable=show_password_var, command=show_password)
check_button.place(x=250, y=570)


title_frame=Frame(win,bg="white",height=232,width=796)
title_frame.place(x=0,y=0)


welcome=Label(win,text="Welcome back! PLease login to your account",font=("Open Sans",10),bg="white",width="50").place(x=180,y=160)
heading=Label(title_frame,text="Login",bg="white",font=("Georgia",30,"bold")).place(x=300,y=80)
username=Label(win,text="Username",bg="white",font=("Open Sans",20)).place(x=250,y=400)
Password=Label(win,text="Password",bg="white",font=("Open Sanas",20))
Password.place(x=250,y=500)
etn_username=Entry(win,text="Username",width="30")
etn_username.place(x=250,y=440)
button_login=Button(win,text="Login",fg="black",bg="#FECE2F",width="12",height="1",font=(30),command = login).place(x=450,y=680)
exit=Button(win,text="Exit",fg="white",bg="black",width="12",height="1",font=(30)).place(x=450,y=730)



win.mainloop()
