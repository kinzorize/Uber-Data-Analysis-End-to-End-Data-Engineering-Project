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
