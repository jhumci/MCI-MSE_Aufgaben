## Project background

### Purpose of project
Es wird eine Software zur Leistungsdiagnostik entwickelt.
Der Ergometer ist bereits vorhanden und kann die Leistung und die Herzfrequenz der Probanden messen. 
Die Daten werden aktuell einfach als Daten gespeichert. Die Software soll nun die Daten auswerten und visualisieren. 

### Scope of project
In 2er Teams wird eine Software zur Leistungsdiagnostik entwicklet. 
Das Tool benötigt kein Interface, da es mittels Kommandozeile bearbeitet wird. 
Ungültige Durchläufe des Leistungstests sollen in seperatem Ordner gespeichert werden.
Ausgegeben werden soll ein Plot, welcher die Herzrate und die Leistung über den Zeitraum des Tests zeigt.

### Other background information
Es wird nur ein Testtyp gefahren. Dauer dieses Tests sind 3 Minuten und der Proband erhält ein zu erreichendes Leistungsziel. 
Ein automatisches Abbruchkriterium ist die Erreichung von 90% der maximalen Herzfrequenz (220-Lebensalter).
Erfasst wird vom Probanden nur das Geburtsdatum, sein Name und eine technische ID.

## Perspectives
### Who will use the system?
Benutzt wird das System vom Diagnostiker. Dieser wird mit der Software hantieren um die Daten auszuwerten und dem Probanden präsentieren. 
Der Proband wird lediglich einen Not-Aus Taster zur Bedinung erhalten um den Test abzubrechen, falls Probleme auftreten.
Ansonsten wird er mit der Software nicht in Berührung kommen.

### Who can provide input about the system
Die Daten (Herzrate und Leistung) werden vom Probanden ins System eingebracht. 
NOTE-JHU: Wording: würde her dagen von Ergometer in einem Ordner abgelegt?

Der Diagnostiker kann jedoch bei Erkennung von Unregelmäßigkeiten in den Daten den Leistungstest manuell als ungültig werten.
Somit können beide Personen input ins System geben.

## Project Objectives
### Known business rules

NOTE-JHU: Was ihr unter Scope of project schon gut beschrieben habt, würde auch hier gut hin passen.

...

### System information and/or diagrams

Beispiel von aufgezeichneten EKG Daten
![](ekg_example.png)

Aus diesem muss die Herzrate bestimmt werden.

### Assumptions and dependencies
Um einen gültigen Leistungstest zu fahren, muss die geforderte Leistung erbracht und die Herzrate nicht überschritten werden.
Somit ist eine Auwertung der Daten abhängig vom Probanden. 

PÜ2 
ecg_data_subject_ enthält die Herzfrequenz von jedem der drei Testpersonen.
power_data_ enthält die gefahrenen Watt Zahlen
subject_ enthält eine der Testperson zugewiesene ID, das Geburtsdatum, die angestrebte Watt Zahl und die Testdauer welche bei allen drei Probanden 180s beträgt. 

NOTE-JHU: Etwas spärlich. Gerne noch Datenformat und Auflösung.

### Design and implementation constraints
Das Tool soll mittells Kommandozeile bedient werden und benötigt zum jetzigen Zeitpunkt kein Nutzerinterface. 

## Risks
Der Proband könnte sich verausgaben oder durch Überanstrengung sein Herz gefährden.
Dieses Risiko wird jedoch durch die Überwachung der Herzfrequenz und des automatischen Abbruchs in Folge zu hoher Herzfrequenz minimiert. 

NOTE-JHU: Eher Fokus auf Projektrisiken ;) Da die Software eine Post-Hoc-Auswertung macht, kann sie ja auch die Herzfrequenz nicht live überwachen.

## Known future enhancements
Ein Nutzerinterface ist zur Zeit nicht geplant, könnte aber in Zukunft relevant werden, da die Bedienung einfacher und intuitiver ist.

## References

- [Link zur Aufgabenstellung](tbd)

## Open, unresolved or TBD issues
Known business rules
