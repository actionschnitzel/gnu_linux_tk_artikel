import tkinter as tk
from PIL import Image, ImageTk
import os
import socket


# Erstelle das Hauptfenster
root = tk.Tk()
root.title("Neofetch-Tk")
root.geometry("800x500")

user = os.getlogin()
hostname = socket.gethostname()

distro_logo = tk.PhotoImage(file="images/test.png")

# Einen Frame Zeichen
logo_frame = tk.Frame(root,background="yellow",padx=20,pady=20)
logo_frame.pack(fill="both",expand=False,side='left')

# Distro-Logo-Label
distro_icon = tk.Label(logo_frame,background="yellow",text="DISTRO LOGO",image=distro_logo)
distro_icon.pack(anchor=tk.NW)

# Einen Frame Zeichen
stat_frame = tk.Frame(root,background="cyan")
stat_frame.pack(fill="both",expand=True,side='left',padx=20,pady=20)

user_at_host = tk.Label(stat_frame,text=f"{user}@{hostname}")
user_at_host.pack(anchor=tk.W)

# Starte die Hauptschleife
root.mainloop()
