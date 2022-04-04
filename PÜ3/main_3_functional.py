# %%
# UC 2.0

import os
import pandas as pd
import neurokit2 as nk
import json
import glob
import numpy as np


# %%

def get_number_of_complete_data_sets(subfolder_name):

    '''
    Funktion, die den gegeben Ordner durchsucht 
    und herausfindet wie viele Datensätze es gibt

    Parameters:
        subfolder_name (string): Name des Unterordners

     Returns:
        counter (int): Anzahl der csv-Dateien
    '''

    counter = len(glob.glob1(subfolder_name,"*.csv"))
        
    return counter

#%%


def get_patient_data(subfolder_name, patient_number):

    '''
    Funktion, die den gegeben Ordner durchsucht 
    und zu einer Patentiennummer die Metadaten zurückgibt

    Parameters:
        subfolder_name (string): Name des Unterordners
        patient_number (int): Nummer des Patienten

     Returns:
        subject_data (dictionary): Metadaten des Patienten
    '''


    folder_current = os.path.dirname(__file__) 
    folder_input_data = os.path.join(folder_current, subfolder_name)



    # Opening JSON file

    file_name = folder_input_data = os.path.join(folder_input_data, 'subject_' + str(patient_number) + '.json')

    f = open(file_name)
    
    # returns JSON object as
    # a dictionary
    subject_data = json.load(f)
    return subject_data


#%% UC 2.1 Einlesen der Daten


def get_egk_data(subfolder_name, patient_number):

    '''
    Funktion, die den gegeben Ordner durchsucht 
    und die EKG-Daten des Patienten ausliest

    Parameters:
        subfolder_name (string): Name des Unterordners
        patient_number (int): Nummer des Patienten

     Returns:
        new_ecg_data (array): Zeitreihe des EKG-Daten
    '''


    folder_current = os.path.dirname(__file__) 
    file_name = os.path.join(folder_current, subfolder_name, "ecg_data_subject_" + str(patient_number) +".csv")

    new_ecg_data= pd.read_csv(file_name)

    return new_ecg_data




#%% UC 2.2 Vorverarbeiten der Daten

## Anlegen einer Zeitreihe der Herzfrequenz aus den EKG-Daten

def calculate_heart_rate(ekg_dataframe):

    '''
    Funktion, die einen DataFrame mit EKG_Daten übernimmt und
    daraus die Herzfrequenz ableitet und diesen in einem neuen Dataframe zurück gibt

    Parameters:
        ekg_dataframe (DataFrame): EKG-Daten

     Returns:
        heartrate_data (array): Zeitreihe des Herzschlags
    '''

    ekg_data=pd.DataFrame()


    #ekg_data["ECG"] = ekg_dataframe["Subject_1"]
    ekg_data["ECG"] = ekg_dataframe.iloc[:,1]


    # Find peaks
    peaks, info = nk.ecg_peaks(ekg_data["ECG"], sampling_rate=1000)

    number_of_heartbeats = peaks["ECG_R_Peaks"].sum()

    duration_test_min = ekg_data.size/1000/60

    average_hr_test = number_of_heartbeats / duration_test_min

    ## Calculate heart rate moving average

    peaks['average_HR_10s'] = peaks.rolling(window=10000).mean()*60*1000
    #peaks['average_HR_10s'].plot()

    return peaks['average_HR_10s']


#%% UC 2.3 Analysieren der Daten auf Abbruch-Kriterium


def is_maximum_pulse_exceeded(heart_rate_data,patient_number):

    '''
    Funktion, die einen DataFrame mit Herzfrequenz einer Person übernimmt und
    und anhand der Patientendaten überprüft, ob maximalpuls überschritten

    Parameters:
        ekg_dataframe (DataFrame): Herzraten-Daten

     Returns:
        termination (Boolean): Abbruch-Kriterium erfüllt
    '''

    ## Vergleich der Maximalen Herzfrequenz mit Alter des Patienten
    termination = False

    maximum_hr = heart_rate_data.max()

    subject_max_hr = 220 - (2022 - get_patient_data("input_data",str(patient_number))["birth_year"])

    if maximum_hr > subject_max_hr*0.90:
        termination = True

    return termination



#%% UC 2.4 Erstellen einer Zusammenfassung

# Opening JSON file

