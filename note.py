import sqlite3
import tkinter

class pad:
    notes = []
    conn = sqlite3.connect("note.db")
    conn.execute(""" CREATE TABLE IF NOT EXISTS notes (contents text NOT NULL); """)
    c = conn.cursor()

    def __init__(self):
        print("hello")
        self.refresh_notes()

    def refresh_notes(self):
        print("refreshing")
        self.notes = []
        for row in self.c.execute('SELECT * FROM notes '):
            held = ''.join(row)
            self.notes.append(held)
        print(self.notes)

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
        if len(self.notes)<=1 :
            print("you cannot delete all your notes fool!")
        else:
            self.say_notes()
            action = input("what note would you like to delete")
            try:
                del self.notes[int(action)-1]
            except:
                print("delete value must be a number between 1 and " + str(len(self.notes)))

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
