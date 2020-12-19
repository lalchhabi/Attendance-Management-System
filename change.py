from tkinter import *
import cv2
import os
from tkinter.ttk import Combobox, Treeview, Scrollbar, Progressbar
from PIL import Image, ImageTk
import pymysql
import csv
from tkinter import messagebox , Message
import numpy as np
from os import listdir
from tkinter import simpledialog
import time
import random
import pandas as pd
from tkinter import filedialog
import gtts
from gtts import gTTS

account = Tk()
account.geometry('500x450+200+200')
account.title('Admin Account')
account.iconbitmap('Photos/Aha-Soft-Free-Large-Boss-Admin.ico')
frame = Frame(account, bg = 'white', height = 480, width = 500)
frame.pack()
oldpass_var = StringVar()
user_var = StringVar()
newpass_var = StringVar()
password_var = StringVar()
title = Label(frame, text = "Admin Account", font = ('times new roman', 20, 'bold') , fg = 'green', bd = 3, relief = SUNKEN)    
title.place(x = 3, y = 3, relwidth = 1)      
logo_icon = PhotoImage(file = 'Photos/logo.png',master = account)
admin_logo = Label(frame, image= logo_icon, bg = 'white').place( y = 70, relwidth = 1)
pass_icon = PhotoImage(file = 'Photos/password.png', master = account)
pass_logo = Label(frame, image = pass_icon).place(x = 7, y = 200)
pass_label = Label(frame, text = 'Old Password', font = ('times new roman', 14, 'bold')).place(x = 55, y = 215)
pass_entry = Entry(frame, show  = '*', font = ('times new roman', 14, 'bold'), textvariable = oldpass_var).place(x = 210, y = 215)
user_icon = PhotoImage(file = 'Photos/user.png', master = account)
user_logo = Label(frame, image = user_icon).place(x = 7, y = 265)
user_label = Label(frame, text = 'Username', font = ('times new roman', 14, 'bold')).place(x = 55, y = 275)
user_entry = Entry(frame, font = ('times new roman', 14, 'bold'), textvariable = user_var).place(x = 210, y = 275)
newpass_logo = Label(frame, image = pass_icon).place(x = 7, y = 325)
newpass_label = Label(frame, text = 'New Password', font = ('times new roman', 14, 'bold')).place(x = 55, y = 335)
newpass_entry = Entry(frame, show = '*', font = ('times new roman', 14, 'bold'), textvariable = newpass_var).place(x = 210, y = 325)


def user_change():
    if oldpass_var.get() == newpass_var.get():
        conn = pymysql.connect(host = "localhost", user = "root", password = "", database = "recognition")
        cur = conn.cursor()
        cur.execute("update login set username = %s, password = %s",(user_var.get(), newpass_var.get()))

        messagebox.showinfo("Success", "All the datas are updated", parent = account)
        account.destroy()
        conn.commit()
        conn.close()
    else:
        messagebox.showerror('Error','Password Not Matched', parent = account)

btn = Button(frame, text = 'Reset', font = ('times new roman', 14, 'bold'), width = 10 , bg = 'green', command = user_change, relief = GROOVE).place(x = 240, y = 380 )
account.mainloop()