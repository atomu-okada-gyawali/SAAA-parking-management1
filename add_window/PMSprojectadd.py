from tkinter import*
import tkinter as tk
import ast

from PIL import Image,ImageTk
window=Tk()
window.title("add window")
#setting up window size and background
window.config(bg="#FECE2F")
window.geometry("1500x1500")
window.resizable(0,1)

box=Frame(bg="white")
box.place(width=780,height=800)

#importing image and logo on our window
img=PhotoImage(file="C:\\Users\\ASUS\\Downloads\\taxi-add-image.png")
label=tk.Label(window,image=img,bg="white",width=700,height=700)
PhotoImage(file="C:\\Users\\ASUS\\Downloads\\taxi-add-image.png")
label.place(x=30,y=80)

logo=PhotoImage(file=r"C:\algorithms and programs\saalogo.png")
lbl=tk.Label(window,image=logo,bg="white",width=246,height=62)
lbl.place(x=50,y=26)



username_label=Label(text="Name  :",bg="#FECE2F",fg="black",font=("Georgia",20))
username_label.place(x=875,y=164)

username_Entry=Entry(window,width=50)
username_Entry.place(x=1120,y=160,height=41)


Phonenum_label=Label(text="Phone Number  :",bg="#FECE2F",fg="black",font=("Georgia",20))
Phonenum_label.place(x=830,y=253)

Phonenum_Entry=Entry(window,width=50)
Phonenum_Entry.place(x=1120,y=250,height=41)


Vehiclenum_label=Label(text="Vehicle Number Plate  :",bg="#FECE2F",fg="black",font=("Georgia",20))
Vehiclenum_label.place(x=795,y=349)

Vehiclenum_Entry=Entry(window,width=50)
Vehiclenum_Entry.place(x=1120,y=342,height=41)


Vehicletype_label=Label(text="Vehicle Type  :",bg="#FECE2F",fg="black",font=("Georgia",20))
Vehicletype_label.place(x=840,y=434)

Vehicletype_Entry=Entry(window,width=50)
Vehicletype_Entry.place(x=1120,y=432,height=41)


Vehiclename_label=Label(text="Vehicle Name  :",bg="#FECE2F",fg="black",font=("Georgia",20))
Vehiclename_label.place(x=830,y=527)

Vehiclename_Entry=Entry(window,width=50)
Vehiclename_Entry.place(x=1120,y=522,height=41)


Duration_label=Label(text="Duration  :",bg="#FECE2F",fg="black",font=("Georgia",20))
Duration_label.place(x=862,y=619)

Duration_Entry=Entry(window,width=50)
Duration_Entry.place(x=1120,y=613,height=41)



#creating a submit button to store all the data entry

btn=Button(window,text="SUBMIT",bg="#FECE2F",fg="black",font=("Georgia",24))
btn.place(x=1000,y=715,width=141,height=50)

window.mainloop()