# Aufgabenstellung: Fakultät berechnen
# Schreibe ein Programm, das die Fakultät einer Zahl berechnet und ausgibt.

# Initialisiere die Variable für das Ergebnis
ergebnis = 1

# Zahl für die Fakultätsberechnung
n = 4

# Berechne die Fakultät
for i in range(1, n+1):
    ergebnis *= i

# Ausgabe des Ergebnisses
print("Die Fakultät von", n, "ist:", ergebnis)
