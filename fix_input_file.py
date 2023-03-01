import os
import re

AIRPORT_ICAO = "ENGM"

DATA_DIR = os.path.join("data", AIRPORT_ICAO)

INPUT_DIR = os.path.join(DATA_DIR, "States")

input_filename = "ENGM_optimization_oct_1_5-6.csv"

full_input_filename = os.path.join(INPUT_DIR, input_filename)

new_filename = "ENGM_optimization_oct_1_5-6_fixed.csv"
full_new_filename = os.path.join(INPUT_DIR, new_filename)

fin = open(full_input_filename, "rt")
fout = open(full_new_filename, "wt")

#for line in fin:
#	fout.write(' '.join(line.split()))

Lines = fin.readlines()
for line in Lines:
    fout.write(re.sub('\s+',' ',line))
    fout.write("\n")
    
fin.close()
fout.close()