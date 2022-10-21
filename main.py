from ctypes import alignment
from tkinter import *
from tkinter import filedialog
from pytube import YouTube

# Create window
window = Tk()
window.title("Downloader")
window.geometry('350x200')

# Create Info Header
lbl = Label(window, text="Video Downloader")
lbl.pack()

# Folder Selection Dialog to select download path
urlinput = Entry(window,width=40)
urlinput.pack()
filepath = ""

# Create placeholder error label
errlbl = Label(window, text="", fg="red")
errlbl.place(y=120)

# Video download function and error reporting
def clicked():
        lbl.config(text="Downloading...", fg="yellow")
        filepath = filedialog.askdirectory()
        url = urlinput.get()
        
        try:
                # Download the video
                yt = YouTube(url)
                yt.streams.filter(file_extension='mp4')
                yt.streams.get_highest_resolution().download(filepath)
                lbl.config(text="Downloaded", fg="green")
        except Exception as e:
                # Update error label text
                errlbl.config(text="Error\n" + repr(e), fg="red", wraplength=300, borderwidth=0, relief="solid", justify="center")
                errlbl.place_configure(y=135, x=175, anchor="center")
                
                lbl.config(text="Failed", fg="red")

# Create download button
btn = Button(window, text="Download", command=clicked)
btn.pack()
note = Label(window, text="Note: at the moment, the video will be downloaded \nin the highest resolution available, capping out at 720p.")
note.pack()

metadata = Label(window, text="Version 1.0.0b")
metadata.place(x=5, y=195, anchor="sw")

# Update method
window.mainloop()
