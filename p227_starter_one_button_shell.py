# p227_starter_one_button_shell.py
# Note this will not run in the code editor and must be downloaded

import subprocess
import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename


def do_command(command):
    global command_textbox
    subprocess.call("ping localhost")
global command_textbox, url_entry
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

# Save function.
def mSave():
  filename = asksaveasfilename(defaultextension='.txt',filetypes = (('Text files', '*.txt'),('Python files', '*.py *.pyw'),('All files', '*.*')))
  if filename is None:
    return
  file = open (filename, mode = 'w')
  text_to_save = command_textbox.get("1.0", tk.END)
  
  file.write(text_to_save)
  file.close()

# Makes the command button pass it's name to a function using lambda
ping_btn = tk.Button(frame, text="Check to see if a URL is up and active", command=lambda:do_command("ping"))
ping_btn.pack()

# tracert button
tracert_btn = tk.Button(frame, text="Tracert Button", command=lambda:do_command("tracert"))
tracert_btn.pack()

# nslookup button
nslookup_btn = tk.Button(frame, text="Nslookup Button", command=lambda:do_command("nslookup"))
nslookup_btn.pack()

# creates the frame with label for the text box
frame_URL = tk.Frame(root, pady=10,  bg="black") # change frame color
frame_URL.pack()

# decorative label
url_label = tk.Label(frame_URL, text="Enter a URL of interest: ", 
    compound="center",
    font=("comic sans", 14),
    bd=0, 
    relief=tk.FLAT, 
    cursor="heart",
    fg="mediumpurple3",
    bg="black")
url_label.pack(side=tk.LEFT)
url_entry= tk.Entry(frame_URL,  font=("comic sans", 14)) # change font
url_entry.pack(side=tk.LEFT)

frame = tk.Frame(root,  bg="black") # change frame color
frame.pack()

# Adds an output box to GUI.
command_textbox = tksc.ScrolledText(frame, height=10, width=100)
command_textbox.pack()

root.mainloop()