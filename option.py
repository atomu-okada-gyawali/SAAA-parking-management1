from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk


#tk() to create window 
b = Tk()
b.title("Options")#title of the created window
b.geometry("1624x961")#geometry  of the created window 
b.config(bg = "#FECE2F")#config to edit the background of the window




def open_image(file_path):
    '''function to import the downloaded image inside 
    the tkinter window 
    '''
    image = Image.open(file_path)
    return ImageTk.PhotoImage(image)

#image path of the imported image inside the window 
image_path = ("SAAA-parking-management1\\resources\\logo_optionpage.png")

img = open_image(image_path)
label1 = tk.Label(b, image = img, width = 328, height = 246, bg = "#FECE2F")
label1.pack()
#using pack and anchor to adjust the location of the image as per the need
label1.place(anchor = "nw", x =-1, y =-35 )


#for dashboard text using label and editing the background foreground and size of the font as per need
db= Label(b, text = "DASHBOARD", fg = "black",bg = "#FECE2F", font = ("Georgia Bold", 16))
db.place(x = 35, y = 220)#using place to place them to the specific location as per need 

op = Label(b, text = "OPTIONS", fg = "white", bg = "#FECE2F", font = ("Georgia Bold", 16))
op.place(x = 50, y = 330)

rec = Label(b, text ="RECORDS", fg = "black", bg ="#FECE2F", font = ("Georgia Bold", 16) )
rec.place(x = 40, y = 440)

sta = Label(b, text = "STATISTICS", fg = "black", bg ="#FECE2F", font = ("Georgia Bold", 16) )
sta.place( x= 37, y = 550)

log = Label(b, text= "LOGOUT", fg = "black", bg = "#FECE2F", font = ("Georgia Bold", 16) )
log.place(x = 45, y = 660)




a1 = Label(b, text = "Four wheeler parking rate :", fg = "black", bg="#FECE2F", font = ("Open Sans", 12))
a1.place(x = 600, y = 290)

#Entry button is used to create a box to input the information
e1 = Entry(b, width = 20)
e1.place(x = 920, y =292 )

a2 = Label(b, text = "Four wheeler parking overtime rate :", fg = "black", bg ="#FECE2F", font = ("Open Sans", 12))
a2.place(x = 600, y = 370 )

e2  = Entry(b, width = 20)
e2.place(x = 920, y=372  )

a3 = Label(b, text= "Two wheeler parking rate :", fg = "black", bg = "#FECE2F", font = ("Open Sans", 12))
a3.place(x = 600, y = 450)

e3 = Entry(b, width = 20)
e3.place(x =920, y= 452 )

a4  = Label(b, text = "Two wheeler parking overtime rate :", fg = "black", bg = "#FECE2F", font = ("Open Sans", 12))
a4.place(x = 600, y = 530)

e4 = Entry(b, width = 20)
e4.place(x = 920, y = 532)


#submit button created in order to submit the information after clicking it
sub_btn = Button(b, text = "  SUBMIT  ", fg = "black", bg = "#FECE2F", font = ("Georgia", 18 ))
sub_btn.place( x = 810, y = 640)

b.mainloop()#mainloop used to display the tkinter window
