import tkinter
import tkinter as tk
from tkinter.constants import *
import cv2
import PIL.Image, PIL.ImageTk
from functools import partial
import threading 
import time
import imutils
from typing import Text
import os
   

def runout():

    stream1 = cv2.VideoCapture("runout.mp4")
    flag = True
    def play(speed):
        global flag
        print(f"You clicked on play. Speed is {speed}")
        
        # Play video Code

        frame1 = stream1.get(cv2.CAP_PROP_POS_FRAMES)
        stream1.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)

        grabbed, frame = stream1.read()
        if not grabbed:
            exit()
        frame = imutils.resize(frame, width=WIDTH, height=HEIGHT)
        frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
        canvas.image = frame
        canvas.create_image(0,0, image=frame, anchor=tkinter.NW)
        # if flag:
        #     canvas.create_text(134, 26, fill="black", font="Times 26 bold", text="Decision Pending")
        # flag = not flag    

    def pending(decision):
    # 1. Display decision pending image
        frame = cv2.cvtColor(cv2.imread("pending.jpg"), cv2.COLOR_BGR2RGB)
        frame = imutils.resize(frame, width=WIDTH, height=HEIGHT)
        frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
        canvas.image = frame
        canvas.create_image(0,0, image=frame, anchor=tkinter.NW)
    # 2. Wait for 1 second
        time.sleep(1.5)

    # 3. Display sponsor image
        frame = cv2.cvtColor(cv2.imread("loading.png"), cv2.COLOR_BGR2RGB)
        frame = imutils.resize(frame, width=WIDTH, height=HEIGHT)
        frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
        canvas.image = frame
        canvas.create_image(0,0, image=frame, anchor=tkinter.NW)

    # 4. Wait for 1.5 second
        time.sleep(2.5)
    # 5. Display out/notout image
        if decision == 'out':
            decisionImg = "out.jpg"   
        else:
            decisionImg = "not_out.jpg"
        frame = cv2.cvtColor(cv2.imread(decisionImg), cv2.COLOR_BGR2RGB)
        frame = imutils.resize(frame, width=WIDTH, height=HEIGHT)
        frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
        canvas.image = frame
        canvas.create_image(0,0, image=frame, anchor=tkinter.NW)

    def out():
        thread = threading.Thread(target=pending, args=("out",))
        thread.daemon = 1
        thread.start()
        print("Player is out")


    def not_out():
        thread = threading.Thread(target=pending, args=("not out",))
        thread.daemon = 1
        thread.start()
        print("Player is not out")

    window1 = tk.Toplevel(root)
    canvas = tk.Canvas(window1, height = HEIGHT, width = WIDTH)
    window1.title("Checking For Run Out")
    canvas.pack()

    btn = tkinter.Button(window1, text="<< Previous (fast)", width=40, command=partial(play, -15))
    btn.pack()
    btn = tkinter.Button(window1, text="Next (fast) >>", width=40, command=partial(play, 15))
    btn.pack()
    btn = tkinter.Button(window1, text="<< Previous (slow)", width=40, command=partial(play, -2))
    btn.pack()
    btn = tkinter.Button(window1, text="Next (slow) >>", width=40, command=partial(play, 2))
    btn.pack()
    btn = tkinter.Button(window1, text="Give Out", width=40, command=out)
    btn.pack()
    btn = tkinter.Button(window1, text="Give Not Out", width=40, command=not_out)
    btn.pack()
    
    

