## Teil 13 ###

import tkinter as tk
from PIL import Image, ImageTk
import os
import socket
import distro
import platform
import psutil
import datetime
import subprocess

# Ließt den Desktop aus
def get_desktop_environment():
    xdg_current_desktop = os.environ.get("XDG_CURRENT_DESKTOP","").lower()

    if xdg_current_desktop == "x-cinnamon" or xdg_current_desktop == "cinnamon":
        return "CINNAMON"
    elif xdg_current_desktop == "unity":
        return "UNITY"
    elif xdg_current_desktop == "ubuntu:gnome":
        return "GNOME"
    elif "gnome" in xdg_current_desktop:
        return "GNOME"
    elif "plasma" == xdg_current_desktop or "kde" == xdg_current_desktop:
        return "KDE"
    elif "xfce" == xdg_current_desktop:
        return "XFCE"
    elif os.environ.get("DESKTOP_SESSION", "").lower() == "lxde-pi-wayfire":
        return "PI-WAYFIRE"
    elif "mate" == xdg_current_desktop:
        return "MATE"
    else:
        return "Unknown"

# Ließt das KDE Theme aus
def get_kde_theme():
    file_path = os.path.expanduser("~/.config/kdeglobals")

    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith("LookAndFeelPackage="):
                look_and_feel = line.strip().split("=")[-1]
                print(line)
                
                if look_and_feel.startswith("org.kde."):
                    look_and_feel = look_and_feel.replace("org.kde.", "")
                return look_and_feel



