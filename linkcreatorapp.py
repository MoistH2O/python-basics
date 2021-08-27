#import modules required for window generation and time/date gathering
import tkinter as tk
import datetime
import os
import subprocess

#check for link folder and make one if needed on desktop
cwd = str(os.getcwd())
dir_slash_1 = cwd.find("\\")
dir_slash_2 = cwd.find("\\",dir_slash_1+1)
dir_slash_3 = cwd.find("\\",dir_slash_2+1)
cwd = cwd[0:dir_slash_3]
cwd = cwd+"\\Desktop\\links"
isdir = os.path.isdir(cwd)
if isdir == False:
    os.mkdir(cwd)

#create a window object
window = tk.Tk()

link_selection_frame = tk.Frame(
master=window,
    width=100,
    height=10,
    relief=tk.RAISED,
    borderwidth=3,
    bg="red"
)
link_selection_frame.pack(
    fill=tk.BOTH,
    side=tk.BOTTOM,
    expand=True
)

list_of_link_names = []
list_of_link_buttons = []
for entry in os.scandir(cwd):
    if entry.path.endswith(".bat") and entry.is_file():
        entry_name = str(entry)
        firstapos = entry_name.find("'")
        secondapos = entry_name.find(".bat")
        entry_name = entry_name[firstapos + 1:secondapos]
        list_of_link_names.append(entry_name)
    link_button_name = entry_name+"_button"
    list_of_link_buttons.append(link_button_name)
    link_button_name = tk.Button(
        master=link_selection_frame,
        borderwidth=3,
        text=entry_name,
    )
    link_button_name.pack(side=tk.RIGHT, padx=5, pady=10)
    link_button_name.bind("<Button-1>", subprocess.call([cwd+"\\"+entry_name+".bat"]))


#create a frame for the generate link button
frame_download_button = tk.Frame(
    master=window,
    width=100,
    height=10,
    bg="red"
)
#place frame for the generate link button
frame_download_button.pack(
    fill=tk.BOTH,
    side=tk.BOTTOM,
    expand=True
)
#create the generate link button
download_button = tk.Button(
    master=frame_download_button,
    borderwidth=3,
    text="Press to create link",
)
download_button.pack(fill=tk.X, padx=5, pady=10)
def download_button_click(event):
    global url
    url = url_entry.get()
    global link_title
    link_title = link_title_entry.get()
    t = datetime.datetime.now()
    t = str(t)
    if link_title == "Name this link:" or len(link_title) == 0:
        link_title = "link" + " " + t
    save_path = cwd + "\\"
    f = open(save_path+link_title+".bat", "w")
    f.write('@echo off\nstart "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"' + " " + url +"\nexit")
    f.close()
    url_entry.delete(0, tk.END)
    link_title_entry.delete(0, tk.END)
    url_entry.insert(0, "Link Created!")
    link_title_entry.insert(0, "Link Created!")
download_button.bind("<Button-1>",download_button_click)


exit_button = tk.Button(
    master=frame_download_button,
    borderwidth=3,
    text="Exit",
)
exit_button.pack(
    side=tk.RIGHT,
    padx=5,
    pady=10
)
def exit_button_click(event):
    exit()
exit_button.bind("<Button-1>",exit_button_click)

#create a frame for the url entry
frame_url_entry = tk.Frame(
    master=window,
    width=300,
    height=10,
    bg="light blue"
)
#place frame for the the url entry
frame_url_entry.pack(
    fill=tk.BOTH,
    side=tk.BOTTOM,
    expand=True
)
#create an entry for url
url_entry = tk.Entry(
    master=frame_url_entry,
    width=100,
)
#place url entry
url_entry.pack(fill=tk.Y, padx=5, pady=10)
url_entry.insert(0,"Paste link here:")
def url_click(event):
    url_entry.delete(0, tk.END)
url_entry.bind("<Button-1>",url_click)

frame_link_title = tk.Frame(
    master=window,
    width=100,
    height=10,
    bg="light blue")
frame_link_title.pack(
    fill=tk.BOTH,
    side=tk.RIGHT,
    expand=True
)
link_title_entry = tk.Entry(
    master=frame_link_title,
    width=100
)
link_title_entry.pack(padx=5, pady=10)
link_title_entry.insert(0,"Name this link:")
def link_title_click(event):
    link_title_entry.delete(0, tk.END)
link_title_entry.bind("<Button-1>",link_title_click)

frame_title = tk.Frame(
    master=window,
    relief=tk.RAISED,
    borderwidth=3,
    width=50,
    height=10,
    bg="grey")
frame_title.pack(
    fill=tk.BOTH,
    side=tk.LEFT,
    expand=True
)
label_title = tk.Label(
    master=frame_title,
    text="Link App",
    relief=tk.RAISED,
    borderwidth=3,
    fg="white",
    bg="blue",
)
label_title.pack(padx=5, pady=5)

window.mainloop()