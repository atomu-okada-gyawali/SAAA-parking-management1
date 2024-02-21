from tkinter import *
import sqlite3
from PIL import ImageTk, Image
import ctypes
from time import strftime
ctypes.windll.shcore.SetProcessDpiAwareness(1)

root = Tk()
root.geometry('1635x962')
root.title('Dashboard')
def time():
    '''This function is event handler for clockLabel in csFrame of rightFrame, which updates the label as the time according to the system clock in real time'''
    string = strftime('%H: %M: %S %p')
    clock.config(text = string)
    clock.after(1000, time)


def select(slot):
    '''This function is event handler for all slot buttons in their respective parkingArea in parkingFrame, which does the following:
    1.highlights the text of the button with light blue color when selected and turns the color of the text into black when deselected
    2. activates the buttons in the buttonFrame when one of the slot buttons is clicked and disables the buttons when slot button is deselected'''
    if slot.cget('fg') == 'lightBlue':
        slot.config(fg = 'SystemButtonText')
        for button in buttonFrame.winfo_children():
            button.config(bg = 'white',state = DISABLED)
    else:
        for parkingArea in parkingFrame.winfo_children():
            for oneSlot in parkingArea.winfo_children():
                oneSlot.config(fg= 'SystemButtonText')
        for button in buttonFrame.winfo_children():
            button.config(state = ACTIVE,bg = 'yellow')
            slot.config(fg = 'lightBlue')