def stumpingg():

    stream1 = cv2.VideoCapture("stumping.mp4")
    flag = True
    def play(speed):
        global flag
        print(f"You clicked on play. Speed is {speed}")

        frame1 = stream1.get(cv2.CAP_PROP_POS_FRAMES)
        stream1.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)

        grabbed, frame = stream1.read()
        if not grabbed:
            exit()
        frame = imutils.resize(frame, width=WIDTH, height=HEIGHT)
        frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
        canvas.image = frame
        canvas.create_image(0,0, image=frame, anchor=tkinter.NW)
        # if flag:
        #     canvas.create_text(134, 26, fill="black", font="Times 26 bold", text="Decision Pending")
        # flag = not flag  
    def pending(decision):
    # 1. Display decision pending image
        frame = cv2.cvtColor(cv2.imread("pending.jpg"), cv2.COLOR_BGR2RGB)
        frame = imutils.resize(frame, width=WIDTH, height=HEIGHT)
        frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
        canvas.image = frame
        canvas.create_image(0,0, image=frame, anchor=tkinter.NW)
    # 2. Wait for 1 second
        time.sleep(1.5)

    # 3. Display loading image
        frame = cv2.cvtColor(cv2.imread("loading.png"), cv2.COLOR_BGR2RGB)
        frame = imutils.resize(frame, width=WIDTH, height=HEIGHT)
        frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
        canvas.image = frame
        canvas.create_image(0,0, image=frame, anchor=tkinter.NW)

    # 4. Wait for 1.5 second
        time.sleep(2.5)
    # 5. Display out/notout image
        if decision == 'out':
            decisionImg = "out.jpg"   
        else:
            decisionImg = "not_out.jpg"
        frame = cv2.cvtColor(cv2.imread(decisionImg), cv2.COLOR_BGR2RGB)
        frame = imutils.resize(frame, width=WIDTH, height=HEIGHT)
        frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
        canvas.image = frame
        canvas.create_image(0,0, image=frame, anchor=tkinter.NW)

    def out():
        thread = threading.Thread(target=pending, args=("out",))
        thread.daemon = 1
        thread.start()
        print("Player is out")


    def not_out():
        thread = threading.Thread(target=pending, args=("not out",))
        thread.daemon = 1
        thread.start()
        print("Player is not out")

    window2 = tk.Toplevel(root)
    canvas = tk.Canvas(window2, height = HEIGHT, width = WIDTH)
    window2.title("Checking for Stumping")
    canvas.pack()
    btn = tkinter.Button(window2, text="<< Previous (fast)", width=40, command=partial(play, -15))
    btn.pack()
    btn = tkinter.Button(window2, text="Next (fast) >>", width=40, command=partial(play, 15))
    btn.pack()
    btn = tkinter.Button(window2, text="<< Previous (slow)", width=40, command=partial(play, -2))
    btn.pack()
    btn = tkinter.Button(window2, text="Next (slow) >>", width=40, command=partial(play, 2))
    btn.pack()
    btn = tkinter.Button(window2, text="Give Out", width=40, command=out)
    btn.pack()
    btn = tkinter.Button(window2, text="Give Not Out", width=40, command=not_out)
    btn.pack()

def naball():

    stream1 = cv2.VideoCapture("no ball.mp4")
    flag = True
    def play(speed):
        global flag
        print(f"You clicked on play. Speed is {speed}")

        frame1 = stream1.get(cv2.CAP_PROP_POS_FRAMES)
        stream1.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)

        grabbed, frame = stream1.read()
        if not grabbed:
            exit()
        frame = imutils.resize(frame, width=WIDTH, height=HEIGHT)
        frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
        canvas.image = frame
        canvas.create_image(0,0, image=frame, anchor=tkinter.NW)
        # if flag:
        #     canvas.create_text(134, 26, fill="black", font="Times 26 bold", text="Decision Pending")
        # flag = not flag

    def pending(decision):
    # 1. Display decision pending image
        frame = cv2.cvtColor(cv2.imread("pending.jpg"), cv2.COLOR_BGR2RGB)
        frame = imutils.resize(frame, width=WIDTH, height=HEIGHT)
        frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
        canvas.image = frame
        canvas.create_image(0,0, image=frame, anchor=tkinter.NW)
    # 2. Wait for 1 second
        time.sleep(1.5)

    # 3. Display sponsor image
        frame = cv2.cvtColor(cv2.imread("loading.png"), cv2.COLOR_BGR2RGB)
        frame = imutils.resize(frame, width=WIDTH, height=HEIGHT)
        frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
        canvas.image = frame
        canvas.create_image(0,0, image=frame, anchor=tkinter.NW)

    # 4. Wait for 1.5 second
        time.sleep(2.5)
    # 5. Display out/notout image
        if decision == 'not_ok':
            decisionImg = "no_ball.png"   
        else:
            decisionImg = "fair_delivery.png"
        frame = cv2.cvtColor(cv2.imread(decisionImg), cv2.COLOR_BGR2RGB)
        frame = imutils.resize(frame, width=WIDTH, height=HEIGHT)
        frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
        canvas.image = frame
        canvas.create_image(0,0, image=frame, anchor=tkinter.NW)

    def ok():
        thread = threading.Thread(target=pending, args=("ok",))
        thread.daemon = 1
        thread.start()
        print("Fair Delivry")    

    def not_ok():
        thread = threading.Thread(target=pending, args=("not_ok",))
        thread.daemon = 1
        thread.start() 
        print("No Ball") 

    window3 = tk.Toplevel(root)
    canvas = tk.Canvas(window3, height = HEIGHT, width = WIDTH)
    window3.title("Checking for No Ball")
    canvas.pack()
    btn = tkinter.Button(window3, text="<< Previous (fast)", width=40, command=partial(play, -15))
    btn.pack()
    btn = tkinter.Button(window3, text="Next (fast) >>", width=40, command=partial(play, 15))
    btn.pack()
    btn = tkinter.Button(window3, text="<< Previous (slow)", width=40, command=partial(play, -2))
    btn.pack()
    btn = tkinter.Button(window3, text="Next (slow) >>", width=40, command=partial(play, 2))
    btn.pack()
    btn = tkinter.Button(window3, text="No Ball", width=40, command=not_ok)
    btn.pack()
    btn = tkinter.Button(window3, text="Fair Delivery", width=40, command=ok)
    btn.pack()

