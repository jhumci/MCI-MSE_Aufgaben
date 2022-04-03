# %% Import der nötigen Pakete
import numpy as np
import matplotlib.pyplot as plt

# %% Öffnen der Datei und konvertieren zu numpy-Array

for i in range (1,4):
    file_name =  'input_data/power_data_' +str(i) + '.txt'
    power_data_watts = open(file_name).read().split("\n")
    x = np.array(power_data_watts)

    plt.title("Line graph")
    plt.plot(x, color="red")

    plt.show()

# %%
