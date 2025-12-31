import tkinter as tk
from tkinter import font
def driver():
root=tk.Tk()
root.geometry("1300x768")
label_font = font.Font(weight="bold")
bg = tk.PhotoImage(file = "image1.png")
label= tk.Label( root, image = bg)
label.image=bg
label.place(x = 0, y = 0)
payment_label=tk.Label (root,text="YOUR PAYMNET IS PROCESSING",font=("Arial",25))
payment_label.place(x=460,y=350)
def fun():
 import tkinter as tk
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
 login.place(x=680,y=400)
fun()
root.mainloop()