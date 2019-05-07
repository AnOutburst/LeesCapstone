import tkinter
from pygame import mixer
import tkinter.filedialog
from PIL import Image, ImageTk

class mp3:
    paused = False
    path = ""
    plps = "pause"
    mixer.init()
    # v = tkinter.StringVar()
    filename = ""

    # mixer.music.load('D:/UserFiles/Music/Akira/Battle Against Clown.mp3')
    # mixer.music.play()
    def __init__(self):
        global fileImg, playImg, pauseImg
        self.eemps = tkinter.Tk()
        self.eemps.configure(background="#008080")
        self.eemps.title("MP3 Player")
        self.eemps.geometry("600x300")
        self.v = tkinter.StringVar()
        print(self.v.get())
        # image = tkinter.Image("file.png")
        # fileImg = tkinter.PhotoImage("file.png")
        # image=tkinter.PhotoImage("file.png")
        #PIL.ImageTk.PhotoImage(
        #fileImg = ImageTk.PhotoImage(Image.open("calculator.png"))
        filebutton = tkinter.Button(self.eemps, command=self.chooseFile, bg="#008080", text="file")
        pathLabel = tkinter.Label(self.eemps, textvariable=self.path, )
        self.path = "No File Selected"
        self.eemps.update()
        filebutton.place(width=30, height=30, x=20, y=20)
        pathLabel.place(width=400, height=30, x=70, y=20)
        self.play = tkinter.Button(self.eemps, command=self.unpauseMusic, bg="#008080", text="play")
        self.pause = tkinter.Button(self.eemps, command=self.pauseMusic, bg="#008080", text="pause")
        self.play.place(width=40, height=40, x=20, y=70)
        self.pause.place(width=40, height=40, x=80, y=70)

        self.eemps.mainloop()
        # mixer.music.play()

    def chooseFile(self):
        self.eemps.update_idletasks()
        self.filename = tkinter.filedialog.askopenfilename(initialdir="/", title="Select file",
                                                           filetypes=(("MP3 files", "*.mp3"), ("All files", "*.*")))
        mixer.music.load(self.filename)
        mixer.music.set_volume(.1)
        mixer.music.play()
        self.v.set(self.filename)
        self.plps = "pause"
        self.eemps.update()

    def playpauselogic(self):
        if self.paused:
            self.unpauseMusic()
            self.paused = False
            self.plps = "pause"
        else:
            self.pauseMusic()
            self.paused = True
            self.plps = "play"

    # def playMusic(self):
    #    mixer.music.play()

    def pauseMusic(self):
        mixer.music.pause()

    def unpauseMusic(self):
        mixer.music.unpause()
