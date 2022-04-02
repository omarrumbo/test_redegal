import pandas as pd
import pandasql as ps
import sys

df = pd.read_csv('../examples/yellow_tripdata_2021-01.csv')
zones = pd.read_csv('zones/taxi+_zone_lookup.csv')

distance = df.trip_distance.quantile(0.95)

q="""SELECT count(1) as trips, zones.Borough as end_borough, zones.Zone as end_zone 
    from df 
    inner join zones 
        on df.PULocationID = zones.LocationID 
    where trip_distance >{0}
    group by df.PULocationID 
    order by trips desc limit 10 """.format(distance)

print (ps.sqldf(q,locals()))