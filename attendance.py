############################################ Importing Tkinter modules and Libraries #####################################################################################


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


####################### Admin Login page #############

face = Tk()
face.title("Admin Login Page")
face.geometry("1350x700+0+0")
face.iconbitmap("Photos/Aha-Soft-Free-Large-Boss-Admin.ico")
    ##  variables for login##
username_var = StringVar()
password_var = StringVar()
user_var = StringVar()
pass_var = StringVar()

                           
################## Function of Admin login page
def login():
    # conn = pymysql.connect(host = "localhost", user = "root", password  = "", database = recognition)
    # curr = conn.cursor()
    # curr.execute("select from login")
    
    if username_var.get() ==  "" or password_var.get() == "":


        messagebox.showerror("Error", "All fields are Required")
        # ob1 = gTTS("All Fields are Required", lang = "en", slow = False)
        # ob1.save("fields.mp3")
        # os.system("fields.mp3")

        ######################################## To change the user data
    
    elif username_var.get() == "sumit" or password_var.get() == "12345":
    
    
    
        ##################################### Functions of facial Based Attendance system page
        def manage_employee():
            
            first = Toplevel()
            first.iconbitmap("Photos/Bokehlicia-Captiva-System-users.ico")
            first.geometry("1350x700+0+0")
            bg_photo = PhotoImage(file = "Photos/background3.png", master = first)
            background_pic = Label(first, image = bg_photo)
            background_pic.pack()
            first.title("Manage Employee post")
            
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


####################### To display the selected items 
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
                Id = simpledialog.askstring("Input", "What is the Employee ID", parent = first)
                name = simpledialog.askstring("Input", "What is the name of Employee ??", parent = first )
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
            btn5 = Button(f3, text = "Add Photo Sample", bg = "yellow", height = "2", width = "16",command = add_photo, font = ("Times new Roman", 14 , "bold")).place(x = 10, y = 60)
            btn6 = Button(f3, text = "Update Photo Sample", bg = "yellow", height = "2", width = "16", font = ("Times new Roman", 14 , "bold")).place(x = 205, y = 60 )
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
            second = Toplevel()
            second.title("Train The System")
            second.geometry("1400x700+0+0")
            second.iconbitmap("Photos/Hopstarter-Soft-Scraps-User-Group.ico")
            img1= PhotoImage(file = "Photos/background5.png", master = second)
            backgrd = Label(second, image = img1)
            backgrd.pack()
            train_title = Label(second, text = "Train the System", font = ("times new roman", 20, "bold"), bg = "cyan")
            train_title.place(x = 0,y = 0, relwidth = 1)
            img2 = PhotoImage(file = "Photos/samples.png")
            train_img2 = Label(second, image = img2)
            train_img2.place(x = 420, y =150)

            def progress():
                
                    progress_bar['value'] = 20
                    second.update_idletasks()
                    time.sleep(1)
                    progress_bar['value'] = 40
                    time.sleep(1)
                    progress_bar['value'] = 60
                    second.update_idletasks()
                    time.sleep(1)
                    progress_bar['value'] = 80
                    second.update_idletasks()
                    time.sleep(1)
                    progress_bar['value'] = 100
                    second.update_idletasks()
                    time.sleep(1)

                    messagebox.showinfo("Success", "All photos are Trained Successfully", parent = second)
          
            btn = Button(second, text = "Start Training", font = ("Times new roman", 20, "bold"), command = progress, bg = "green" )
            btn.place(x = 600, y = 450) 
            progress_bar = Progressbar(second, orient = HORIZONTAL, length = 500, mode = 'determinate')
            progress_bar.place(x = 430, y = 520)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
            second.mainloop()

