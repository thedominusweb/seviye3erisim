import socket
import os
from threading import Thread
from Tkinter import *
from PIL import ImageTk, Image

msg = "dGhlZG9taW51c3dlYi5vbmxpbmUvdW5kZXJncm91bmQvc2V2aXllMi9zZXZpeWUzZXJpc2ltLnBocA=="
base64_bytes = msg.encode('ascii')
msg_bytes = base64.b64decode(base64_bytes)
decoded_msg = msg_bytes.decode('ascii')

def command_clear():
    if os.name=="nt":
        os.system('cls')
    elif os.name=="posix":
        os.system('clear')

def printit():
    pencere.destroy()
    pencere2 = Tk()
    pencere2.title('Seviye3')
    pencere2.configure(background='black')
    pencere2.geometry('750x600')
    w = Label(pencere2, text=msg)
    w.pack()

pencere = Tk()
pencere.title('Seviye3')
pencere.configure(background='black')
pencere.geometry('750x600')
img = ImageTk.PhotoImage(Image.open("generatedtext.png"))
img_label = Label(pencere, image=img)
img_label.pack()
B = Button(pencere, text ="Click Me", command = printit)
B.pack()
pencere.mainloop()



command_clear()

#w = Label(pencere, text="Hello World")
#w.pack()
