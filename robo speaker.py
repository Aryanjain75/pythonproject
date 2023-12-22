import pyttsx3
from tkinter import *


def case():
    engine = pyttsx3.init()
    spoke=s.get()
    engine.say(spoke)
    engine.runAndWait()


f = Tk()
f.geometry("400x100")
f.title("ROBOSPEAKER")
label = Label(f, text="FILL BELOW INFORMATION TO SPEAK", relief="sunken", padx=3, pady=4, fg="red",
              font="comicsansms 9 bold ")
label.grid(row=0, column=9)
l = StringVar()
s = Entry(f, textvariable=l)
s.grid(row=2, column=9)
Button(f, text="submit ", padx=3, pady=4, command=case).grid(row=3, column=7)
f.mainloop()
