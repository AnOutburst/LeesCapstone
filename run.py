import tkinter
import sqlite3
import calculator
import note
import klondikesolitaire

#all code unless otherwise stated written by Lee Hayes for his capstone project
#Klondike Solitaire is an opensource project created by artexcercise on github and can be found here
#github.com/artexercise/814446dc03189b5e41d7d04568254597

def runCalc():
    calc = calculator.Calculator
    calc.test(calc)

def runNote():
    print("not in yet")
    notePad = note.pad()
    notePad.add_note()
    # notePad.say_notes()



if __name__ == '__main__':
    conn = sqlite3.connect('note.db')
    window = tkinter.Tk()
    window.configure(background="#008080")
    window.title("Business Applications")
    window.geometry("1280x720")

    label = tkinter.Label(window, text="Welcome to the bathroom", font=("Times New Roman", 50), bg="#008080")

    calcImg = tkinter.PhotoImage(file="calculator.png")
    noteImg = tkinter.PhotoImage(file="note.png")
    calcButton = tkinter.Button(window, image=calcImg, command=runCalc, bg="#008080")
    noteButton = tkinter.Button(window, image=noteImg, command=runNote, bg="#008080")
    #label.grid(column=0, row=0)
    calcButton.grid(column=0, row=1, ipadx=10, ipady=10)
    noteButton.grid(column=0, row=2, ipadx=10, ipady=10)


    window.mainloop()
