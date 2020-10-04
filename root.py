#@abdeljalilsalhi
from tkinter import *
from tkinter import messagebox
import youtube_dl

root = Tk(className="yt Downloader @abdeljalilsalhi")
root.iconphoto(True, PhotoImage(file="icon.png"))
root.configure(bg="black")
root.resizable(width=False, height=False)
bgc = "black"
fgc = "#00FFFF"

def DLok():
    if ytTYPEradioVar.get() == '1':
        audioDL()
    elif ytTYPEradioVar.get() == '2':
        videoDL()
    else:
        messagebox.showerror("Choose", "Choose the download type you want.")

def audioDL():
    YTlink = ytLINKentryVar.get()
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([YTlink])
        messagebox.showinfo("Done...", "Video downloaded to format .MP3")
    except:
        messagebox.showerror("Error...", "ERROR !")

def videoDL():
    YTlink = ytLINKentryVar.get()
    try:
        ydl_opts = {}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([YTlink])
        messagebox.showinfo("Done...", "Video downloaded to format .MP4")
    except:
        messagebox.showerror("Error...", "ERROR !")

rootTitle = Label(root, text="Youtube Downloader @abdeljalilsalhi", font=32, bg=bgc, fg=fgc)
rootTitle.grid(row=0, column=1)
#YOUTUBE DOWNLOADER FRAME
ytDLframe = LabelFrame(root, text="YOUTUBE DOWNLOADER", fg=fgc, bg=bgc)
ytDLframe.grid(row=1, column=0, columnspan=3, padx=10, pady=5)
ytTYPEradioVar = StringVar()
ytTYPEradio1 = Radiobutton(ytDLframe, text="AUDIO DOWNLOAD", variable=ytTYPEradioVar, value="1",
                           fg=fgc, bg=bgc, activebackground=bgc, activeforeground=fgc)

ytTYPEradio1.grid(row=0, column=1)
ytTYPEradio2 = Radiobutton(ytDLframe, text="VIDEO DOWNLOAD", variable=ytTYPEradioVar, value="2",
                           fg=fgc, bg=bgc, activebackground=bgc, activeforeground=fgc)
ytTYPEradio2.grid(row=1, column=1)
ytLINKlabel = Label(ytDLframe, text="VIDEO LINK", fg=fgc, bg=bgc)
ytLINKlabel.grid(row=2, column=0, sticky=W)
ytLINKentryVar = StringVar()
ytLINKentry = Entry(ytDLframe, textvariable=ytLINKentryVar, width=40)
ytLINKentry.grid(row=3, column=0, columnspan=3, sticky=W, pady=5)
ytDLbutton = Button(ytDLframe, text="DOWNLOAD", cursor="cross", command=DLok,
                    bg=bgc, fg=fgc, pady=5)
ytDLbutton.grid(row=4, column=0)

root.mainloop()
