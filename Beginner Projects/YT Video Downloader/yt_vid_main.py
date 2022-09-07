'''
A simple Youtube Video Downloader with GUI
Made in python with pytube and tkinter
author: Dama D. Daliman (a.k.a RunningPie)
'''

# import the libraries used
from PIL import Image, ImageTk  # library for image processing
from io import BytesIO  # library to handle byte input and output
import urllib.request   # library to handle url requests
from pytube import YouTube  # library for interacting with youtube
from tkinter import filedialog  # module for filedialog
from tkinter import messagebox  #module for messagebox
import tkinter as tk   # library for GUI

# define function to ask for save directory
def ask_dir():
    # ask_dir() opens up a filedialog for the user to select the download directory for the video
    
    path_entry = filedialog.askdirectory(mustexist=True)    
    SAVE_PATH.set(path_entry)   
    
def display_thumb():
    global yt
    # display_thumb() shows the video thumbnail and title for user to make sure it is the correct video
    c.delete("all")
    
    try:
        yt = YouTube(str(link.get()))
    except:
        # executed when youtube link is invalid
        yt = ""
        vid_title_label.configure(text="Invalid Youtube Link") 
        messagebox.showwarning(title="Invalid Link", message="Please enter a valid youtube link")
    
    # creates thumbnail image to show on canvas    
    raw_data = urllib.request.urlopen(yt.thumbnail_url).read()
    im = Image.open(BytesIO(raw_data)).resize((384, 216))
    image = ImageTk.PhotoImage(im)
    window.image = image
    c.create_image((0,0), anchor="nw", image=image)
    vid_title_label.configure(text=yt.title) 

# define function to download the yt video
def Download_Video():
    # Download_Video() performs the download through pytube
    global yt
    global vid_to_down
    
    try:
        yt = YouTube(str(link.get()))
    except:
        # executed when youtube link is invalid
        yt = ""
        vid_title_label.configure(text="Invalid Youtube Link") 
        messagebox.showwarning(title="Invalid Link", message="Please enter a valid youtube link")
    
    
    # Validating download directory
    if str(SAVE_PATH.get()) == "":
        messagebox.showwarning(title="Empty Directory", message="Please enter a directory to save the video to")
    else:
        print(yt.streams.filter(progressive=True).get_highest_resolution().itag)
        iTagHighestResVideo = yt.streams.filter(progressive=True).get_highest_resolution().itag

        # try:
        vid_to_down = yt.streams.get_by_itag(iTagHighestResVideo)
        vid_to_down.download(output_path=str(SAVE_PATH.get()), filename=str(savename.get())+".mp4")
        print("Video downloaded")
        down_notice_label.config(text="Video Downloaded Successfully")
        # except:
        #     print("Error in downloading video")
        #     down_notice_label.config(text="Error in downloading video")
    

# setting up the main window for GUI
window_bg = "orange"
window = tk.Tk()
window.geometry("700x1000")
window.config(bg=window_bg)
window.resizable(width=False, height=True)
window.title("YT Video Downloader")

# declaring string variables
SAVE_PATH = tk.StringVar()
link = tk.StringVar()
savename = tk.StringVar()

# Creating a title label
window_title = tk.Label(window,text = "Youtube Video Downloader", font =("Miriam", 20, "bold"),fg="White",bg="Black")
window_title.pack(fill=tk.X)

# This part is for entering the yputube link
link_entry_label = tk.Label(window, text = "Paste Your YouTube Link Here:", font = ("Miriam", 20),fg="Black",bg="#EC7063")
link_enter = tk.Entry(window, width = 53,textvariable = link,font = ("Miriam",15, "bold"),bg="lightgreen")
link_entry_label.place(x= 5 , y = 50)
link_enter.place(x = 5, y = 100)

# This part is for checking the video that will be downloaded
check_video_btn = tk.Button(window,text = 'CHECK VIDEO', font = ("Miriam", 15, "bold") ,fg="white",bg = 'black', padx = 2,command=display_thumb)
c = tk.Canvas(window, width=384, height=216)
vid_title_label = tk.Label(window, text = "", font = ("Miriam", 20, "bold"),fg="White",bg="#EC7063")
check_video_btn.place(x=5 ,y = 150)
c.place(x=100, y=200)
vid_title_label.place(x= 10 , y = 450)

# This part is for directory selecting
path_entry_label = tk.Label(window, text = "Select a directory for download", font = ("Miriam", 20),fg="Black",bg="#EC7063")
browse_btn = tk.Button(window,text = "BROWSE", font = ("Miriam", 15, "bold") ,fg="white",bg = 'black', padx = 2,command=ask_dir)
selected_dir_label = tk.Label(window, text = "Selected directory: ", font = ("Miriam", 20),fg="Black",bg="#EC7063")
show_selected_dir = tk.Label(window, textvariable = SAVE_PATH, font = ("Miriam", 10, "bold"),fg="Black",bg="#EC7063")
path_entry_label.place(x= 5 , y = 500)
browse_btn.place(x=5 ,y = 550)
selected_dir_label.place(x= 5 , y = 600)
show_selected_dir.place(x= 5 , y = 650)

# This part is for entering a filename for the video that will be downloaded
filename_label = tk.Label(window, text = "Enter file name: ", font = ("Miriam", 20),fg="Black",bg="#EC7063")
filename_label.place(x= 5 , y = 700)
savename_entry = tk.Entry(window, width = 53,textvariable = savename,font = ("Miriam", 15, "bold"),bg="lightgreen")
savename_entry.place(x = 5, y = 750)

# Button for performing the download
down_btn = tk.Button(window,text = "DOWNLOAD VIDEO", font = ("Miriam", 15, "bold") ,fg="white",bg = 'black', padx = 2,command=Download_Video)
down_notice_label = tk.Label(window, text = '', font = ("Miriam", 20, "bold"),fg="White",bg=window_bg)
down_btn.place(x=385 ,y = 800)
down_notice_label.place(x= 100 , y = 850)

window.mainloop()
