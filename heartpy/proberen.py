import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import heartpy as hp
import matplotlib.pyplot as plt
import pandas as pd
import heartpy.exceptions as exceptions

# Define path to CSV file
file_path = r"C:\Users\20192414\OneDrive - TU Eindhoven\Desktop\24-25\Stage\proefdata\proefHR.csv"  

# Load the data using pandas to handle a single column
data = pd.read_csv(file_path, header=None, skiprows=2)  # Assuming no headers, load as a single column
data = data.iloc[:, 0]  # Extract the single column of data

# Create a simple timer (time values) based on the row index, assuming equal intervals
timer = list(range(1, len(data) + 1))

# Set the sample rate (in Hz)
sample_rate = 64  # Adjust this to match your data's actual sample rate

# First Plot: Original Heart Rate Data
plt.figure(figsize=(10, 6))
plt.plot(timer, data, label='Original Heart Rate Data', color='b')
plt.xlabel('Time (arbitrary units)')
plt.ylabel('Heart Rate (bpm)')
plt.title('Original Heart Rate Data')
plt.legend()
plt.grid(True)

# Second Plot: Filtered Heart Rate Data
filtered_data = hp.filter_signal(data, [0.7, 3.5], sample_rate=sample_rate, order=3, filtertype='bandpass')
plt.figure(figsize=(10, 6))
plt.plot(timer, filtered_data, label='Filtered Heart Rate Data', color='g')
plt.xlabel('Time (arbitrary units)')
plt.ylabel('Heart Rate (bpm)')
plt.title('Filtered Heart Rate Data')
plt.legend()
plt.grid(True)

# Third Plot: Filtered Heart Rate Data with Detected Peaks
wd, m = hp.process(filtered_data, sample_rate)
plt.figure(figsize=(10, 6))
plt.plot(timer, filtered_data, label='Filtered Heart Rate Data', color='g')
plt.scatter(wd['peaklist'], filtered_data[wd['peaklist']], color='r', label='Detected Peaks')  # Red dots for peaks
plt.xlabel('Time (arbitrary units)')
plt.ylabel('Heart Rate (bpm)')
plt.title('Filtered Heart Rate Data with Detected Peaks')
plt.legend()
plt.grid(True)

# Show all plots at once
plt.show()

# Display measures computed
for measure in m.keys():
    print('%s: %f' % (measure, m[measure]))
