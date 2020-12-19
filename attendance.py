# ############################################ Importing Tkinter modules and Libraries #####################################################################################


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


 
# ####################### Admin Login page #############


def manage_employee():

    first = Toplevel()
    first.iconbitmap("Photos/Bokehlicia-Captiva-System-users.ico")
    first.geometry("1350x700+0+0")
    bg_photo = PhotoImage(file = "Photos/background3.png", master = first)
    background_pic = Label(first, image = bg_photo)
    background_pic.pack()
    first.title("Manage Employee post")
    print("Hi Chhabi lal tamang")
    face = Label(first, text = "Management of Employee & post" , bg = "green" , fg = "yellow", padx = 15, pady = 15, font = ("Times New Roman", 20, "bold") ,borderwidth = 5, relief = RIDGE).place(x = 500, y = 10)
    main = Label(first, bg = "gray", borderwidth = 1).pack()
    #All Required variables for database
    eid_var = StringVar()
    post_var = StringVar()
    fname_var = StringVar()
    gender_var = StringVar()
    contact_var = StringVar()
    address_var = StringVar()
    DOJ_var = StringVar()
    search_by = StringVar()
    search_text = StringVar()

    #################################################### Functions of Employee Management form #########################



    ########################################## To Add the Employee
    def add_employee():
        if post_var.get() == "" or fname_var.get() == "" or gender_var.get() ==  "" or contact_var.get() == "" or address_var.get() == "" or DOJ_var.get() == "":
            messagebox.showerror("Error","All fields are Required", parent = first)
        else:

            conn = pymysql.connect(host = "localhost", user = "root", password = "", database = "recognition")
            cur = conn.cursor()
            cur.execute("insert into attendance VALUES (%s,%s,%s,%s,%s,%s,%s)", (eid_var.get(),
                                                                                        post_var.get(),
                                                                                        fname_var.get(),
                                                                                        gender_var.get(),
                                                                                        contact_var.get(),
                                                                                        address_var.get(),
                                                                                        DOJ_var.get()
                                                                                        ))
            conn.commit()

            display()
            clear()
            conn.close()

        ######################################################################## To Display the data of Employee

    def display():

        conn = pymysql.connect(host = "localhost", user = "root", password = "", database = "recognition")
        cur = conn.cursor()
        cur.execute("select * from attendance")
        data = cur.fetchall()
        if len(data)!= 0:
            table1.delete(*table1.get_children())
            for row in data:
                table1.insert('', END, values = row)                                                                                                                                                                                                                                                                                                                                                                    
            conn.commit()
        conn.close()
        ########################################### To clear the data
    def clear():

        eid_var.set("")
        post_var.set("")
        fname_var.set("")
        gender_var.set("")
        contact_var.set("")
        address_var.set("")
        DOJ_var.set("")


####################### To display the selected items in text field area
    def focus_data(event):
        cursor = table1.focus()
        contents = table1.item(cursor)
        row = contents['values']
        eid_var.set(row[0])
        post_var.set(row[1])
        fname_var.set(row[2])
        gender_var.set(row[3])
        contact_var.set(row[4])
        address_var.set(row[5])
        DOJ_var.set(row[6])
############################## To update the data  
    def update():
        if post_var.get() == "" or fname_var.get() == "" or gender_var.get() ==  "" or contact_var.get() == "" or address_var.get() == "" or DOJ_var.get() == "":
            messagebox.showerror("Error","All fields are Required", parent = first)
        else:
            conn = pymysql.connect(host = "localhost", user = "root", password = "", database = "recognition")
            cur = conn.cursor()
            cur.execute("update attendance set post = %s, fname = %s, gender = %s, contact_no = %s, email_address = %s, date_of_join = %s where eid = %s", (                                                               
                                                                            post_var.get(),
                                                                            fname_var.get(),
                                                                            gender_var.get(),
                                                                            contact_var.get(),
                                                                            address_var.get(),
                                                                            DOJ_var.get(),
                                                                            eid_var.get()
                                                                            ))
            conn.commit()
            display()
            clear()
            conn.close()

