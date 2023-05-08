import io
import pandas as pd
import requests

# the raw dataset from nyc.gov
url = 'https://storage.googleapis.com/uber-data-engineering-project/uber_data.csv'
response = requests.get(url)

# Read the csv dataset
df = pd.read_csv(io.StringIO(response.text), sep=',')

# Display 5 rows of the dataset
df.head()

# Display the info including the data type of the dataset.
df.info()

# convert the data types below from 'Object' to 'datetime' object
df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])

df.info()

# This line of code remove duplicate from 'df' and reset the index to a new index
# And ensure that the old index is not added to the new column called 'trip_id'

df = df.drop_duplicates().reset_index(drop=True)
df['trip_id'] = df.index

df.head()

# create a new dataframe called 'datetime_dim' by selecting two columns
# 'tpep_pickup_datetime' and 'tpep_dropoff_datetime', from the original DataFrame df.

datetime_dim = df[['tpep_pickup_datetime',
                   'tpep_dropoff_datetime']].reset_index(drop=True)
datetime_dim['tpep_pickup_datetime'] = datetime_dim['tpep_pickup_datetime']
# It attract the hour component of the date and time value which contain integer between 0 and 23.
# other follows using 'dt.hour', 'dt.day' etc
datetime_dim['pick_hour'] = datetime_dim['tpep_pickup_datetime'].dt.hour
datetime_dim['pick_day'] = datetime_dim['tpep_pickup_datetime'].dt.day
datetime_dim['pick_month'] = datetime_dim['tpep_pickup_datetime'].dt.month
datetime_dim['pick_year'] = datetime_dim['tpep_pickup_datetime'].dt.year
datetime_dim['pick_weekday'] = datetime_dim['tpep_pickup_datetime'].dt.weekday

datetime_dim['tpep_dropoff_datetime'] = datetime_dim['tpep_dropoff_datetime']
datetime_dim['drop_hour'] = datetime_dim['tpep_dropoff_datetime'].dt.hour
datetime_dim['drop_day'] = datetime_dim['tpep_dropoff_datetime'].dt.day
datetime_dim['drop_month'] = datetime_dim['tpep_dropoff_datetime'].dt.month
datetime_dim['drop_year'] = datetime_dim['tpep_dropoff_datetime'].dt.year
datetime_dim['drop_weekday'] = datetime_dim['tpep_dropoff_datetime'].dt.weekday


datetime_dim['datetime_id'] = datetime_dim.index

# datetime_dim = datetime_dim.rename(columns={'tpep_pickup_datetime': 'datetime_id'}).reset_index(drop=True)
datetime_dim = datetime_dim[['datetime_id', 'tpep_pickup_datetime', 'pick_hour', 'pick_day', 'pick_month', 'pick_year', 'pick_weekday',
                             'tpep_dropoff_datetime', 'drop_hour', 'drop_day', 'drop_month', 'drop_year', 'drop_weekday']]
#

datetime_dim.head()
