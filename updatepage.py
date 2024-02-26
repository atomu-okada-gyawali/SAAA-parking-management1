from tkinter import *
from PIL import ImageTk, Image


win=Tk()
win.configure(bg="yellow",width=700,height=100)
win.title("Update") #to change the tilte we used .title
# win.iconbitmap("icon.ico") # to change the icon
win.geometry("1624x962")


update=Frame(win,bg="white",width=812,height=962)
update.place(x=0,y=0)

img = Image.open("SAAA-parking-management1\\resources\\logo_updatepage.jpg")
backg = ImageTk.PhotoImage(img)

photoLabel = Label(win, image=backg,bg="white")
photoLabel.place(x=36, y=33)


img1 = Image.open("SAAA-parking-management1\\resources\\image_updatepage.jpg")
backg1 = ImageTk.PhotoImage(img1)

photoLabel1 = Label(win, image=backg1,bg="white")
photoLabel1.place(x=102, y=169)




Vehicle_id=Label(win,text="VEHICLE ID",font=("Georgia",20),fg="Black",bg="#FECE2F").place(x=940,y=125)

Vehicle_number_plate=Label(win,text="VEHICLE NUMBER PLATE",font=("Georgia",20),fg="Black",bg="#FECE2F").place(x=865,y=200)

vehicle_type=Label(win,text="VEHICLE TYPE",font=("Georgia",20),fg="Black",bg="#FECE2F").place(x=927,y=275)

parking_slot_id=Label(win,text="PARKING SLOT ID",font=("Georgia",20),fg="Black",bg="#FECE2F").place(x=912,y=350)

name=Label(win,text="NAME",font=("Georgia",20),fg="Black",bg="#FECE2F").place(x=971,y=425)

phone_number=Label(win,text="PHONE NUMBER",font=("Georgia",20),fg="Black",bg="#FECE2F").place(x=929,y=500)

time=Label(win,text="TIME",font=("Georgia",20),fg="Black",bg="#FECE2F").place(x=975,y=575)

Sumbit=Button(win,text="SUMBIT",font=("Georgia",20),fg="Black",bg="#FECE2F").place(x=1250,y=700)


Vehicle_id=Entry(win,text="VEHICLE ID",width="40").place(x=1240,y=125)

Vehicle_number_plate=Entry(win,text="VEHICLE NUMBER",width="40").place(x=1240,y=210)

vehicle_type=Entry(win,text="VEHICLE TYPE",width="40").place(x=1240,y=290)

parking_slot_id=Entry(win,text="parking slot ID",width="40").place(x=1240,y=355)

name=Entry(win,text="NAME",width="40").place(x=1240,y=430)

phone_number=Entry(win,text="PHONE NUMBER",width="40").place(x=1240,y=510)

time=Entry(win,text="TIME",width="40").place(x=1240,y=585)








win.mainloop()