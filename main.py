from ctypes import alignment
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from pytube import YouTube
import traceback

# Create window
window = Tk()
window.title("Downloader")
window.geometry('350x300')
window.resizable(False, False)

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

progressbar=ttk.Progressbar(window, orient=HORIZONTAL, length=200, mode='determinate')
progressbar.place(x=175, y=200, anchor="center"), 


# Video download function and error reporting
def clicked():
        global filesize
        # progressbar['value']=0
        lbl.config(text="Downloading...", fg="orange")
        filepath = filedialog.askdirectory()
        url = urlinput.get()
        
        try:
                # Download the video
                yt = YouTube(url)
                filesize = yt.streams.filter(file_extension='mp4', progressive=True).get_highest_resolution().filesize
                # Register the callback function
                yt.register_on_progress_callback(progress)
                yt.streams.filter(file_extension='mp4', progressive=True).get_highest_resolution().download(filepath)
                lbl.config(text="Downloaded", fg="green")
        except Exception as e:
                # Update error label text
                print(traceback.print_exc())
                errlbl.config(text="Error\n" + repr(e), fg="red", wraplength=300, borderwidth=0, relief="solid", justify="center")
                errlbl.place_configure(y=135, x=175, anchor="center")
                lbl.config(text="Failed", fg="red")


# Update progress bar with video download progress
def progress(chunk, file_handle, bytes_remaining):
        remaining = (100 * bytes_remaining) / filesize
        step = 100 - int(remaining)
        print(step)
        progressbar['value'] = step
        progressbar.update()

# Create download button
btn = Button(window, text="Download", command=clicked)
btn.pack()
note = Label(window, text="Note: at the moment, the video will be downloaded \nin the highest resolution available, capping out at 720p.")
note.pack()

# Add button that links to Github repo
def openGithub():
        import webbrowser
        webbrowser.open_new("github.com/dairyproducts/ytdownloader")
ghbtn = Button(window, text="????", command=openGithub)
ghbtn.place(x=345, y=295, anchor="se")

metadata = Label(window, text="Version 1.0.0b")
metadata.place(x=5, y=295, anchor="sw")

# Update method
window.mainloop()
