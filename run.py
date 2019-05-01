import tkinter
import sqlite3
import calculator
import note
import klondikesolitaire
import music

#all code unless otherwise stated written by Lee Hayes for his capstone project
#Klondike Solitaire is an opensource project created by artexcercise on github and can be found here
#github.com/artexercise/814446dc03189b5e41d7d04568254597

def runCalc():
    calc = calculator.Calculator
    calc.test(calc)

def runNote():
    notePad = note.pad()

def runsolitaire():
    klondikesolitaire.initRun()

def runmusic():
    player  = music.player()


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
    mp3Img = tkinter.PhotoImage(file="music.png")
    calcButton = tkinter.Button(window, image=calcImg, command=runCalc, bg="#008080")
    noteButton = tkinter.Button(window, image=noteImg, command=runNote, bg="#008080")
    solButton = tkinter.Button(window, image=solImg, command=runsolitaire, bg="#008080")
    mp3Button = tkinter.Button(window, image=mp3Img, command=runmusic, bg="#008080")
    #label.grid(column=0, row=0)
    #calcButton.grid(column=0, row=1, ipadx=10, ipady=10)
    #noteButton.grid(column=0, row=2, ipadx=10, ipady=10)

    calcButton.place(width=50, height=50, x=20, y=20)
    noteButton.place(width=50, height=50, x=20, y=90)
    solButton.place(width=50, height=50, x=20, y=160)
    mp3Button.place(width=50, height=50, x=20, y=230)


    window.mainloop()
