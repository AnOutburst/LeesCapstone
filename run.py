import tkinter
import sqlite3
import calculator
import klondikesolitaire

#all code unless otherwise stated written by Lee Hayes for his capstone project
#Klondike Solitaire is an opensource project created by artexcercise on github and can be found here
#github.com/artexercise/814446dc03189b5e41d7d04568254597

def runCalc():
    calc = calculator.Calculator
    calc.press(calc, 5)



if __name__ == '__main__':
    conn = sqlite3.connect('note.db')
    window = tkinter.Tk()
    window.configure(background="#008080")
    window.title("Business Applications")
    window.geometry("1280x720")

    label = tkinter.Label(window, text="Welcome to the bathroom", font=("Times New Roman", 50), bg="#008080")

    calcImg = tkinter.PhotoImage(file="calculator.png")
    bathroom = tkinter.Button(window, image=calcImg, command=runCalc, bg="#008080")
    #label.grid(column=0, row=0)
    bathroom.grid(column=0, row=1)


    window.mainloop()
