import tkinter
import vlc


class player:

    path=""
    #p = vlc.MediaPlayer("file:resonance.mp3")

    def __init__(self):
        #self.p.play()
        gui = tkinter.Tk()
        gui.configure(background="#008080")
        gui.title("MP3 Player")
        gui.geometry("600x300")

