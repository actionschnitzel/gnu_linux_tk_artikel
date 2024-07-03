import pwd
import os

# Holt sich die Benutzer-ID des aktuellen Prozesses
uid = os.getuid()

# Holt sich den Passwortdatenbank-Eintrag für diese Benutzer-ID
user_info = pwd.getpwuid(uid)


print(f"Benutzername: {user_info.pw_name}")
print(f"Benutzer-ID: {user_info.pw_uid}")
print(f"Gruppen-ID: {user_info.pw_gid}")
print(f"Vollständiger Name: {user_info.pw_gecos}")
print(f"Heimatverzeichnis: {user_info.pw_dir}")
print(f"Standardshell: {user_info.pw_shell}")
