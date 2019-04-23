import tkinter

class Calculator:
    def test(self):
        print("calc pressed")

    def doPress(self, number):
        self.expression += str(number)
        self.equation.set(self.expression)

    def doEqual(self):
        try:
            total = str(eval(self.expression))
            self.equation.set(total)
            self.expression = ""
        except BaseException:
            self.equation.set("ILLEGAL OPERATION")

    def __init__(self):
        print("calc inited")
        self.numLine = ""

