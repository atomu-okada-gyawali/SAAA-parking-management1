from tkinter import *
import sqlite3
from PIL import ImageTk, Image
from time import strftime
from tkinter import messagebox

#initiating currentSlot.txt which stores the recently clicked slot
with open('currentSlot.txt','w') as currentSlot:
        currentSlot.write('')

root = Tk()
root.geometry('1635x962')
root.title('Dashboard')

def time():
    '''This function is event handler for clockLabel in csFrame of rightFrame, which updates the label as the time according to the system clock in real time'''
    string = strftime('%H: %M: %S %p')
    clock.config(text = string)
    clock.after(1000, time)

def goto_billpage():
        '''go to add page'''
        root.destroy()
        import billpage
        
def goto_addpage():
        '''go to add page'''
        root.destroy()
        import add_page

def goto_updatepage():
        '''go to update page'''
        root.destroy()
        import updatepage

def goto_optionspage():
        '''go to options page'''
        root.destroy()
        import optionpage

def goto_firstpage():
        log_out = messagebox.askquestion('Log out Confirmation','Are you sure you want to log out?')
        if log_out == 'yes':
                root.destroy()
                import firstpage
                with open('currentlyLoggedUser.txt', 'w') as currentUser:
                        currentUser.write('')

# def info_retreive():
#         conn = sqlite3.connect('parkingManagement.db')
#         c = conn.cursor()
#         c.execute(f'SELECT * FROM employee WHERE ParkingSlotName = {slotInFile}')
#         current_record = c.fetchone()
#         print(current_record)
#         conn.close()

def delete():
        with open('currentSlot.txt', 'r') as currentSlot:
                        slotInFile = currentSlot.read()
        answer = messagebox.askquestion("Delete Record?", f"Do you want to delete record from {slotInFile}?")
        if answer == 'yes':
                conn = sqlite3.connect('parkingManagement.db')
                cursor = conn.cursor()
                cursor.execute('''DELETE FROM Customer WHERE ParkingSlotName = (?)''',(slotInFile,))
                conn.commit()
                conn.close()
                for subparkingFrame in parkingFrame.winfo_children():
                        for cSlot in subparkingFrame.winfo_children():
                                if cSlot.cget('text') == slotInFile:
                                        cSlot.config(bg = 'SystemButtonFace')
                                        conn = sqlite3.connect('parkingManagement.db')
                                        cursor = conn.cursor()
                                        cursor.execute("""SELECT * FROM customer""")
                                        usedSlots = len(cursor.fetchall())
                                        space.config(text = f'{28-usedSlots}')
                                        conn.close()
                                        select(cSlot)


        else:
                pass
        
        
        
def select(slot):
        '''this function writes the name of the currently clicked slot button in the currentSlot.txt, but writes empty string when the slotButton is clicked twice indicating the deselection'''
        with open('currentSlot.txt', 'r') as currentSlot:
                slotInFile = currentSlot.read(2)

                

        if slotInFile != slot.cget('text') or slotInFile == '':
                with open('currentSlot.txt', 'w') as currentSlot:
                        currentSlot.write(slot.cget('text'))
                conn = sqlite3.connect('parkingManagement.db')
                c = conn.cursor()
                with open('currentSlot.txt', 'r') as currentSlot:
                        slotInFile = currentSlot.read()
                        c.execute('SELECT * FROM Customer WHERE ParkingSlotName = (?)',(slotInFile,))
                        current_record = c.fetchone()
                        if current_record != None:
                                nameValue.config(text = current_record[1])
                                ciValue.config(text = current_record[2])
                                coValue.config(text = current_record[3])
                                phoneValue.config(text=current_record[4])
                                vNoValue.config(text=current_record[6])
                                vNameValue.config(text = current_record[7])
                                slotValue.config(text = current_record[8])
                                conn.close()

                                addButton.config(state = DISABLED, bg = '#FECE2F')
                                updateButton.config(state = NORMAL, bg = '#FECE2F')
                                deleteButton.config(state = NORMAL, bg = '#FECE2F')
                                billButton.config(state = NORMAL, bg = '#FECE2F')
                        else:
                                nameValue.config(text = "")
                                ciValue.config(text = "")
                                coValue.config(text = "")
                                phoneValue.config(text="")
                                vNoValue.config(text="")
                                vNameValue.config(text = "")
                                slotValue.config(text = slot.cget('text'))

                                addButton.config(state = NORMAL, bg = '#FECE2F')
                                updateButton.config(state = DISABLED, bg = '#FECE2F')
                                deleteButton.config(state = DISABLED, bg = '#FECE2F')
                                billButton.config(state = DISABLED, bg = '#FECE2F')

        elif slotInFile == slot.cget('text'):
                with open('currentSlot.txt', 'w') as currentSlot:
                        currentSlot.write('')
                nameValue.config(text = "")
                ciValue.config(text = "")
                coValue.config(text = "")
                phoneValue.config(text="")
                vNoValue.config(text="")
                vNameValue.config(text = "")
                slotValue.config(text = "")
                addButton.config(state = DISABLED, bg = 'white')
                updateButton.config(state = DISABLED, bg = 'white')
                deleteButton.config(state = DISABLED, bg = 'white')
                billButton.config(state = DISABLED, bg = 'white')

