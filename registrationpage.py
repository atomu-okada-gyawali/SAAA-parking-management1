#import modules to import necessary objects inside the window 
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import tkinter.ttk as ttk
import sqlite3
from tkinter import messagebox
import string
#tk() is used to create a tkinter window 
win = Tk()
win.title = ("registration page")#title for the tkinter window 
win.geometry("1624x950")#geometric specification of the tkinter window 
win.config(bg = "white")#using config to change the background color of the window

def register():
    try:
        entryValuesList = [f1.get(),l1.get(),u1.get(),e1.get(),p1.get(),selected_option.get(),int(spin_temp.get()),positon_option.get(),int(ph1.get())]

        for spCh in string.punctuation:
            if not e1.get().startswith(spCh) and (e1.get().endswith('@gmail.com')):
                isValidEmail = True
            else:
                isValidEmail = False
                break
        
        assert isValidEmail,'Invalid email entry'
        assert True in map(lambda x: bool(x), entryValuesList), 'You have incomplete entry, please try again'
        assert p1.get() == c1.get(), 'Your passwords are not matching'
        conn = sqlite3.connect('parkingmanagement.db')
        cursor = conn.cursor()
        cursor.execute('SELECT UserUName FROM User')
        usernameList = cursor.fetchall()[0]
        assert u1.get() not in usernameList, 'Username already taken'

        conn.close()
        conn = sqlite3.connect('parkingManagement.db')
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO User(UserFName,UserLName,UserUName,UserEmail,UserPassword,UserGender,UserAge,UserPosition,UserPhoneNumber) VALUES(?,?,?,?,?,?,?,?,?)""",entryValuesList)
        conn.commit()
        conn.close()
        win.destroy()
        import loginpage

    except AssertionError as error:
        response = messagebox.showerror('Registration Error',str(error))
        if response:
            pass
        else:
            pass
    except ValueError:
        response = messagebox.showerror('Invalid value','Enter your values appropriately')



#function created in order to import image inside the tkinter window 
def open_image(file_path):
    image = Image.open(file_path)
    return ImageTk.PhotoImage(image)

#image path of the image 1 
image_path = ("SAAA-parking-management1\\resources\\image_registrationpage.png")

img = open_image(image_path)
label = tk.Label(win, image=img, bg = "white", width = 692, height = 766)
label.pack( side = LEFT) #pack is also another method to adjust object position insdie the tkinte window 

#image path of the second image 
image_path = ("SAAA-parking-management1\\resources\\logo_registrationpage.png")
img2 = open_image(image_path)
label2 = tk.Label(win, image=img2, bg = "white",width = 246, height = 61.38)
label2.pack() 
#pack used for the same purpose as the for the above image 1  
label2.place(anchor = "nw",x = 25, y = 10)#anchoring image to the northwest side of the window denoted by "nw"

def firstpage():
    win.destroy()
    import firstpage


#label to create a text inside the window and changing the background foreground and the size of font according to the need 
lbl1 = Label(win, text = "Welcome to SAAA", fg = "black", bg =  'white' ,font = ("Georgia Bold", 25))
lbl1.place(x =868, y = 24)

lbl2 = Label(win, text = "make your own space", fg = "black",bg =   'white', font = ("Georgia", 10))
lbl2.place(x =945, y = 70)




firstname = Label(win, text= "First Name", fg = "black",bg = 'white', font =("Open Sans",9))
firstname.place(x =780, y = 199)


#entry is used to open a empty box inside the window where the texts can be inserted and it can be edited according to the need 
f1 = Entry(win, width = 29 )
#height width is adjusted 
f1.place(x = 782, y = 222)#placed to the location as per the need

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


#for user to be able to select their gender as per their specific gender drop down button is created where only male and female option are available
selected_option  = tk.StringVar()
dropdown = tk.OptionMenu(win, selected_option, "Male", "Female")
dropdown.place(x = 1023, y = 326)#placed accordint to the need
dropdown.config(bg  = "white")#background color is changed using config





username = Label(win, text = "Username", fg = "black", bg = "white", font = ("open sans", 9))
username.place(x = 780, y =407 )
 
u1  = Entry(win, width = 29)
u1.place(x = 782, y =430 ) 


age = Label(win, text = "Age", fg = "black", bg = "white", font = ("open sans", 9))
age.place( x= 1023, y = 407)


#spinbox is added in order to enter the age inside the box of the user 
spin_temp = ttk.Spinbox()
spin_temp.place(x =1023 , y = 430 )



password = Label(win,  text = "Password" ,fg = "black", bg = "white", font = ("open sans", 9))
password.place(x= 780, y = 511)

p1 = Entry(win, width = 29)
p1.place(x = 782, y = 534)

position = Label(win, text = "Position", fg = "black", bg = "white", font = ("open sans", 9))
position.place(x= 1023, y = 511)


#optionmenu is used for the user to select the their respective role either staff or the manager
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

#button for resgistration process to proceed 
reg_btn = Button(win, text = "        Register Now       ",fg ="black", bg = "#FFC125", font = ("open sans",10), command= register)
reg_btn.place(x = 1023, y = 730)

cancel_btn = Button(win, text = "               Cancel              ", fg ="#FCFAF7", bg ="black", font= ("open sans",9), command = firstpage  )
cancel_btn.place( x= 860, y = 730)



win.mainloop()#mainloop to display the window 