def plot_patient_data(subject_data,hr_data):

    '''
    Funktion, die alle Infos über den Patienten printet

    Parameters:
        subject_data (dictionary): Metadaten des Patienten
        hr_data (array): Zeitreihe des Herzschlags
    '''


    print("Summary for Subject " + str(subject_data["subject_id"]))
    print("Year of birth:  " + str(subject_data["birth_year"]))
    print("Test level power in W:  " + str(subject_data["test_power_w"]))
    print("Maximum HR was: " + str(220 - (2022 - subject_data["birth_year"])))
    termination = is_maximum_pulse_exceeded(hr_data, str(subject_data["subject_id"]))
    print("Was test terminated because exceeding HR: " + str(termination))
    print(" \n")
    print(" \n")

#%% UC 2.5 Visualisierung der Daten


def load_power_data(subfolder_name, patient_number):

    '''
    Funktion, die den gegeben Ordner durchsucht 
    und die EKG-Daten des Patienten ausliest

    Parameters:
        subfolder_name (string): Name des Unterordners
        patient_number (int): Nummer des Patienten

     Returns:
        power_data_watts (array): Zeitreihe der Leistungsdaten
    '''

    folder_current = os.path.dirname(__file__) 
    folder_input_data = os.path.join(folder_current, subfolder_name)
    file_name =  os.path.join(folder_input_data, 'power_data_'+ str(patient_number) +'.txt')
    power_data_watts = open(file_name).read().split("\n")
    power_data_watts.pop(-1)
    power_data_watts = [int(x) for x in power_data_watts]
    power_data_watts = np.array(power_data_watts)
    return power_data_watts


# %%
    ## Erstellung eines Plots

def open_and_plot_hr_data(subfolder_name, patient_number, heart_rate_data):

    '''
    Funktion, die den Unterordner, Patientennummer und die HR-Daten übernimmt und
    einen Plot erzeugt

    Parameters:
        subfolder_name (string): Name des Unterordners
        heart_rate_data (array): Zeitreihe des Herzschlags
        patient_number (int): Nummer des Patienten
    '''
    #peaks['average_HR_10s'].plot()

    peaks_downsampled = heart_rate_data[heart_rate_data.index % 1000 == 0]  

    peaks_downsampled = peaks_downsampled.reset_index(drop=True)
  

    peaks_downsampled.plot()



#%% UC 2.6 Manuelle Eingabe eines Abbruchkritierums


def ask_for_manual_termination():

    '''
    Funktion, die den Diagnosiker nach einem Grund für Abbruch fragt
    Gibt zurück, ob Abgebrochen wurde oder nicht

     Returns:
        termination (Boolean): Abbruch-Kriterium erfüllt
    '''

## Abfrage an Nutzer:in, ob Abgebrochen werden soll

    manual_termination = False
    manual_termination = input("Is this test invalid? (leave blank if valid): ")

    if manual_termination != False:
        termination = True

    return manual_termination



#%% UC 2.7 Speichern der Daten

def store_data(subject_data, manual_termination, hr_data, power_data):


    '''
    Funktion, die die Ergebnisse in einer JSON Datei speichert

    Parameters:
        subject_data (dictionary): Metadaten des Patienten

    '''

    # Speichern der Daten
    data = {"User ID": subject_data["subject_id"], "Reason for test termation": manual_termination, "Average Heart Rate": hr_data.mean(), "Maximum Heart Rate": hr_data.max(), "Test Length (s)": len(hr_data)/1000, "Test Power (W)": subject_data["test_power_w"], "Average Power": power_data.mean()}

    json_data_to_save = json.dumps(data)

    folder_current = os.path.dirname(__file__) 
    folder_input_data = os.path.join(folder_current, 'result_data')
    results_file = os.path.join(folder_input_data, 'data.json')

    with open(results_file, 'w', encoding='utf-8') as f:
        json.dump(json_data_to_save, f, ensure_ascii=False, indent=4)


# %% Ablauf des Programms

subfolder_name = "input_data"
number_of_patients = get_number_of_complete_data_sets(subfolder_name)

for patient_number in range(1, 4):

    subject_data = get_patient_data(subfolder_name, patient_number)
    ekg_data = get_egk_data(subfolder_name, patient_number)
    power_data = load_power_data(subfolder_name, patient_number)
    hr_data = calculate_heart_rate(ekg_data)
    termination = is_maximum_pulse_exceeded(hr_data,patient_number)
    plot_patient_data(subject_data, hr_data)
    open_and_plot_hr_data(subfolder_name, patient_number, hr_data)
    termination = ask_for_manual_termination()
    store_data(subject_data, termination, hr_data, power_data)



# %%