#initiating database accoriding to the er diagram
conn = sqlite3.connect('parkingManagement.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Customer(
               CustomerID INTEGER PRIMARY KEY AUTOINCREMENT,
               CustomerName TEXT NOT NULL,
               Check_in TEXT NOT NULL,
               Check_out TEXT NOT NULL,
               PhoneNumber INTEGER NOT NULL,
               Duration INTEGER NOT NULL,
               VehicleNumber INTEGER NOT NULL,
               VehicleName TEXT NOT NULL,
               ParkingSlotName TEXT NOT NULL,
               VehicleType TEXT NOT NULL
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Bill(
               BillID INTEGER PRIMARY KEY AUTOINCREMENT,
               CustomerID INTEGER,
               Amount INTEGER,
               UserID INTEGER,
               FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS Bill_User(
               BillID INTEGER,
               UserID INTEGER,
               FOREIGN KEY (BillID) REFERENCES Bill(BillID),
               FOREIGN KEY (UserID) REFERENCES User(UserID)
)''')

conn.commit()
conn.close()



#Creates sidebar
sidebarFrame = Frame(root, width = 327, height = 962, bg = '#FECE2F')
sidebarFrame.pack(side = LEFT,fill = Y)
sidebarFrame.pack_propagate(False)

#Creates logo in the sidebar
img = ImageTk.PhotoImage(Image.open("SAAA-parking-management1\\resources\\logo_mainpage.png"))
logo = Label(sidebarFrame, image = img)
logo.pack()

#Frame for Buttons in the sidebar
sideButtonFrame = Frame(sidebarFrame,width = 327, height = 300, bg = '#FECE2F')
sideButtonFrame.pack()
sideButtonFrame.pack_propagate(False)

loggerInfoFrame = Frame(sidebarFrame,width = 327, height = 100,bg = '#FECE2F')
loggerInfoFrame.pack()
loggerInfoFrame.pack_propagate(False)

#Frame for currently logged in info
loggedInInfo = Label(loggerInfoFrame, text='Currently logged in as ', bg = '#FECE2F', font = ('Georgia', 13))
loggedInInfo.pack()
with open('currentlyLoggedUser.txt','r') as currentUser:
        cUser = currentUser.read()
conn = sqlite3.connect('parkingManagement.db')
cursor = conn.cursor()
cursor.execute('''SELECT * FROM User WHERE UserID = (?)''',(cUser,))
loggedUser = cursor.fetchone()[3]
print(loggedUser)
loggedInInfoValue = Label(loggerInfoFrame,text = str(loggedUser), bg = '#FECE2F', font = ('Georgia bold', 17))
loggedInInfoValue.pack()
#Buttons for Sidebar----------------------------------------------
parkingButton = Button(sideButtonFrame, text = 'Dashboard', font = ('Georgia bold', 16), height = 2, relief = FLAT, bg = '#FECE2F')
parkingButton.pack(fill = X)

# optionsButton = Button(sideButtonFrame, text = 'Options', font = ('Georgia bold', 16), height = 2, relief = FLAT, bg = '#FECE2F',command = goto_optionspage)
# optionsButton.pack(fill = X)

# currentRecordsButton = Button(sideButtonFrame, text = 'Current Records', font = ('Georgia bold', 16), height = 2)
# currentRecordsButton.pack(fill = X)

# statisticsButton = Button(sideButtonFrame, text = 'Statistics', font = ('Georgia bold', 16), height = 2)
# statisticsButton.pack(fill = X)

logoutButton = Button(sideButtonFrame, text = 'Logout', font = ('Georgia bold', 16), height = 2, relief = FLAT, bg = '#FECE2F',command = goto_firstpage)
logoutButton.pack(fill = X)
#----------------------------------------------------------------

#Creates middle Frame that contains parking areas
middleFrame = Frame(root, width = 986, height = 962, bg = 'white')
middleFrame.pack(side = LEFT)
middleFrame.pack_propagate(False)

#Heading for parking area
paText = Label(middleFrame, text = 'PARKING AREA', bg = 'white', font = ('Georgia bold',40))
paText.pack(pady = 20)

#Creates parking Frame (contains 4 parking Areas -D) inside middle frame
parkingFrame = Frame(middleFrame, width = 948, height = 792, bg = 'white',bd=6)
parkingFrame.pack()

#parkingAreaA Frame
parkingAreaA  = Frame(parkingFrame, bg = 'white', padx= 50, pady = 50)
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
parkingAreaB  = Frame(parkingFrame, bg = 'white', padx= 50, pady = 50)
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
parkingAreaC  = Frame(parkingFrame, bg = 'white', padx= 50, pady = 50)
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
parkingAreaD = Frame(parkingFrame, bg = 'white', padx= 50, pady = 67)
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
rightFrame = Frame(root, width = 325, height = 962, bg = 'white')
rightFrame.pack(side = LEFT, fill = BOTH)
rightFrame.pack_propagate(False)

#Creates frame at the top in rightFrame, which contains the clock and the available slots
csFrame = Frame(rightFrame, width = 292, height = 200 )
csFrame.pack()
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

conn = sqlite3.connect('parkingManagement.db')
cursor = conn.cursor()
cursor.execute('''SELECT * FROM Customer ''')
currentCustomerRecords = cursor.fetchall()
currentSlotList = []
for customerRecord in currentCustomerRecords:
        currentSlotList.append(customerRecord[8])
currentCustomerNO = len(currentCustomerRecords)
conn.commit()
conn.close()
availableSlots = 28 - currentCustomerNO

for subparkingFrame in parkingFrame.winfo_children():
        for currentyUsedSlot in subparkingFrame.winfo_children():
                if currentyUsedSlot.cget('text') in currentSlotList:
                        currentyUsedSlot.config(bg = 'lime')
space = Label(csFrame,text = str(availableSlots), font = ('Georgia', 15))
space.pack()

# 2nd Frame in the rightFrame, which displays the attributes of the currently used selected slots--------------------------------------------------------------------------------------------------------------------------------
infoFrame = Frame(rightFrame, width = 292, height = 253)
infoFrame.pack()
infoFrame.pack_propagate(False)

info1Frame = Frame(infoFrame, bg = 'gold')
info1Frame.pack(pady = 20)

slotLabel = Label(info1Frame, text = 'Slot: ', font = ('Georgia', 13))
slotLabel.grid(row = 0, column = 0)

slotValue = Label(info1Frame, text = '', font = ('Georgia', 13))
slotValue.grid(row = 0, column = 1)

info2Frame = Frame(infoFrame)
info2Frame.pack()

nameLabel = Label(info2Frame, text = 'Name: ')
nameLabel.grid(row = 0, column = 0)

nameValue = Label(info2Frame, text = '')
nameValue.grid(row = 0, column = 1)

vNoLabel = Label(info2Frame, text = 'Vehicle No: ')
vNoLabel.grid(row = 1, column = 0)

vNoValue = Label(info2Frame, text = '')
vNoValue.grid(row = 1, column = 1)

vNameLabel = Label(info2Frame, text = 'Vehicle Name: ')
vNameLabel.grid(row = 2, column = 0)

vNameValue = Label(info2Frame, text = '')
vNameValue.grid(row = 2, column = 1)

phoneLabel = Label(info2Frame, text = 'Phone No.: ')
phoneLabel.grid(row = 3, column = 0)

phoneValue = Label(info2Frame, text = '')
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
buttonFrame.pack()
buttonFrame.pack_propagate(False)

addButton = Button(buttonFrame,state = DISABLED, text = 'Add Vehicle', width = 20, height = 2,command = goto_addpage)
addButton.pack(pady = 15)

updateButton = Button(buttonFrame,state = DISABLED, text = 'Update Slot', width = 20, height = 2, command = goto_updatepage)
updateButton.pack(pady = 15)

deleteButton = Button(buttonFrame,state = DISABLED, text = 'Delete Vehicle', width = 20, height = 2,command = delete)
deleteButton.pack(pady = 15)

billButton = Button(buttonFrame,state = DISABLED, text = 'Bill', width = 20, height = 2,command = goto_billpage)
billButton.pack(pady = 15)
root.mainloop()