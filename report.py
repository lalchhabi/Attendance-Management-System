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
report = Tk()
report.geometry("1400x700+0+0")
report.title("Attendance Report")
report.iconbitmap("Photos/Aha-Soft-Large-Seo-SEO.ico")
report.config(bg = "green")
title = Frame(report, bg = "cyan", bd = "3", relief = SUNKEN )
title.pack(fill = BOTH)
title_label = Label(title, text = "Attendance Report", font = ("times new roman", 30, "bold"), fg = "maroon", bg = "cyan")
title_label.pack()
####################################### Report Management Frame
report_manage = Frame(report, height = 620, width = 400, bg = "yellow", borderwidth = "3", relief = SUNKEN)
report_manage.place(x = 10, y = 70)
report_title = Label(report_manage, text = "Manage Attendance", font = ("times new roman", 20, "bold"), bg = "yellow")
report_title.place(x = 10, y = 10, relwidth = 1)
id_label = Label(report_manage, text = "Employee Id", font = ("times new roman",13, "bold"), bg = "yellow")
id_label.place(x = 10, y = 100)
id_entry = Entry(report_manage, font = ("times new roman", 13, "bold"))
id_entry.place(x = 180, y = 100)
name_label = Label(report_manage, text = "Employee Name", font = ("times new roman", 13, "bold"), bg = "yellow")
name_label.place(x = 10,y = 150)
name_entry = Entry(report_manage, font = ("times new roman", 13, "bold"))
name_entry.place(x = 180, y = 150)
date_label = Label(report_manage, text = "Date(dd-mm-yyyy", font = ("times new roman", 13, "bold"), bg = "yellow")
date_label.place(x = 10, y = 200 )
date_entry = Entry(report_manage, font = ("times new roman", 13, "bold"))
date_entry.place(x = 180, y = 200)
status_dropdown = Label(report_manage, text = "Attendance Status", font = ("times new roman", 13, "bold"), bg = "yellow")
status_dropdown.place (x = 10, y = 250)
status_combo = Combobox(report_manage, values = ['Present','Absent'],state = 'readonly', font = ("timed new roman", 11, "bold"))
status_combo.place(x = 180, y= 250)

clear_btn = Button(report_manage, text = "Clear", bg= "cyan", font = ("times new roman", 15, "bold"), width = 8)
clear_btn.place(x = 10, y = 300)
update_btn = Button(report_manage, text = "Update", bg = "cyan", font = ("times new roman", 15, "bold"), width = 8)
update_btn.place(x = 135, y = 300)
delete_btn = Button(report_manage, text = "Delete", bg = "cyan", font = ("times new roman", 15, "bold"), width = 8)
delete_btn.place(x = 260, y = 300) 


####################################### Textfill Frame 
text_fill = Frame(report, height = 620, width = 930, bg= "yellow", borderwidth = "3", relief = SUNKEN)
text_fill.place(x = 420, y = 70)
search_label = Label(text_fill, text = "Search By:", font = ("times new roman", 15, "bold"), bg = "yellow")
search_label.place(x = 10, y = 13)
search_combo = Combobox(text_fill, values = ['Attendance Id', 'Employee Id'], state = 'readonly', font = ("times new roman", 15),width = "15")
search_combo.place(x = 110, y = 13)
search_entry = Entry(text_fill, font = ("times new roman", 15 ), width = "15")
search_entry.place(x = 300 , y = 13)
search_btn = Button(text_fill, text = "Search", font = ("times new roman", 15, "bold"), width = 8)
search_btn.place(x = 490, y = 10)
search_today = Button(text_fill, text = "Today's Report", font = ("times new roman", 15, "bold"), width = 12)
search_today.place(x = 625, y = 10 )
show_btn = Button(text_fill,  height = "1", text = "Show All", font = ("times new roman", 15, "bold"), width = 8)
show_btn.place(x = 807, y = 10)
###################################### Table frame
table_frame = Frame(text_fill, borderwidth = "3", relief = GROOVE, bg = "white")
table_frame.place(x= 10, y= 55, height = 560, width = 905)
scroll_x = Scrollbar(table_frame, orient = HORIZONTAL)
scroll_y = Scrollbar(table_frame, orient = VERTICAL)
login_table = Treeview(table_frame, columns = ("aid", "eid", "name", "post", "status", "date", "time"), xscrollcommand = scroll_x.set, yscrollcommand = scroll_y.set)
scroll_x.pack(side = BOTTOM, fill = X )
scroll_y.pack(side = RIGHT, fill = Y)
scroll_x.config( command = login_table.xview)
scroll_y.config( command = login_table.yview)  
login_table.heading("aid", text ="Attendance ID")
login_table.heading("eid", text ="Employee ID")
login_table.heading('name', text = "Name")
login_table.heading("post", text= "post")
login_table.heading("status", text = "Attendance Status")
login_table.heading("date", text = "Date")
login_table.heading("time", text = "Time")
login_table['show'] = 'headings'
login_table.column("aid",  width = 119)
login_table.column("eid", width = 119)
login_table.column("name", width = 119)
login_table.column("post", width = 119)
login_table.column("status", width = 119)
login_table.column("date", width = 119)
login_table.column("time", width = 119)
login_table.pack(fill = BOTH, expand = 1)
report.mainloop()