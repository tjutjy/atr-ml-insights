import numpy as np
import csv
import scipy.signal as sg
import matplotlib.pyplot as plt

#It is aimed to find peak.

#-------------------------------------------
#Read data
#-------------------------------------------
x = list()
yyy = list() #Store the data in the first column

with open('x.csv','r',encoding='utf-8-sig') as f:  #Read in x, round it up, to find the peak
    reader=csv.reader(f)
    for row in reader:
        x.append(int(row[0]))
x=np.array(x)

with open('yyy.csv','r',encoding='utf-8-sig') as f: #Enter Y, which was the absorbance at different wave numbers. In CSV files, each line represents a raw material.
    reader=csv.reader(f)
    for row in reader:
        yyy.append(row)

#-------------------------------------------
#Find peak
#-------------------------------------------
peak_x=list()
peak_y=list()
for i in range(0,len(yyy)):
    peak_id,peak_property = sg.find_peaks(yyy[i], height=0, distance=100, prominence=0.014)
    peak_freq = x[peak_id]
    peak_height = peak_property['peak_heights']
    peak_x.append(peak_freq.tolist())
    peak_y.append(peak_height.tolist())

#-------------------------------------------
#Export Data
#-------------------------------------------
output=csv.writer(open('peaks-.csv','a+',newline=''),dialect='excel')
output.writerows(map(lambda x:[x],peak_x))
