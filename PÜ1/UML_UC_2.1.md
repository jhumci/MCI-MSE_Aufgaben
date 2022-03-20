# Beschreibung der Anwendungsfälle

## UML-Diagramm
![UML_UseCase_Ergometer](https://user-images.githubusercontent.com/101809825/159174582-b824246f-1123-4218-ab2e-bfd60d0fb44f.svg)


## Tabellen


### UC 2.1. - Einlesen der Daten


|                                | Erklärung                                                                                                                                                                               | Beispiel                                                                                                                                         |
|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
|Sensoren	|Sensoren, die Puls messen	|Sensoren, die auf dem Brustgürtel montiert sind.||
Zeitmessung	|Im System wird die Zeit erfasst.	|Messen der Testdauer.|| 
Gemessene Puls – Format	|Nummerische Daten. Vorgesehen sind drei Ziffern. 	|068||
Erfassung	|Die Pulsdaten werden zusammen mit der jeweiligen Zeit erfasst und in Zeitreihen gespeichert.  	|Der gemessene Puls ist einer Zeit zugeordnet.||
Zeit Format	|Die Zeit wird in folgendem Format gespeichert werden : xx:xx:xx	|23:43:45||
Bluetooth 	|Die Daten werden von Sensoren zum Computer über Bluetooth zugewiesen. 	|Bluetooth- connection|| 
Einlesen Bedingungen 	|Um das Einlesen der Daten starten zu können, müssen verschiedene Bedingungen erfüllt sein. 	|Karte von Proband:in muss geöffnet sein. Proband:in Daten müssen erfühlt sein.|| 
Daten Erkennung	|Die Software erkennt den Typ von eingelesen Daten. 	|Die Daten werden von der Software auf ihren Typ überprüft|| 
Daten Überprüfung 	|Alle Daten werden immer erfasst. 	|Daten, die in Wirklichkeit nicht plausibel sind, werden auch erfasst.|| 
Umgang mit Fehlern	|Daten müssen immer einer Zeit zugeordnet sein. Wenn keine Daten vorhanden sind, wird NV (nicht vorhanden) eingetragen. 	|Bei Bufferoverflow oder fehlenden Messdaten muss die Zeit dennoch korrekt erfasst werden. Die fehlenden Werte werden mit NV eingetragen und können später interpoliert und interpretiert werden.||   
Abbruch |Compuer-seitig darf es nicht zu einem Abbruch kommen. 	|Es wird gewartet bis Daten ankommen oder manuell abgebrochen wird.|| 
Speicherung 	|Nach der Erkennung des Datentyps sind die Daten in entsprechenden Zellen gespeichert in früher von derTester:in geöffneten Karte von Proband:in.	|Gemessener Puls ist in „Puls“- Zelle eingetragen.||
