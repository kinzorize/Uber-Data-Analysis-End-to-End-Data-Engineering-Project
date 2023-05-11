SELECT 
f.VendorID,
dt.tpep_pickup_datetime,
dt.tpep_dropoff_datetime,
p.passenger_count,
t.trip_distance,
r.rate_code_name,
pu.pickup_latitude,
pu.pickup_longitude,
d.dropoff_latitude,
d.dropoff_longitude,
py.payment_type_name,
f.fare_amount,
f.extra,
f.mta_tax,
f.tip_amount,
f.tolls_amount,
f.improvement_surcharge,
f.total_amount
FROM
`kingsley-gcp-data-eng.uber_data_engineering_kc.fact_table` f
JOIN `kingsley-gcp-data-eng.uber_data_engineering_kc.passenger_count_dim` p ON p.passenger_count_id = f.passenger_count_id
JOIN `kingsley-gcp-data-eng.uber_data_engineering_kc.trip_distance_dim` t ON t.trip_distance_id = f.trip_distance_id
JOIN `kingsley-gcp-data-eng.uber_data_engineering_kc.rate_code_dim` r ON r.rate_code_id = f.rate_code_id
JOIN `kingsley-gcp-data-eng.uber_data_engineering_kc.pickup_location_dim` pu ON pu.pickup_location_id = f.pickup_location_id
JOIN `kingsley-gcp-data-eng.uber_data_engineering_kc.dropoff_location_dim` d ON d.dropoff_location_id = f.dropoff_location_id
JOIN `kingsley-gcp-data-eng.uber_data_engineering_kc.payment_type_dim` py ON py.payment_type_id = f.payment_type_id
JOIN `kingsley-gcp-data-eng.uber_data_engineering_kc.datetime_dim` dt ON dt.datetime_id = f.datetime_id

-- Creating a table

CREATE OR REPLACE TABLE `kingsley-gcp-data-eng.uber_data_engineering_kc.tbl_analytics` AS (
SELECT 
f.VendorID,
dt.tpep_pickup_datetime,
dt.tpep_dropoff_datetime,
p.passenger_count,
t.trip_distance,
r.rate_code_name,
pu.pickup_latitude,
pu.pickup_longitude,
d.dropoff_latitude,
d.dropoff_longitude,
py.payment_type_name,
f.fare_amount,
f.extra,
f.mta_tax,
f.tip_amount,
f.tolls_amount,
f.improvement_surcharge,
f.total_amount
FROM
`kingsley-gcp-data-eng.uber_data_engineering_kc.fact_table` f
JOIN `kingsley-gcp-data-eng.uber_data_engineering_kc.passenger_count_dim` p ON p.passenger_count_id = f.passenger_count_id
JOIN `kingsley-gcp-data-eng.uber_data_engineering_kc.trip_distance_dim` t ON t.trip_distance_id = f.trip_distance_id
JOIN `kingsley-gcp-data-eng.uber_data_engineering_kc.rate_code_dim` r ON r.rate_code_id = f.rate_code_id
JOIN `kingsley-gcp-data-eng.uber_data_engineering_kc.pickup_location_dim` pu ON pu.pickup_location_id = f.pickup_location_id
JOIN `kingsley-gcp-data-eng.uber_data_engineering_kc.dropoff_location_dim` d ON d.dropoff_location_id = f.dropoff_location_id
JOIN `kingsley-gcp-data-eng.uber_data_engineering_kc.payment_type_dim` py ON py.payment_type_id = f.payment_type_id
JOIN `kingsley-gcp-data-eng.uber_data_engineering_kc.datetime_dim` dt ON dt.datetime_id = f.datetime_id);

