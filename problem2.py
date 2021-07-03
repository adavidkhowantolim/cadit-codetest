# Problem 2: Sensor Aggregation
# David Khowanto

# This program didn't check for acceptable file type and content of the file
# Assumption: - file type and its contents are always correct 
#             - only aggregation ('min','max','median','mean') are accepted

## Import libraries
import json
from pandas import DataFrame, pivot_table

## Aggregation Dataframe Function
def aggregateBy(df, aggfunc):
  if (aggfunc != 'all' and aggfunc != 'min' and aggfunc != 'max' and aggfunc != 'median' and aggfunc != 'mean'):
    return -1
  if (aggfunc == 'all'): 
    aggfunc = ['min','max','median','mean']
  return pivot_table(df, values=['humidity','temperature'], index='timestamp', columns='roomArea',aggfunc=aggfunc)

## Main Logic for Sensor Aggregation
def sensorAggregation(json_file, aggfunc):
  # Get data from JSON file
  f = open(json_file)
  data = json.load(f)['array']
  f.close()

  # Convert list of dictionary into pandas dataframe
  sensor_df = DataFrame.from_records(data)

  # Aggregate humidity and temperature on roomArea and by day (timestamp)
  result_df = aggregateBy(sensor_df, aggfunc)
  if(isinstance(result_df, DataFrame)):
    print("Aggregation: ", ('min','max','median','mean') if (aggfunc=='all') else aggfunc)
    print(result_df)
    return(result_df, aggfunc)
  else:
    print("Aggregation", aggfunc, "Not Supported")
    return(-1, aggfunc)

## Run the program
sensorAggregation('JSON Files/sensor_data.json', 'all')
sensorAggregation('JSON Files/sensor_data.json', 'min')
sensorAggregation('JSON Files/sensor_data.json', 'max')
sensorAggregation('JSON Files/sensor_data.json', 'median')
sensorAggregation('JSON Files/sensor_data.json', 'mean')
sensorAggregation('JSON Files/sensor_data.json', 'avg')
sensorAggregation('JSON Files/sensor_data.json', "percentile")