import tkinter
from pygame import mixer
import tkinter.filedialog


class mp3:
    paused = False
    path = ""
    mixer.init()
    #v = tkinter.StringVar()
    filename = ""
    #mixer.music.load('D:/UserFiles/Music/Akira/Battle Against Clown.mp3')
    #mixer.music.play()
    def __init__(self):
        self.eemps = tkinter.Tk()
        self.eemps.configure(background="#008080")
        self.eemps.title("MP3 Player")
        self.eemps.geometry("600x300")
        self.v = tkinter.StringVar()
        print(self.v.get())
        #image = tkinter.Image("file.png")
        #fileImg = tkinter.PhotoImage("file.png")
        #image=tkinter.PhotoImage("file.png")
        filebutton = tkinter.Button(self.eemps, command=self.chooseFile, bg="#008080")
        pathLabel = tkinter.Label(self.eemps, textvariable=self.path, )
        self.path = "No File Selected"
        self.eemps.update()
        filebutton.place(width=30, height=30, x=20, y=20)
        pathLabel.place(width = 400, height=30, x=70, y=20)
        self.playpausebutton = tkinter.Button(self.eemps, command=self.playpauselogic,  bg="#008080")
        self.playpausebutton.place(width=30, height=30, x=20, y=70)

        self.eemps.mainloop()
        #mixer.music.play()

    def chooseFile(self):
        self.filename = tkinter.filedialog.askopenfilename(initialdir="/", title="Select file",
                                                   filetypes=(("MP3 files", "*.mp3"),("All files","*.*")))
        mixer.music.load(self.filename)
        mixer.music.set_volume(.1)
        mixer.music.play()
        self.v.set(self.filename)
        self.eemps.update()

    def playpauselogic(self):
        if self.paused:
            self.unpauseMusic()
            self.paused = False
        else:
            self.pauseMusic()
            self.paused = True


    #def playMusic(self):
    #    mixer.music.play()

    def pauseMusic(self):
        mixer.music.pause()

    def unpauseMusic(self):
        mixer.music.unpause()
