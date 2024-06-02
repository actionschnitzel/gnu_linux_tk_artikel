from tkinter import *
import tkinter as tk

# Erstelle das Hauptfenster
root = tk.Tk()
root.title("Neofetch-Tk")
root.geometry("400x300")


# Einen Frame Zeichen
logo_frame = Frame(root,background="yellow")
logo_frame.pack(fill="both",expand=True,side='left')
# Einen Frame Zeichen
stat_frame = Frame(root,background="cyan")
stat_frame.pack(fill="both",expand=True,side='left')


# Starte die Hauptschleife
root.mainloop()
