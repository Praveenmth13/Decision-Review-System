import tkinter
import cv2
import PIL.Image, PIL.ImageTk
from functools import partial   
import threading                
import imutils
import time

SET_WIDTH = 600
SET_HEIGHT = 350

stream = cv2.VideoCapture("clip1.mp4")
flag = True

def play(speed):
    print(f"You clicked on play. Speed is {speed}")
    global flag
    
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)   
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)
    grabbed, frame = stream.read()
    
    if not grabbed:
        exit()
        
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)

    if flag:
        canvas.create_text(134, 26, fill="black",
                           font="Times 26 bold", text="Decision Pending")
    flag = not flag

def out():
    thread = threading.Thread(target=pending, args=("out",))
    thread.daemon = 1
    thread.start()
    print("player is out")

def not_out():
    thread = threading.Thread(target=pending, args=("not_out",))
    thread.daemon = 1
    thread.start()
    print("player is not_out")



def pending(decision):
    
    frame = cv2.cvtColor(cv2.imread("pending.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)   
    #imutils function for resizing the image
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)
    
    
    time.sleep(2.5)
    
   
    frame = cv2.cvtColor(cv2.imread("sponsor.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
    
    
    time.sleep(1.5)
    
    
    if decision == "out":
        decisionImg = "out.png"
    else:
        decisionImg = "not_out.png"
    frame = cv2.cvtColor(cv2.imread(decisionImg), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
    

window = tkinter.Tk()
window.title("Third Umpire Decision Review System")

cv_img = cv2.cvtColor(cv2.imread("dhoni.png"), cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window, width=SET_WIDTH, height=SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0,0, anchor=tkinter.NW, image=photo)
canvas.pack()



b1 = tkinter.Button(window, text="<< Previous (fast)",
                    width=30, command=partial(play, -25))
b1.pack()

b2 = tkinter.Button(window, text="<< Previous (slow)",
                    width=30, command=partial(play, -2))
b2.pack()

b3 = tkinter.Button(window, text="Next (slow) >>",
                    width=30, command=partial(play, 2))
b3.pack()

b4 = tkinter.Button(window, text="Next (fast) >>", 
                    width=30, command=partial(play,25))
b4.pack()

b5 = tkinter.Button(window, text="Out", width=30, command=out)
b5.pack()

b6 = tkinter.Button(window, text="Not Out", width=30, command=not_out)
b6.pack()

window.mainloop()
