# %% Import der nötigen Pakete
from importlib.resources import path
import numpy as np
import matplotlib.pyplot as plt
# OS (Operating System) importieren, um Zugriff auf das Directory zu erlangen		#Flo
import os

# %% Dateipfade erlangen; Source: https://www.geeksforgeeks.org/file-searching-using-python/		#Flo
# Funktion definieren, welche den Dateipfad für gesuchte Dateien findet		#Flo
def getFilePath(filename):

	# Ordnerstruktur des auführenden Systems einlesen		#Flo
	dir_path = os.path.dirname(os.path.realpath(__file__))

	# leeres Numpy Array zur Speicherung der relevanten Ordnerpfade		#Flo
	filepath = np.array([])

	# Schleife zum Durchlaufen der Ordnerstruktur	#Flo
	for root, dirs, files in os.walk(dir_path):
		# Schleife zum Vergleich jeder einzelnen Datei mit dem Suchparameter		#Flo
		for file in files:

			# Dateien auf Suchparameter untersuchen		#Flo
			if file.startswith(filename):
				# Variable zur Speicherung des Dateipfades definieren		#Flo
				pathstring = (root+'/'+str(file))
				# Entsprechenden Dateipfad an Numpy Array "anhängen"		#Flo
				filepath = np.append(filepath, pathstring)

	# Numpy Array als Resultat der Suche zurückgeben		#Flo
	return filepath

# %% Funktionsaufruf um Dateipfade für 'power_data' Dateien zu erlangen
file_names =  getFilePath('power_data_')

# Dateien öffnen und aus Werten Plots erstellen (i=Dateifpad in file_names)			#Flo
for i in file_names:
	# Zeilen einzeln auslesen		#Flo
	power_data_watts = open(i).read().split("\n")
	# Numpy Array aus ausgelesenen Werten erstellen		#Flo
	x = np.array(power_data_watts)

	# Erstellen des Plots aus ausgelesenen Werten (x)		#Flo
	plt.title("Line graph")
	plt.plot(x, color="red")
	
	# Plot ausgeben
	plt.show()
