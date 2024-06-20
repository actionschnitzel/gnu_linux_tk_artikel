## Teil 4 ###
import tkinter as tk
from PIL import Image, ImageTk


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

user_host_label = tk.Label(stat_frame,text="USER@HOST")
user_host_label.pack(anchor=tk.NW)

user_host_label = tk.Label(stat_frame,text="OS:")
user_host_label.pack(anchor=tk.NW)

# Starte die Hauptschleife
root.mainloop()