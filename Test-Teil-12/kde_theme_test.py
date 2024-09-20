import os

def get_kde_theme():
    # Pfad zur kdeglobals-Datei
    kde_config_dir = os.path.expanduser("~/.config")
    kde_config_file = os.path.join(kde_config_dir, "kdeglobals")
    
    # Überprüfen, ob die kdeglobals-Datei existiert
    if os.path.exists(kde_config_file):
        with open(kde_config_file, "r") as file:
            kde_theme = None
            kde_font_size = None

            # Datei zeilenweise durchsuchen
            for line in file:
                if line.startswith("Theme="):  # Sucht nach der Zeile mit dem Theme
                    kde_theme = line.split("=")[1].strip()  # Extrahiert den Theme-Namen
                elif line.startswith("font="):  # Sucht nach der Zeile mit der Schriftart
                    kde_font_size = line.split(",")[1].strip()  # Extrahiert die Schriftgröße

            # Theme und Schriftgröße verarbeiten
            if kde_theme:
                if kde_font_size:
                    kde_theme = f"{kde_theme} {kde_font_size}"
                kde_theme = f"{kde_theme} [KDE/Plasma]"
                return kde_theme
            else:
                return "KDE theme not found."
    else:
        return "KDE config files not found."

# Beispiel für die Verwendung
print(get_kde_theme())
