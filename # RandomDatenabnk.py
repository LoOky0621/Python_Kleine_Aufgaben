import sqlite3
import os
import random

# Ändern des Arbeitsverzeichnisses zum Speicherort der Datenbankdatei
os.chdir("c:/Users/Student/Desktop/Übungen Python GFN/test")

# Verbindung zur SQLite-Datenbank herstellen
conn = sqlite3.connect('personalverwaltung.db')
c = conn.cursor()

# Aufgabenstellung: Random-Datenbank
# Entwickle ein Programm zur Verwaltung von Personalinformationen in einer SQLite-Datenbank.
# Die Datenbank soll eine Tabelle namens "personendatenbank" enthalten, die Vorname, Nachname, Ort und Alter der Mitarbeiter speichert.
# Das Programm soll die folgenden Funktionen enthalten:
# 1. Funktion zum Erstellen der Tabelle in der Datenbank, falls sie nicht existiert.
# 2. Funktion zum Einfügen von Daten in die Tabelle, entweder durch Benutzereingabe oder zufällige Generierung.
# 3. Funktion zum Aktualisieren von Daten in der Tabelle, z.B. das Ändern des Orts für alle Mitarbeiter aus "Ludwigshafen" in "Lumpenhafen".

# Funktion zum Erstellen der Tabelle in der Datenbank
def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS personendatenbank(Vorname TEXT, Nachname TEXT, Ort TEXT, Alt INTEGER)") 

# Funktion zum Einfügen von Daten in die Tabelle
def insert_daten(vorname, nachname, ort, alter):
    c.execute("INSERT INTO personendatenbank (Vorname, Nachname, Ort, Alt) VALUES (?, ?, ?, ?)", (vorname, nachname, ort, alter))
    conn.commit()

# Funktion zum Erstellen einer Liste von zufälligen Daten und Einfügen in die Tabelle
def create_list():
    vorname_list = ["Adrian", "Thomas", "Juri", "Rafal", "Simeon", "Frank", "Denis", "Alexander", "Laura", "Nadine"]
    nachname_list = ["Waletzki", "Hans", "Peter", "Wolfgang", "Obi", "Holz", "Potter", "Müller"]
    wohnort_list = ["Mannheim", "Heidelberg", "Ludwigshafen", "Worms", "Weinheim", "Viernheim"]
    
    for i in range(0, 250):
        vorname = random.choice(vorname_list)
        nachname = random.choice(nachname_list)
        ort = random.choice(wohnort_list)
        alter = random.randint(6,99)
        insert_daten(vorname, nachname, ort, alter)

# Funktion zum Einfügen von Daten durch Benutzereingabe
def data_entry():
    vorname = input("Vorname: ")
    nachname = input("Nachname: ") 
    ort = input("Ort: ")
    alter = input("Alter: ")
    insert_daten(vorname, nachname, ort, alter)

# Funktion zum Aktualisieren von Daten in der Tabelle
def data_update():
    c.execute("UPDATE personendatenbank SET Ort='Lumpenhafen' WHERE Ort='Ludwigshafen'")
    conn.commit()

# Tabelle erstellen (wenn sie nicht existiert)
create_table()

# Funktionen für Datenverwaltung aufrufen
# data_entry()  # Benutzer kann Daten eingeben
# create_list()  # Zufällige Daten generieren und einfügen
# data_update()  # Daten aktualisieren

# Datenbankverbindung schließen
c.close()
conn.close()
