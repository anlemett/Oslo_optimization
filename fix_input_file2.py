import pandas as pd
import os

AIRPORT_ICAO = "ENGM"

DATA_DIR = os.path.join("data", AIRPORT_ICAO)

INPUT_DIR = os.path.join(DATA_DIR, "States")

input_filename = "ENGM_optimization_oct_1_5-6_fixed.csv"

full_input_filename = os.path.join(INPUT_DIR, input_filename)

output_filename = "ENGM_optimization_oct_1_5-6_fixed2.csv"

full_output_filename = os.path.join(INPUT_DIR, output_filename)

df = pd.read_csv(full_input_filename, sep=' ', 
                on_bad_lines='warn', 
                #names = ['flightId', 'sequence', 'timestamp', 'lat', 'lon', 'rawAltitude', 'altitude', 'velocity', 'beginDate', 'endDate'],
                names = ['flightId', 'sequence', 'timestamp', 'lat', 'lon', 'rawAltitude', 'altitude', 'velocity', 'endDate'],
                #dtype={'flightId':str, 'sequence':int, 'timestamp':int, 'lat':float, 'lon':float, 'rawAltitude':float, 'altitude':float, 'velocity':float, 'beginDate':str, 'endDate':str})
                dtype={'flightId':str, 'sequence':int, 'timestamp':float, 'lat':float, 'lon':float, 'rawAltitude':float, 'altitude':float, 'velocity':float, 'endDate':str},
                index_col=False
                )
       

df['altitude'] = df.apply(lambda row: row['altitude']/3.281, axis=1)
df['rawAltitude'] = df.apply(lambda row: row['rawAltitude']/3.281, axis=1)

df.set_index(['flightId', 'sequence'], inplace=True)

newdf = pd.DataFrame()

for flight_id, flight_group in df.groupby(level='flightId'):
    group_len = len(flight_group)
    new_seq = range(0, group_len)
    flight_group["new_seq"] = new_seq
    newdf = pd.concat([newdf, flight_group])

newdf = newdf.reset_index(level='sequence')

newdf = newdf.drop('sequence', axis=1)

newdf = newdf.rename(columns={'new_seq': 'sequence'})

newdf.reset_index(inplace=True)
newdf.set_index(['flightId', 'sequence'], inplace=True)

print(newdf.head())

newdf.to_csv(full_output_filename, sep = ' ', header = False, index = True)
