import threading
import tkinter as tk
root= tk.Tk()
root.title("login page")
root.geometry("1000x1000")
login=tk.Button(text="log in")
name_label=tk.Label (root,text="name")
name_entry=tk.Entry(root)
password_label=tk.Label(root,text="password")
password_entry=tk.Entry(root)
name_label.grid(row=1,column=0)
password_label.grid(row=2,column=0)
name_entry.grid(row=1,column=1)
password_entry.grid(row=2,column=1)
login.grid(row=3,column=0)
image=tk.PhotoImage(file="car1.png")
label=tk.Label(root,image=image).grid(row=0, column=0)
def window3():
 root= tk.Tk()
 root.title("cab booken")
 root.geometry("500x500")
 cab_label=tk.Label (root,text="cab has been booked for u").grid(row=1,column=1) 
def window2():
  root.title("last step")
  person_label=tk.Label(text="haw many persons")
  person_label.grid(row=1,column=0)
  person_entry=tk.Entry(root)
  person_entry.grid(row=1,column=1)
  number_label=tk.Label(text="enter u r number")
  number_entry=tk.Entry(root)
  number_label.grid(row=2,column=0)
  number_entry.grid(row=2,column=1)
  finish=tk.Button(text=" finish it ")
  finish.grid(row=3,column=0)
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
  finish.config(command=last)   
def window1():    #destination
  root.title("destination")
  root.geometry("500x500")
  next=tk.Button(text="next step")
  next.grid(row=3,column=0)
  from_label=tk.Label(root,text="Pickup point")
  from_entry=tk.Entry(root)
  to_label=tk.Label(root,text="Drop point")
  to_entry=tk.Entry(root)
  from_label.grid(row=1,column=0)
  from_entry.grid(row=1,column=1)
  to_label.grid(row=2,column=0)
  to_entry.grid(row=2,column=1)
  def drop():     #destination codition
   pickup=from_entry.get()
   drop=to_entry.get()
   if(pickup==""and drop==""): 
    root= tk.Tk()
    root.title(" enter correctly")
    root.geometry("500x500")
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
   import mysql.connector
   data=mysql.connector.connect(host='localhost', user='root',password = '',database='taxisql',)
   mycursor=data.cursor()
   sql = "INSERT INTO destination (Pickup point,Drop point) VALUES (%s,%s)"
   val =(pickup,drop)
   mycursor.execute(sql,val)
   data.commit()
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
 import mysql.connector
 data=mysql.connector.connect(host='localhost', user='root',password = '',database='taxisql',)
 mycursor=data.cursor()
 sql = 'INSERT INTO Login (Name,Password) VALUES (%s,%s)'
 val = (name,password)
 mycursor.execute(sql,val)
 data.commit()
login.config(command=fun)
root.mainloop()


