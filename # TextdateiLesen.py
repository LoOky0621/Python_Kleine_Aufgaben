# Aufgabenstellung: Dateiinhalt ausgeben

# Öffne die Textdatei 'textdatei.txt' im Lesemodus
datei = open('c:/Users/Student/Desktop/Übungen Python GFN/textdatei.txt', 'r')

# Iteriere über jede Zeile der Datei und gib den Inhalt aus
for zeile in datei:
    print("Inhalt aus Datei: ")
    print(zeile)

# Schließe die Datei
datei.close()
