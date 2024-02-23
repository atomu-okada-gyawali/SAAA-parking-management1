from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk


b = Tk()
b.title("Options")
b.geometry("1624x961")
b.config(bg = "#FECE2F")


# frame1 = Frame(b, width = 327, height = 962, bg = "#FFD700")
# frame1.pack(side = LEFT)

# frame2 = Frame(b, width =1280, height = 919, bg= "#FFD700" )
# frame2.pack(side = RIGHT)

# frame3 = Frame(b, width = 277, height = 500, bg = "#FFD700")
# frame3.place(x =10, y = 246 )


def open_image(file_path):
    image = Image.open(file_path)
    return ImageTk.PhotoImage(image)

image_path = ("SAAA-parking-management1\\resources\\logo_optionpage.png")

img = open_image(image_path)
label1 = tk.Label(b, image = img, width = 328, height = 246, bg = "#FECE2F")
label1.pack()
label1.place(anchor = "nw", x =-1, y =-35 )

db= Label(b, text = "DASHBOARD", fg = "black",bg = "#FECE2F", font = ("Georgia Bold", 16))
db.place(x = 35, y = 220)

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

submitButton = Button(b, text = 'Submit', font = ('Georgia', 16), bg = "#FECE2F")
submitButton.place(x = 970, y = 700)

b.mainloop()
