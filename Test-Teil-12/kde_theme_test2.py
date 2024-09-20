import os
import subprocess

def get_kde_theme():
    kde_config_dir = os.path.expanduser("~/.config")
    kde_config_file = os.path.join(kde_config_dir, "kdeglobals")
    
    if os.path.exists(kde_config_file):
        with open(kde_config_file, "r") as file:
            kde_theme = None
            kde_font_size = None

            # Durchsuche kdeglobals-Datei
            for line in file:
                if line.startswith("Name="):  # KDE-Thema extrahieren
                    kde_theme = line.split("=")[1].strip()
                elif line.startswith("font="):  # Schriftgröße extrahieren
                    kde_font_size = line.split(",")[1].strip()  # Extrahiert nur die Schriftgröße

            # Wenn ein KDE-Thema und Schriftgröße gefunden wird
            if kde_theme:
                if kde_font_size:
                    kde_theme = f"{kde_theme} {kde_font_size}"
                return f"{kde_theme} [KDE/Plasma]"
            else:
                return "KDE theme not found."
    else:
        return "KDE config files not found."

def get_desktop_theme():
    de = get_desktop_environment()

    if de == "GNOME":
        result = subprocess.run(['gsettings', 'get', 'org.gnome.desktop.interface', 'gtk-theme'], capture_output=True, text=True, check=True)
        return result.stdout.strip().strip("'")
    
    if de == "CINNAMON":
        result = subprocess.run(['gsettings', 'get', 'org.cinnamon.desktop.interface', 'gtk-theme'], capture_output=True, text=True, check=True)
        return result.stdout.strip().strip("'")        

    if de == "MATE":
        result = subprocess.run(['gsettings', 'get', 'org.mate.interface', 'gtk-theme'], capture_output=True, text=True, check=True)
        return result.stdout.strip().strip("'")
    
    if de == "XFCE":
        result = subprocess.run(['xfconf-query', '-c', 'xsettings', '-p', '/Net/ThemeName'], capture_output=True, text=True, check=True)
        return result.stdout.strip().strip("'")
    
    if de == "PI-WAYFIRE":
        result = subprocess.run(['gsettings', 'get', 'org.gnome.desktop.interface', 'gtk-theme'], capture_output=True, text=True, check=True)
        return result.stdout.strip().strip("'")
    
    if de.startswith("KDE") or de.startswith("Plasma"):
        return get_kde_theme()

    return "Desktop environment not supported."

def get_desktop_environment():
    xdg_current_desktop = os.environ.get("XDG_CURRENT_DESKTOP")
    
    if xdg_current_desktop == "x-cinnamon":
        return "CINNAMON"
    elif xdg_current_desktop == "UNITY":
        return "UNITY"
    elif xdg_current_desktop == "ubuntu:GNOME":
        return "GNOME"
    elif xdg_current_desktop.startswith("KDE") or xdg_current_desktop == "Plasma":
        return "KDE"
    else:
        return xdg_current_desktop

# Beispiel: Ausgabe des aktuellen Themes
print(get_desktop_theme())
