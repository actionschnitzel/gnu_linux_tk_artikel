## Teil 6 ###

#https://thepythoncode.com/article/get-hardware-system-information-python

import tkinter as tk
from PIL import Image, ImageTk
import os
import socket
import distro
import platform
import psutil



def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor
        
        
user = os.environ["USER"]
hostname = socket.gethostname()
os_release_pretty = distro.name(pretty=True)
kernel_release = platform.release()
svmem = psutil.virtual_memory()


# Erstelle das Hauptfenster
root = tk.Tk()
root.title("Neofetch-Tk")
root.geometry("800x500")

distro_logo = tk.PhotoImage(file="images/test.png")

# Einen Frame Zeichen
logo_frame = tk.Frame(root,background="yellow")
logo_frame.pack(fill="both",expand=False,side='left',padx=10,pady=10)

# Distro-Logo-Label
distro_icon = tk.Label(logo_frame,text="DISTRO LOGO",image=distro_logo,background="yellow")
distro_icon.pack(anchor=tk.NW)

# Einen Frame Zeichen
stat_frame = tk.Frame(root,background="cyan")
stat_frame.pack(fill="both",expand=True,side='left',padx=10,pady=10)

# Label mit Text USER@HOST
user_host_label = tk.Label(stat_frame,text=f"{user}@{hostname}")
user_host_label.pack(anchor=tk.NW)

# Label mit Text OS:
os_label = tk.Label(stat_frame,text=f"OS: {os_release_pretty}")
os_label.pack(anchor=tk.NW)

host_label = tk.Label(stat_frame,text=f"Host: {hostname}")
host_label.pack(anchor=tk.NW)

kernel_label = tk.Label(stat_frame,text=f"Kernel: {kernel_release}")
kernel_label.pack(anchor=tk.NW)

mem_label = tk.Label(stat_frame,text=f"Memory: {(get_size(svmem.used))}/{get_size(svmem.total)}")
mem_label.pack(anchor=tk.NW)

# Starte die Hauptschleife
root.mainloop()
