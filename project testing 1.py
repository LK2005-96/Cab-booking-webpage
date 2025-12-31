#import mysql.connector
from tkinter import font
from tkinter import messagebox
import tkinter as tk
admin=["Dom","Brain","Driver","Travis","Ken Miles","Frank",]
adminpass=["Dom3","Brain5","Driver6","Travis6","Ken Miles8","Frank5"]
root= tk.Tk()
root.title("Login page")
root.geometry("1300x768")
label_font = font.Font(weight="bold")
bg = tk.PhotoImage(file = "image1.png")
label= tk.Label( root, image = bg)
label.image=bg
label.place(x = 0, y = 0)
login=tk.Button(text="Log in",font=label_font)
name_label=tk.Label (root,text="Username",font=label_font)
name_entry=tk.Entry(root)
password_label=tk.Label(root,text="Password",font=label_font)
password_entry=tk.Entry(root)
name_label.place(x=580,y=300)
password_label.place(x=580,y=350)
name_entry.place(x=670,y=305)
password_entry.place(x=670,y=355)
login.place(x=680,y=400)
'''def fun():
  root=tk.Tk()
  root.title("Login page")
  root.geometry("1300x768")
  label_font = font.Font(weight="bold")
  bgr = tk.PhotoImage(file = "image1.png")
  label_pay= tk.Label( root,image = bgr)
  label_pay.image=bgr
  label_pay.place(x = 0, y = 0)
  login=tk.Button(text="Log in",font=label_font)
  name_label=tk.Label (root,text="Username",font=label_font)
  name_entry=tk.Entry(root)
  password_label=tk.Label(root,text="Password",font=label_font)
  password_entry=tk.Entry(root)
  name_label.place(x=580,y=300)
  password_label.place(x=580,y=350)
  name_entry.place(x=670,y=305)
  password_entry.place(x=670,y=355)
  login.place(x=680,y=400)'''
def payment():
 root.geometry("1300x768")
 label_font = font.Font(weight="bold")
 bg = tk.PhotoImage(file = "image1.png")
 label= tk.Label( root, image = bg)
 label.image=bg
 label.place(x = 0, y = 0)
 payment_label=tk.Label (root,text="YOUR PAYMNET IS PROCESSING",font=("Arial",25))
 payment_label.place(x=460,y=350)
 fun()
def last():
 messagebox.showwarning("showinfo","Taxi has been booked")
 import tkinter as tk
 root=tk.Tk()
 root.title("Login page")
 root.geometry("1025x512")
 label_font = font.Font(weight="bold")
 login=tk.Button(text="Log in",font=label_font)
 name_label=tk.Label (root,text="Username",font=label_font)
 name_entry=tk.Entry(root)
 password_label=tk.Label(root,text="Password",font=label_font)
 password_entry=tk.Entry(root)
 name_label.place(x=580,y=300)
 password_label.place(x=580,y=350)
 name_entry.place(x=670,y=305)
 password_entry.place(x=670,y=355)
 login.place(x=680,y=400)
 bg = tk.PhotoImage(file = "image4.png")
 label= tk.Label( root, image = bg)
 label.image=bg
 label.place(x = 0, y = 0)
def window3():
 root.title("Drivers and no")
 root.geometry("1300x768")
 bg = tk.PhotoImage(file = "image1.png")
 label= tk.Label( root, image = bg)
 label.image=bg
 label_font = font.Font(weight="bold")
 label.place(x = 0, y = 0)
 title_label=tk.Label(text="NAMES AND VECHICLE NUMBERS OF TAXI ON THAT ROUTE",font=label_font).place(x=400,y=200)
 dom_label=tk.Label(text="Name:Dom,Car no:XAB 235",font=label_font).place(x=520,y=300)
 brain_label=tk.Label(text="Name:Brain,Car no:Jn 302 7983",font=label_font).place(x=520,y=340)
 driver_label=tk.Label(text="Name:Driver,Car no:Tn 33 9999",font=label_font).place(x=520,y=380)
 travis_label=tk.Label(text="Name:Travis,Car no:Tn 1759",font=label_font).place(x=520,y=420)
 miles_label=tk.Label(text="Name:Ken Miles,Car no:Tn gt40",font=label_font).place(x=520,y=460)
 frank_label=tk.Label(text="Name:Frank,Car no:Tn 05 B93",font=label_font).place(x=520,y=500)
 book=tk.Button(text="Book",command=payment,font=label_font).place(x=600,y=540)
