import tkinter as tk
from tkinter import Message , Text
import cv2, os
import shutil
import csv
import numpy as np
#from PIL import Image, ImageTk
#import pandas as pd
import datetime
import time
import tkinter.ttk as ttk
import tkinter.font as font


window = tk.Tk()
window.title("Face Recogniser")
window.geometry('1280x720')
dialog_title = 'QUIT'
dialog_text = 'Are you sure?'
window.configure(background='cyan4')
window.grid_rowconfigure(0, weight=1 )
window.grid_columnconfigure(0, weight=1)

message = tk.Label(window, text = "Attendance Management System",bg="LightBlue4", fg="black", width=50, height=3,font=('times', 30))
message.place(x=100, y=20)

lbl=tk.Label(window, text= "Enter ID",width=20, height=2, fg="dark slate gray", bg="white smoke", font=("times", 15, 'bold'))
lbl.place (x=200, y=200)
txt=tk.Entry(window,width=20,bg="white smoke", fg="dark slate gray" , font=("time",25, 'bold'))
txt.place(x= 500,y=210)

lbl2=tk.Label(window, text= "Enter Name",width=20, height=2, fg="dark slate gray", bg="white smoke", font=("times", 15, 'bold'))
lbl2.place (x=200, y=300)
txt2=tk.Entry(window,width=20,bg="white smoke", fg="dark slate gray" , font=("time",25, 'bold'))
txt2.place(x= 500,y=310)

lbl3=tk.Label(window, text= "Notification",width=20, height=2, fg="dark slate gray", bg="white smoke", font=("times", 15, 'bold'))
lbl3.place (x=200, y=400)

message=tk.Label(window, text="", bg="white smoke", fg="dark slate gray" , width=30, height=2, activebackground="yellow" , font=("times" , 15, 'bold'))
message.place(x=500, y=400)
                                                                                                                
lbl3=tk.Label(window, text="Attendance",width=20, fg="dark slate gray",bg="white smoke",height=2, font=("times", 15, 'bold underline'))
lbl3.place(x=200,y=620)

message2=tk.Label(window, text="", bg="white smoke", fg="dark slate gray" , width=30, height=2, activebackground="white smoke" , font=("times" , 15, 'bold'))
message2.place(x=500, y=620)

def clear():
    txt.delete(0, 'end')    
    res = ""
    message.configure(text= res)

def clear2():
    txt2.delete(0, 'end')    
    res = ""
    message.configure(text= res)    
    
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False
 
def TakeImages():        
    Id=(txt.get())
    name=(txt2.get())
    if(is_number(Id) and name.isalpha()):
        cam = cv2.VideoCapture(0)
        harcascadePath = "haarcascade_frontalface_default.xml"
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
                cv2.imwrite("TrainingImage\ "+name +"."+Id +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])
                #display the frame
                cv2.imshow('frame',img)
            #wait for 100 miliseconds 
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            # break if the sample number is morethan 100
            elif sampleNum>60:
                break
        cam.release()
        cv2.destroyAllWindows() 
        res = "Images Saved for ID : " + Id +" Name : "+ name
        row = [Id , name]
        with open('StudentDetails\StudentDetails.csv','a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        message.configure(text= res)
    else:
        if(is_number(Id)):
            res = "Enter Alphabetical Name"
            message.configure(text= res)
        if(name.isalpha()):
            res = "Enter Numeric Id"
            message.configure(text= res)

def TrainImages():
    recognizer = cv2.face_LBPHFaceRecognizer.create()#recognizer = cv2.face.LBPHFaceRecognizer_create()#$cv2.createLBPHFaceRecognizer()
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector =cv2.CascadeClassifier(harcascadePath)
    faces,Id = getImagesAndLabels("TrainingImage")
    recognizer.train(faces, np.array(Id))
    recognizer.save("TrainingImageLabel\Trainner.yml")
    res = "Image Trained"#+",".join(str(f) for f in Id)
    message.configure(text= res)

def getImagesAndLabels(path):
    #get the path of all the files in the folder
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)] 
    #print(imagePaths)
    
    #create empth face list
    faces=[]
    #create empty ID list
    Ids=[]
    #now looping through all the image paths and loading the Ids and the images
    for imagePath in imagePaths:
        #loading the image and converting it to gray scale
        pilImage=Image.open(imagePath).convert('L')
        #Now we are converting the PIL image into numpy array
        imageNp=np.array(pilImage,'uint8')
        #getting the Id from the image
        Id=int(os.path.split(imagePath)[-1].split(".")[1])
        # extract the face from the training image sample
        faces.append(imageNp)
        Ids.append(Id)        
    return faces,Ids


clearButton = tk.Button(window, text="Clear", command=clear  ,fg="dark slate gray"  ,bg="white smoke"  ,width=20  ,height=2 ,activebackground = "Red" ,font=('times', 15, ' bold '))
clearButton.place(x=950, y=200)

clearButton2 = tk.Button(window, text="Clear", command=clear2  ,fg="dark slate gray"  ,bg="white smoke"  ,width=20  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
clearButton2.place(x=950, y=300)

takeImg = tk.Button(window, text="Take Images", command=TakeImages  ,fg="dark slate gray"  ,bg="white smoke"  ,width=20  ,height=3, activebackground = "Red" ,font=('times', 15, ' bold '))
takeImg.place(x=200, y=500)

trainImg = tk.Button(window, text="Train Images", command=""  ,fg="dark slate gray"  ,bg="white smoke"  ,width=20  ,height=3, activebackground = "Red" ,font=('times', 15, ' bold '))
trainImg.place(x=500, y=500)

trackImg = tk.Button(window, text="Track Images", command=""  ,fg="dark slate gray"  ,bg="white smoke"  ,width=20  ,height=3, activebackground = "Red" ,font=('times', 15, ' bold '))
trackImg.place(x=800, y=500)

quitWindow = tk.Button(window, text="Quit", command=window.destroy  ,fg="red"  ,bg="white smoke"  ,width=20  ,height=3, activebackground = "Red" ,font=('times', 15, ' bold '))
quitWindow.place(x=1100, y=500)
                    