def cach():

    stream1 = cv2.VideoCapture("catch.mp4")
    flag = True
    def play(speed):
        global flag
        print(f"You clicked on play. Speed is {speed}")

        frame1 = stream1.get(cv2.CAP_PROP_POS_FRAMES)
        stream1.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)

        grabbed, frame = stream1.read()
        if not grabbed:
            exit()
        frame = imutils.resize(frame, width=WIDTH, height=HEIGHT)
        frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
        canvas.image = frame
        canvas.create_image(0,0, image=frame, anchor=tkinter.NW)
        # if flag:
        #     canvas.create_text(134, 26, fill="black", font="Times 26 bold", text="Decision Pending")
        # flag = not flag
    def pending(decision):
    # 1. Display decision pending image
        frame = cv2.cvtColor(cv2.imread("pending.jpg"), cv2.COLOR_BGR2RGB)
        frame = imutils.resize(frame, width=WIDTH, height=HEIGHT)
        frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
        canvas.image = frame
        canvas.create_image(0,0, image=frame, anchor=tkinter.NW)
    # 2. Wait for 1 second
        time.sleep(1.5)

    # 3. Display sponsor image
        frame = cv2.cvtColor(cv2.imread("loading.png"), cv2.COLOR_BGR2RGB)
        frame = imutils.resize(frame, width=WIDTH, height=HEIGHT)
        frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
        canvas.image = frame
        canvas.create_image(0,0, image=frame, anchor=tkinter.NW)

    # 4. Wait for 1.5 second
        time.sleep(2.5)
    # 5. Display out/notout image
        if decision == 'out':
            decisionImg = "out.jpg"   
        else:
            decisionImg = "not_out.jpg"
        frame = cv2.cvtColor(cv2.imread(decisionImg), cv2.COLOR_BGR2RGB)
        frame = imutils.resize(frame, width=WIDTH, height=HEIGHT)
        frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
        canvas.image = frame
        canvas.create_image(0,0, image=frame, anchor=tkinter.NW)

    def out():
        thread = threading.Thread(target=pending, args=("out",))
        thread.daemon = 1
        thread.start()
        print("Player is out")


    def not_out():
        thread = threading.Thread(target=pending, args=("not out",))
        thread.daemon = 1
        thread.start()
        print("Player is not out")

    window4 = tk.Toplevel(root)
    canvas = tk.Canvas(window4, height = HEIGHT, width = WIDTH)
    window4.title("Checking for Fair Catch")
    canvas.pack()
    btn = tkinter.Button(window4, text="<< Previous (fast)", width=40, command=partial(play, -15))
    btn.pack()
    btn = tkinter.Button(window4, text="Next (fast) >>", width=40, command=partial(play, 15))
    btn.pack()
    btn = tkinter.Button(window4, text="<< Previous (slow)", width=40, command=partial(play, -2))
    btn.pack()
    btn = tkinter.Button(window4, text="Next (slow) >>", width=40, command=partial(play, 2))
    btn.pack()
    btn = tkinter.Button(window4, text="Give Out", width=40, command=out)
    btn.pack()
    btn = tkinter.Button(window4, text="Give Not Out", width=40, command=not_out)
    btn.pack()

