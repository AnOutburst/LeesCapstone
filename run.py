import tkinter
import sqlite3
import calculator
import note
import klondikesolitaire
import media
import time

time1 = ''

#all code unless otherwise stated written by Lee Hayes for his capstone project
#Klondike Solitaire is an opensource project created by artexcercise on github and can be found here
#github.com/artexercise/814446dc03189b5e41d7d04568254597

def runCalc():
    calc = calculator.Calculator()

def runNote():
    notePad = note.pad()

def runsolitaire():
    klondikesolitaire.initRun()

def runMedia():
    mp3 = media.mp3()

def tick():
    global time1
    # get the current local time from the PC
    time2 = time.strftime('%H:%M:%S')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    clock.after(200, tick)

if __name__ == '__main__':
    conn = sqlite3.connect('note.db')
    window = tkinter.Tk()
    window.configure(background="#008080")
    window.title("Business Applications")
    window.geometry("1280x720")

    label = tkinter.Label(window, text="Welcome to the bathroom", font=("Times New Roman", 50), bg="#008080")

    calcImg = tkinter.PhotoImage(file="calculator.png")
    noteImg = tkinter.PhotoImage(file="note.png")
    solImg = tkinter.PhotoImage(file="solitaire.png")
    mediaImg = tkinter.PhotoImage(file="music.png")

    calcButton = tkinter.Button(window, image=calcImg, command=runCalc, bg="#008080")
    noteButton = tkinter.Button(window, image=noteImg, command=runNote, bg="#008080")
    solButton = tkinter.Button(window, image=solImg, command=runsolitaire, bg="#008080")
    mediaButton = tkinter.Button(window, image=mediaImg, command=runMedia, bg="#008080")


    #label.grid(column=0, row=0)
    #calcButton.grid(column=0, row=1, ipadx=10, ipady=10)
    #noteButton.grid(column=0, row=2, ipadx=10, ipady=10)

    calcButton.place(width=50, height=50, x=20, y=20)
    noteButton.place(width=50, height=50, x=20, y=90)
    solButton.place(width=50, height=50, x=20, y=160)
    mediaButton.place(width=50, height=50, x=20, y=230)

    bottom = tkinter.Canvas(window, width=1280, height=35, bg="#B9BABD")
    #bottom.create_rectangle(0,0,1280,35, fill="#B9BABD")
    clock = tkinter.Label(bottom, font=('times', 20, 'bold'), bg='#dedee0', text="test")
    clock.place(x=1210)
    bottom.place(x=0, y=685)

    tick()

    window.mainloop()
