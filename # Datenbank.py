'''Aufgabenstellung: Personalverwaltung

Entwickle ein Programm zur Verwaltung von Personalinformationen. Das Programm soll eine SQLite-Datenbank verwenden, um Informationen wie Vorname, Nachname, Ort und Alter der Mitarbeiter zu speichern.

Datenbankverbindung herstellen und Tabelle erstellen: Erstelle eine SQLite-Datenbank mit dem Namen "personalverwaltung2.db" und einer Tabelle namens "personendatenbank", um die Personalinformationen zu speichern. Die Tabelle soll die folgenden Spalten haben: "vorname" (REAL), "nachname" (TEXT), "ort" (TEXT) und "alt" (REAL).

Daten einfügen: Schreibe eine Funktion data_entry(), die den Benutzer nach Vorname, Nachname, Ort und Alter eines Mitarbeiters fragt und diese Informationen in die Datenbank einfügt.

Daten aktualisieren: Schreibe eine Funktion data_update(), die das Alter aller Mitarbeiter mit dem Wert '1' auf '15' aktualisiert.

Sorge dafür, dass die Datenbankverbindung nach jeder Operation ordnungsgemäß geschlossen wird.'''

import sqlite3
import os

# Ändere das Arbeitsverzeichnis zum Speicherort der Datenbankdatei
os.chdir("c:/Users/Student/Desktop/Übungen Python GFN/test")

# Verbindung zur Datenbank herstellen
conn = sqlite3.connect('personalverwaltung2.db')
c = conn.cursor()

# Tabelle erstellen
def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS personendatenbank(vorname REAL, nachname TEXT, ort TEXT, alt REAL)") 

# Datensätze einfügen
def data_entry():
    vorname = input("Vorname: ")
    nachname = input("Nachname: ") 
    ort = input("Ort: ")
    alt = input("Alter: ")
    c.execute("INSERT INTO personendatenbank (vorname, nachname, ort, alt) VALUES (?, ?, ?, ?)",
          (vorname, nachname, ort, alt))
    conn.commit()

# Daten aktualisieren
def data_update():
    c.execute("UPDATE personendatenbank SET alt='15' WHERE alt='1'") 
    conn.commit()

# Datenbankverbindung schließen
c.close()
conn.close()

create_table()
#data_entry()
#data_update()
