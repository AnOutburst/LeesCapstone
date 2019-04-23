import sqlite3
import tkinter

class pad:
    notes = []
    conn = sqlite3.connect("note.db")
    conn.execute(""" CREATE TABLE IF NOT EXISTS notes (contents text NOT NULL); """)
    c = conn.cursor()

    def __init__(self):
        print("hello")
        self.l = tkinter.StringVar()
        self.refresh_notes()
        gui = tkinter.Tk()
        gui.configure(background="#008080")
        gui.title("Note Taking")
        gui.geometry("300x600")
        addButton = tkinter.Button(gui, text="add a note", command=self.add_note, bg="#008080")
        self.e = tkinter.Entry(gui)
        self.e.insert(0, "number to delete")
        deleteButton = tkinter.Button(gui, text="delete entered item", command=self.delete_note, bg="#008080")
        #itemlist = tkinter.Label(gui, textVariable=self.l)
        addButton.grid(column=0,row=0)
        self.e.grid(column=0,row=1)
        deleteButton.grid(column=0,row=2)

        gui.mainloop()

    def refresh_notes(self):
        print("refreshing")
        self.notes = []
        stringhold = ""
        index = 1
        for row in self.c.execute('SELECT * FROM notes '):
            held = ''.join(row)
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
        action = input("what would you like to say")
        self.c.execute("INSERT INTO notes VALUES (?)", (action,))
        self.conn.commit()
        self.refresh_notes()
        #self.notes.append(action)

        print("note " + action + " added as number " + str(len(self.notes)))

    def delete_note(self):
        num = 0
        try:
            num = int(self.e.get())
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





# if len(self.notes)<=1 :
#     print("you cannot delete all your notes fool!")
# else:
#     self.say_notes()
#     action = input("what note would you like to delete")
#     try:
#         del self.notes[int(action)-1]
#     except:
#         print("delete value must be a number between 1 and " + str(len(self.notes)))

# if __name__ == 'note':
#     myNote = pad()
#     print("Welcome to notes!")
#     myNote.say_notes()
#     while True:
#         action = input("add note [A], delete note [D], show notes [S]").upper()
#         if action not in "ADS" or len(action) != 1:
#             print("invalid val")
#             continue
#         if action == "A":
#             myNote.add_note()
#         elif action =="D":
#             myNote.delete_note()
#         elif action =="S":
#             myNote.say_notes()