###################### To delete the items
    def delete():
        if post_var.get() == "" or fname_var.get() == "" or gender_var.get() ==  "" or contact_var.get() == "" or address_var.get() == "" or DOJ_var.get() == "":
            messagebox.showerror("Error","All fields are Required", parent = first)
        else:
            conn = pymysql.connect(host = "localhost", user = "root", password = "", database = "recognition")
            cur = conn.cursor()
            cur.execute("delete  from attendance where eid = %s",eid_var.get())
            conn.commit()
            conn.close()
            display()
            clear()

    def search_data():

        conn = pymysql.connect(host = "localhost", user = "root", password = "", database = "recognition")
        cur = conn.cursor()
        cur.execute("select * from attendance where " + str(search_by.get()) + " like '%" + str(search_text.get()) + "%'")
        data = cur.fetchall()
        if len(data)!= 0:
            table1.delete(*table1.get_children())
            for row in data:
                table1.insert('', END, values = row)
            conn.commit()
        conn.close()




    def show_data():
        display()


    def add_photo():
        Id = eid_var.get()
        name = fname_var.get()
        if (Id == "" or name == ""):
            messagebox.showerror("Error", "ID and Name are Required", parent = first)

        else:
            cam = cv2.VideoCapture(0)
            harcascadePath = "C:/Users/lant/Desktop/Project/haarcascades_files/opencv-master/data/haarcascades/haarcascade_frontalface_default.xml"
            detector=cv2.CascadeClassifier(harcascadePath)
            sampleNum=0
            while(True):
                ret, img = cam.read()
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = detector.detectMultiScale(gray, 1.3, 5)
                for (x,y,w,h) in faces:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)        
                    #incrementing sample number 
                    sampleNum=sampleNum+1
                    #saving the captured face in the dataset folder TrainingImage

                    file_path = 'C:/Users/lant/Desktop/Project/TrainingImage/'+ name + "." + Id + '.' + str(sampleNum) + ".jpg"
                    cv2.imwrite(file_path,  gray[y:y+h,x:x+w])

                    #display the frame
                    cv2.putText(img,str(sampleNum),(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
                    cv2.imshow('frame',img)
                #wait for 100 miliseconds 
                if cv2.waitKey(100) & 0xFF == ord('q'):
                    break
                # break if the sample number is morethan 30
                elif sampleNum>30:
                    break
            cam.release()
            cv2.destroyAllWindows()
            messagebox.showinfo("Success", "All photos are collected", parent = first) 
            print("All samples are collected Successfully")

            row = [Id , name]
            with open('StudentDetails\StudentDetails.csv','a+') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(row)
            csvFile.close()


################################################## Employee Management form ###############################
    f2 = Frame(first, bg = "gray",borderwidth = "3", relief = SUNKEN, height = 600, width = 420)
    titles = Label(f2, text = "Manage Employee" ,bg = "gray", font = ("Italic", 20, "bold")).place(x = 90, y = 30)
    id = Label(f2, text = "Employee ID", bg = "gray", font = ("italic",13, "bold")).place(x = 35, y = 100 )
    E1 = Entry(f2, width = 20, textvariable = eid_var,  font = ("italic",13, "bold") ).place(x = 180  , y = 100)
    post = Label(f2, text = "Post", bg = "gray",  font = ("italic",13, "bold")).place(x = 35, y = 150 )
    E2 = Entry(f2, width = 20, textvariable = post_var,  font = ("italic",13, "bold")).place(x =180, y = 150)
    name = Label(f2, text = "Full Name", bg = "gray", font = ("italic",13, "bold")).place(x =35, y = 200)
    E3 = Entry(f2, width = 20, textvariable = fname_var , font = ("italic",12, "bold")).place(x = 180, y = 200)
    gender = Label(f2, text = "Gender", bg = "gray", font = ("italic",12, "bold")).place(x = 35, y= 250)
    E7 = Combobox(f2, textvariable = gender_var , values = ["Male","Female","Others"], state = "readonly",  font = ("italic",11, "bold")).place(x = 180, y = 250)
    no = Label(f2, text = "Contact.No", bg = "gray", font = ("italic",12, "bold")  ).place(x = 35, y = 300)
    E4 = Entry(f2, width = 20, textvariable = contact_var , font = ("italic",12, "bold") ).place(x = 180, y = 300 ) 
    address = Label(f2, text = " Email Address", bg = "gray", font = ("italic",12, "bold")).place(x = 35, y = 350)
    E5 = Entry(f2, width = 20, textvariable = address_var , font = ("italic",12, "bold") ).place(x = 180, y = 350)
    date = Label(f2, text = "D.O.J(dd mm yyyy)", bg = "gray",font = ("italic",12, "bold")).place(x = 35, y = 400 )
    E6 = Entry(f2, textvariable = DOJ_var , font = ("italic",12, "bold")).place(x = 180, y = 400)
    f2.place(x = 10, y = 90)
    # b2 = Button(first, text = "Close", command = first.destroy ).place(x = 135, y = 600)
    f3 = Frame(first, bg = "white", height = 130, width = 402)
    btn1 = Button(f3, text = "Add", bg = "green", height = "1", width = "7",command = add_employee, font = ("Times new Roman", 14 , "bold")).place(x = 10, y = 10)
    btn2 = Button(f3, text = "Update", bg = "green", height = "1", width = "7", command = update, font = ("Times new Roman", 14 , "bold")).place(x = 105, y = 10)
    btn3 = Button(f3, text = "Delete", bg = "green",  height = "1", width = "7", command = delete,  font = ("Times new Roman", 14 , "bold")).place(x = 205, y = 10)
    btn4 = Button(f3, text = "Clear", bg = "green", height = "1", width = "7", command = clear, font = ("Times new Roman", 14 , "bold")).place(x = 305, y = 10)
    btn5 = Button(f3, text = "Add Photo Sample", bg = "yellow", height = "2", width = "34",command = add_photo, font = ("Times new Roman", 14 , "bold")).place(x = 10, y = 60)

    f3.place(x = 20, y = 550)
################################################################################### Large Frame
    f4 = Frame(first, height = 600, width = 900, bg = "gray", borderwidth = "3", relief = SUNKEN)
    f4.place(x = 440, y = 90)
    l1 = Label(first, text = "Search By:",font = ("times new roman", 18 ,"bold"),bg = "gray", fg = "white").place(x = 460, y = 100 )
    c1 = Combobox(first, textvariable = search_by, values = ["eid","fname","post"], state = "readonly", width = "25").place(x = 580, y = 109)
    E7 = Entry(first, textvariable = search_text, width = "25", font = ("times new Roman",10) ).place(x = 780, y = 109)
    btn7 = Button(first,  text = "Search ",  height = "1", width = "16", command = search_data, font = ("Times new Roman", 13 , "bold")).place(x = 960, y = 100 )
    btn8 = Button(first, text = "Show All",  height = "1", width = "16", command = show_data, font = ("Times new Roman", 13 , "bold")).place(x = 1150, y = 100)
################################################################################## Table frame
    f5 = Frame(f4, bg = "green", borderwidth = "2", relief = SUNKEN)
    f5.place(x = 20, y = 45, height = 550, width = 855 )
    scroll_x =Scrollbar(f5, orient = HORIZONTAL)
    scroll_y = Scrollbar(f5, orient = VERTICAL)
    table1 = Treeview(f5, columns = ("eid","post", "fname","gender","contact.no","address","DOJ"), xscrollcommand = scroll_x.set, yscrollcommand = scroll_y.set)
    scroll_x.pack(side = BOTTOM, fill = X )
    scroll_y.pack(side = RIGHT, fill = Y)
    scroll_x.config(command = table1.xview)
    scroll_y.config(command = table1.yview)
    table1.heading("eid", text ="Employee ID")
    table1.heading('post', text = "Post")
    table1.heading("fname", text= "Full Name")
    table1.heading("gender",text = "Gender")
    table1.heading("contact.no", text = "Contact_No")
    table1.heading("address", text = " Email Address")
    table1.heading("DOJ", text= "Date Of Join")
    table1['show'] = 'headings'
    table1.column("eid", width = 119)
    table1.column("post", width = 119)
    table1.column("fname", width = 119)
    table1.column("gender", width = 119)
    table1.column("contact.no", width = 119)
    table1.column("address", width = 119)
    table1.column("DOJ", width = 119)

    table1.pack(fill = BOTH, expand = 1)
    table1.bind("<ButtonRelease-1>", focus_data)
    display()
    first.mainloop()
def train():
   import train
######################################### Function to recognize the face
def face_recognize():
    import recognize

######################################## To change the user data
######################## User Admin
    
def change():
    import change
    
######################################## To display the attendance register report 
def report():
   import report 

################################## Function to exit the attendance management form ####################################
def exit():
    
    ques = messagebox.askyesnocancel("Notification","Do you Really want to exit?", parent = attendance)
    if (ques == True):
        attendance.destroy()
    

#             ############################## Face Based Attendance Management Slider ##############################
def faceslider():
    global count, text

    if (count>= len(manage)):
        count = -1
        text = ''
        topic.config(text = text)
    else:
        text = text + manage[count]
        topic.config(text = text)
        count += 1
    topic.after(200, faceslider)





#             ############################### Slider Colors

colors = ['red','green','pink','gold2','blue','black','yellow','purple']
def faceslidercolor():
    fg = random.choice(colors)
    topic.config(fg = fg)
    topic.after(30,faceslidercolor)

#################################### Function to display the all Images
def photo_samples():
    global my_image
    attendance.photo_path = filedialog.askopenfilename(initialdir ='C://Users//lant//Desktop//Project//TrainingImage', title = "Select Photo", filetypes = (("jpg files", "*.jpg"), ("all files", "*.*")), master = attendance)
    my_label = Label(attendance, text = attendance.photo_path).pack()
    my_image = ImageTk.PhotoImage(Image.open(attendance.photo_path))
    my_image_label = Label(attendance, image = my_image).pack()


#################################### Function for the face alignment
def face_align():
    align = Toplevel()
    align.title("Face Alignment")
    align.geometry("1350x700+0+0")
    align.mainloop()
    
#             ######################################### Facial Based Attendance system page ########################

attendance = Tk()
attendance.title("Facial based Attendance system")
attendance.iconbitmap("Photos/Aha-Soft-Free-Large-Boss-Admin.ico")
attendance.geometry("1350x700+0+0")
bg_image = PhotoImage(file = "Photos/background2.png", master = attendance)
background_photo = Label(attendance, image = bg_image)
background_photo.pack()

topic = Label(attendance, text = 'Face Based Attendance Management System' , bg = "blue" , fg = "yellow", padx = 15, pady = 15, font = ("Times New Roman", 20, "bold") ,borderwidth = 5, relief = RIDGE)
topic.place (x = 0, y = 0,relwidth = 1)
# faceslider()
# faceslidercolor()

photo1 = PhotoImage(file = "Photos/management.png", master = attendance)
B1 = Button(attendance, image = photo1, text = "Employee Management",font = ("Times New Roman" , 15), fg = "green", height =230, width = 265, command = manage_employee, compound = BOTTOM )
B1.place(x = 20, y = 100)

photo2 = PhotoImage(file = "Photos/face_recognizer.png",  master = attendance)
B2 = Button(attendance, image = photo2 , text = "Face Rocognizer", font = ("Times new roman", 15), fg = "green", height = 230, width= 265, command = face_recognize, compound = BOTTOM )
B2.place(x = 20, y = 400)
photo3 = PhotoImage(file = "Photos/train.png",  master = attendance)
B3 =  Button(attendance , image = photo3 , text = "Train the Data" , font = ("Times new roman", 15), fg = "green" , height = 230, width= 265, command = train , compound = BOTTOM )
B3.place(x = 360, y = 100)
photo4 = PhotoImage(file = "Photos/exit1.png",  master = attendance )
B4 = Button(attendance, image = photo4, fg = "green", height = 230, width = 265 , command = exit, compound = BOTTOM)
B4.place(x =1040, y = 400)
photo5 = PhotoImage(file = "Photos/report.png" ,  master = attendance)
B5 = Button(attendance, text = "Attendance Report", fg = "green", font = ("Times new roman", 15), image = photo5, height = 230, width = 265, command = report, compound = BOTTOM)
B5.place(x = 360, y = 400)
photo6 = PhotoImage(file = "Photos/photosample.png",  master = attendance)
B6 = Button(attendance, text = "Photo Samples" ,fg = "green", font =("Times new roman",15), image = photo6, height = 230, width = 265, command = photo_samples, compound = BOTTOM )
B6.place(x = 700, y= 100) 
photo7 = PhotoImage(file = "Photos/passwordchange.png", master = attendance)
B7 = Button(attendance, fg = "green", image = photo7, height = 230, width = 265, command = change, compound = BOTTOM )
B7.place(x = 700, y = 400)
photo8 = PhotoImage(file = "Photos/face_alignment.png", master = attendance)
B8 = Button(attendance, text = "Face Alignment", fg = "green", font = ("Times new Roman", 15), image = photo8, height = 230, width = 265, compound = BOTTOM)
B8.place(x = 1040, y =100)

attendance.mainloop()

            