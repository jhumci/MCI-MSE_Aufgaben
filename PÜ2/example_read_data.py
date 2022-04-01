'''
# %% Import der nötigen Pakete
import numpy as np
import matplotlib.pyplot as plt

# %% Öffnen der Datei und konvertieren zu numpy-Array
file_name =  'input_data/power_data_1.txt'
power_data_watts = open(file_name).read().split("\n")
x = np.array(power_data_watts)

# %% Erstellen des Plots
plt.title("Line graph")
plt.plot(x, color="red")

plt.show()

'''


# %% Musterlösung von  Richard und Rafael


# import required modules
import os
import numpy as np
import matplotlib.pyplot as plt

# assign directory to run through
directory = "./input_data"
 
# iterate over files in directory
for filename in os.listdir(directory):
    
    # checking if it is a power data file
    if filename.startswith("power_data") and filename.endswith(".txt"):
        
        # open file and convert to numpy array
        power_data_watts = open(os.path.join(directory, filename)).read().split("\n")
        data = np.array(power_data_watts)

        # get number of power data for plot
        number = filename.split("_")
        number = number[2].split(".")

        # plot data with multiple windows
        plt.figure("Power Data " + number[0])
        plt.title("Power Data " + number[0])
        plt.plot(data, color="red")

plt.show()
# %%

def load_power_data(directory):
    
    power_data = []
    
    # hier code

    return power_data

# %%

def plot_time_series_data(array_data, title, line_color):

    # plot data with multiple windows

    # store data

    # Where the figure is stored
    path = ""


    return path

# %% Anwendung

directory = ""

all_power_data = load_power_data(directory)

for power_array in all_power_data:
    plot_time_series_data(power_array, "Power Data", "red")

# %%
import os
import numpy as np
import matplotlib.pyplot as plt

def create_figure_from_power_data(directory):

    figures = []

    # iterate over files in directory
    for filename in os.listdir(directory):
        
        # checking if it is a power data file
        if filename.startswith("power_data") and filename.endswith(".txt"):
            
            # open file and convert to numpy array
            power_data_watts = open(os.path.join(directory, filename)).read().split("\n")
            data = np.array(power_data_watts)

            # get number of power data for plot
            number = filename.split("_")
            number = number[2].split(".")

            # plot data with multiple windows
            plt.figure("Power Data " + number[0])
            plt.title("Power Data " + number[0])
            plt.plot(data, color="red")
            

    return figures
    