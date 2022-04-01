# %% Import der nötigen Pakete
import numpy as np
import matplotlib.pyplot as plt

#%% Öffnen der Datei und konvertieren zu numpy-Array
def performance_data():
    for i in range (1,4):
        file_name =  ('input_data/power_data_{0}.txt'.format(i))
        power_data_watts = open(file_name).read().split("\n")
        x = np.array(power_data_watts)
        plt.title(("Line graph {0}").format(i))
        plt.plot(x, color="red")

        plt.show()

# %% Erstellen des Plots
performance_data()

# Bewertung: Gute Lösung, vor allem die direkte Umsetzung in einer Funktion. Beim nächsten mal die For-Schleife um die Funktion herumbauen. Siehe unten:
# for i in range(1,4)
#   performance_data(i)
# %%

# %%
