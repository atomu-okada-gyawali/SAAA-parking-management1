#different import modules are used to import the necessary objects inside the tkinter window
from tkinter import*
import tkinter as tk
from PIL import Image, ImageTk #this module is used to import the image inside the window 
import tkinter.ttk as ttk
import sqlite3

b = Tk()#creating the tkinter window 
b.title("Bill")#title of the window 
b.geometry("1624x962")#setting the geometry of the window
b.config(bg = "#FECE2F")#setting the background color of the window




def open_image(file_path):
    '''
    this function is created in order to open the image or import image inside the window
    
    '''
    image = Image.open(file_path)
    return ImageTk.PhotoImage(image)

image_path = ("SAAA-parking-management1\\resources\\image_billPage.png") #here is the image path and also the image format should me mentioned 
#in order for it to be imported successfully

image = open_image(image_path)
label = tk.Label(b, image=image,bg = "white", width = 742, height = 962)#background and geometry of image is changed according to the window 
label.pack() #pack is one of the method to adjust image location inside the tkinter window
label.place( x = 820, y = 0 )

#the image path for next image 
image_path = ("SAAA-parking-management1\\resources\\logo_billPage.png")
img = open_image(image_path)
lblll = tk.Label(b, image = img, bg = "#FECE2F", width = 246, height = 61.38)
lblll.pack()
lblll.place(anchor ="nw", x= 23, y = 32)





#creating text and adjusting text inside the window using labal and place methods 

lbl1 = Label(b, text = "Amount :", fg= "black", bg ="#FECE2F", font = ("Georgia ", 14 ))
lbl1.place(x =132, y = 208 )


lbl2 = Label(b, text = "VEHICLE TYPE :", fg = "black", bg = "#FECE2F", font = ("georgia", 14))
lbl2.place(x =120 , y = 302)

lbl3 = Label(b, text= "VEHICLE NAME :", fg = "black", bg = "#FECE2F", font = ("Georgia ", 14))
lbl3.place(x =116, y = 399)

lbl4 = Label(b, text= "CHECK IN TIME :", fg = "black", bg = "#FECE2F", font = ("Georgia ", 14))
lbl4.place(x =117 , y = 487)

lbl5 = Label(b, text = "CHECK OUT TIME :", fg = "black", bg = "#FECE2F", font = ("Georgia", 14))
lbl5.place(x = 108, y = 571)

lbl6 = Label(b, text = "VEHICLE NUMBER PLATE :", fg = "black", bg = "#FECE2F", font = ("Georgia ", 14))
lbl6.place(x =71, y = 672 )

lbl7 = Label(b, text = "PARKING TIME :", fg = "black", bg = "#FECE2F", font = ("Georgia", 14))
lbl7.place(x = 532 , y = 208)

lbl8 = Label(b, text ="OVER TIME :", fg = "black", bg = "#FECE2F", font = ("georgia", 14) )
lbl8.place(x = 550, y = 297)

lbl9 = Label(b, text = "NAME :", fg = "black", bg = "#FECE2F", font = ("georgia", 14))
lbl9.place(x =576, y = 394)

lbll = Label(b, text= "DATE :", fg = "black", bg = "#FECE2F", font = ("georgia ", 14))
lbll.place(x =577, y = 487 )

lbll1 = Label(b, text = "DURATION :", fg = "black", bg = "#FECE2F", font = ("georgia", 14))
lbll1.place(x =553, y = 571)

lbll2 = Label( b, text = "PARKING RATE :", fg = "black", bg = "#FECE2F", font = ("georgia ", 14))
lbll2.place(x = 533, y = 672 )

vehicleidvalue = Label(b, text = "", fg= "black", bg ="#FECE2F", font = ("Georgia ", 14 ))
vehicleidvalue.place(x =300, y = 208 )

vehicleTypeValue = Label(b, text ='unchi',bg = "#FECE2F", font = ("georgia",14))
vehicleTypeValue.place(x = 300, y = 302)

vehiclenameValue = Label(b, text ='two-wheeler',bg = "#FECE2F", font = ("georgia",14))
vehiclenameValue.place(x = 300, y = 399)

checkintimeValue = Label(b, text ='two-wheeler',bg = "#FECE2F", font = ("georgia",14))
checkintimeValue.place(x = 300, y = 487)

checkouttimeValue = Label(b, text ='two-wheeler',bg = "#FECE2F", font = ("georgia",14))
checkouttimeValue.place(x = 300, y = 571)

vehiclenumberplateValue = Label(b, text ='',bg = "#FECE2F", font = ("georgia",14))
vehiclenumberplateValue.place(x = 320, y = 672)

parkingtimevalue = Label(b, text ='two-wheeler',bg = "#FECE2F", font = ("georgia",14))
parkingtimevalue.place(x = 700, y = 208)


overtimeValue = Label(b, text ='two-wheeler',bg = "#FECE2F", font = ("georgia",14))
overtimeValue.place(x = 700, y = 297)

NameValue = Label(b, text ='two-wheeler',bg = "#FECE2F", font = ("georgia",14))
NameValue.place(x = 700, y = 394)

DateValue = Label(b, text ='two-wheeler',bg = "#FECE2F", font = ("georgia",14))
DateValue.place(x = 700, y = 487)

Durationvalue= Label(b, text = "DURATION :", fg = "black", bg = "#FECE2F", font = ("georgia", 14))
Durationvalue.place(x = 700, y = 571)

parkingratevalue= Label( b, text = "PARKING RATE :", fg = "black", bg = "#FECE2F", font = ("georgia ", 14))
parkingratevalue.place(x = 700, y = 672 )


with open('currentSlot.txt') as currentSlot:
    cSlot = currentSlot.read(2)
conn = sqlite3.connect('parkingManagement.db')
cursor = conn.cursor()
cursor.execute('SELECT * FROM Customer WHERE ParkingSlotName = (?)',(cSlot,))
currentRecord = cursor.fetchone()
vehicleidvalue.config(text= currentRecord[0])
vehicleTypeValue.config(text = currentRecord[9])
vehiclenameValue.config(text = currentRecord[1])
checkintimeValue.config(text = currentRecord[2])
checkouttimeValue.config(text = currentRecord[3])
vehiclenumberplateValue.config(text = currentRecord[7])
overtimeValue.config(text = currentRecord[5])
NameValue.config(text = currentRecord[6])
# DateValue.config(text = currentRecord[])
Durationvalue.config(text = currentRecord[8])
# parkingratevalue.config(text = currentRecord[9])
conn.commit()
conn.close()
    

#button used to insert the clickable button inside the window and setting the background, foreground and the fonts of the text 
total_btn = Button(b, text= "   TOTAL   ", fg = "black", bg  = "#FECE2F", font = ("georgia",18))
total_btn.place(x = 360, y = 750)
b.mainloop()#mainloop used to display the window 
