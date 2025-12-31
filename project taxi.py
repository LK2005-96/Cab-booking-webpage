import mysql.connector
from tkinter import font
from tkinter import messegebox
import tkinter as tk
root= tk.Tk()
root.title("login page")
root.geometry("1300x768")
label_font = font.Font(weight="bold")
bg = tk.PhotoImage(file = "image1.png")
label= tk.Label( root, image = bg)
label.image=bg
label.place(x = 0, y = 0)
login=tk.Button(text="log in",font=label_font)
name_label=tk.Label (root,text="Username",font=label_font)
name_entry=tk.Entry(root)
password_label=tk.Label(root,text="Password",font=label_font)
password_entry=tk.Entry(root)
name_label.place(x=580,y=300)
password_label.place(x=580,y=350)
name_entry.place(x=670,y=305)
password_entry.place(x=670,y=355)
login.place(x=680,y=400)
def window3():
 root= tk.Tk()
 root.title("cab booken")
 root.geometry("500x500")
 cab_label=tk.Label (root,text="cab has been booked for u").grid(row=1,column=1) 
def window2():
  root.geometry("1300x768")
  bg = tk.PhotoImage(file = "image3.png")
  label= tk.Label( root, image = bg)
  label.image=bg
  label_font = font.Font(weight="bold")
  label.place(x = 0, y = 0)
  root.title("last step")
  person_label=tk.Label(text="how many persons",font=label_font)
  person_label.place(x=535,y=300)
  person_entry=tk.Entry(root)
  person_entry.place(x=698,y=305)
  number_label=tk.Label(text="enter u r number",font=label_font)
  number_entry=tk.Entry(root)
  number_label.place(x=535,y=350)
  number_entry.place(x=698,y=355)
  finish=tk.Button(text=" finish it ",font=label_font)
  finish.place(x=660,y=400)
  def last():
   person=person_entry.get()
   number=number_entry.get()
   if(person==""and number==""): 
    root= tk.Tk()
    root.title(" enter correctly")
    root.geometry("500x500")
    per_label=tk.Label (root,text="enter no of persons and ph.no").grid(row=1,column=1)
   elif(person==""):
    root= tk.Tk()
    root.title("enter persons")
    root.geometry("500x500")
    num_label=tk.Label (root,text="enter no of persons").grid(row=1,column=1)     
   elif(number==""):
    root= tk.Tk()
    root.title("enter number")
    root.geometry("500x500")
    numb_label=tk.Label (root,text="enter u r number").grid(row=1,column=1)
   else:
    window3()
   '''data=mysql.connector.connect(host='localhost', user='root',password = '',database='taxisql',)
   mycursor=data.cursor()
   sql1 = 'INSERT INTO destination (Persons,Ph_no) VALUES (%s,%s)'
   val1 =(pickup,drop)
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
  root.title("destination")
  next=tk.Button(text="next step",font=label_font)
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
    root= tk.Tk()
    root.title(" enter correctly")
    pic_label=tk.Label (root,text="enter pickup point and drop point").grid(row=1,column=1)
   elif(pickup==""):
    root= tk.Tk()
    root.title("enter name")
    root.geometry("500x500")
    pick_label=tk.Label (root,text="enter pickup point").grid(row=1,column=1)     
   elif(drop==""):
    root= tk.Tk()
    root.title("enter password")
    root.geometry("500x500")
    dro_label=tk.Label (root,text="enter drop point").grid(row=1,column=1)
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
  root= tk.Tk()
  root.title(" enter name")
  root.geometry("500x500")
  nam_label=tk.Label (root,text="enter ur name and password").grid(row=1,column=1)
 elif(name==""):
  root= tk.Tk()
  root.title("enter name")
  root.geometry("500x500")
  pass_label=tk.Label (root,text="enter ur name").grid(row=1,column=1)
 elif(password==""):
  root= tk.Tk()
  root.title("enter password")
  root.geometry("500x500")
  pass_label=tk.Label (root,text="enter ur password").grid(row=1,column=1)
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


