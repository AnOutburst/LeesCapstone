import tkinter


class Calculator:
    expression = ""
    def test(self):
        print("calc pressed")

    def doPress(self, query):
        self.expression += str(query)
        self.equation.set(self.expression)

    def doEqual(self):
        try:
            total = str(eval(self.expression))
            self.equation.set(total)
            self.expression = ""
        except BaseException:
            self.equation.set("ILLEGAL OPERATION")

    def clear(self):
        self.expression = ""
        self.equation.set("")

    def __init__(self):
        self.calcgui = tkinter.Toplevel()
        print("calc inited")
        self.calcgui.configure(background="#008080")
        self.calcgui.title("Calculator")
        self.calcgui.geometry("265x125")
        self.equation = tkinter.StringVar()
        self.expressionField = tkinter.Entry(self.calcgui , textvariable=self.equation)
        self.expressionField.grid(columnspan=4, ipadx=70)

        self.equation.set('enter')

        button1 = tkinter.Button(self.calcgui, text=' 1 ', fg='black', bg='red',
                                 command=lambda: self.doPress(1), height=1, width=7)
        button1.grid(row=2, column=0)

        button2 = tkinter.Button(self.calcgui, text=' 2 ', fg='black', bg='red',
                                 command=lambda: self.doPress(2), height=1, width=7)
        button2.grid(row=2, column=1)

        button3 = tkinter.Button(self.calcgui, text=' 3 ', fg='black', bg='red',
                                 command=lambda: self.doPress(3), height=1, width=7)
        button3.grid(row=2, column=2)

        button4 = tkinter.Button(self.calcgui, text=' 4 ', fg='black', bg='red',
                                 command=lambda: self.doPress(4), height=1, width=7)
        button4.grid(row=3, column=0)

        button5 = tkinter.Button(self.calcgui, text=' 5 ', fg='black', bg='red',
                                 command=lambda: self.doPress(5), height=1, width=7)
        button5.grid(row=3, column=1)

        button6 = tkinter.Button(self.calcgui, text=' 6 ', fg='black', bg='red',
                                 command=lambda: self.doPress(6), height=1, width=7)
        button6.grid(row=3, column=2)

        button7 = tkinter.Button(self.calcgui, text=' 7 ', fg='black', bg='red',
                                 command=lambda: self.doPress(7), height=1, width=7)
        button7.grid(row=4, column=0)

        button8 = tkinter.Button(self.calcgui, text=' 8 ', fg='black', bg='red',
                                 command=lambda: self.doPress(8), height=1, width=7)
        button8.grid(row=4, column=1)

        button9 = tkinter.Button(self.calcgui, text=' 9 ', fg='black', bg='red',
                                 command=lambda: self.doPress(9), height=1, width=7)
        button9.grid(row=4, column=2)

        button0 = tkinter.Button(self.calcgui, text=' 0 ', fg='black', bg='red',
                                 command=lambda: self.doPress(0), height=1, width=7)
        button0.grid(row=5, column=0)

        plus = tkinter.Button(self.calcgui, text=' + ', fg='black', bg='red',
                              command=lambda: self.doPress("+"), height=1, width=7)
        plus.grid(row=2, column=3)

        minus = tkinter.Button(self.calcgui, text=' - ', fg='black', bg='red',
                               command=lambda: self.doPress("-"), height=1, width=7)
        minus.grid(row=3, column=3)

        multiply = tkinter.Button(self.calcgui, text=' * ', fg='black', bg='red',
                                  command=lambda: self.doPress("*"), height=1, width=7)
        multiply.grid(row=4, column=3)

        divide = tkinter.Button(self.calcgui, text=' / ', fg='black', bg='red',
                                command=lambda: self.doPress("/"), height=1, width=7)
        divide.grid(row=5, column=3)

        equal = tkinter.Button(self.calcgui, text=' = ', fg='black', bg='red',
                               command=self.doEqual, height=1, width=7)
        equal.grid(row=5, column=2)

        clear = tkinter.Button(self.calcgui, text='Clear', fg='black', bg='red',
                               command=self.clear, height=1, width=7)
        clear.grid(row=5, column='1')

        self.numLine = ""

        self.calcgui.mainloop()
