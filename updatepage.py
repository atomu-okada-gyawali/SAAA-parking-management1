from tkinter import *
from PIL import ImageTk, Image
import sqlite3


win=Tk()
win.configure(bg="yellow",width=700,height=100)
win.title("Update") #to change the tilte we used .title
# win.iconbitmap("icon.ico") # to change the icon
win.geometry("1624x962")
with open('currentSlot.txt', 'r') as currentSlot:
        slotInFile = currentSlot.read(2)
def submit():
    conn = sqlite3.connect('parkingManagement.db')
    c = conn.cursor()
    c.execute(f'''
        UPDATE Customer SET
            CustomerName = :name,
            PhoneNumber = :phone,
            VehicleNumber = :vehicle_number,
            VehicleType = :vehicle_type,
            ParkingSlotName = :parking_slot_name
        WHERE ParkingSlotName = :slot_name
        ''',
        {
            'name': nameValue.get(),
            'phone': phoneNumValue.get(),
            'vehicle_number': vehicle_noValue.get(),
            'vehicle_type': vehicleTypeValue.get(),
            'parking_slot_name': parkingSlotValue.get(),
            'slot_name': slotInFile  # Assuming slotInFile is a variable
            })
    conn.commit()
    conn.close()
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


Vehicle_number_plate=Label(win,text="VEHICLE NUMBER PLATE",font=("Georgia",20),fg="Black",bg="Yellow").place(x=865,y=200)

vehicle_type=Label(win,text="VEHICLE TYPE",font=("Georgia",20),fg="Black",bg="Yellow").place(x=927,y=275)

parking_slot_id=Label(win,text="PARKING SLOT ID",font=("Georgia",20),fg="Black",bg="Yellow").place(x=912,y=350)

name=Label(win,text="NAME",font=("Georgia",20),fg="Black",bg="Yellow").place(x=971,y=425)

phone_number=Label(win,text="PHONE NUMBER",font=("Georgia",20),fg="Black",bg="Yellow").place(x=929,y=500)




vehicle_noValue=Entry(win,text="",width="40")
vehicle_noValue.place(x=1240,y=210)

vehicleTypeValue=Entry(win,text="",width="40")
vehicleTypeValue.place(x=1240,y=290)

parkingSlotValue=Entry(win,text="",width="40")
parkingSlotValue.place(x=1240,y=355)

nameValue=Entry(win,text="",width="40")
nameValue.place(x=1240,y=430)

phoneNumValue=Entry(win,text="",width="40")
phoneNumValue.place(x=1240,y=510)



conn = sqlite3.connect('parkingManagement.db')
with open('currentSlot.txt') as currentSlot:
    slotInFile = currentSlot.read(2)
c = conn.cursor()
c.execute("SELECT * FROM Customer WHERE ParkingSlotName=?", (slotInFile,))
currentRecord = c.fetchone()
vehicle_noValue.insert(0,currentRecord[7])
nameValue.insert(0,currentRecord[1])
parkingSlotValue.insert(0,currentRecord[10])
vehicleTypeValue.insert(0,currentRecord[9])
phoneNumValue.insert(0,currentRecord[4])

conn.commit()
conn.close()

Submit=Button(win,text="SUMBIT",font=("Georgia",20),fg="Black",bg="Yellow",command = submit)
Submit.place(x=1250,y=700)

win.mainloop()