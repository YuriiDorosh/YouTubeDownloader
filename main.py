
from tkinter import *
from pytube import YouTube
from tkinter import messagebox

# Reasking if User wanna to leave the app

def on_closing():
    if messagebox.askokcancel('Exit', 'Do You want to exit the App?\n Process will be stopped'):
        root.destroy()


root = Tk()
root.geometry('500x300')
root.eval('tk::PlaceWindow . center')
root.iconbitmap('youtubedowloader.ico')
root.protocol('WM_DELETE_WINDOW', on_closing)
root.wm_attributes('-topmost', 1)
root.resizable(0,0)
root.title("YouTube Downloader(720p,30fps)")
root.configure(bg='White')




Label(root, text = "YouTube Downloader", font = "Arial_black 18 bold").pack()

link = StringVar()
Label(root, text = "Paste the video link:", font = "arial 15 bold").place(x=155, y = 60)
link_enter = Entry(root, width = 70, textvariable = link).place(x = 30, y = 90)

def Downloader():
	url = YouTube(str(link.get()))
	video = video = url.streams.get_by_itag(22) #itag ( you can change tag to one from this site: https://pypi.org/project/pytube3/)
	video.download()
	Label(root, text = "Successfully!", font = "arial 15").place(x=187, y = 210)
	Label(root, text = f"Video title: {video.title}", font = "arial 12").place(x=20, y = 260)

Button(root, text = "Dowload", font = "arial 14 bold", bg = "Red", padx = 2, command = Downloader).place(x=195, y=150)




root.mainloop()