def window2():
  root.geometry("1300x768")
  bg = tk.PhotoImage(file = "image3.png")
  label= tk.Label( root, image = bg)
  label.image=bg
  label_font = font.Font(weight="bold")
  label.place(x = 0, y = 0)
  root.title("Last step")
  person_label=tk.Label(text="How many persons",font=label_font)
  person_label.place(x=535,y=300)
  person_entry=tk.Entry(root)
  person_entry.place(x=698,y=305)
  number_label=tk.Label(text="Enter your number",font=label_font)
  number_entry=tk.Entry(root)
  number_label.place(x=535,y=350)
  number_entry.place(x=698,y=355)
  finish=tk.Button(text=" Finish it ",font=label_font)
  finish.place(x=660,y=400)
  def last():
   person=person_entry.get()
   number=number_entry.get()
   if(person==""and number==""): 
    messagebox.showwarning("showwarning","Enter no of persons and ph.no")   
   elif(person==""):
    messagebox.showwarning("showwarning","Enter no of persons")   
   elif(number==""):
    messagebox.showwarning("showwarning","Enter your number")
   else:
    window3()
   '''data=mysql.connector.connect(host='localhost', user='root',password = '',database='taxisql',)
   mycursor=data.cursor()
   sql1 = 'INSERT INTO destination (Persons,Ph_no) VALUES (%s,%d)'
   val1 =(person,number)
   mycursor.execute(sql1,val1)
   data.commit()'''
  finish.config(command=last)   
def window1():    #destination
  label_font = font.Font(weight="bold")
  root.geometry("1300x768")
  bg = tk.PhotoImage(file = "image2.png")
  label= tk.Label( root, image = bg)
  label.image=bg
  label.place(x = 0, y = 0)
  root.title("Destination")
  next=tk.Button(text="Next step",font=label_font)
  next.place(x=660,y=400)
  from_label=tk.Label(root,text="Pickup point",font=label_font)
  from_entry=tk.Entry(root)
  to_label=tk.Label(root,text="Drop point",font=label_font)
  to_entry=tk.Entry(root)
  from_label.place(x=565,y=300)
  from_entry.place(x=680,y=305)
  to_label.place(x=565,y=350)
  to_entry.place(x=680,y=355)
  pickup=from_entry.get()
  drop=to_entry.get()
  def drop():     #destination codition
   pickup=from_entry.get()
   drop=to_entry.get()
   if(pickup==""and drop==""): 
     messagebox.showwarning("showwarning","Enter pickup point and drop point")
   elif(pickup==""):
    messagebox.showwarning("showwarning","Enter pickup point")
   elif(drop==""):
    messagebox.showwarning("Error","Enter drop point")
   else:
    window2()
  ''' data=mysql.connector.connect(host='localhost', user='root',password = '',database='taxisql',)
   mycursor=data.cursor()
   sql1 = 'INSERT INTO destination (Pickup_point,Drop_point) VALUES (%s,%s)'
   val1 =(pickup,drop)
   mycursor.execute(sql1,val1)
   data.commit()'''
  next.config(command=drop)   
def fun():
 password=password_entry.get()
 name=name_entry.get()
 if(name==""and password==""):
  messagebox.showwarning("showwarning","Enter name and password")
 elif(name==""):
  messagebox.showwarning("showwarning","Enter your name ")
 elif(password==""):
  messagebox.showwarning("showwarning","Enter your password")
 else:
  window1()
 '''data=mysql.connector.connect(host='localhost', user='root',password = '',database='taxisql',)
 mycursor=data.cursor()
 sql = 'INSERT INTO Login (Name,Password) VALUES (%s,%s)'
 val = (name,password)
 mycursor.execute(sql,val)
 data.commit()  '''
login.config(command=fun)
root.mainloop()

