from tkinter import*
from functools import partial
import cv2
import numpy as np
import os 
import time
from PIL import Image
import os
from datetime import datetime

sclocal_time ='00:00:00'
sglocal_time ='00:00:00'
uclocal_time ='00:00:00'
uglocal_time ='00:00:00'
rclocal_time ='00:00:00'
rglocal_time ='00:00:00'
pclocal_time ='00:00:00'
pglocal_time ='00:00:00'

def worktime():

    global  sclocal_time
    global sglocal_time
    global uclocal_time
    global uglocal_time
    global rclocal_time
    global rglocal_time
    global pclocal_time
    global pglocal_time

    gui = Tk()  

    gui.geometry('400x200+100+200')  
    
    gui.title('Employee Work Time')  
    
    labelNum1 = Label(gui, text="Employee Nane").grid(row=1, column=0)  
    
    labelNum2 = Label(gui, text="Time").grid(row=1, column=3)  

    FMT = '%H:%M:%S'

    ut= datetime.strptime(uglocal_time, FMT) - datetime.strptime(uclocal_time, FMT)
    
    labelNum1 = Label(gui, text="Udit Agrawal").grid(row=3, column=0)  
    
    labelNum2 = Label(gui, text=ut).grid(row=3, column=3)  
        
    st=datetime.strptime(sglocal_time, FMT) - datetime.strptime(sclocal_time, FMT)
    
    labelNum1 = Label(gui, text="Sagar Yadav").grid(row=4, column=0)  
    
    labelNum2 = Label(gui, text=st).grid(row=4, column=3)  

    rt=datetime.strptime(rglocal_time, FMT) - datetime.strptime(rclocal_time, FMT)    
    labelNum1 = Label(gui, text="Rishu").grid(row=5, column=0)  
    
    labelNum2 = Label(gui, text=rt).grid(row=5, column=3)  

    pt=datetime.strptime(pglocal_time, FMT) - datetime.strptime(pclocal_time, FMT)
    
    labelNum1 = Label(gui, text="Pushpend").grid(row=6, column=0)  
    
    labelNum2 = Label(gui, text=pt).grid(row=6, column=3)  

    gui.mainloop()

def cfacerecognition():

        global  sclocal_time
        global sglocal_time
        global uclocal_time
        global uglocal_time
        global rclocal_time
        global rglocal_time
        global pclocal_time
        global pglocal_time
        
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read('trainer/trainer.yml')
        cascadePath = "haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(cascadePath)
        c1=0
        c2=0
        c3=0
        c4=0
        font = cv2.FONT_HERSHEY_SIMPLEX

        #iniciate id counter
        id = 0

        # names related to ids: example ==> Marcelo: id=1,  etc
        names = ['None', 'sagar', 'pushpendra', 'udit', 'rishu', 'shifu'] 

        # Initialize and start realtime video capture
        cam = cv2.VideoCapture(0)
        cam.set(3, 640) # set video widht
        cam.set(4, 480) # set video height

        # Define min window size to be recognized as a face
        minW = 0.1*cam.get(3)
        minH = 0.1*cam.get(4)

        while True:

            ret, img =cam.read()
            #img = cv2.flip(img, -1) # Flip vertically

            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

            faces = faceCascade.detectMultiScale( 
                gray,
                scaleFactor = 1.2,
                minNeighbors = 5,
                minSize = (int(minW), int(minH)),
            )

            for(x,y,w,h) in faces:

                cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

                id, confidence = recognizer.predict(gray[y:y+h,x:x+w])

                # Check if confidence is less them 100 ==> "0" is perfect match 
                if (confidence < 100):
                    id = names[id]
                    confidence = "  {0}%".format(round(100 - confidence))
                else:
                    id = "unknown"
                    confidence = "  {0}%".format(round(100 - confidence))
                
                cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
                cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  

                f3 = open('face.txt','a+')
        
            if c1==0 and c2==0 and c3==0 and c4==0:
                f3.write(str("\n"))
                f3.write(str("\n"))
                local_time = time.asctime(time.localtime(time.time()))
                f3.write(str("\t\t\t\t\t"))
                f3.write(str(local_time))
                f3.write(str("\n"))
                f3.write(str("\n"))
                f3.write(str("\n"))
            if str(id) == "udit" and c1==0:
                f3.write(str("\n"))
                f3.write(str("Employee name = Udit Agrawal"))
                f3.write(str("\n"))
                f3.write(str("Coming Time and Date = ")) 
                now = datetime.now()
                uclocal_time = now.strftime("%H:%M:%S")
                f3.write(str(uclocal_time))
                f3.write(str("\n"))
                c1=1

            if str(id) == "sagar" and c2==0:
                f3.write(str("\n"))
                f3.write(str("Employee name = Sagar Yadav"))
                f3.write(str("\n"))
                f3.write(str("Coming Time and Date = ")) 
                now = datetime.now()
                sclocal_time = now.strftime("%H:%M:%S")
                f3.write(str(sclocal_time))
                f3.write(str("\n"))
                f3.close()
                c2=1
            if str(id) == "rishu" and c3==0:
                f3.write(str("\n"))
                f3.write(str("Employee name =Rishu"))
                f3.write(str("\n"))
                f3.write(str("Coming Time and Date = ")) 
                now = datetime.now()
                rclocal_time = now.strftime("%H:%M:%S")
                f3.write(str(rclocal_time))
                f3.write(str("\n"))
                c3=1
            if str(id) == "pushpendra" and c4==0:
                f3.write(str("\n"))
                f3.write(str("Employee name = Pushpendra"))
                f3.write(str("\n"))
                f3.write(str("Coming Time and Date = ")) 
                now = datetime.now()
                pclocal_time = now.strftime("%H:%M:%S")
                f3.write(str(pclocal_time))
                f3.write(str("\n"))
                c4=1
            
            cv2.imshow('camera',img) 

            k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
            if k == 27:
                break

        # Do a bit of cleanup
        print("\n [INFO] Exiting Program and cleanup stuff")
        cam.release()
        cv2.destroyAllWindows()

