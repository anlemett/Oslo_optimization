import pandas as pd
import os
import matplotlib.pyplot as plt

#conda install -c conda-forge mscorefonts

#from matplotlib import font_manager
#print(font_manager.findfont("Times New Roman") )

# activate latex text rendering
#plt.rcParams["text.usetex"] = True
plt.rcParams["font.family"] = "Times New Roman"
#plt.rcParams["font.family"] = "serif"
#plt.rcParams["font.serif"] = "Times New Roman"
#plt.rcParams['font.weight']= 'bold'

from matplotlib import rcParams
rcParams.update({'figure.autolayout': False})

import statistics
from textwrap import wrap

AIRPORT_ICAO = "ENGM"

PI_name = "timeOnLevelsPercent"
notPMlegs = True

PI_y_label = "Time Flown Level (%)"
figure_filename = "boxplot_time_on_levels_4"

PIs_dict = {}

DATA_DIR = os.path.join("data", AIRPORT_ICAO)
PIs_DIR = os.path.join(DATA_DIR, "PIs")

filename1 = "states_before_optimization_PIs_vertical_by_flights.csv"
filename2 = "ENGM_optimization_oct_1_5-6_fixed2_PIs_vertical_by_flights.csv"
filename3 = "states_before_optimization_PIs_vertical_by_flights_notPMlegs.csv"
filename4 = "ENGM_optimization_oct_1_5-6_fixed2_PIs_vertical_by_flights_notPMlegs.csv"
                        
full_filename1 = os.path.join(PIs_DIR, filename1)
full_filename2 = os.path.join(PIs_DIR, filename2)
full_filename3 = os.path.join(PIs_DIR, filename3)
full_filename4 = os.path.join(PIs_DIR, filename4)

PIs_df1 = pd.read_csv(full_filename1, sep=' ')
PIs_df2 = pd.read_csv(full_filename2, sep=' ')
PIs_df3 = pd.read_csv(full_filename3, sep=' ')
PIs_df4 = pd.read_csv(full_filename4, sep=' ')
    
PIs_dict["before opt"] = PIs_df1[PI_name]
PIs_dict["after opt"] = PIs_df2[PI_name]
PIs_dict["before opt no seq.legs"] = PIs_df3[PI_name]
PIs_dict["after opt no seq.legs"] = PIs_df4[PI_name]


PI_median1 = PIs_dict["before opt"].median()
PI_mean1 = PIs_dict["before opt"].mean()
PI_std1 = statistics.stdev(PIs_dict["before opt"])
PI_min1 = PIs_dict["before opt"].min()
PI_max1 = PIs_dict["before opt"].max()

PI_median2 = PIs_dict["after opt"].median()
PI_mean2 = PIs_dict["after opt"].mean()
PI_std2 = statistics.stdev(PIs_dict["after opt"])
PI_min2 = PIs_dict["after opt"].min()
PI_max2 = PIs_dict["after opt"].max()

PI_median3 = PIs_dict["before opt no seq.legs"].median()
PI_mean3 = PIs_dict["before opt no seq.legs"].mean()
PI_std3 = statistics.stdev(PIs_dict["before opt no seq.legs"])
PI_min3 = PIs_dict["before opt no seq.legs"].min()
PI_max3 = PIs_dict["before opt no seq.legs"].max()

PI_median4 = PIs_dict["after opt no seq.legs"].median()
PI_mean4 = PIs_dict["after opt no seq.legs"].mean()
PI_std4 = statistics.stdev(PIs_dict["after opt no seq.legs"])
PI_min4 = PIs_dict["after opt no seq.legs"].min()
PI_max4 = PIs_dict["after opt no seq.legs"].max()

# median/mean/std/min/max    
print("before opt " + PI_name + f" {PI_median1:.2f}" + f" {PI_mean1:.2f}" + f" {PI_std1:.2f}" + f" {PI_min1:.2f}" + f" {PI_max1:.2f}")
print("after opt " + PI_name + f" {PI_median2:.2f}" + f" {PI_mean2:.2f}" + f" {PI_std2:.2f}" + f" {PI_min2:.2f}" + f" {PI_max2:.2f}")
print("before opt no seq.legs " + PI_name + f" {PI_median3:.2f}" + f" {PI_mean3:.2f}" + f" {PI_std3:.2f}" + f" {PI_min3:.2f}" + f" {PI_max3:.2f}")
print("after opt no seq.legs " + PI_name + f" {PI_median4:.2f}" + f" {PI_mean4:.2f}" + f" {PI_std4:.2f}" + f" {PI_min4:.2f}" + f" {PI_max4:.2f}")


#fig, ax = plt.subplots(1, 1,figsize=(7,5))
fig, ax = plt.subplots(1, 1,figsize=(7,5), dpi = None)

boxprops = dict(linestyle='--', linewidth=1, color='gray')
meanpointprops = dict(marker='s', markersize=5, markeredgecolor='dimgrey', markerfacecolor='grey')
box_plot = ax.boxplot(PIs_dict.values(), sym='+', boxprops=boxprops, meanprops=meanpointprops, patch_artist=True, showmeans=True)

###########Color version###################

# Colors are from: https://colorbrewer2.org/#type=diverging&scheme=RdYlBu&n=3
# 3 data classes, diverging, colorblind safe, print friendly
orange_rgb = (252,141,89)
yellow_rgb = (255,255,191)
blue_rgb = (145,191,219)

orange = tuple(c/255 for c in orange_rgb)
yellow = tuple(c/255 for c in yellow_rgb)
blue = tuple(c/255 for c in blue_rgb)

colors = [orange,  blue, orange,  blue]

for patch, color in zip(box_plot['boxes'], colors):
    patch.set_facecolor(color)
    #patch.set_alpha(0.5)

for flier, color in zip(box_plot['fliers'], colors):
    #flier.set(markeredgecolor = color, alpha = 0.9)
    flier.set(markeredgecolor = 'darkgray', alpha = 0.9)
    
for element in ['whiskers', 'caps', 'medians']:
    plt.setp(box_plot[element], color='dimgray')

for whisker in box_plot['whiskers']:
    whisker.set(linestyle ="--")

########################################

labels = ["before opt", "after opt", "before opt no seq.legs", "after opt no seq.legs"]
labels = ['\n'.join(wrap(x, 11)) for x in  labels]
ax.set_xticklabels(labels, fontsize=16)
plt.ylabel(PI_y_label, fontsize=22)
plt.yticks(fontsize=16)

plt.subplots_adjust(left=0.11, right=0.99, top=0.99, bottom=0.12)
#plt.tight_layout()

#plt.savefig(os.path.join(PIs_DIR, figure_filename + ".eps"), dpi=300)
plt.savefig(os.path.join(PIs_DIR, figure_filename + ".png"), dpi=300)

plt.show()
