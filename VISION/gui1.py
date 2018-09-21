from tkinter import *
import sys
import os
from tkinter.filedialog import askopenfilename
 
window = Tk()
 
window.title("Welcome to the VISION")
 
window.geometry('350x200')
lb1 = Label(window, text="Initialize")
lb2 = Label(window, text="Classify your Images")
lb3 = Label(window, text="Test your Image")
lb4 = Label(window, text="Test the video from your phone")
 
lb1.grid(column=0, row=0)
lb2.grid(column=0, row=1)
lb3.grid(column=0, row=2)
lb4.grid(column=0, row=3)
def clicked1():
 
    os.system('python initializer.py')
   
def clicked2():
 
    os.system('python classifier_train.py')

def clicked3():
    
    os.system('python test_image.py')

def clicked4():
    
    os.system('python test_video.py')
 
btn1 = Button(window, text="Click Me", command=clicked1)
btn2 = Button(window, text="Click Me", command=clicked2)
btn3 = Button(window, text="Click Me", command=clicked3)
btn4 = Button(window, text="Click Me", command=clicked4)
 
btn1.grid(column=1, row=0)
btn2.grid(column=1, row=1)
btn3.grid(column=1, row=2)
btn4.grid(column=1, row=3)
 
window.mainloop()
