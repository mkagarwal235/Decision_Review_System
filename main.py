import tkinter
import cv2
import PIL.Image,PIL.ImageTk
from functools import partial
import threading
import time
import imutils
stream=cv2.VideoCapture("clip.mp4")
flag=True
def play(speed):
    global flag
    # print(f"you click on play.speed is {speed}")
    frame1=stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES,frame1+speed)
    grabbed,frame=stream.read()
    if not grabbed:
        exit()
    frame=imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)
    if flag:
        canvas.create_text(134,26,fill="black",font="Times 26 bold",text="Decision Pending")
    flag= not flag
def pending(decision):
    # 1.Display decision pending images
    frame=cv2.cvtColor(cv2.imread("pending.png"),cv2.COLOR_BGR2RGB)
    frame=imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)

    # 2.wait for 1 sec
    time.sleep(1)
    # 3.Display sponsor image
    frame=cv2.cvtColor(cv2.imread('sponsor.png'),cv2.COLOR_BGR2RGB)
    frame=imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)

    # 4.wait for 1.5 sec
    time.sleep(1.5)
    # 5.display out/not_out images
    if decision == "out":
        decisionImg= "out.png"
    else:
        decisionImg="not_out.png"
    frame=cv2.cvtColor(cv2.imread(decisionImg),cv2.COLOR_BGR2RGB)
    frame=imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)

def out():
    thread=threading.Thread(target=pending,args=("out",))
    thread.daemon=1
    thread.start()
    # print("player is out")
def not_out():
    thread=threading.Thread(target=pending,args=("not_out",))
    thread.daemon=1
    thread.start()
    # print("player is not out")



# width and height of our main screen

SET_WIDTH=650
SET_HEIGHT=368

# Tkinter GUI start here.

window=tkinter.Tk()
window.title("DecisionReviewSystem By Mk agarwal")
cv_img=cv2.cvtColor(cv2.imread("welcome.png"),cv2.COLOR_BGR2RGB)
canvas=tkinter.Canvas(window,width=SET_WIDTH,height=SET_HEIGHT)
photo=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas=canvas.create_image(0,0,image=photo,anchor=tkinter.NW)
canvas.pack()

# Buttons to control playback

btn=tkinter.Button(window,text="<< Previous(fast)",width=30,bg="red",fg="black"
                   ,font="Times 12 bold",command=partial(play,-25))
btn.pack(pady=2)
btn=tkinter.Button(window,text="<< Previous(slow)",width=30,bg="red",fg="black"
                   ,font="Times 12 bold",command=partial(play,-2))
btn.pack(pady=2)
btn=tkinter.Button(window,text="Next(slow) >>",width=30,bg="red",fg="black"
                   ,font="Times 12 bold",command=partial(play,2))
btn.pack(pady=2)
btn=tkinter.Button(window,text="Next(fast) >>",width=30,bg="red",fg="black"
                   ,font="Times 12 bold",command=partial(play,25))
btn.pack(pady=2)
btn=tkinter.Button(window,text="Give out",width=30,bg="red",fg="black"
                   ,font="Times 12 bold",command=out)
btn.pack(pady=2)
btn=tkinter.Button(window,text="Give not out",width=30,bg="red",fg="black"
                   ,font="Times 12 bold",command=not_out)
btn.pack(pady=2)
window.mainloop()