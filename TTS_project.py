import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os


engine=pyttsx3.init()

def speaknow():
    text=Text_area.get(1.0,END)
    gender=Gender_dd.get()
    speed=Speed_dd.get()
    voices=engine.getProperty('voices')

    def setvoice():
        if (gender=='Male'):
            engine.setProperty('voice',voices[0].id)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty('voice',voices[1].id)
            engine.say(text)
            engine.runAndWait()
    if (text):
        if (speed=='Fast'):
            engine.setProperty('rate',250)
            setvoice()
        elif (speed=='Normal'):
            engine.setProperty('rate',150)
            setvoice()
        else:
            engine .setProperty('rate',60)
            setvoice()

def download():
    text=Text_area.get(1.0,END)
    gender=Gender_dd.get()
    speed=Speed_dd.get()
    voices=engine.getProperty('voices')

    def setvoice():
        if (gender=='Male'):
            engine.setProperty('voice',voices[0].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,'TXT.mp3')
            engine.runAndWait()
        else:
            engine.setProperty('voice',voices[1].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,'TXT.mp3')
            engine.runAndWait()
    if (text):
        if (speed=='Fast'):
            engine.setProperty('rate',250)
            setvoice()
        elif (speed=='Normal'):
            engine.setProperty('rate',150)
            setvoice()
        else:
            engine .setProperty('rate',60)
            setvoice()





root=Tk()
root.title("Text to Speech Converter")
root.geometry("800x500")
root.resizable(False,False)

root.configure(bg="#305065")

Top_frame=Frame(root,bg="white",width=800,height=100)
Top_frame.place(x=0,y=0)

"""Logo=PhotoImage(file="C:/Users/Bharath P/Desktop/TXT project/TXT.png")
Label(Top_frame,image=Logo,bg="white").place(x=0,y=0,width=100,height=50)"""

Label(Top_frame,text="Text To Speech Converter", font="arial 30 bold", bg="white", fg="black").place(x=150,y=30)

Text_area=Text(root,font="Arail 10",bg="white",relief=GROOVE,wrap=WORD)
Text_area.place(x=20,y=150,width=500,height=250)

Label(root, text="Gender", font="arial 13 bold", bg="#305065", fg="white").place(x=560,y=175)
Gender_dd=Combobox(root, value=["Male","Female"], font="arial 10", state='r', width=10)
Gender_dd.place(x=550,y=200)
Gender_dd.set("Male")

Label(root, text="Speed", font="arial 13 bold", bg="#305065", fg="white").place(x=700,y=175)
Speed_dd=Combobox(root, value=["Slow","Normal","Fast"], font="arial 10", state='r', width=10)
Speed_dd.place(x=690,y=200)
Speed_dd.set("Normal")

#btnimg=PhotoImage(file="C:/Users/Bharath P/Desktop/TXT project/speak.png")
btn1=Button(root,text="Speak", font="arial 10", command=speaknow)
btn1.place(x=550,y=280,width=80)

btn2=Button(root,text="Save", font="arial 10",command=download)
btn2.place(x=690,y=280,width=80)



root.mainloop()