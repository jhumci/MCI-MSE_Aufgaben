## Project background

### Purpose of project

Mithilfe einer Leistungsdiagnostik am Fahrradergometer kann der gesundheitliche Zustand einer Privatperson, bzw. der Leistungsstand eines Sportlers/einer Spotlerin bestimmt werden. Dies geschieht mithilfe einer Software, welche die aufgezeichnete Änderung der Vitalparameter wie zum Beispiel Sauerstoffsättigung und Herzfrequenz mit steigender Belastung aufzeichnet. Zusätzlich können die Ableitungen von einem Elektrokardiagramm in einem Schaubild abgebildet werden. 
Ein Leistungstest wird meistens zu Beginn einer Saison gemacht, um den momentanen Leistungsstand eines Sportlers/einer Sportlerin zu analysieren und Schwachstellen aufdecken zu können.
Im Gesundheitssektor können mithilfe einer Leistungsdiagnostik Erkrankungen frühzeitig erkannt werden oder der Zustand einer bereits bestehenden Krankheit beurteilt werden.

### Scope of project

Der Leistungstest startet auf niedriger Stufe, wodurch sich die Nutzer:innen erst einmal aufwärmen kann und das Herz-Kreislauf-System angekurbelt wird. In bestimmten Zeitabständen wird nun die Schwierigkeit erhöht. Dadurch steigt zum Beispiel der Puls oder der Laktatwert im Blut der Nutzer:innen, was dann in einem Schaubild aufgezeichnet wird. Das Schaubild kann anschließend ausgewertet und analysiert werden. Eine Leistungsdiagnotik kann in gewissen Abständen (mehrere Wochen) wiederholt werden, um Veränderungen zu erkennen.

### Other background information

Vor jeder Leistungsdiagnostik kommt es zu einem Gespräch zwischen Nutzer:in und behandelnder Person. Hierbei komtm es zu einer ausführlichen Anamnese, in der der aktuelle Leistungsstand/Gesundheitszustand besprochen werden. Zusätzlich wird die sportliche/gesundheitliche Vergangenheit der Nutzer:in besprochen, um einschätzen zu können, auf was für einer Schwierigkeit mit der Leistungsdiagnostik angefangen wird. Währende der Leistungsuntersuchung und auch danach wird man durchgehend von medizinischem Fachpersonal betreut, um die Risiken einer Verletzung oder ählichem möglichst gering zu halten.

## Perspectives
### Who will use the system?

Zum einen kann die Leistungsdiagnostik von Hausärzten:innen oder Sportmediziner:innen verwendet werden, um den allgemeinen Gesundheitszustand eines Patients oder einer Patientin zu bestimmen. Dies wird häufig verwendet, um die Herzfunktion/Lunegnfunktion und weitere Parameter nach einer langwierigen Erkrankung (wie zum Beispiel Covid19) anzuschauen und zu analysieren, wie gravierend die Folgen sind und wie man wieder mit der Rehabilitation anfängt.
Das System wird immer von medizinischen Fachpersonal bedient. Sei es der Leistungssportler der sich auf einen Marathon vorbereitet oder eine ältere Dame welcher nach einer langen Erkrankung wieder fit werden will, die Betreuung und Bedienung obliegt immer medizinischem Personal, welches mit dem System vertraut ist und Erfahrung hat.

### Who can provide input about the system?

Die Schwierigkeit des Leistungstests wird über den Bremswiderstand der Räder beziehungsweise der Pedale reguliert. Bei ansteigender Stufe wird der Widerstand dementsprechend erhöht. Vitalparamter wie der Puls werden über bestimmte Sensoren in den Griffen gemessen, welche die elektrischen Signale in der Hand aufnehmen.
Die Sauerstoffsättigung wird über ein Pulsoxymeter gemessen, die EKG-Ableitungen werden über ein 4-oder 12-Kanal-EKG aufgezeichnet. All diese Werte werden mithilfe der Software anschließend in mehrerer Schaubildern abgebildet.


## Project Objectives
### Known business rules