def get_kde_theme_new():
    # Prüfe die Version von Plasma
    result = subprocess.run(['plasmashell', '--version'], capture_output=True, text=True, check=True)
    plasma_version = result.stdout.strip()
    
    # Pfad zu ~/.config/kdeglobals auflösen
    kdeglobals_path = os.path.expanduser('~/.config/kdeglobals')
    
    if "plasmashell 5." in plasma_version:
        # Verwende kreadconfig5, um das Thema zu lesen
        theme_result = subprocess.run(['kreadconfig5', '--file', kdeglobals_path, '--group', 'KDE', '--key', 'LookAndFeelPackage'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        theme_result_output = theme_result.stdout.strip()
        
        # Entferne "org.", "kde." und ".desktop", falls vorhanden
        look_and_feel = theme_result_output
        
        if look_and_feel.startswith("org."):
            look_and_feel = look_and_feel.replace("org.", "")
        if look_and_feel.startswith("kde."):
            look_and_feel = look_and_feel.replace("kde.", "")
        if look_and_feel.endswith(".desktop"):
            look_and_feel = look_and_feel.replace(".desktop", "")
        
        print(look_and_feel)
        return look_and_feel


    
    elif "plasmashell 6." in plasma_version:
        # Verwende kreadconfig5, um das Thema zu lesen
        theme_result = subprocess.run(['kreadconfig6', '--file', kdeglobals_path, '--group', 'KDE', '--key', 'LookAndFeelPackage'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        theme_result_output = theme_result.stdout.strip()
        
        # Entferne "org.", "kde." und ".desktop", falls vorhanden
        look_and_feel = theme_result_output
        
        if look_and_feel.startswith("org."):
            look_and_feel = look_and_feel.replace("org.", "")
        if look_and_feel.startswith("kde."):
            look_and_feel = look_and_feel.replace("kde.", "")
        if look_and_feel.endswith(".desktop"):
            look_and_feel = look_and_feel.replace(".desktop", "")
        
        print(look_and_feel)
        return look_and_feel



# Ließt das DE-Theme aus
def get_desktop_theme():
    
    if get_desktop_environment() == "GNOME":
        result = subprocess.run(['gsettings', 'get', 'org.gnome.desktop.interface', 'gtk-theme'],capture_output=True,text=True, check=True
        )
        return result.stdout.strip().strip("'")
    
    if get_desktop_environment() == "CINNAMON":
        result = subprocess.run(['gsettings', 'get', 'org.cinnamon.desktop.interface', 'gtk-theme'],capture_output=True,text=True, check=True
        )
        return result.stdout.strip().strip("'")        

    if get_desktop_environment() == "MATE":
        result = subprocess.run(['gsettings', 'get', 'org.mate.interface', 'gtk-theme'],capture_output=True,text=True, check=True
        )
        return result.stdout.strip().strip("'")
    
    if get_desktop_environment() == "XFCE":
        result = subprocess.run(['xfconf-query', '-c', 'xsettings', '-p','/Net/ThemeName'],capture_output=True,text=True, check=True
        )
        return result.stdout.strip().strip("'")
    
    if get_desktop_environment() == "PI-WAYFIRE":
        result = subprocess.run(['gsettings', 'get', 'org.gnome.desktop.interface', 'gtk-theme'],capture_output=True,text=True, check=True
        )
        return result.stdout.strip().strip("'")
    
    if get_desktop_environment() == "KDE":
        return get_kde_theme_new()
        

# Ließt den Window-Manager aus
def get_window_manager_name():
    try:
        result = subprocess.run(
            ["wmctrl", "-m"], capture_output=True, text=True, check=True
        )

        output_lines = result.stdout.strip().split("\n")
        for line in output_lines:
            if line.startswith("Name: "):
                window_manager_name = line.split("Name: ")[1]
                if window_manager_name == "GNOME Shell":
                    return "Mutter"
                return window_manager_name
    except subprocess.CalledProcessError as e:
        print(f"Error running wmctrl: {e}")


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
    elif distro_id == "mint":
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
root["background"]="#FFFFFF" # Weiß

# Distro Logos
distro_logo = tk.PhotoImage(file="images/test.png")
arch_logo = tk.PhotoImage(file="images/arch_logo_350.png")
debian_logo = tk.PhotoImage(file="images/debian_logo_350.png")
mint_logo = tk.PhotoImage(file="images/mint_logo_350.png")
suse_logo = tk.PhotoImage(file="images/osuse_logo_350.png")
ubuntu_logo = tk.PhotoImage(file="images/ubuntu_logo_350.png")
fedora_logo = tk.PhotoImage(file="images/fedora_logo_350.png")

# Einen Frame Zeichen
logo_frame = tk.Frame(root,background="#FFFFFF")
logo_frame.pack(fill="both",expand=False,side='left',padx=10,pady=10)

# Distro-Logo-Label
distro_icon = tk.Label(logo_frame,text="DISTRO LOGO",image=distro_logo,background="#FFFFFF")
distro_icon.pack(anchor=tk.NW)

# Einen Frame Zeichen
stat_frame = tk.Frame(root,background="#FFFFFF")
stat_frame.pack(fill="both",expand=True,side='left',padx=10,pady=10)

# Label mit Text USER@HOST
user_host_label = tk.Label(stat_frame,text=f"{user}@{hostname}",background="#FFFFFF",font=("Sans",14))
user_host_label.pack(anchor=tk.NW)

# Label mit Text OS:
os_label = tk.Label(stat_frame,text=f"OS: {os_release_pretty}",background="#FFFFFF",font=("Sans",14))
os_label.pack(anchor=tk.NW)

# Label mit Text Host:
host_label = tk.Label(stat_frame,text=f"Host: {hostname}",background="#FFFFFF",font=("Sans",14))
host_label.pack(anchor=tk.NW)

# Label mit Text Kernel:
kernel_label = tk.Label(stat_frame,text=f"Kernel: {kernel_release}",background="#FFFFFF",font=("Sans",14))
kernel_label.pack(anchor=tk.NW)

# Label mit Text Uptime:
uptime_label = tk.Label(stat_frame,text=f"Uptime: {get_sys_uptime()}",background="#FFFFFF",font=("Sans",14))
uptime_label.pack(anchor=tk.NW)

# Label mit Text Shell:
shell_label = tk.Label(stat_frame,text=f"Shell: {active_shell}",background="#FFFFFF",font=("Sans",14))
shell_label.pack(anchor=tk.NW)

# Label mit Text Resolution:
res_label = tk.Label(stat_frame,text=f"Resolution: {get_screen_size()}",background="#FFFFFF",font=("Sans",14))
res_label.pack(anchor=tk.NW)

# Label mit Text DE:
de_label = tk.Label(stat_frame,text=f"DE: {get_desktop_environment()}",background="#FFFFFF",font=("Sans",14))
de_label.pack(anchor=tk.NW)

# Label mit Text Window-Manager
wm_label = tk.Label(stat_frame,text=f"WM: {get_window_manager_name()}",background="#FFFFFF",font=("Sans",14))
wm_label.pack(anchor=tk.NW)

# Label mit Text Theme
wm_theme_label = tk.Label(stat_frame,text=f"Theme: {get_desktop_theme()}",background="#FFFFFF",font=("Sans",14))
wm_theme_label.pack(anchor=tk.NW)

# Label mit Text CPU:
cpu_label = tk.Label(stat_frame,text=f"CPU: ({cpu_core_count}) @ {cpu_freq.max:.2f} Mhz",background="#FFFFFF",font=("Sans",14))
cpu_label.pack(anchor=tk.NW)

# Label mit Text Memory:
mem_label = tk.Label(stat_frame,text=f"Memory: {(get_size(svmem.used))}/{get_size(svmem.total)}",background="#FFFFFF",font=("Sans",14))
mem_label.pack(anchor=tk.NW)

# Führt get_distro_logo aus
get_distro_logo()

# Starte die Hauptschleife
root.mainloop()
