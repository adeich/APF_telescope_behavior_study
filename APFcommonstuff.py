from io import StringIO
import pandas

csv_string = """
raw_name,short_name,units,description
DateTimeLocal, Local Datetime,,Datetime at Lick Observatory 
YearMonthDayHour,,, 
EpocSeconds,,, 
exposure_begin_datetime, Beginning of exposure, , Time the exposure began 
exposure_end_datetime, End of exposure, , Time the exposure ended
velocity, velocity, m/s, measured velocity of a benchmark star 
velocity_error,,, 
stellar_activity1,,, 
stellar_activity2,,, 
total_counts,,, 
brad_doesnt_know,,, 
DateTimeUTC,,,
starID,,,
MIDPTFIN,,,
AZ,Telescope azimuth,degrees,Telescope's azimuthal direction (0 degrees is north) 
EL,Telescope elevation,degrees,Telescope's vertical angle 
AZENCPOS,Azimuthal Encoder Position,counts,Telescope's vertical angle encoder position 
ELENCPOS,Elevation Encoder Position,counts,
AZENCVEL,Azimuth encoder velocity,counts/sec, 
ELENCVEL,Elevation encoder velocity,counts/sec, 
AZFLWERR,Azimuth following error,encoder counts, 
ELFLWERR,Elevation following error,encoder counts, 
OUTFILE,,, 
OBSNUM,,, 
MODE,,, 
AVG_FWHM,Average full-width-half-max of spectrum,pixels,If the FWHM is large then either the seeing sucks or there is a problem with the telescope (oscillations) or the focus is badly awry. 
M5WIND,APF windspeed,mph, 
M5WINDAZ,APF wind direction,degrees from North, 
TAVERAGE,Average temperature,degrees C, 
TM1S210,Temperature of mirror 1,degrees C, 
TM2CAIR,Temperature of can air,degrees C,Temperature of air can behind mirror 
OFFSET_AZ,Azimuth offset,arcsec,In a guide image the Az offset of the object from the guide center.  Ie this is how much the guider wants to move the telescope in azimuth 
OFFSET_EL,Elevation offset,arcsec,In a guide image the el offset of the object from the guide center. Ie this is how much the guider wants to move the telescope in elevation 
RMSOFFSET_AZ,,, 
RMSOFFSET_EL,,, 
AVGOFFSET_AZ,,, 
AVGOFFSET_EL,,, 
HATCHPOS,,, 
night_start_temperature,dome temperature at 5pm prior,deg C, 
night_start_TM1S210,Mirror temperature at 5pm prior,deg C, 
night_start_TM2CAIR,Can air temperature at 5pm prior,deg C, 
delta_TAVERAGE,Change in dome temp,deg C, 
delta_TM1S210,Change in Mirror Temp,deg C, 
delta_TM2CAIR,Change in can air temp,deg C, 
wind_dome_angle,Angle between wind and dome direction,degrees, 
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

def shortname_and_units(raw_name):
    output_string = '{2}--{0} ({1})'.format(
      shortname(raw_name), units(raw_name), raw_name)
    return output_string

stars = pandas.DataFrame([['HD10700_APF.vels', 'b'], ['HD185144_APF.vels', 'g'], 
                            ['HD9407_APF.vels', 'r']], columns=['starID', 'color'])
