# Dieses Programm simuliert eine Lottoziehung, indem es 6 zufällige Zahlen aus einer Liste von 49 Zahlen auswählt.

# Die Aufgabenstellung lautet:
# Schreibe ein Programm, das eine Lottoziehung simuliert.
# Das Programm soll 6 zufällige Zahlen aus einer Liste von 49 Zahlen auswählen und ausgeben.

import random  # Importiere die Funktion random, die eine Zufallszahl erzeugt

lotto = []  # Erstelle eine leere Liste für die Lottozahlen

# Fülle die Liste mit den Zahlen von 1 bis 49
for i in range(1, 50):
    lotto.append(i)

# Wähle 6 zufällige Zahlen aus der Liste aus und gebe sie aus
print(random.sample(lotto, k=6))
