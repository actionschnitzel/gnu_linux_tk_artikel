## Teil 8 ###


import tkinter as tk
from PIL import Image, ImageTk
import os
import socket
import distro
import platform
import psutil
import datetime


# Macht die RAM-Größe lesbar
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

# Findet die Auflösung heraus
def get_screen_size():
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    return f"{screen_width}x{screen_height}"

def get_sys_uptime():

    # System-Startzeit ermitteln
    boot_time_timestamp = psutil.boot_time()
    boot_time = datetime.datetime.fromtimestamp(boot_time_timestamp)

    # Aktuelle Zeit
    now = datetime.datetime.now()

    # Uptime berechnen
    uptime = now - boot_time

    # Uptime in Stunden und Minuten umrechnen
    uptime_hours, remainder = divmod(uptime.total_seconds(), 3600)
    uptime_minutes = remainder // 60
    
    # Weist an das diese Funktion Stunden und Minuten ausgeben soll
    return f"{int(uptime_hours)} h , {int(uptime_minutes)} m"

# Setzt das korrekte Logo für die Distro
def get_distro_logo():
    if distro_id == "debian":
        distro_icon.configure(image=debian_logo)
    elif distro_id == "arch":
        distro_icon.configure(image=arch_logo)        
    elif distro_id == "linuxmint":
        distro_icon.configure(image=mint_logo)
    elif distro_id == "ubuntu":
        distro_icon.configure(image=ubuntu_logo)
    elif distro_id == "opensuse":
        distro_icon.configure(image=osuse_logo)
    elif distro_id == "fedora":
        distro_icon.configure(image=fedora_logo)
    else:
       distro_icon.configure(image=distro_logo)




# Vars für die Labels
# Ließt den User aus
user = os.environ["USER"]
# Ließt den Host aus
hostname = socket.gethostname()
# Ließt den Pretty Name  aus
os_release_pretty = distro.name(pretty=True)
# Ließt den Kernel aus
kernel_release = platform.release()
# Basis um den RAM auszulesen
svmem = psutil.virtual_memory()
# Basis um CPU-Werte auszulesen
cpu_freq = psutil.cpu_freq()
# Ließt Anzahl der CPU-Kerne aus
cpu_core_count = psutil.cpu_count(logical=False)
# Gibt die aktuelle Shell aus
active_shell = os.environ["SHELL"]
# Gibt die Distro-ID aus
distro_id = distro.id()






# Erstelle das Hauptfenster
root = tk.Tk()
root.title("Neofetch-Tk")
root.geometry("800x500")

# Distro Logos
distro_logo = tk.PhotoImage(file="images/test.png")
arch_logo = tk.PhotoImage(file="images/arch_logo_350.png")
debian_logo = tk.PhotoImage(file="images/debian_logo_350.png")
mint_logo = tk.PhotoImage(file="images/mint_logo_350.png")
suse_logo = tk.PhotoImage(file="images/osuse_logo_350.png")
ubuntu_logo = tk.PhotoImage(file="images/ubuntu_logo_350.png")
fedora_logo = tk.PhotoImage(file="images/fedora_logo_350.png")



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

# Label mit Text Host:
host_label = tk.Label(stat_frame,text=f"Host: {hostname}")
host_label.pack(anchor=tk.NW)

# Label mit Text Kernel:
kernel_label = tk.Label(stat_frame,text=f"Kernel: {kernel_release}")
kernel_label.pack(anchor=tk.NW)

# Label mit Text Uptime:
uptime_label = tk.Label(stat_frame,text=f"Uptime: {get_sys_uptime()}")
uptime_label.pack(anchor=tk.NW)

# Label mit Text Shell:
shell_label = tk.Label(stat_frame,text=f"Shell: {active_shell}")
shell_label.pack(anchor=tk.NW)

# Label mit Text Resolution:
res_label = tk.Label(stat_frame,text=f"Resolution: {get_screen_size()}")
res_label.pack(anchor=tk.NW)

# Label mit Text CPU:
cpu_label = tk.Label(stat_frame,text=f"CPU: ({cpu_core_count}) @ {cpu_freq.max:.2f} Mhz")
cpu_label.pack(anchor=tk.NW)

# Label mit Text Memory:
mem_label = tk.Label(stat_frame,text=f"Memory: {(get_size(svmem.used))}/{get_size(svmem.total)}")
mem_label.pack(anchor=tk.NW)

# Führt get_distro_logo aus
get_distro_logo()

# Starte die Hauptschleife
root.mainloop()
