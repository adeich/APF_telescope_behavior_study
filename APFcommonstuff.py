from io import StringIO
import pandas

csv_string = """
raw_name,short_name,units,description
DateTimeLocal, Local Datetime,,Datetime at Lick Observatory 
YearMonthDayHour,,, 
EpocSeconds, , , 
exposure_begin_datetime, Beginning of exposure, , Time the exposure began 
exposure_end_datetime, End of exposure, , Time the exposure ended
velocity, velocity, m/s, measured velocity of a benchmark star 
velocity_error, , , 
stellar_activity1, , , 
stellar_activity2, , , 
total_counts, , , 
brad_doesnt_know, , , 
DateTimeUTC, , , 
starID, , , 
MIDPTFIN, , , 
AZ, , , 
EL, , , 
AZENCPOS,Azimuthal Encoder Position,clicks,Telescope's vertical angle encoder position. 
ELENCPOS,Elevation Encoder Position,clicks,
AZENCVEL, , , 
ELENCVEL, , , 
AZFLWERR, , , 
ELFLWERR, , , 
OUTFILE, , , 
OBSNUM, , , 
MODE, , , 
AVG_FWHM, , , 
M5WIND, , , 
M5WINDAZ, , , 
TAVERAGE, , , 
TM1S210, , , 
TM2CAIR, , , 
OFFSET_AZ, , , 
OFFSET_EL, , , 
RMSOFFSET_AZ, , , 
RMSOFFSET_EL, , , 
AVGOFFSET_AZ, , , 
AVGOFFSET_EL, , , 
HATCHPOS, , , 
night_start_temperature, , , 
night_start_TM1S210, , , 
night_start_TM2CAIR, , , 
delta_TAVERAGE, , , 
delta_TM1S210, , , 
delta_TM2CAIR, , , 
wind_dome_angle, , , 

"""

string_io = StringIO(csv_string)
df = pandas.read_csv(string_io)
df.set_index('raw_name', inplace=True)

def shortname(raw_name):
    output_string = str(df.loc[raw_name]['short_name'])
    return output_string

def units(raw_name):
    output_string = str(df.loc[raw_name]['units'])
    return output_string

def description(raw_name):
    output_string = str(df.loc[raw_name]['description'])
    return output_string