def gfacerecognition():
    
        global  sclocal_time
        global sglocal_time
        global uclocal_time
        global uglocal_time
        global rclocal_time
        global rglocal_time
        global pclocal_time
        global pglocal_time
        
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read('trainer/trainer.yml')
        cascadePath = "haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(cascadePath)
        d1=0
        d2=0
        d3=0
        d4=0
        font = cv2.FONT_HERSHEY_SIMPLEX

        #iniciate id counter
        id = 0

        # names related to ids: example ==> Marcelo: id=1,  etc
        names = ['None', 'sagar', 'pushpendra', 'udit', 'rishu', 'shifu'] 

        # Initialize and start realtime video capture
        cam = cv2.VideoCapture(0)
        cam.set(3, 640) # set video widht
        cam.set(4, 480) # set video height

        # Define min window size to be recognized as a face
        minW = 0.1*cam.get(3)
        minH = 0.1*cam.get(4)

        while True:

            ret, img =cam.read()
            #img = cv2.flip(img, -1) # Flip vertically

            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

            faces = faceCascade.detectMultiScale( 
                gray,
                scaleFactor = 1.2,
                minNeighbors = 5,
                minSize = (int(minW), int(minH)),
            )

            for(x,y,w,h) in faces:

                cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

                id, confidence = recognizer.predict(gray[y:y+h,x:x+w])

                # Check if confidence is less them 100 ==> "0" is perfect match 
                if (confidence < 100):
                    id = names[id]
                    confidence = "  {0}%".format(round(100 - confidence))
                else:
                    id = "unknown"
                    confidence = "  {0}%".format(round(100 - confidence))
                
                cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
                cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  

                f3 = open('gface.txt','a+')
        
            if d1==0 and d2==0 and d3==0 and d4==0:
                f3.write(str("\n"))
                f3.write(str("\n"))
                local_time = time.asctime(time.localtime(time.time()))
                f3.write(str("\t\t\t\t\t"))
                f3.write(str(local_time))
                f3.write(str("\n"))
                f3.write(str("\n"))
                f3.write(str("\n"))
            if str(id) == "udit" and d1==0:
                f3.write(str("\n"))
                f3.write(str("Employee name = Udit Agrawal"))
                f3.write(str("\n"))
                f3.write(str("Going Time = ")) 
                now = datetime.now()
                uglocal_time = now.strftime("%H:%M:%S")
                f3.write(str(uglocal_time))
                f3.write(str("\n"))
                d1=1

            if str(id) == "sagar" and d2==0:
                f3.write(str("\n"))
                f3.write(str("Employee name = Sagar Yadav"))
                f3.write(str("\n"))
                f3.write(str("Going Time and Date = ")) 
                now = datetime.now()
                sglocal_time = now.strftime("%H:%M:%S")
                f3.write(str(sglocal_time))
                f3.write(str("\n"))
                f3.close()
                d2=1
            if str(id) == "rishu" and d3==0:
                f3.write(str("\n"))
                f3.write(str("Employee name =Rishu"))
                f3.write(str("\n"))
                f3.write(str("Going Time = ")) 
                now = datetime.now()
                rglocal_time = now.strftime("%H:%M:%S")
                f3.write(str(rglocal_time))
                f3.write(str("\n"))
                d3=1
            if str(id) == "pushpendra" and d4==0:
                f3.write(str("\n"))
                f3.write(str("Employee name = Pushpendra"))
                f3.write(str("\n"))
                f3.write(str("Going Time = ")) 
                now = datetime.now()
                pglocal_time = now.strftime("%H:%M:%S")
                f3.write(str(pglocal_time))
                f3.write(str("\n"))
                d4=1
            
            cv2.imshow('camera',img) 

            k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
            if k == 27:
                break

        # Do a bit of cleanup
        print("\n [INFO] Exiting Program and cleanup stuff")
        cam.release()
        cv2.destroyAllWindows()


