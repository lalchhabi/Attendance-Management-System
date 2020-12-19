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
    time.sleep(1)
    progress_bar['value'] = 20
    second.update_idletasks()
    time.sleep(1)
    progress_bar['value'] = 40
    second.update_idletasks()
    time.sleep(1)
    progress_bar['value'] = 60
    """
    Trine ML Model to Classify / Identify the person using extracted face embeddings
    """

    from sklearn.preprocessing import LabelEncoder
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.svm import SVC
    import pickle
    import numpy as np
    import os

    from sklearn.model_selection import train_test_split
    from sklearn.model_selection import GridSearchCV
    from sklearn.metrics import classification_report

    import warnings
    warnings.filterwarnings('ignore')


    currentDir = os.getcwd()

    # paths to embedding pickle file
    embeddingPickle = os.path.join(currentDir, "Face_Recognition_System_Using_Transferlearning_with_VGGFACE2_in_Facenet-master/Face_Recognition_System_Using_Transferlearning_with_VGGFACE2_in_Facenet-master/output/FinalEmbeddings.pickle")

    # path to save recognizer pickle file
    recognizerPickle = os.path.join(currentDir, "Face_Recognition_System_Using_Transferlearning_with_VGGFACE2_in_Facenet-master/Face_Recognition_System_Using_Transferlearning_with_VGGFACE2_in_Facenet-master/output/FinalRecognizer.pickle")

    # path to save labels pickle file
    labelPickle = os.path.join(currentDir, "Face_Recognition_System_Using_Transferlearning_with_VGGFACE2_in_Facenet-master/Face_Recognition_System_Using_Transferlearning_with_VGGFACE2_in_Facenet-master/output/FinalLabel.pickle")

    # loading embeddings pickle
    data = pickle.loads(open(embeddingPickle, "rb").read())

    # encoding labels by names
    label = LabelEncoder()
    labels = label.fit_transform(data["names"])

    # getting embeddings
    Embeddings = np.array(data["embeddings"])

    print("Total number of embeddings : ", Embeddings.shape)
    print("Total number of labels :", len(labels))


    ############ If you want to train SVM Classifier uncomment below code #########
    
    recognizer = KNeighborsClassifier(n_neighbors=5)
    recognizer.fit(Embeddings, labels)

    # write the actual face recognition model to disk
    f = open(recognizerPickle, "wb")
    f.write(pickle.dumps(recognizer))
    f.close()



    # write the label encoder to disk
    f = open(labelPickle,"wb")
    f.write(pickle.dumps(label))
    f.close()

    print("[Info] : Models are saved successfully :) ")

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
