# p227_starter_one_button_shell.py
# Note this will not run in the code editor and must be downloaded

import subprocess
import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename
from tkinter import ttk



def do_command(command):
    global command_textbox, url_entry

    # If url_entry is blank, use localhost IP address 
    url_val = url_entry.get()
    if (len(url_val) == 0):
        # url_val = "127.0.0.1"
        url_val = "::1"
    
    command_textbox.delete(1.0, tk.END)
    command_textbox.insert(tk.END, command + " working....\n")
    command_textbox.update()

    with subprocess.Popen(command + ' ' + url_val, stdout=subprocess.PIPE, bufsize=1, universal_newlines=True) as p:
        for line in p.stdout:
            command_textbox.insert(tk.END,line)
            command_textbox.update()
root = tk.Tk()
root.geometry("500x300")
frame = tk.Frame(root, width=50, height=100)
frame.pack(side="left", padx=10, pady=20)

# adds border to frame
frame['borderwidth'] = 2
frame['relief'] = 'sunken'

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
ping_btn = tk.Button(frame, text="Ping", command=lambda:do_command("ping"))
ping_btn.pack()


# tracert button
tracert_btn = tk.Button(frame, text="Tracert", command=lambda:do_command("tracert"))
tracert_btn.pack()

# nslookup button
nslookup_btn = tk.Button(frame, text="Nslookup", command=lambda:do_command("nslookup"))
nslookup_btn.pack()

# combo box

combo = ttk.Combobox(root,values=["Ping", "Tracert", "Nslookup","Ping/Tracert","Ping/Nslookup","Tracert/Nslookup","Hide All"],state="readonly")
combo.pack(padx=20, pady=20)


# creates the frame with label for the text box
frame_URL = tk.Frame(root, pady=10,) # change frame color
frame_URL.pack()

# border for url entry
frame['borderwidth'] = 2
frame['relief'] = 'sunken'

# decorative label
url_label = tk.Label(frame_URL, text="Enter URL: ", 
    compound="center",
    font=("comic sans", 14),
    bd=0, 
    relief=tk.FLAT, 
    fg="white",
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