######################################### Function to recognize the face
        def face_recognize():
            recognizer = cv2.face.LBPHFaceRecognizer_create()#cv2.createLBPHFaceRecognizer()
            recognizer.read('PhotosLabel/Trainner.yml')
            harcascadePath = "haarcascade_frontalface_default.xml"
            faceCascade = cv2.CascadeClassifier(harcascadePath);    
            df=pd.read_csv("StudentDetails\StudentDetails.csv")
            cam = cv2.VideoCapture(0)
            font = cv2.FONT_HERSHEY_SIMPLEX        
            col_names =  ['Id','Name','Date','Time']
            attendance = pd.DataFrame(columns = col_names)    
            while True:
                ret, im =cam.read()
                gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
                faces=faceCascade.detectMultiScale(gray, 1.2,5)    
                for(x,y,w,h) in faces:
                    cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
                    Id, conf = recognizer.predict(gray[y:y+h,x:x+w])                                   
                    if(conf < 50):
                        ts = time.time()      
                        date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                        timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                        aa=df.loc[df['Id'] == Id]['Name'].values
                        tt=str(Id)+"-"+aa
                        attendance.loc[len(attendance)] = [Id,aa,date,timeStamp]
                        
                    else:
                        Id='Unknown'                
                        tt=str(Id)  
                    if(conf > 75):
                        noOfFile=len(os.listdir("ImagesUnknown"))+1
                        cv2.imwrite("ImagesUnknown\Image"+str(noOfFile) + ".jpg", im[y:y+h,x:x+w])            
                    cv2.putText(im,str(tt),(x,y+h), font, 1,(255,255,255),2)        
                attendance=attendance.drop_duplicates(subset=['Id'],keep='first')    
                cv2.imshow('im',im) 
                if (cv2.waitKey(1)==ord('q')):
                    break
            ts = time.time()      
            date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
            timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
            Hour,Minute,Second=timeStamp.split(":")
            fileName="Attendance\Attendance_"+date+"_"+Hour+"-"+Minute+"-"+Second+".csv"
            attendance.to_csv(fileName,index=False)
            cam.release()
            cv2.destroyAllWindows()
# ######################################## To change the user data
            user_var = StringVar()
            pass_var = StringVar()

        
        def change():
            account = Toplevel()
            account.geometry("435x390+200+200")
            account.title("User Account")
            account.grab_set()
            account.focus_force()
            frame1= Frame(account, bg = "white")
            frame1.place(x = 0, y =0)
            logo_icon = PhotoImage(file = "Photos/logo.png", master= frame1)
            logo_image = Label(frame1, image = logo_icon, bd =0 ).grid( row = 0, columnspan = 3 , pady = 40, padx= 40)
            user_icon = PhotoImage(file = "Photos/user.png", master = frame1)
            password_icon = PhotoImage(file = "Photos/password.png", master = frame1)
            user_label = Label(frame1 , text = "Username", image = user_icon, bg= "white", compound = LEFT, font = ("times new roman", 15, "bold")).grid( row  = 1 , column = 0, padx = 30, pady = 5)
            user_entry = Entry(frame1, textvariable = user_var, font = ("times new roman", 15, "bold"), relief = GROOVE).grid(row = 1, column= 1, padx= 10, pady = 5)
            password_label = Label(frame1, text = " Password", image = password_icon, bg ="white", compound = LEFT, font = ("times new roman", 15, "bold")).grid(row = 2, column = 0, padx = 30, pady = 5)
            password_entry = Entry(frame1, textvariable = pass_var, show = "*", font = ("times new roman", 15,"bold"), relief = GROOVE).grid(row = 2, column = 1, padx = 20, pady = 5)
            def user_change():
                conn = pymysql.connect(host = "localhost", user = "root", password = "", database = "recognition")
                cur = conn.cursor()
                cur.execute("update login set username = %s, password = %s",(user_var.get(), pass_var.get()))

                messagebox.showinfo("Success", "All the datas are updated", parent = account)
                account.destroy()
                                                                    
                conn.commit()
                conn.close()
            
            submit_btn = Button(frame1, text = "Reset",width = 10, activebackground = "blue", activeforeground = "white" , font = ("times new roman", 20, "bold"), command = user_change ,relief = GROOVE, bg = "green").grid(row = 3, column = 1, pady =25, padx = 25)    
            account.mainloop()

        
######################################## To display the attendance register report 
        def report():
          report = Toplevel()
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

################################## Function to exit the attendance management form ####################################
        def exit():
            ques = messagebox.askyesnocancel("Notification","Do you Really want to exit?", parent = attendance)
            if (ques == True):
                attendance.destroy()
             

        ############################## Face Based Attendance Management Slider ##############################
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





        ############################### Slider Colors

        colors = ['red','green','pink','gold2','blue','black','yellow','purple']
        def faceslidercolor():
            fg = random.choice(colors)
            topic.config(fg = fg)
            topic.after(30,faceslidercolor)

            
        manage = " Face Based Attendance Management System "
        

      
