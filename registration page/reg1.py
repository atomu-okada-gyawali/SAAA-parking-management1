from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import tkinter.ttk as ttk


win = Tk()
win.title = ("registration page")
win.geometry("1624x950")
win.config(bg = "white")



def open_image(file_path):
    image = Image.open(file_path)
    return ImageTk.PhotoImage(image)

image_path = (r"C:\Users\user\Downloads\taxiimage.png")

img = open_image(image_path)
label = tk.Label(win, image=img, bg = "white", width = 692, height = 766)
label.pack( side = LEFT)


image_path = (r"C:\Users\user\Downloads\saaa.png")
img2 = open_image(image_path)
label2 = tk.Label(win, image=img2, bg = "white",width = 246, height = 61.38)
label2.pack()   
label2.place(anchor = "nw",x = 25, y = 10)





lbl1 = Label(win, text = "Welcome to SAAA", fg = "black", bg =  'white' ,font = ("Georgia Bold", 25))
lbl1.place(x =868, y = 24)

lbl2 = Label(win, text = "make your own space", fg = "black",bg =   'white', font = ("Georgia", 10))
lbl2.place(x =945, y = 70)




firstname = Label(win, text= "First Name", fg = "black",bg = 'white', font =("Open Sans",9))
firstname.place(x =780, y = 199)

f1 = Entry(win, width = 29 )
f1.place(x = 782, y = 222)

lastname = Label(win, text= "Last Name", fg = "black", bg ="white", font = ("Open Sans", 9))
lastname.place(x =1023, y = 199)

l1 = Entry(win, width = 29)
l1.place(x = 1021, y = 222)

email = Label(win, text= "Email", fg = "black", bg="white", font =("Open Sans", 9))
email.place(x =780, y = 303)

e1 = Entry(win, width = 29)
e1.place(x=782, y = 326)

Gender = Label(win, text= "Gender", fg = "black", bg ="white", font = ("Open Sans", 9))
Gender.place(x =1023, y = 303)

# lblg = tk.Label(win, text = "Select an option from the dropdown menu:")
# lblg.place( x= 1023, y = 330)

# instruction = tk.Label(win, text = "Click the dropdown and make a selection.")
# instruction.pack()

selected_option  = tk.StringVar()
dropdown = tk.OptionMenu(win, selected_option, "Male", "Female")
dropdown.place(x = 1023, y = 326)

dropdown.config(bg  = "white")





username = Label(win, text = "Username", fg = "black", bg = "white", font = ("open sans", 9))
username.place(x = 780, y =407 )
 
u1  = Entry(win, width = 29)
u1.place(x = 782, y =430 ) 


age = Label(win, text = "Age", fg = "black", bg = "white", font = ("open sans", 9))
age.place( x= 1023, y = 407)

sel_option = tk.StringVar()
dpdown = tk.OptionMenu(win, sel_option,"1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19","20")
dpdown.place(x = 1023, y = 426)
dpdown.config(bg = "white")




password = Label(win,  text = "Password" ,fg = "black", bg = "white", font = ("open sans", 9))
password.place(x= 780, y = 511)

p1 = Entry(win, width = 29)
p1.place(x = 782, y = 534)

position = Label(win, text = "Position", fg = "black", bg = "white", font = ("open sans", 9))
position.place(x= 1023, y = 511)

positon_option = tk.StringVar()
ddown = tk.OptionMenu(win, positon_option, "Staff", "Manager" )
ddown.place(x = 1023, y =535 )
ddown.config(bg = "white")

confirm_pass = Label(win, text ="Confirm Password", fg = "black", bg = "white", font = ("open sans", 9))
confirm_pass.place(x= 780, y = 615)

c1 = Entry(win, width = 29)
c1.place(x = 782, y = 638)

ph_number =Label(win, text= "Phone Number", fg = "black", bg = "white", font = ("open sans", 9))
ph_number.place(x = 1023, y = 615)

ph1 = Entry(win, width = 29)
ph1.place(x = 1023, y =638 )


reg_btn = Button(win, text = "        Register Now       ",fg ="black", bg = "#FFC125", font = ("open sans",10))
reg_btn.place(x = 938, y = 730)



win.mainloop()