conn = sqlite3.connect('parkingManagement.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Customer(
               CustomerID INTEGER PRIMARY KEY AUTOINCREMENT,
               CustomerName TEXT,
               ParkingSlot TEXT,
               Check_in TIMESTAMP,
               Check_out TIMESTAMP,
               PhoneNumber INTEGER,
               Overtime_duration INTEGER
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Vehicle(
               VehicleID INTEGER PRIMARY KEY AUTOINCREMENT,
               CustomerID INTEGER,
               VehicleNumber INTEGER,
               VehicleName TEXT,
               VehicleType TEXT,
               FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
)''')
conn.commit()
conn.close()

#Creates sidebar
sidebarFrame = Frame(root, width = 327, height = 962, bg = '#FBBC05')
sidebarFrame.pack(side = LEFT,fill = Y)
sidebarFrame.pack_propagate(False)

#Creates logo in the sidebar
img = ImageTk.PhotoImage(Image.open(r"main_page\logo.png"))
logo = Label(sidebarFrame, image = img)
logo.pack()

#Frame for Buttons in the sidebar
sideButtonFrame = Frame(sidebarFrame,width = 327, height = 500, bg = 'brown')
sideButtonFrame.pack()
sideButtonFrame.pack_propagate(False)

#Buttons for Sidebar----------------------------------------------
parkingButton = Button(sideButtonFrame, text = 'Dashboard', font = ('Georgia bold', 16), height = 2)
parkingButton.pack(fill = X)

optionsButton = Button(sideButtonFrame, text = 'Options', font = ('Georgia bold', 16), height = 2)
optionsButton.pack(fill = X)

currentRecordsButton = Button(sideButtonFrame, text = 'Current Records', font = ('Georgia bold', 16), height = 2)
currentRecordsButton.pack(fill = X)

statisticsButton = Button(sideButtonFrame, text = 'Statistics', font = ('Georgia bold', 16), height = 2)
statisticsButton.pack(fill = X)

logoutButton = Button(sideButtonFrame, text = 'Logout', font = ('Georgia bold', 16), height = 2)
logoutButton.pack(fill = X)
#----------------------------------------------------------------

#Creates middle Frame that contains parking areas
middleFrame = Frame(root, width = 986, height = 962, bg = 'blue')
middleFrame.pack(side = LEFT)
middleFrame.pack_propagate(False)

#Heading for parking area
paText = Label(middleFrame, text = 'PARKING AREA', font = ('Georgia bold',40))
paText.pack(pady = 20)

#Creates parking Frame (contains 4 parking Areas -D) inside middle frame
parkingFrame = Frame(middleFrame, width = 948, height = 792, bg = 'brown')
parkingFrame.pack()

#parkingAreaA Frame
parkingAreaA  = Frame(parkingFrame, bg = 'lime', padx= 50, pady = 50)
parkingAreaA.place(x = 0, y = 0)

slotA1 = Button(parkingAreaA, text = 'A1', width = 13, height = 3, command = lambda: select(slotA1))
slotA1.grid(row = 0, column = 0, padx = 10, pady = 5)
slotA2 = Button(parkingAreaA, text = 'A2', width = 13, height = 3, command = lambda: select(slotA2))
slotA2.grid(row = 0, column = 1, padx = 10, pady = 5)
slotA3 = Button(parkingAreaA, text = 'A3', width = 13, height = 3, command = lambda: select(slotA3))
slotA3.grid(row = 1, column = 0, padx = 10, pady = 5)
slotA4 = Button(parkingAreaA, text = 'A4', width = 13, height = 3, command = lambda: select(slotA4))
slotA4.grid(row = 1, column = 1, padx = 10, pady = 5)
slotA5 = Button(parkingAreaA, text = 'A5', width = 13, height = 3, command = lambda: select(slotA5))
slotA5.grid(row = 2, column = 0, padx = 10, pady = 5)
slotA6 = Button(parkingAreaA, text = 'A6', width = 13, height = 3, command = lambda: select(slotA6))
slotA6.grid(row = 2, column = 1, padx = 10, pady = 5)

#parking Area B frame
parkingAreaB  = Frame(parkingFrame, bg = 'lime', padx= 50, pady = 50)
parkingAreaB.place( x = 580, y = 0)

slotB1 = Button(parkingAreaB, text = 'B1', width = 13, height = 3, command = lambda: select(slotB1))
slotB1.grid(row = 0, column = 0, padx = 10, pady = 5)
slotB2 = Button(parkingAreaB, text = 'B2', width = 13, height = 3, command = lambda: select(slotB2))
slotB2.grid(row = 0, column = 1, padx = 10, pady = 5)
slotB3 = Button(parkingAreaB, text = 'B3', width = 13, height = 3, command = lambda: select(slotB3))
slotB3.grid(row = 1, column = 0, padx = 10, pady = 5)
slotB4 = Button(parkingAreaB, text = 'B4', width = 13, height = 3, command = lambda: select(slotB4))
slotB4.grid(row = 1, column = 1, padx = 10, pady = 5)
slotB5 = Button(parkingAreaB, text = 'B5', width = 13, height = 3, command = lambda: select(slotB5))
slotB5.grid(row = 2, column = 0, padx = 10, pady = 5)
slotB6 = Button(parkingAreaB, text = 'B6', width = 13, height = 3, command = lambda: select(slotB6))
slotB6.grid(row = 2, column = 1, padx = 10, pady = 5)

#parking Area C Frame
parkingAreaC  = Frame(parkingFrame, bg = 'lime', padx= 50, pady = 50)
parkingAreaC.place(x = 0, y = 440)

slotC1 = Button(parkingAreaC, text = 'C1', width = 13, height = 3, command = lambda: select(slotC1))
slotC1.grid(row = 0, column = 0, padx = 10, pady = 5)
slotC2 = Button(parkingAreaC, text = 'C2', width = 13, height = 3, command = lambda: select(slotC2))
slotC2.grid(row = 0, column = 1, padx = 10, pady = 5)
slotC3 = Button(parkingAreaC, text = 'C3', width = 13, height = 3, command = lambda: select(slotC3))
slotC3.grid(row = 1, column = 0, padx = 10, pady = 5)
slotC4 = Button(parkingAreaC, text = 'C4', width = 13, height = 3, command = lambda: select(slotC4))
slotC4.grid(row = 1, column = 1, padx = 10, pady = 5)
slotC5 = Button(parkingAreaC, text = 'C5', width = 13, height = 3, command = lambda: select(slotC5))
slotC5.grid(row = 2, column = 0, padx = 10, pady = 5)
slotC6 = Button(parkingAreaC, text = 'C6', width = 13, height = 3, command = lambda: select(slotC6))
slotC6.grid(row = 2, column = 1, padx = 10, pady = 5)

#parking Area D Frame (two-wheelers)
parkingAreaD = Frame(parkingFrame, bg = 'lime', padx= 50, pady = 67)
parkingAreaD.place(x = 509, y =440)

slotD1 = Button(parkingAreaD, text = 'D1', width = 6, height = 4, command = lambda: select(slotD1))
slotD1.grid(row = 0, column = 0, padx = 5, pady = 8)
slotD2 = Button(parkingAreaD, text = 'D2', width = 6, height = 4, command = lambda: select(slotD2))
slotD2.grid(row = 0, column = 1, padx = 5, pady = 8)
slotD3 = Button(parkingAreaD, text = 'D3', width = 6, height = 4, command = lambda: select(slotD3))
slotD3.grid(row = 0, column = 2, padx = 5, pady = 8)
slotD4 = Button(parkingAreaD, text = 'D4', width = 6, height = 4, command = lambda: select(slotD4))
slotD4.grid(row = 0, column = 3, padx = 5, pady = 8)
slotD5 = Button(parkingAreaD, text = 'D5', width = 6, height = 4, command = lambda: select(slotD5))
slotD5.grid(row = 0, column = 4, padx = 5, pady = 8)
slotD6 = Button(parkingAreaD, text = 'D6', width = 6, height = 4, command = lambda: select(slotD6))
slotD6.grid(row = 1, column = 0, padx = 5, pady = 8)
slotD7 = Button(parkingAreaD, text = 'D7', width = 6, height = 4, command = lambda: select(slotD7))
slotD7.grid(row = 1, column = 1, padx = 5, pady = 8)
slotD8 = Button(parkingAreaD, text = 'D8', width = 6, height = 4, command = lambda: select(slotD8))
slotD8.grid(row = 1, column = 2, padx = 5, pady = 8)
slotD9 = Button(parkingAreaD, text = 'D9', width = 6, height = 4, command = lambda: select(slotD9))
slotD9.grid(row = 1, column = 3, padx = 5, pady = 8)
slotD10 = Button(parkingAreaD, text = 'D10', width = 6, height = 4, command = lambda: select(slotD10))
slotD10.grid(row = 1, column = 4, padx = 5, pady = 8)

#Creates rightmost Frame
rightFrame = Frame(root, width = 325, height = 962, bg = 'pink')
rightFrame.pack(side = LEFT, fill = BOTH)
rightFrame.pack_propagate(False)

#Creates frame at the top in rightFrame, which contains the clock and the available slots
csFrame = Frame(rightFrame, width = 292, height = 200 )
csFrame.pack(pady = 30)
csFrame.pack_propagate(False)

#Clock
clockLabel = Label(csFrame, text = 'Current Time', font = ('Georgia', 10))
clockLabel.pack(pady = 10)

clock = Label(csFrame, font = ('Georgia', 15))
clock.pack()
#Calls time so that the clockLabel updates every second that displays the current time
time()

#No. of available slots
spaceLabel = Label(csFrame, text = 'Availabe Slots', font = ('Georgia', 10))
spaceLabel.pack(pady = 20)

space = Label(csFrame,text = '1', font = ('Georgia', 15))
space.pack()

# 2nd Frame in the rightFrame, which displays the attributes of the currently used selected slots--------------------------------------------------------------------------------------------------------------------------------
infoFrame = Frame(rightFrame, width = 292, height = 253)
infoFrame.pack(pady = 30)
infoFrame.pack_propagate(False)

info1Frame = Frame(infoFrame, bg = 'gold')
info1Frame.pack(pady = 20)

slotLabel = Label(info1Frame, text = 'Slot: ', font = ('Georgia', 13))
slotLabel.grid(row = 0, column = 0)

slotValue = Label(info1Frame, text = 'A1', font = ('Georgia', 13))
slotValue.grid(row = 0, column = 1)

info2Frame = Frame(infoFrame)
info2Frame.pack()

nameLabel = Label(info2Frame, text = 'Name: ')
nameLabel.grid(row = 0, column = 0)

nameValue = Label(info2Frame, text = 'Sailesh Ranabhat')
nameValue.grid(row = 0, column = 1)

vNoLabel = Label(info2Frame, text = 'Vehicle No: ')
vNoLabel.grid(row = 1, column = 0)

vNoValue = Label(info2Frame, text = 'Province X AB 0123 X')
vNoValue.grid(row = 1, column = 1)

vNameLabel = Label(info2Frame, text = 'Vehicle Name: ')
vNameLabel.grid(row = 2, column = 0)

vNameValue = Label(info2Frame, text = 'white, Maruti')
vNameValue.grid(row = 2, column = 1)

phoneLabel = Label(info2Frame, text = 'Phone No.: ')
phoneLabel.grid(row = 3, column = 0)

phoneValue = Label(info2Frame, text = '981111111111')
phoneValue.grid(row = 3, column = 1)

ciLabel = Label(info2Frame, text = 'Check-in: ')
ciLabel.grid(row = 4, column = 0)

ciValue = Label(info2Frame, text = '')
ciValue.grid(row = 4, column = 1)

coLabel = Label(info2Frame, text = 'Check-out: ')
coLabel.grid(row = 5, column = 0)

coValue = Label(info2Frame, text = '')
coValue.grid(row = 5, column = 1)
#------------------------------------------------------------------------------------------------------------------------------------

#3rd Frame of the righFrame, which contains the buttons for CRUD and billing of the selected slot
buttonFrame = Frame(rightFrame, width = 292, height = 417 )
buttonFrame.pack(pady = 30)
buttonFrame.pack_propagate(False)

addButton = Button(buttonFrame, state = DISABLED, text = 'Add Vehicle', width = 20, height = 2, bg = 'white')
addButton.pack(pady = 15)

updateButton = Button(buttonFrame, state = DISABLED, text = 'Update Slot', width = 20, height = 2, bg = 'white')
updateButton.pack(pady = 15)

deleteButton = Button(buttonFrame, state = DISABLED, text = 'Delete Vehicle', width = 20, height = 2, bg = 'white')
deleteButton.pack(pady = 15)

billButton = Button(buttonFrame, state = DISABLED, text = 'Bill', width = 20, height = 2, bg = 'white')
billButton.pack(pady = 15)
root.mainloop()