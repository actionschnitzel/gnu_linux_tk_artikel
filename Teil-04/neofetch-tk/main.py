import tkinter as tk
from PIL import Image, ImageTk


# Erstelle das Hauptfenster
root = tk.Tk()
root.title("Neofetch-Tk")
root.geometry("800x500")

distro_logo = tk.PhotoImage(file="images/test.png")

# Einen Frame Zeichen
logo_frame = tk.Frame(root,background="yellow",padx=20,pady=20)
logo_frame.pack(fill="both",expand=False,side='left')

# Distro-Logo-Label
distro_icon = tk.Label(logo_frame,background="yellow",text="DISTRO LOGO",image=distro_logo)
distro_icon.pack(anchor=tk.NW)

# Einen Frame Zeichen
stat_frame = tk.Frame(root,background="cyan")
stat_frame.pack(fill="both",expand=True,side='left')


# Starte die Hauptschleife
root.mainloop()