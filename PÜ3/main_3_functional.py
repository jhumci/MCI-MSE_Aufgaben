# UC 2.0

#%% UC 2.1 Einlesen der Daten

## Überprüfen ob Dateien vorhanden sind

import os
from pydoc import doc
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def getFilePath(filename, fileformat):

	# Ordnerstruktur des auführenden Systems einlesen
	dir_path = os.path.dirname(os.path.realpath(__file__))

	# leeres Numpy Array zur Speicherung der relevanten Ordnerpfade
	filepath = np.array([])

	# Schleife zum Durchlaufen der Ordnerstruktur
	for root, dirs, files in os.walk(dir_path):
		# Schleife zum Vergleich jeder einzelnen Datei mit dem Suchparameter
		for file in files:

			# Dateien auf Suchparameter untersuchen
			if file.startswith(filename) & file.endswith(fileformat):
				# Variable zur Speicherung des Dateipfades definieren
				pathstring = (root+'/'+str(file))
				# Entsprechenden Dateipfad an Numpy Array "anhängen"
				filepath = np.append(filepath, pathstring)

	# Numpy Array als Resultat der Suche zurückgeben
	return filepath

# CSV-Dateien auslesen über Pandas
def get_csv_data(pathstring):
    
    #Subject ID aus Pfad auslesen
    subject_id = pathstring.split(".")[0][-1]   
    #CSV-Datei auslesen und in Variable speichern
    new_test_data = pd.read_csv(pathstring)

    #Rückgabewerte Inhalt der CSV-Datei sowie Datei-ID
    return new_test_data, subject_id

def plot_data(title, dataset, id):

    #Plot-Titel definieren 
    plt.title(title+": "+ id)
    #Dataset plotten
    dataset["Subject_"+ id].plot()

    #Dataset ausgeben
    plt.show()

#Dateipfade für EKG-Daten erhalten
ecg_paths = getFilePath('ecg_data', '.csv')

#Schleife zur Erstellung von EKG-Plot
for i in ecg_paths:

    #für jeden Dateipfad CSV-Dateien auslesen
    ecg_data, subject_id = get_csv_data(i)

    #Werter aus CSV-Dateien einzeln plotten
    plot_data("ECG-Data", ecg_data, subject_id)





#%% UC 2.2 Vorverarbeiten der Daten

## Anlegen einer Zeitreihe der Herzfrequenz aus den EKG-Daten

import neurokit2 as nk

# Find peaks
def find_peaks(datacolumn):

    #EKG-Peaks aus Datensatz ermitteln und in variable speichern
    peaks, info = nk.ecg_peaks(datacolumn, sampling_rate=1000)

    #Anzahl der Herzschläge aus Peaks ermitteln
    number_of_heartbeats = peaks["ECG_R_Peaks"].sum()

    #Anzahl der Werte pro Minute ermitteln
    duration_test_min = datacolumn.size/1000/60

    #Durchschnittliche Herschfrequenz pro Minute bestimmen
    average_hr_test = number_of_heartbeats / duration_test_min


    ## Calculate heart rate moving average
    peaks['average_HR_10s'] = peaks.rolling(window=10000).mean()*60*1000
   
    #Durchschnittswerte(Peaks) zur Weiterverarbeitung zurückgeben
    return peaks['average_HR_10s']

#Pandas Dataframe erzeugen
ekg_data=pd.DataFrame()
sub_peaks = np.array([])

#Schleife die Pfade für ecg-data einzeln ausliest
for e in ecg_paths:

    #EKG-Daten in Variable speichern, zugehörige Test-ID auslesen
    new_ecg_data, subject_id = get_csv_data(e)

    #Dataframe an Stelle[subject_id](=1-3) mit EKG-Daten befüllen
    ekg_data[subject_id] = new_ecg_data["Subject_"+subject_id]

    #Schleife zum Auslesen der einzelnen Spalten im Dataframe
    for column in ekg_data:

        #Funktionsaufruf find_peaks 
        peaks_avg = find_peaks(ekg_data[column])
        
        sub_peaks = np.append(sub_peaks, peaks_avg)

    #Plot Titel erstellen
    plt.title("ECG: "+ column)
    #Peak-Datensätze plotten
    peaks_avg.plot()

    #Plot zu verarbeiteten EKG-Werten ausgeben (Filterung der Werte wird sichtbar)
    plt.show()   

