from tkinter import *
from tkinter import ttk
from pytube import YouTube,Playlist

#Create an instance of tkinter frame or window
win= Tk()
#Set the geometry of tkinter frame
win.geometry("1550x1250")

def get_value():
   e_text=entry.get()
   e_text1=int(entry2.get())
   e_text3=entry3.get()
   Label(win, text=e_text, font= ('Century 15 bold')).pack(pady=20)
   Label(win, text=e_text1, font=('Century 15 bold')).pack(pady=20)
   Label(win, text=e_text3, font=('Century 15 bold')).pack(pady=20)

   p=Playlist(e_text)
   for url in p.video_urls[: e_text1]:
      mp4 = YouTube(url).streams.get_highest_resolution().download(output_path=e_text3)



#Create an Entry Widget
entry= ttk.Entry(win,font=('Century 12'),width=40)
entry.pack(pady= 30)

entry2= ttk.Entry(win,font=('Century 12'),width=40)
entry2.pack(pady= 30)

entry3= ttk.Entry(win,font=('Century 12'),width=40)
entry3.pack(pady= 30)



#Create a button to display the text of entry widget
button= ttk.Button(win, text="Enter", command= get_value)
button.pack()

win.mainloop()
