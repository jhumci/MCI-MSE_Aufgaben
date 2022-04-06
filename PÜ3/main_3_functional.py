#%% UC 2.0

#Bibliotheken importieren

import os
import pandas as pd
import numpy as np
import neurokit2 as nk
import json

#%% UC 2.1 Einlesen der Daten------------------------------------------------------------------------------------------------------------------------------------------

## Überprüfen ob Dateien vorhanden sind

list_of_new_tests = [] #leeres Array erstellen wo später die Daten der Tests gespeichert werden
folder_current = os.path.dirname(__file__) 
folder_input_data = os.path.join(folder_current, 'input_data')

def einlesen_daten(folder_input_data):
    """
    Function that loads data from a folder with intput data and returns the data in a list
    
        Parameters:
            - folder_input_data (str): path to the data
         
        Returns:
            - new_ecg_data (array)_ List with EGK data
    
    """
    for file in os.listdir(folder_input_data):
        if file.endswith(".csv"):  #Dateien in diesem Ordner auf die Endung ".csv" überprüft. 
            file_name = os.path.join(folder_input_data, file) #Dateien mit der ".csv"-Endung werden ausgelesen
            subject_id = file_name.split(".")[0][-1]
            new_ecg_data= pd.read_csv(file_name) 
            ## Erstellen einer Liste von Tests, die zu verarbeiten sind
            list_of_new_tests.append(new_ecg_data) #Dateien werden zum leeren Array hinzugefügt
            
    return new_ecg_data
            
new_ecg_data = einlesen_daten() 
new_ecg_data["Subject_3"].plot() #kann geplottet werden


#%% UC 2.2 Vorverarbeiten der Daten------------------------------------------------------------------------------------------------------------------------------------

## Anlegen einer Zeitreihe der Herzfrequenz aus den EKG-Daten

def erste_verarbeitung_Daten(new_ecg_data)

    ekg_data=pd.DataFrame() #Tabelle erstellen (EKG Zeitreihe) 
    ekg_data["ECG"] = new_ecg_data["Subject_3"]

    #find Peaks
    peaks, info = nk.ecg_peaks(ekg_data["ECG"], sampling_rate=1000)#EKG-Peaks aus Datensatz ermitteln und in variable speichern
    number_of_heartbeats = peaks["ECG_R_Peaks"].sum() #Anzahl der Herzschläge aus Peaks ermitteln
    duration_test_min = ekg_data.size/1000/60   #Anzahl der Werte pro Minute ermitteln
    average_hr_test = number_of_heartbeats / duration_test_min #Durchschnittliche Herschfrequenz pro Minute bestimmen

    ## Calculate heart rate moving average
    peaks['average_HR_10s'] = peaks.rolling(window=10000).mean()*60*1000
    peaks['average_HR_10s'].plot()
    
    return peaks, average_hr_test

average_hr_test, peaks = vorverarbeiten(ecg_data_3)


#%% UC 2.3 Analysieren der Daten auf Abbruch-Kriterium-----------------------------------------------------------------------------------------------------------------

#Terminationskriterium standardgemäß auf 'False' setzen

termination = False

## Vergleich der Maximalen Herzfrequenz mit Alter des Patienten

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


    
#%% UC 2.4 Erstellen einer Zusammenfassung----------------------------------------------------------------------------------------------------------------------------

def zusammenfassung(subject, max_hr, term): #druckt alle benötigten Werte aus

    print("Summary for Subject " + str(subject["subject_id"]))
    print("Year of birth:  " + str(subject["birth_year"]))
    print("Test level power in W:  " + str(subject["test_power_w"]))
    print(" \n")
    print("Maximum HR was: " + str(max_hr))
    print("Was test terminated because exceeding HR " + str(term))

## Ausgabe einer Zusammenfassung
print zusammenfassung()

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


#%% UC 2.5 Visualisierung der Daten-----------------------------------------------------------------------------------------------------------------------------------

## Öffnen der Leistungsdaten

# Opening JSON file #Öffnet Leistungsdaten und gibt Länge und power_watts wieder
folder_input_data = os.path.join(folder_current, 'input_data')
file_name =  os.path.join(folder_input_data, 'power_data_3.txt')
power_data_watts = open(file_name).read().split("\n")
power_data_watts.pop(-1)
len(power_data_watts)


# %%
## Erstellung eines Plots

def downsample_peaks():
    
    peaks_downsampled = peaks[peaks.index % 1000 == 0]  
    peaks_downsampled = peaks_downsampled.reset_index(drop=True)
    peaks_downsampled = peaks_downsampled.drop(["ECG_R_Peaks"],axis=1)
    peaks_downsampled["Power (Watt)"] = pd.to_numeric(power_data_watts)
    return peaks_downsampled

peaks_downsampled = downsample_peaks()
peaks_downsampled.plot()

#%% UC 2.6 Manuelle Eingabe eines Abbruchkritierums-------------------------------------------------------------------------------------------------------------------

## Abfrage an Nutzer:in, ob Abgebrochen werden soll

manual_termination = False
manual_termination = input("Is this test invalid? (leave blank if valid): ")

if manual_termination != False:
    termination = True


    
#%% UC 2.7 Speichern der Daten----------------------------------------------------------------------------------------------------------------------------------------


# Speichern der Daten
data = {"User ID": subject_data["subject_id"], "Reason for test termation": manual_termination, "Average Heart Rate": average_hr_test, "Maximum Heart Rate": subject_max_hr, "Test Length (s)": len(power_data_watts), "Test Power (W)": subject_data["test_power_w"], "Average Power": peaks_downsampled["Power (Watt)"].mean()}

json_data_to_save = json.dumps(data)

folder_current = os.path.dirname(__file__) 
folder_input_data = os.path.join(folder_current, 'result_data')
results_file = os.path.join(folder_input_data, 'data.json')

with open(results_file, 'w', encoding='utf-8') as f:
    json.dump(json_data_to_save, f, ensure_ascii=False, indent=4)
# %%
