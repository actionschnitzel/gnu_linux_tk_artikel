from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk


# Erstelle das Hauptfenster
root = tk.Tk()
root.title("Neofetch-Tk")
root.geometry("800x500")

distro_id = "debian"

if distro_id == "test":
    distro_logo = PhotoImage(file="images/test.png")
else:
    distro_logo = PhotoImage(file="images/dist-logo-debian-350x350.png")
    



# Einen Frame Zeichen
logo_frame = Frame(root,background="yellow",padx=20,pady=20)
logo_frame.pack(fill="both",expand=False,side='left')

# Distro-Logo-Label
distro_icon = Label(logo_frame,background="yellow",text="DISTRO LOGO",image=distro_logo)
distro_icon.pack(anchor=tk.NW)

# Einen Frame Zeichen
stat_frame = Frame(root,background="cyan")
stat_frame.pack(fill="both",expand=True,side='left')


# Starte die Hauptschleife
root.mainloop()
