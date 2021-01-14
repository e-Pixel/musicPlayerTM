from pygame import mixer
import tkinter as tk 
from functools import partial
import os 

'''

mixer.init() 

# command 
mixer.music.load("test.mp3")
mixer.music.set_volume(0.6)

mixer.music.play() # the real one 

while True:
    pause = None # useful for later 

    print("Press 'p' to pause")
    print("Press 'r' to resume")
    print("Press 'v' set volume")
    print("Press 'e' to exit")
    ch = input("['p','r','v','e']>>>").lower()
    if ch == "p":
        if (pause == True):
            mixer.music.unpause()
        mixer.music.pause()
        pause = True
    elif ch == "r":
        mixer.music.unpause()
    elif ch == "v":
        v = float(input("Enter volume(0 to 1): "))
        mixer.music.set_volume(v)
    elif ch == "e":
        mixer.music.stop()
        break 
    
    
'''


class Music:
    
    def setUp(self):
        mixer.init(channels = 1) # channel 1 = stereo 
        print(mixer.get_init(), "(FREQUENCY, FORMAT, CHANNELS)")

    def writeEvery(self):
        print("YEP COCK")

    def actionWithArgument(self, arg):
        print(arg)

    def setPointer(self,filename):
        mixer.music.load("texting/" + filename)
        mixer.music.play()

class Application(tk.Frame):
    starting = Music()
    starting.setUp()

    channel_1 = mixer.Channel(0)
    channel_2 = mixer.Channel(1)

    def __init__(self, master = None):
        super().__init__(master)
        master.title("Spotify 2: Artists\' Strike Back")
        icon = tk.PhotoImage(file = "spoti.png")
        master.iconphoto(False, icon)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        appMusic = Music()

        def changeTXT(newText):
            self.theText.delete("1.0", "end")
            self.theText.insert(tk.END, newText)

        flist = os.listdir("texting/")
        lbox = tk.Listbox(self)
        songToPlay = None # CHANGE THIS (be able to change through songs)
        toPlay = None
        
        def opensystem(event):
            x = lbox.curselection()[0]
            os.system(lbox.get(x))
        
        def returnValue(filename):
            mixer.music.load("texting/" + filename)
            mixer.music.play()

        def CurSelet(evt):
            value=str((lbox.get(tk.ANCHOR)))
            global songToPlay
            global toPlay

            songToPlay = value
            toPlay = partial(appMusic.setPointer, songToPlay) # CHECK OUT LATER
            
            returnValue(songToPlay)

            changeTXT(f"Currently playing [ {songToPlay} ]")
            print(type(songToPlay))
            return value
        
        def pausing():
                mixer.music.pause()
                changeTXT("Currently playing [ Nothing ]")
    # THE ITEMS INSERTED WITH A LOOP
        for item in flist:
            print(item)
            lbox.insert(tk.END, item)

        self.pause = tk.Button(self)
        self.pause["text"] = "PAUSE"
        self.pause["command"] = pausing 

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)


        # action_with_args = partial(action, arg1, arg2... argN)

        txtVar = tk.StringVar()
        self.theText = tk.Text()
        self.theText.insert(tk.INSERT, f"Currently playing [ Nothing ]")

        # lbox.bind('<<ListboxSelect>>',CurSelet)
        lbox.bind("<Double-Button-1>", CurSelet)

        lbox.pack(side = "bottom")
        # self.quit.pack(side="bottom") # NOT NECESSARY 
        self.theText.pack(side = "bottom", expand = 1)
        self.pause.pack(side = "top", expand = 1)  

    def checkBusy(self):
        if mixer.get_busy() == True:
            print(":D/ OCCUPIED")
        else: print("nah bro im good")

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
root.geometry("500x250+300+300")
app = Application(master = root)
app.mainloop()
