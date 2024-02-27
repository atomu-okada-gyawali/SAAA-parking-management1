from tkinter import *
import tkinter.ttk as ttk
import tkinter as tk
import sqlite3
from PIL import Image, ImageTk

conn = sqlite3.connect('parkingManagement.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS User(
            UserID INTEGER PRIMARY KEY AUTOINCREMENT,
            UserFName TEXT NOT NULL,
            UserLName TEXT NOT NULL,
            UserUName TEXT NOT NULL,
            UserEmail TEXT NOT NULL,
            UserPassword TEXT NOT NULL,
            UserGender TEXT NOT NULL,
            UserAge TEXT NOT NULL,
            UserPosition TEXT NOT NULL,
            UserPhoneNumber TEXT NOT NULL
)''')


conn.commit()
conn.close()
#creating a tkinter window
root = Tk()
#title of the tkinter window
root.title("First Page")
#the windows geometric specification is done using geometry
root.geometry("1625x950")
#using config to edit the background of the window
root.config (bg = "white")

def goto_login():
    '''Here the login funtion is created 
    in order to go from one window to another destroying the previous 
    window in process using the destroy() and 
    also the new window is import using import module 
    
    '''
    root.destroy()
    import loginpage

def goto_register():
    root.destroy()
    import registrationpage

#frame is used to create a separate frame inside the tkinter window and it's bg and geometry can be changed
frame1 = Frame(root, height = 497,bg = "white", width = 700)
frame1.pack(side = "right")
frame1.place(anchor =CENTER, x =800 , y = 420)

def open_image(file_path):
    '''function to display any image inside the tkinter window 
    first we have to define a function name and create image path for us to use the image inside the tkinter window
    '''
    image = Image.open(file_path)
    return ImageTk.PhotoImage(image)

image_path = ("SAAA-parking-management1\\resources\\image_firstpage.png") #here is the image path and also the image format should me
#mentioned in order for it to be imported successfully

image = open_image(image_path)
label = tk.Label(root, image=image,bg = "white", width = 600, height = 650)#background and geometry of image is changed according to the window 
label.pack()
label.place(anchor = CENTER, x =790, y = 400 ) #anchor is used to adjust the image inside the window, here it is used to adjust it at the center of the window


#this is the second image along with its path in the computer 
image_path = ("SAAA-parking-management1\\resources\\logo_firstpage.png")

img2 = open_image(image_path)
label2 = tk.Label(root,image = img2,bg = "white",width = 246, height = 61.38 )
label2.pack()
label2.place(anchor = "nw", x = 25, y = 15)







#using label to write text inside the window and editing its background foreground and font according to the need 
lbl1 = Label(text = "Welcome to SAAA", bg = "white", fg = "black", font = ("Georgia Bold",29 ))
#place is used to adjust where we can place the written text to be inside the tkinter window
lbl1.place(x =600, y = 30 )

lbl2 = Label(root, text = "make your own space", bg = "white", fg = "black", font = ("Georgia", 12))
lbl2.place(x =692, y = 85 )

#button is used to create a button that is functional when clicked and it can be edited according to the need 
log_btn = Button(root, text = "          LOGIN          ", fg = "black", bg = "#FFC125", font = ("Georgia", 14),command = goto_login)
log_btn.place(x =700, y = 660 )

signup_btn = Button(root, text = "         SIGNUP         ", bg = "#FFC125", fg = "black", font = ("Georgia",14),command = goto_register)
#here login command is added in order to go the next window when we click the that specific button
signup_btn.place(x = 700, y=740)





#mainloop is the finish line of the window it is used to display the window without it no window is created 
root.mainloop()