#%% UC 2.3 Analysieren der Daten auf Abbruch-Kriterium

#Terminationskriterium standardgemäß auf 'False' setzen
termination = False

## Vergleich der Maximalen Herzfrequenz mit Alter des Patienten

import json

#Json-Objekte auslesen/laden
def load_json(path):

    #JSON-Datei öffnen nach mitgegebenem Dateipfad
    j_f = open(path)
    
    # returns JSON object as
    # a dictionary
    subject_data = json.load(j_f)
    #Subect-ID des JSON-Objekts speichern
    json_id = str(subject_data['subject_id'])

    return subject_data, json_id


#Terminationskriterium ermittlen
def examine_hr(subject_data, hr_peaks):

    maximum_hr = hr_peaks.max()

    subject_max_hr = 220 - (2022 - subject_data["birth_year"])

    if maximum_hr > subject_max_hr*0.90:
        termination = True

    return maximum_hr, termination


#UC 2.4 Erstellen einer Zusammenfassung

def summarize(subject, max_hr, term):

    print("Summary for Subject " + str(subject["subject_id"]))
    print("Year of birth:  " + str(subject["birth_year"]))
    print("Test level power in W:  " + str(subject["test_power_w"]))
    print(" \n")
    print("Maximum HR was: " + str(max_hr))
    print("Was test terminated because exceeding HR " + str(term))

## Ausgabe einer Zusammenfassung

#Dateipfade zu Json-Datein ermitteln
json_file = getFilePath("subject_", "json")

#Dateipfade iterativ abarbeiten
for j in json_file:

    #Json-Datei und Objekt-ID auslesen/laden
    subject_data, json_id = load_json(j)

    #Herzraten/Peaks für Weiterverarbeitung auslesen
    peaks = find_peaks(ekg_data[json_id])

    #Terminationskriterium ermitteln (Vergleich Alter-Herzrate)
    max_hr, term = examine_hr(subject_data, peaks)

    #Zusammenfassung erstellen (Json-Objekt, Herzrate und Term.-Kriterium) und ausgeben
    summarize(subject_data, max_hr, term)





# %% UC 2.5 Visualisierung der Daten
## Erstellung eines Plots

def plot_power(power_data, subject_peak):


    peaks_downsampled = subject_peak[peaks.index % 1000 == 0]  

    peaks_downsampled = peaks_downsampled.reset_index(drop=True)
    peaks_downsampled = peaks_downsampled.drop(["ECG_R_Peaks"],axis=1)

    peaks_downsampled["Power (Watt)"] = pd.to_numeric(power_data_watts)

    peaks_downsampled.plot()


#Leistungsdaten von Ergometer ermitteln, Pfad zu Leistungsmessungen ermitteln
power_data_path = getFilePath("power_data_", ".txt")

#Leistungsdaten iterativ abarbeiten
for p in power_data_path:

    #Textdateien öffnen und Inhalt in 
    power_data_watts = open(p).read().split("\n")
    power_data_watts.pop(-1)
    
    plot_power(power_data_watts, peaks_avg)



#%% UC 2.6 Manuelle Eingabe eines Abbruchkritierums

## Abfrage an Nutzer:in, ob Abgebrochen werden soll

manual_termination = False
manual_termination = input("Is this test invalid? (leave blank if valid): ")

if manual_termination != False:
    termination = True


#%% UC 2.7 Speichern der Daten


# Speichern der Daten
data = {"User ID": subject_data["subject_id"], "Reason for test termation": manual_termination, "Average Heart Rate": average_hr_test, "Maximum Heart Rate": subject_max_hr, "Test Length (s)": len(power_data_watts), "Test Power (W)": subject_data["test_power_w"], "Average Power": peaks_downsampled["Power (Watt)"].mean()}

json_data_to_save = json.dumps(data)

folder_current = os.path.dirname(__file__) 
folder_input_data = os.path.join(folder_current, 'result_data')
results_file = os.path.join(folder_input_data, 'data.json')

with open(results_file, 'w', encoding='utf-8') as f:
    json.dump(json_data_to_save, f, ensure_ascii=False, indent=4)
# %%

# %%