#################################### Function to display the all Images
        def photo_samples():
            global my_image
            attendance.photo_path = filedialog.askopenfilename(initialdir ='C://Users//lant//Desktop//Project//TrainingImage', title = "Select Photo", filetypes = (("jpg files", "*.jpg"), ("all files", "*.*")), master = attendance)
            my_label = Label(attendance, text = attendance.photo_path).pack()
            my_image = ImageTk.PhotoImage(Image.open(attendance.photo_path))
            my_image_label = Label(attendance, image = my_image).pack()
        
        ######################################### Facial Based Attendance system page ########################

        attendance = Tk()
        attendance.title("Facial based Attendance system")
        attendance.iconbitmap("Photos/Aha-Soft-Free-Large-Boss-Admin.ico")
        attendance.geometry("1350x700+0+0")
        bg_image = PhotoImage(file = "Photos/background2.png", master = attendance)
        background_photo = Label(attendance, image = bg_image)
        background_photo.pack()

        topic = Label(attendance, text = manage  , bg = "blue" , fg = "yellow", padx = 15, pady = 15, font = ("Times New Roman", 20, "bold") ,borderwidth = 5, relief = RIDGE)
        topic.place (x = 0, y = 0,relwidth = 1)
        faceslider()
        faceslidercolor()
       
        photo1 = PhotoImage(file = "Photos/management.png", master = attendance)
        B1 = Button(attendance, image = photo1, text = "Manage Employee post",font = ("Times New Roman" , 15), fg = "green", height =230, width = 265, command = manage_employee, compound = BOTTOM )
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

    else:
        messagebox.showerror("Error", "Invalid Data")
count = 0 
text = ""
     

################################Clock #####################
def tick():
    time_string = time.strftime("%H:%M:%S")
    date_string = time.strftime("%d:%m:%Y")
    print(time_string , date_string)
    clock.config (text = "Time :" + time_string  + "\n" + "Date :" + date_string)
    clock.after(200,tick)

########################### Admin login page form ####################################
bg_icon = PhotoImage(file = "Photos/background.png", master = face)
background_image = Label(face, image = bg_icon)
background_image.pack()

title = Label(face, text = "Admin Login Page" , font = ("times new roman", 30, "bold"), bg = "green", fg = "yellow", bd = 7, relief = GROOVE)
title.place(x = 0, y = 0, relwidth = 1)

clock = Label(face , font = ("times",20,"bold"), bg = "green", relief = GROOVE)
clock.place(x = 1000, y= 600)
tick()
login_frame= Frame(face, bg = "white" )
login_frame.place(x = 400, y = 200)
logo_icon = PhotoImage(file = "Photos/logo.png", master= login_frame)
logo_image = Label(login_frame, image = logo_icon, bd = 0 ).grid( row = 0, columnspan = 3 , pady = 40, padx= 40)
user_icon = PhotoImage(file = "Photos/user.png", master = login_frame)
password_icon = PhotoImage(file = "Photos/password.png", master = login_frame)
user_label = Label(login_frame , text = "Username", image = user_icon, bg= "white", compound = LEFT, font = ("times new roman", 15, "bold")).grid( row  = 1 , column = 0, padx = 30, pady = 5)
user_entry = Entry(login_frame, font = ("times new roman", 15, "bold"), relief = GROOVE, textvariable = username_var, bg = "lightgray").grid(row = 1, column= 1, padx= 10, pady = 5)
password_label = Label(login_frame, text = "Password", image = password_icon, bg ="white", compound = LEFT, font = ("times new roman", 15, "bold")).grid(row = 2, column = 0, padx = 30, pady = 5)
password_entry = Entry(login_frame, show = "*", font = ("times new roman", 15,"bold"), relief = GROOVE, textvariable = password_var, bg = "lightgray").grid(row = 2, column = 1, padx = 20, pady = 5)
submit_btn = Button(login_frame, text = "Log In",width = 10, activebackground = "blue", activeforeground = "white", command = login , font = ("times new roman", 20, "bold"),relief = GROOVE, bg = "green").grid(row = 3, column = 1, pady =25, padx = 25) 
                
face.mainloop()
            
