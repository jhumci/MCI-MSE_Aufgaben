# Programmierübung

## PÜ1 - Anforderungsanalyse App Leistungsdiagnostik


### Aufgabenstellung 

Ihr Team soll eine Software zur Leistungsdiagnostik entwickeln basierend auf einem Ergometer entwickeln.
Ihr Auftraggeber ist ein Hersteller von Ergometern, der bereits über ein funktionierenden Ergometer verfügt, bei dem die von der Probandin zu bringende Leistung eingestellt werden kann und sowohl die von der Proband:in erbrachte Leistung sowie deren Elektrokardiogramm aufgezeichnet wird. Die Daten hierzu werden aktuell einfach als Dateien gespeichert.
Als Proof-Of-Concept soll nun zunächst eine sehr einfache Software geschrieben werden, die die Daten auswertet und visualisiert. 

### Aufgaben

1. Forken Sie das folgende Github Projekt an und machen Sie sich mit den bereitgestellten Daten vertraut
    - laden Sie alle Teammitglieder mit ein
    - laden Sie zudem https://github.com/yheyer, https://github.com/yschm, und https://github.com/jhumci ein
2. Verfassen sie einen ersten Entwurf für 
    - eine Readme.md (nur die fett hervorgehobenen Inhalte) und 
    - eine Discussion Summary (3-6 Sätze pro Kapitel) für das Projekt und legen Sie diese im Github Repository ab

3. Beschreiben Sie einen der Use-Cases 2.X anhand einer Tabelle (vergleichbar der Datei Anwendungsfaelle.md). Berücksichtigen Sie die Rollen Ergometer und Diagnostiker:in und das <include> Statement.
- Erstellen der Daten durch Ergometer
- Auswertung der Leistungsdaten: Gesamtprozess zum Einlesen und Auswerten der Daten
- Einlesen der Daten: Lädt Daten aus Datei ein
- Vorverarbeiten der Daten: Bereitet eingelesene Daten für Visualisierung vor
- Analysieren der Daten auf Abbruchkriterium: Überprüft ob Abbruchkriterium erfüllt
- Manuelle Eingabe eines Abbruch-Kriteriums: Abfrage, ob Test als Abgebrochen gewertet werden soll.
- Erstellen einer Zusammenfassung: Auswertung der eingelesenen Daten
- Visualisierung der Daten: Plot der Ausgewerteten Daten
- Speichern der Ergebnisse: Speichern der vorverarbeiteten Daten und Plots

4. Ergänzen Sie alle Ihre Änderungen im GIT-Repository


 
---

### Anforderungen des Auftraggebers

Folgende Wünsche gibt Ihnen der Auftraggeber direkt mit auf den Weg:
- Ablauf der Leistungstest: Aktuell wird nur ein Test-Typ Gefahren. Der Proband:in wird ein festes Leistungsziel für eine feste Zeit (3 Minuten) vorgegeben. Der Puls und die erbrachte Leistung wird als Zeitreihe erfasst und gespeichert.
- Der Fahrradergometer speichert gibt die abgeschlossenen Tests als separate Dateien (Zeitreihe mit Leistung und Herzrate)
- Das Tool soll mittels Kommandozeile bedient werden, ein Nutzerinterface wird zunächst nicht benötigt
- Einige der Durchläufe sind ungültig. Zum Beispiel wenn Das Abbruchkriterium (Puls 90 % der maximalen Herzfrequenz (220 – Lebensalter) erreicht wird.
- Es gibt auch andere Gründe zum Abbruch, wieder die Diagnostikerin nach Begutachtung der Daten manuell vermerken können soll.
- Von den Versuchspersonen wird Name, eine technische ID, und das Geburtsdatum gespeichert.
- Ergebnis ist ein Plot der die Herzrate und die Leistung über den Zeitraum darstellt
- Die Plots und die verarbeiteten Daten sollen gespeichert werden.
- Erfolgreiche und abgebrochene Versuche sollen in separaten Ordnern gespeichert werden

Der Auftraggeber hat im Gespräch noch weitere Ideen angedeutet, welche im Folgeprojekten münden könnten.
- Mögliche zukünftige Erweiterungsmöglichkeiten
    - Eine Applikation mit Nutzerinterface soll eine Diganostiker:in durch einen Leistungstest führen
    - Vor der Durchführung soll eine Abfrage auf Kontraindikationen [p11](https://www.klinikum.uni-heidelberg.de/fileadmin/medizinische_klinik/Abteilung_7/pdf/ergo_bf.pdf) ausgeführt werden

### Beispiel von aufgezeichneten EKG Daten
![](ekg_example.png)



###### https://upload.wikimedia.org/wikipedia/commons/f/f2/L-Tests.png
