# Dieses Programm überwacht den Status eines Parkhauses und gibt entsprechende Warnmeldungen aus, basierend auf verschiedenen Kriterien wie der Anzahl der belegten Parkplätze, der Verfügbarkeit von Eingang und Ausgang sowie der Vermietung des Parkhauses.

# Aufgabenstellung:
# Schreibe ein Programm, das den Status eines Parkhauses überwacht und Warnmeldungen ausgibt, basierend auf folgenden Kriterien:
# - Anzahl der belegten Parkplätze
# - Verfügbarkeit von Eingang und Ausgang
# - Vermietung des Parkhauses
# Das Programm soll verschiedene Szenarien testen und den entsprechenden Parkhausstatus ausgeben.


def status_anzeigen(anzahl_parkplätze_belegt, eingang_frei, ausgang_frei, vermietet):
    # Berechnung der Auslastung in Prozent
    auslastung = (anzahl_parkplätze_belegt * 100) / 500
    
    # Überprüfung der verschiedenen Bedingungen für den Parkhausstatus
    if (eingang_frei == True or ausgang_frei == True) or vermietet == True:
        print("Parkhaus gesperrt")  # Wenn der Eingang oder Ausgang frei ist oder das Parkhaus vermietet ist, ist es gesperrt
    elif auslastung > 95: 
        print("Parkhaus belegt")    # Wenn die Auslastung über 95% liegt, ist das Parkhaus belegt
    else:
        print("Parkhaus frei")      # Ansonsten ist das Parkhaus frei

def main():
    # Testen verschiedener Szenarien
    status_anzeigen(490, True, True, True)   # Parkhaus gesperrt (eingang_frei = True, ausgang_frei = True, vermietet = True)
    status_anzeigen(490, True, True, False)  # Parkhaus gesperrt (eingang_frei = True, ausgang_frei = True, vermietet = False)
    status_anzeigen(490, False, False, True) # Parkhaus gesperrt (eingang_frei = False, ausgang_frei = False, vermietet = True)
    status_anzeigen(490, False, False, False) # Parkhaus frei (eingang_frei = False, ausgang_frei = False, vermietet = False)
    
    status_anzeigen(330, True, True, True)   # Parkhaus belegt (eingang_frei = True, ausgang_frei = True, vermietet = True)
    status_anzeigen(330, True, True, False)  # Parkhaus belegt (eingang_frei = True, ausgang_frei = True, vermietet = False)
    status_anzeigen(330, False, False, True) # Parkhaus gesperrt (eingang_frei = False, ausgang_frei = False, vermietet = True)
    status_anzeigen(330, False, False, False) # Parkhaus frei (eingang_frei = False, ausgang_frei = False, vermietet = False)

main()
