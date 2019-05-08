import tkinter
from pygame import mixer
import tkinter.filedialog

class mp3:
    paused = False
    mixer.init()
    filename = "No File Selected"

    def __init__(self):
        global fileImg, playImg, pauseImg
        self.eemps = tkinter.Toplevel()
        self.eemps.configure(background="#008080")
        self.eemps.title("MP3 Player")
        self.eemps.geometry("500x130")
        self.v = tkinter.StringVar()
        self.v.set(self.filename)
        self.plps = tkinter.StringVar()
        self.plps.set("pause")
        filebutton = tkinter.Button(self.eemps, command=self.chooseFile, bg="#008080", text="file")
        pathLabel = tkinter.Label(self.eemps, textvariable=self.v, )
        self.eemps.update()
        filebutton.place(width=30, height=30, x=20, y=20)
        pathLabel.place(width=400, height=30, x=70, y=20)
        self.play = tkinter.Button(self.eemps, command=self.playpauselogic, bg="#008080", textvariable=self.plps)
        self.stop = tkinter.Button(self.eemps, command=self.stopMusic, bg="#008080", text="stop")
        self.play.place(width=40, height=40, x=20, y=70)
        self.stop.place(width=40, height=40, x=80, y=70)

        self.eemps.mainloop()

    def chooseFile(self):
        self.eemps.update_idletasks()
        self.filename = tkinter.filedialog.askopenfilename(initialdir="Music", title="Select file",
                                                           filetypes=(("MP3 files", "*.mp3"), ("All files", "*.*")))
        mixer.music.load(self.filename)
        mixer.music.set_volume(.1)
        mixer.music.play()
        self.v.set(self.filename.rsplit('/', 1)[-1])
        print(self.v.get())
        self.plps.set("pause")
        self.paused = False
        self.eemps.update()

    def playpauselogic(self):
        if self.paused:
            self.unpauseMusic()
            self.paused = False
            self.plps.set("pause")
        else:
            self.pauseMusic()
            self.paused = True
            self.plps.set("play")

    def pauseMusic(self):
        mixer.music.pause()

    def unpauseMusic(self):
        mixer.music.unpause()

    def stopMusic(self):
        mixer.music.stop()
        self.paused = False
        self.plps.set("pause")
        self.filename = ""
        self.v.set("No File Selected")
