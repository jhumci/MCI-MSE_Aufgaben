# UC 2.0

#Hauptprogramm
   # UP – Unterprogramm 

	# Erstellung von Proband:in Karte 
		
		#Pflichtfelder: Name, Nachname, Gewicht, Körpergröße, Geburtsdatum, Geschlecht
		# Nicht-pflichtfelder:  Sozialversicherungsnummer, Krankheiten, Ziel des Testdurchführung, Andere 

		# Erstellung von Unterkarte – jeweilige Test 
			
			# Erstellung der Name von Unterkarte des Proband:in Karte – Datum des Tests
			# Abrufen der Daten von Proband:in Karte: Nachname, Körpergröße, Geschlecht
			# Berechnung der Alter von Geburtsdatum 
			# Pflichtfelder : Derzeitige Gewicht 
			# Automatische Erstellung von Datum und Uhrzeit des Tests 
			# Daten, die von andere Unterprogramme ausgefüllt sein werden 

	# UP Einlesen und bearbeiten der Daten
	
		# UC 2.1 Einlesen der Daten
			# Abrufen der Daten von einem Gerät
			# Zwischenspeicherung der Daten 
		
		# UC 2.2 Vorverarbeiten der Daten
			# Überprüfung der Daten nach Typ 
			# Überprüfung der Daten nach Einstimmung mit der Zeit
			# Kompensation von Bufferoverfolw
				# Darstellung von fehlenden Daten mit NV
			# Daten überprüfen nach Zeitrheinfolge
				# Falls gemischt – sortieren 
			# Speicherung der Daten in Proband:in Karte 
			# Messwert ohne Zeit Eingabe, sollte von Interpretation abgeschlossen werden und mit Warnung geliefert 

		# UC 2.3 Analysieren der Daten nach Abbruchkriterium 
			# Abbrechen Softwareseitig nur in extrem Fall möglich !
			# Der Nutzen von einem Abbruch kann lediglich das Einsparren von Speicherplatz sein. Speicherplatz ist nicht der limitierende Faktor. 
			# Bei sehr grossen Messdaten und sehr geringem Speicherplatz sollte abbgebrochen werden, wenn der Speicherplatz voll ist, damit nicht die bewusst gestartete Messung uberschriben wird, falls der sensor nach Beendigung vom Messvorgang weiter Daten lifert. 
			# Abbrechen falls Threshold/Schwelwert unter oder überschritten wird. Puls unter 0 und über 1000, eine Wert von der Puls deutlich unter oder über Durchschnitt liegt, nicht von Software bekannte Format kommt  { Bei Messverfahren sollte jedoch nie nach Wert-Kriterium abgebrochen werden. Die Daten sollten troztdem aufgezeichnet werden. Wobei mit einer automatischer Warnung. Die Daten sollten für eine Interpretation vorhanden bleiben. } 
			# Sensoren sind passive Geräten und können einen Patienten:in/Teilnehmer:in durch eine Aufzeichnung nie gefährden. Es kann von dieser Seite keine Abbruchbedingungen geben.

		# UC 2.6  Manuelle Eingabe eines Abbruch-Kriteriums 
			
			# Von Testdurchführer:in abgegebene Threshold Werte – Abbruch falls Unter oder Überschreitung 
			# Von Testdurchführer:in abgegebene Zeit, nach welchem Daten geliefert sein sollten  – Abbruch falls Überschreitung 
			# Andere Eingabe 


	# UP UC 2.5 Visualisierung der Daten 
		
		# Abrufen von Daten : Puls – Zeit aus Unterkarte Probad:in 
		# Ploten der Daten in Abhängigkeit: Zeit- Leistung ( Puls)
		# Speicherung des Grafen in Proband:in Karte 

	# UC 2.4 Erstellen einer Zugsamenfassung 	
		# UP Berechnung des Leistungsziels 

			# Abrufen der Daten von Proband:in Karte:  Körpergröße, Derzeitige Gewicht, Geschlecht, Alter 

			# Berechnung des Leistungsziels 
			# Export des Ergebnisses zum Proband:in Karte

			# Ploten des Ergebnisses 
			# Speicherung in Proband:in Karte

		# Grafische Darstellung des Leistung mit Leistungsziel 

			# Abrufen der Daten : Leistung 
			# Abrufen der Daten : Leistungsziel
			# Zusammen ploten 
			# Speicher in Unterkarte des Proband:in Karte 

		# Platz für Interpretation der Daten von Testdurchführer:in 

		# UP Verglich von Testen aus verscheidenden Zeiten
			# Wahl den Tagen
			# Abrufen der Daten von gewählte Tagen 
			# Zusammenploten 
			# Möglichkeit von Export und Darstellung in anderen Formaten z.B. .pdf
			# Platz für Kommentare 

	# UC 2.7 Speichern der Daten

		# Frage nach Überprüfung der Daten  
		# Speichern der Daten in Proband:in Karte 
		
# Bewertung: Sehr schön gelöst und durch die Einrückungen sehr übersichtlich!
