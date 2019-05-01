import sqlite3
import tkinter

class pad:
    notes = []
    conn = sqlite3.connect("note.db")
    conn.execute(""" CREATE TABLE IF NOT EXISTS notes (contents text NOT NULL); """)
    c = conn.cursor()

    def __init__(self):
        self.l = tkinter.StringVar()
        gui = tkinter.Tk()
        gui.configure(background="#008080")
        gui.title("Note Taking")
        gui.geometry("300x600")
        addButton = tkinter.Button(gui, text="add a note", command=self.add_note, bg="#008080", width=40)
        self.e = tkinter.Entry(gui, width=50)
        self.e.insert(0, "note text here")
        deleteButton = tkinter.Button(gui, text="delete selected item", command=self.delete_note, bg="#008080", width=40)

        #itemlist = tkinter.Label(gui, textVariable=self.l)
        self.scrollbar = tkinter.Scrollbar(gui, orient=tkinter.VERTICAL)
        self.itemlist = tkinter.Listbox(gui, selectmode=tkinter.SINGLE, width=50, height=6,
                                        yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.itemlist.yview)
        #self.itemlist.pack()
        self.itemlist['yscroll'] = self.scrollbar.set

        addButton.grid(column=0,row=0)
        self.e.grid(column=0,row=1)
        deleteButton.grid(column=0,row=2)
        self.itemlist.grid(column=0, row=4, columnspan=2)
        #self.scrollbar.grid()

        self.refresh_notes()

        gui.mainloop()

    def refresh_notes(self):
        self.itemlist.delete(0,tkinter.END)
        print("refreshing")
        self.notes = []
        stringhold = ""
        index = 1
        for row in self.c.execute('SELECT * FROM notes '):
            held = ''.join(row)
            self.itemlist.insert(tkinter.END, held)
            stringhold +=  str(index) + ". " + held + "\n"
            index+=1
            self.notes.append(held)
        #self.l.set(stringhold)
        print(self.notes)
        print(stringhold)
        #print(self.l)

    def say_notes(self):
        index = 0
        for note in self.notes:
            index += 1
            print("note " + str(index) + ": " + note)

    def add_note(self):
        #action = input("what would you like to say")
        action = str(self.e.get())
        self.c.execute("INSERT INTO notes VALUES (?)", (action,))
        self.conn.commit()
        self.refresh_notes()
        #self.notes.append(action)

        print("note " + action + " added as number " + str(len(self.notes)))

    def delete_note(self):
        try:
            num = self.itemlist.curselection()[0] + 1
            #num = int(self.e.get())
            if 0 < num <= len(self.notes):
                print("cool")
                valu = self.notes[num-1]
                print(valu)
                self.c.execute("DELETE FROM notes WHERE contents = (?)", (valu,))
                self.conn.commit()
                self.refresh_notes()
            else:
                print("bad")
        except:
            print("you fucked up bozo")