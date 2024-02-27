from tkinter import *
from PIL import ImageTk, Image
import sqlite3
from tkinter import messagebox

win=Tk()
win.configure(bg="#FECE2F",width=700,height=100)
win.title("Update") #to change the tilte we used .title
win.geometry("1624x962")

with open('currentSlot.txt', 'r') as currentSlot:
        slotInFile = currentSlot.read(2)
def submit():
    '''updates the record of the customer in selected slot'''
    try:

        entryList = [nameValue.get(), phoneNumValue.get(), vehicle_noValue.get(), parkingSlotValue.get()] 

        assert True in map(lambda x: bool(x), entryList), 'Incomplete entry' #truth value of every items in the entryList must be True
        
        conn = sqlite3.connect('parkingManagement.db')
        parking_slot = parkingSlotValue.get()

        # Assures the the name of the parking slot is an alphabet followed by a number
        assert len(parking_slot) == 2 and parking_slot[0].isalpha() and parking_slot[1].isnumeric(), 'There must be a letter followed by a number while naming a parking slot'

        # Further assures the name of the parking slot is correct
        assert parking_slot[0] in ['A','B','C','D'], f'No {parking_slot[0]} in name of parking_slot'
        if parking_slot[0] in ['A','B','C']:
             assert int(parking_slot[1]) in range(1,7), 'No numbers more than 6 after A, B OR C'
        if parking_slot[0] == 'D':
            assert int(parking_slot[1]) in range(1,11), 'No numbers more than 10 after D'

        # Check if the entered parking slot is occupied or not
        conn = sqlite3.connect('parkingManagement.db')
        cursor = conn.cursor()
        cursor.execute('''SELECT ParkingSlotName FROM Customer''')
        occupiedSlotList = cursor.fetchall()[0]
        occupiedSlotList = list(occupiedSlotList)
        if slotInFile in occupiedSlotList:
            occupiedSlotList.remove(slotInFile)
        assert parking_slot not in occupiedSlotList,f'{parking_slot} is currently occupied'
        conn.close()

        #if all the assertions are passed, then the updation of the record occurs
        conn = sqlite3.connect('parkingManagement.db')
        c = conn.cursor()
        c.execute(f'''
            UPDATE Customer SET
                CustomerName = :name,
                PhoneNumber = :phone,
                VehicleNumber = :vehicle_number,
                ParkingSlotName = :parking_slot_name
            WHERE ParkingSlotName = :slot_name
            ''',
            {
                'name': nameValue.get(),
                'phone': phoneNumValue.get(),
                'vehicle_number': vehicle_noValue.get(),
                'parking_slot_name': parking_slot,
                'slot_name': slotInFile  
                })
        conn.commit()
        conn.close()
        win.destroy()
        import mainpage
    #When the assertion error occurs
    except AssertionError as e:
         messagebox.askretrycancel('Updation Error', e)
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



Vehicle_number_plate=Label(win,text="VEHICLE NUMBER PLATE",font=("Georgia",20),fg="Black",bg="#FECE2F").place(x=865,y=200)

parking_slot_id=Label(win,text="PARKING SLOT ID",font=("Georgia",20),fg="Black",bg="#FECE2F").place(x=912,y=350-75)

name=Label(win,text="NAME",font=("Georgia",20),fg="Black",bg="#FECE2F").place(x=971,y=425-75)

phone_number=Label(win,text="PHONE NUMBER",font=("Georgia",20),fg="Black",bg="#FECE2F").place(x=929,y=500-75)




vehicle_noValue=Entry(win,text="",width=40)
vehicle_noValue.place(x=1240,y=210)

parkingSlotValue=Entry(win,text="",width=40)
parkingSlotValue.place(x=1240,y=355-75)

nameValue=Entry(win,text="",width=40)
nameValue.place(x=1240,y=430-75)

phoneNumValue=Entry(win,text="",width=40)
phoneNumValue.place(x=1240,y=510-75)


# inserts the values to be updated in their respective entry boxes individually
conn = sqlite3.connect('parkingManagement.db')
with open('currentSlot.txt') as currentSlot:
    slotInFile = currentSlot.read(2)
c = conn.cursor()
c.execute("SELECT * FROM Customer WHERE ParkingSlotName=?", (slotInFile,))
currentRecord = c.fetchone()
vehicle_noValue.insert(0,currentRecord[6])
nameValue.insert(0,currentRecord[1])
parkingSlotValue.insert(0,currentRecord[8])

phoneNumValue.insert(0,currentRecord[4])

conn.commit()
conn.close()

Submit=Button(win,text="SUMBIT",font=("Georgia",20),fg="Black",bg="#FECE2F",command = submit)
Submit.place(x=1250,y=700)

win.mainloop()