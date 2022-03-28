# UC 2.0

#%% UC 2.1 Einlesen der Daten



#Hauptprogramm
   # UP – Unterprogramm 

	# Erstellung von Proband:in Karte 
		
		#Pflichtfelder: Name, Nachname, Gewicht, Körpergröße, Geburtsjahr, Geschlecht
		# Nicht-pflichtfelder:  Sozialversicherungsnummer, Krankheiten, Ziel des 			Testdurchführung, Andere 

		# Erstellung von Unterkarte – jeweilige Test 
			
			# Erstellung der Name von Unterkarte des Proband:in Karte – Datum des 			Tests
			# Abrufen der Daten von Proband:in Karte: Nachname, Körpergröße, 				Geschlecht
			# Pflichtfelder : Derzeitige Gewicht 
			# Automatische Erstellung von Datum und Uhrzeit des Tests 
			# Daten, die von andere Unterprogramme ausgefüllt sein werden 

	# UP Einlesen und bearbeiten der Daten
	
		# UC 2.1 Einlesen der Daten
			# Abrufen der Daten von einem Gerät
			# Zwischenspeicheung der Daten 
		
		# UC 2.2 Vorverarbeiten der Daten
			# Überprüfung der Daten nach Typ 
			# Überprüfung der Daten nach Einstimmung mit der Zeit
			# Kompensation von Bufferoverfolw
				# Darstellung von fehlenden Daten mit NV
		#Speicherung der Daten in Proband:in Karte 

	# UP Ploten 

		# Ploten der Daten in Abhängigkeit: Zeit- Leistung 
		# Speicherung des Grafen in Proband:in Karte 

	# UP Berechnung des Leistungsziels 

		# Abrufuen der Daten von Proband:in Karte:  Körpergröße, Derzeitige Gewicht, 			Geschlecht 

		# Berechnung des Leistungsziels 
		# Export des Ergebnisses zum Proband:in Karte

		# Ploten des Ergebnisses 
		# Speicherung in Proband:in Karte

	# Grafische Darstellung des Leistungs mit Leistungsziel 

		# Abrufen der Daten : Leistung 
		# Abrufen der Daten : Leistungsziel
		# Zusammen ploten 
		# Speicher in Unterkarte des Proband:in Karte 

