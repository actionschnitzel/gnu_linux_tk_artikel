print("Jutta hat doppelt so viele Eier wie Achim. Er besitzt genau 6 Eier. Jutta schenkt Achim die Hälfte ihrer Eier.\n\nFrage: Wie viele Eier hat Achim?")

achims_eier = 6

juttas_eier = achims_eier * 2

check_plural = "Ei"

if achims_eier >=2:
    check_plural = "Eier"

print("\nLösung:\n")
#print(f"Achim hat {achims_eier} {check_plural}")
#print(f"Jutta hat {juttas_eier} {check_plural}")

print(f"Achim hat die Hälfte von Juttas {juttas_eier} Eiern bekommen.\nEs sind genau {juttas_eier / 2 } {check_plural}.\nDas heißt, Achim hat jetzt {achims_eier + juttas_eier / 2} {check_plural}.")
