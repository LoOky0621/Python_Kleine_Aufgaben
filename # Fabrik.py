# Aufgabenstellung: Teileüberprüfung und Lagerung
#
# Entwickle ein Python-Programm, das simuliert, wie Teile in einer Fabrik gescannt und gelagert werden. Die Fabrik produziert zwei Arten von Teilen, die jeweils unterschiedliche Prüf- und Lagerungsanforderungen haben.
#
# Schritte:
# 1. Simuliere die Produktion von 1000 Teilen, wobei jedes Teil entweder zur Kategorie 1 oder zur Kategorie 2 gehört.
# 2. Für jedes Teil:
#    - Simuliere das Scannen der Teile-ID, um festzustellen, zu welcher Kategorie das Teil gehört (1 oder 2).
#    - Simuliere das Scannen des Zustands des Teils (OK oder defekt).
#    - Zähle die Anzahl der Teile in jeder Kategorie und die Anzahl der defekten Teile.


# Importiere das Modul random, um Zufallszahlen zu generieren
import random

# Initialisiere Variablen für die Zählung und Zustände der Teile und Lagerung
anzahlTeil1 = 0
anzahlTeil2 = 0
defekt1 = 0
defekt2 = 0
scanZustandTeil1 = 0 # Zustand des gescannten Teils 1 (defekt, OK)
scanZustandTeil2 = 0 # Zustand des gescannten Teils 2 (defekt, OK)
lagerungsBoxSchaden = 0 # Zustand der Lagerungsboxen (defekt, OK)
lagerungBox1 = 0 # Anzahl Teile in Lagerungsbox 1
lagerungBox2 = 0 # Anzahl Teile in Lagerungsbox 2

# Iteriere über eine Anzahl von Teilen (hier: 1000)
for i in range(0, 1000):
    
    # Funktion zum Scannen der Teile-ID (1 oder 2)
    def scanTeileID():
        return random.randint(1, 2)
    
    # Scanne die Teile-ID
    teileID = scanTeileID()
    
    # Überprüfe die gescannte Teile-ID und führe entsprechende Aktionen aus
    if teileID == 1:
        
        # Funktion zum Scannen des Zustands des Teils 1 (defekt oder OK)
        def scanTeileIDneu():
            return random.randint(1, 2)
        
        # Scanne den Zustand des Teils 1
        scanZustandTeil1 = scanTeileIDneu()

        # Zähle die Anzahl der Teile 1
        anzahlTeil1 = anzahlTeil1 + 1
        
        # Überprüfe den Zustand des gescannten Teils 1 und aktualisiere die Lagerung
        if scanZustandTeil1 == 1:
            lagerungBox1 = lagerungBox1 + 1 # Füge das Teil 1 zur Lagerungsbox 1 hinzu
        else:
            defekt1 = defekt1 + 1 # Zähle das defekte Teil 1
            
    else:
        
        # Funktion zum Scannen des Zustands des Teils 2 (defekt oder OK)
        def scanTeileIDneu():
            return random.randint(1, 2)
        
        # Scanne den Zustand des Teils 2
        scanZustandTeil2 = scanTeileIDneu()

        # Zähle die Anzahl der Teile 2
        anzahlTeil2 = anzahlTeil2 + 1
        
        # Überprüfe den Zustand des gescannten Teils 2 und aktualisiere die Lagerung
        if scanZustandTeil2 == 1:
            lagerungBox2 = lagerungBox2 + 1 # Füge das Teil 2 zur Lagerungsbox 2 hinzu
        else:
            defekt2 = defekt2 + 1 # Zähle das defekte Teil 2

# Gib die Ergebnisse der Teileüberprüfung und Lagerung aus
print("Gesamtanzahl Teile 1:", anzahlTeil1)
print("Teile in Lagerungsbox 1:", lagerungBox1)
print("Defekte Teile 1:", defekt1)

print("Gesamtanzahl Teile 2:", anzahlTeil2)
print("Teile in Lagerungsbox 2:", lagerungBox2)
print("Defekte Teile 2:", defekt2)