def leg():
    stream1 = cv2.VideoCapture("clip.mp4")
    flag = True
    def play(speed):
        global flag
        print(f"You clicked on play. Speed is {speed}")

        frame1 = stream1.get(cv2.CAP_PROP_POS_FRAMES)
        stream1.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)

        grabbed, frame = stream1.read()
        if not grabbed:
            exit()
        frame = imutils.resize(frame, width=WIDTH, height=HEIGHT)
        frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
        canvas.image = frame
        canvas.create_image(0,0, image=frame, anchor=tkinter.NW)
        # if flag:
        #     canvas.create_text(134, 26, fill="black", font="Times 26 bold", text="Decision Pending")
        # flag = not flag
    def pending(decision):
    # 1. Display decision pending image
        frame = cv2.cvtColor(cv2.imread("pending.jpg"), cv2.COLOR_BGR2RGB)
        frame = imutils.resize(frame, width=WIDTH, height=HEIGHT)
        frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
        canvas.image = frame
        canvas.create_image(0,0, image=frame, anchor=tkinter.NW)
    # 2. Wait for 1 second
        time.sleep(1.5)

    # 3. Display sponsor image
        frame = cv2.cvtColor(cv2.imread("loading.png"), cv2.COLOR_BGR2RGB)
        frame = imutils.resize(frame, width=WIDTH, height=HEIGHT)
        frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
        canvas.image = frame
        canvas.create_image(0,0, image=frame, anchor=tkinter.NW)

    # 4. Wait for 1.5 second
        time.sleep(2.5)
    # 5. Display out/notout image
        if decision == 'out':
            decisionImg = "out.jpg"   
        else:
            decisionImg = "not_out.jpg"
        frame = cv2.cvtColor(cv2.imread(decisionImg), cv2.COLOR_BGR2RGB)
        frame = imutils.resize(frame, width=WIDTH, height=HEIGHT)
        frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
        canvas.image = frame
        canvas.create_image(0,0, image=frame, anchor=tkinter.NW)

    def out():
        thread = threading.Thread(target=pending, args=("out",))
        thread.daemon = 1
        thread.start()
        print("Player is out")


    def not_out():
        thread = threading.Thread(target=pending, args=("not out",))
        thread.daemon = 1
        thread.start()
        print("Player is not out")

    window5 = tk.Toplevel(root)
    canvas = tk.Canvas(window5, height = HEIGHT, width = WIDTH)
    window5.title("Checking for Leg Before Wicket (LBW)")
    canvas.pack()
    btn = tkinter.Button(window5, text="<< Previous (fast)", width=40, command=partial(play, -15))
    btn.pack()
    btn = tkinter.Button(window5, text="Next (fast) >>", width=40, command=partial(play, 15))
    btn.pack()
    btn = tkinter.Button(window5, text="<< Previous (slow)", width=40, command=partial(play, -2))
    btn.pack()
    btn = tkinter.Button(window5, text="Next (slow) >>", width=40, command=partial(play, 2))
    btn.pack()
    btn = tkinter.Button(window5, text="Give Out", width=40, command=out)
    btn.pack()
    btn = tkinter.Button(window5, text="Give Not Out", width=40, command=not_out)
    btn.pack()    


HEIGHT = 368
WIDTH = 650

root = tk.Tk()
root.title("DECISION REVIEW SYSTEM")
canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
cv_img = cv2.cvtColor(cv2.imread("welcome.png"), cv2.COLOR_RGB2BGR)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0, 0, ancho=tkinter.NW, image=photo)
canvas.pack()


button = tk.Button(root, text = "Run Out",width=40 ,command= lambda : runout())
button.pack()
button = tk.Button(root, text = "Stumping",width=40 , command= lambda : stumpingg())
button.pack()
button = tk.Button(root, text = "No Ball",width=40 , command= lambda : naball())
button.pack()
button = tk.Button(root, text = "Catch",width=40 , command= lambda : cach())
button.pack()
button = tk.Button(root, text = "LBW",width=40 , command= lambda : leg())
button.pack()

root.mainloop()