Die aufgenommenen Daten stehen unter ärztlicher Schweigepflicht und sind streng vertraulich. Dementsprechend dürfen die Daten nicht an Dritte weitergegeben werden, dies kann nur mit einem Einverständnis der Nutzer:innen erfolgen. Die Daten werden auf den Datenbanken der Krankenhäuser, Sportleistungszentren etc. abgespeichert und nur von der betreuenden Fachkraft eingesehen.

### System information and/or diagrams

Beispiel von aufgezeichneten EKG Daten
![](ekg_example.png)

Anhand dieser Abbildungen, welche aus den aufgenommenen Daten des Leistungstests aufgenommen werden, können wichtige Werte wie die Herzfrequenz, die Amplitude der QRS-Komplexe und die Herzfrequenzvariablität ausgelsen werden. Die Herzfrequenzvariablität bschreibt, wie regelmäßig die einzelnen Herzschläge aufeinander folgen und welche Abstände dazwischen herrschen. Anhand der Auslenkung der Komplexe kann erkannt werden, wie gut die Reizweiterleitung im Herzen funktioniert. Außerdem können mithilfe eines EKGs Erkrankungen wie ein Herzinfarkt oder Kammerflimmern an Unregelmäßigkeiten in den Ableitungen erkannt werden.

### Assumptions and dependencies

Die Daten in den power_data_i.txt Dateien zeigen die sich ändernde Leistung über die Zeit. Die 3 Probanden, welche mit unterschiedlichen Widerständen und somit unterschiedlichen Leistungen (P1 mit 200W, P2 mit 100W und P3 mit 300W) fahren, schwanken mit einer Leistungsbweichung von maximal 10% von Ihrem Ausgangswert. Die Testdauer beträgt bei allen Probanden 3 Minuten, was 180 Sekunden entspricht. Hierbei wird jede Sekunde ein neuer Wert ermittelt, was zu 180 Kraftmessungen in 180 Sekunden führt (Frequenz = 1Hz). Proband 1 und 2 sind jeweils 34 Jahre alt, Proband 3 ist 28 Jahre alt. Zusätzlich werden von jedem Probanden die EKG-Daten gespeichert und aufgezeichnet, welche in den ecg_data_subject_i_csv Dateien zu finden sind.
### Design and implementation constraints

Das Fahrradergometer ähnelt im Aufabeu sehr dem eines handelsüblichen Fahrrad. Die Funktion des Ergometers muss bei Verkauf von den Medizintechnikern kontrolliert und von einem Fachunternehmen abgenommen werden. Erst dann steht es zum Verkauf bereit. Die Prozessabläufe und die Implementierung der Daten muss auch regelmäßig auf Funktion und Richtigkeit kontrolliert werden, damit eine reibungslose Leistungsdiagnose gewährleistet werden kann.

## Risks

Die größe Gefahr besteht darin, sich auf dem Fahrradergometer zu verletzen (zum Beispiel Oberschenkelfraktur). Deswegen ist eine gute Einführung und eine genaue Betreuung notwendig. Ein weiteres Risiko ist, dass Patienten:innen mit einer unerkannten Herzerkrankung zu schnell anfangen und es zu ernsthaften Komplikationen (zum Beispiel Kammerflimmern, Synkope) kommen kann. Aus diesem Grund ist ein ausführliches Vorgespräch notwendig, um das Risiko zu minimieren.

## Known future enhancements

In Zukunft will man erreichen, dass man zusätzlich die aufgewendete Energie messen kann. Diese wird benötigt, um das Ergometer unterschiedlich schnell zu beschleunigen, was sich wiederum unterschiedlich auf die Herzfrequent auswirkt. Außerdem will man versuchen, den Radwiderstand (Reibewiderstand etc.) so gering wie möglich zu halten, damit man möglichst genau bestimmen kann, was für ein Widerstand gerade wirkt. (im Optimalfall nur der eingestellte Bremswiderstand)

## References

- [Link zur Aufgabenstellung](tbd)

## Open, unresolved or TBD issues

Noch unklar, da noch Informationen fehlen.