def train():
    # Path for face image database
    path = 'dataset'

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    # function to get the images and label data


    def getImagesAndLabels(path):

        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
        faceSamples = []
        ids = []

        for imagePath in imagePaths:

            PIL_img = Image.open(imagePath).convert('L')  # convert it to grayscale
            img_numpy = np.array(PIL_img, 'uint8')

            id = int(os.path.split(imagePath)[-1].split(".")[1])
            faces = detector.detectMultiScale(img_numpy)

            for (x, y, w, h) in faces:
                faceSamples.append(img_numpy)
                ids.append(id)

        return faceSamples, ids


    print("\n [INFO] Training faces. It will take a few seconds. Wait ...")
    faces, ids = getImagesAndLabels(path)
    recognizer.train(faces, np.array(ids))

    # Save the model into trainer/trainer.yml
    # recognizer.save() worked on Mac, but not on Pi
    recognizer.write('trainer/trainer.yml')

    # Print the numer of faces trained and end program
    print("\n [INFO] {0} faces trained. Exiting Program".format(
        len(np.unique(ids))))

def faceid():
    gui = Tk()  

    gui.geometry('400x200+100+200')  
    
    gui.title('Employee if')  
    
    number1 = StringVar()  

    number2 = StringVar()  
    
    labelNum1 = Label(gui, text="Employee_name").grid(row=1, column=0)  
    
    labelNum2 = Label(gui, text="Employee_id").grid(row=2, column=0)  
    
    labelResult = Label(gui)  
    
    labelResult.grid(row=7, column=2)  
    
    entryNum1 = Entry(gui, textvariable=number1).grid(row=1, column=2)  
    
    entryNum2 = Entry(gui, textvariable=number2).grid(row=2, column=2)  
    
    call_result = partial(facedata,number2)  
    
    buttonCal = Button(gui, text="Check", fg='white', bg='black', command=call_result).grid(row=3, column=0)  

    gui.mainloop()

def facedata(n2):

    cam = cv2.VideoCapture(0)
    cam.set(3, 640)  # set video width
    cam.set(4, 480)  # set video height

    face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # For each person, enter one numeric face id
    face_id =int(n2.get())

    #print("\n [INFO] Initializing face capture. Look the camera and wait ...")
    # Initialize individual sampling face count
    count = 0

    while(True):

        ret, img = cam.read()
        # img = cv2.flip(img, -1)  # flip video image vertically
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:

            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            count += 1

            # Save the captured image into the datasets folder
            cv2.imwrite("dataset/User." + str(face_id) + '.' +
                        str(count) + ".jpg", gray[y:y+h, x:x+w])

            cv2.imshow('image', img)

        k = cv2.waitKey(100) & 0xff  # Press 'ESC' for exiting video
        if k == 27:
            break
        elif count >= 30:  # Take 30 face sample and stop video
            break

    # Do a bit of cleanup
    print("\n [INFO] Exiting Program and cleanup stuff")
    cam.release()
    cv2.destroyAllWindows()

def aclose_window (): 

    #gui.destroy()
    cfacerecognition()  

def gclose_window (): 

    #gui.destroy()
    gfacerecognition()  

def tclose_window (): 

    gui.destroy()
    train()  

def wkclose_window (): 
    gui.destroy()
    worktime()

def dclose_window (): 
    gui.destroy()
    faceid()

def check_password(label_result, n1, n2):  
    m=str(n1.get())
    p=str(n2.get())
    n="udit"
    nn="000"
 
    if m==n and p==nn:
        button1 = Button (gui, text = "Coming Attendance", fg='white', bg='navy blue', command = aclose_window).grid(row=6,column=3)
        button2 = Button (gui, text = "Going Attendance", fg='white', bg='navy blue', command = gclose_window).grid(row=7,column=3)
        button3 = Button (gui, text = "Train photo", fg='white', bg='navy blue', command = tclose_window).grid(row=8,column=3)
        button4 = Button (gui, text = "Add Employee", fg='white', bg='navy blue', command = dclose_window).grid(row=9,column=3)   
        button5 = Button (gui, text = "Total Time Work", fg='white', bg='navy blue', command = wkclose_window).grid(row=10,column=3) 
    
    else:
 
         label_result.config(text="Wrong password or Id _name",font="bold")
         button2 = Button (gui, text = "EXIT.", fg='white', bg='black', command = wclose_window).grid(row=5,column=2)

 
    return 





gui = Tk()  

gui.geometry('400x200+100+200')  
  
gui.title('Login_page')  
   
number1 = StringVar()  

number2 = StringVar()  
  
labelNum1 = Label(gui, text="Id_name").grid(row=1, column=0)  
  
labelNum2 = Label(gui, text="Password").grid(row=2, column=0)  
  
labelResult = Label(gui)  
  
labelResult.grid(row=7, column=2)  
  
entryNum1 = Entry(gui, textvariable=number1).grid(row=1, column=2)  
  
entryNum2 = Entry(gui, textvariable=number2).grid(row=2, column=2)  
  
call_result = partial(check_password, labelResult, number1, number2)  
  
buttonCal = Button(gui, text="Check", fg='white', bg='black', command=call_result).grid(row=3, column=0)  

gui.mainloop()
 
