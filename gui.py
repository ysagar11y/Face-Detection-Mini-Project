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
message.place(x=550, y=400)
                                                                                                                
lbl3=tk.Label(window, text="Attendance",width=20, fg="dark slate gray",bg="white smoke",height=2, font=("times", 15, 'bold underline'))
lbl3.place(x=200,y=620)

message2=tk.Label(window, text="", bg="white smoke", fg="dark slate gray" , width=30, height=2, activebackground="white smoke" , font=("times" , 15, 'bold'))
message2.place(x=500, y=620)


clearButton = tk.Button(window,text="clear",command="",fg="dark slate gray",bg="white smoke",width=20,height=2,activebackground="white smoke",font=('times',15,"bold"))
clearButton.place(x=950,y=210)
clearButton2 = tk.Button(window,text="clear",command="",fg="dark slate gray",bg="white smoke",width=20,height=2,activebackground="white smoke",font=('times',15,"bold"))
clearButton2.place(x=950,y=310)

takeImg = tk.Button(window ,text="Take image",command="",fg"dark slate gray",bg="white smake",width=20,height=3,activebackground="white smoke",font=('times',15,"bold")
takeImg.place(x=90,y=500)

trainImg = tk.Button(window ,text="Train image",command="",fg"dark slate gray",bg="white smake",width=20,height=3,activebackground="white smoke",font=('times',15,"bold")
trainImg.place(x=390,y=500)

trackImg = tk.Button(window ,text="Track image",command="",fg"dark slate gray",bg="white smake",width=20,height=3,activebackground="white smoke",font=('times',15,"bold")
trackImg.place(x=690,y=500)

quitImg = tk.Button(window ,text="QUIT",command="z,fg"dark slate gray",bg="white smake",width=20,height=3,activebackground="white smoke",font=('times',15,"bold")
quitImg.place(x=990,y=500)

window.mainloop()
