from tkinter import *
import tkinter.ttk as ttk
import tkinter as tk
from PIL import Image, ImageTk



root = Tk()
root.title("First Page")
root.geometry("1625x950")
root.config (bg = "white")

def goto_registration():
    root.destroy()
    import registrationpage




frame1 = Frame(root, height = 497,bg = "white", width = 700)
frame1.pack(side = "right")
frame1.place(anchor =CENTER, x =800 , y = 420)

def open_image(file_path):
    image = Image.open(file_path)
    return ImageTk.PhotoImage(image)

image_path = ("SAAA-parking-management1\\resources\\image_firstpage.png")

image = open_image(image_path)
label = tk.Label(root, image=image,bg = "white", width = 600, height = 650)
label.pack()
label.place(anchor = CENTER, x =790, y = 400 )


image_path = ("SAAA-parking-management1\\resources\\logo_firstpage.png")

img2 = open_image(image_path)
label2 = tk.Label(root,image = img2,bg = "white",width = 246, height = 61.38 )
label2.pack()
label2.place(anchor = "nw", x = 25, y = 15)








lbl1 = Label(text = "Welcome to SAAA", bg = "white", fg = "black", font = ("Georgia Bold",29 ))
lbl1.place(x =600, y = 30 )

lbl2 = Label(root, text = "make your own space", bg = "white", fg = "black", font = ("Georgia", 12))
lbl2.place(x =692, y = 85 )

log_btn = Button(root, text = "          LOGIN          ", fg = "black", bg = "#FFC125", font = ("Georgia", 14))
log_btn.place(x =700, y = 660 )

signup_btn = Button(root, text = "         SIGNUP         ", bg = "#FFC125", fg = "black", font = ("Georgia",14),command = goto_registration)
signup_btn.place(x = 700, y=740)






root.mainloop()