# Beschreibung der Anwendungsfälle

## UML-Diagramm

![](UML_UseCase_Ergometer.svg)

## Tabellen


### UC 2.1. - Einlesen der Daten


|                                | Erklärung                                                                                                                                                                               | Beispiel                                                                                                                                         |
|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
|Einlesen	|Daten sind aus Sensoren gelesen.	| Die Sensoren messen die Daten, welche Software mit dem Zeit zusammensetzt ||
Typ der Daten |Der Software erkennt der Typ von eingelesen Daten. 	|Erhaltene Daten sind von Software nach Typ überprüft|| 
Hauptordner	|Karte der jeweiligen Proband:in, wo alle gemachte Tests werden gespeichert.| ||	
Sozialversicherungsnummer 	|Früher von Tester:in eingegebene Datei. Wird auch als Name von Hauptorder verwendet. 	|1287030224||
Unterordner	|Als Unterordner ist jede neu gemachte Test gemacht. Die Name ist das Datum des gemachtes Test in Format tt/mm/jjjj.	|20.03.22||
Speicherung 	|Nach Erkennung von Datentyp, sind die Daten in entsprechenden Zellen gespeichert in früher von Tester:in geöffnete Karte von Proband:in.	|Gemessene Puls ist in „Puls“- Zelle eingetragen.||
Name von Proband:in	|Eine Textdaten, welche vor Testdurchführung in Hauptordner eingetragen sein musst. 	|Max Muster||
Abgeschlossenen Tests	|Unter abgeschlossene Test versteht man erfolgreich durchgemachte Test. 	|Bei Testdurchführung ist keine Fehler oder Abbruch passiert.|| 
Separate Dateien	|Jede durchgeführte Test von jeweiligen Proband:in ist als separate Datei in Hauptordner gespeichert 	|Unterordner mit Datum als Name. Kann als PDF Datei exportiert werden.|| 
Puls	Nummerische Daten, welche später noch von softer bearbeitet sind. Eingeordnet mit Zeitreihe. Vorgesehen sind drei Ziffern. 	|68||
Leistung	|Resultat des Test.	|Grafisch gestellt|| 
Zeitreihe	|Nummerische Daten, welche später noch von softer bearbeitet sind. Eingeordnet mit gemessenen Puls. Format mm:ss	|23:43:00||
Leistungsziel	|Früher von Software berechnete idealer Puls für jede Sekunde von Testdauer. Berechnung basiert auf Alter, Gewicht, Körpergröße, Geschlecht. 	|087||
