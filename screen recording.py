from tkinter import *
import pyscreenrec
import tkinter.messagebox as msg

root= Tk()
root.geometry('400x600')
root.title('Screen Recording ')
root.config(bg="white")
root.resizable(False, False)



def start_rec():

    msg.showinfo("Recording", "Recording has started")
    file = Filename.get()
    rec.start_recording(str(file+".mp4"),1)


def pause_rec():
    rec.pause_recording()
    msg.showinfo('Recording', 'Recording has been Paused')

def resume_rec():
    rec.resume_recording()
    msg.showinfo('Recording', 'Recording has been Resumed')

def stop_rec():
    rec.stop_recording()
    msg.showinfo('Recording', 'Recording has been Saved')


rec = pyscreenrec.ScreenRecorder()


#icon
image_icon = PhotoImage(file = 'images/recording icon.png')
root.iconphoto(False, image_icon)

#background images
image1 = PhotoImage(file="images/bg_yellow-removebg-preview.png")
Label(root, image=image1, bg="#fff").place(x=-7, y=0)

image2 = PhotoImage(file="images/bg_blue-removebg-preview.png")
Label(root, image=image2, bg="#fff").place(x=100, y=400)


#heading
lbl = Label(root, text="Screen Recording", font="arial 15 bold")
lbl.pack(pady=20)

image3= PhotoImage(file="images/recording img.png")
Label(root, image= image3, bd=0).pack(pady=30)

# entry
Filename = StringVar()
entry = Entry(root, textvariable=Filename, width=18, font="arial 15")
entry.place(x=100, y=350)
Filename.set("recording")

#buttons
start = Button(root, text="start", font="arial 40", command= start_rec)
start.place(x=110, y=225)

image4 = PhotoImage(file="images/pause button.png")
pause = Button(root, image=image4, command=pause_rec)
pause.place(x=50, y=450)


image5 = PhotoImage(file="images/play button (2).png")
resume = Button(root, image=image5, command=resume_rec)
resume.place(x=150, y= 450)

image6 = PhotoImage(file="images/stop button.png")
stop = Button(root, image= image6, command=stop_rec)
stop.place(x=250, y= 450)

root.mainloop()