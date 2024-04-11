# Dieses Programm überwacht den Zustand eines Serverraums anhand von Temperatursensoren und gibt Warnmeldungen aus, wenn die Temperatur bestimmte Schwellenwerte überschreitet.

# Aufgabenstellung:
# Schreibe ein Programm, das den Zustand eines Serverraums überwacht und Warnmeldungen ausgibt, wenn die Temperatur bestimmte Schwellenwerte überschreitet.
# Die Temperatur wird von drei Sensoren (sensor1, sensor2, sensor3) gemessen, die jeweils den Wert 1 anzeigen, wenn sie aktiv sind, und 0, wenn sie nicht aktiv sind.
# Die Temperatur wird in drei Kategorien eingeteilt: Grün (20-30 Grad Celsius), Gelb (<20 oder 30-35 Grad Celsius) und Rot (>35 Grad Celsius).
# Wenn mindestens einer der Sensoren aktiv ist, überprüft das Programm den Temperaturbereich und gibt entsprechende Warnmeldungen aus.
# Wenn kein Sensor aktiv ist, wird eine generelle Warnmeldung ausgegeben.

# Zustand der Sensoren
sensor1 = 1
sensor2 = 0
sensor3 = 0

# Schwellenwerte für die Temperatur
grün = 31  # 20-30 Grad Celsius
gelb = 33  # <20 oder 30-35 Grad Celsius
rot = 40   # >35 Grad Celsius oder ein Sensor ist defekt

# Überwachung des Serverraums basierend auf den Sensorwerten und Temperaturschwellenwerten
if sensor1 == 1 or sensor2 == 1 or sensor3 == 1:
    # Überprüfung des Status der Sensoren und Temperaturbereiche
    if grün < 20:
        if sensor1 == 1:
            print("Lampe: GELB Temp:", gelb)
        else:
            print("ROT1: Temperatur zu niedrig und Sensor defekt")
    elif gelb > 30:
        if sensor2 == 1:
            print("Lampe: GELB Temp:", gelb)
        else:
            print("ROT2: Temperatur zu hoch und Sensor defekt")
    elif rot > 35:
        if sensor3 == 1:
            print("Lampe: GELB Temp:", gelb)
        else:
            print("ROT3: Temperatur zu hoch und Sensor defekt")
    else:
        print("Aktuelle Temperatur:", grün, "Grad Celsius")
else:
    print("WARNUNG: Keine aktiven Sensoren im Serverraum!")
