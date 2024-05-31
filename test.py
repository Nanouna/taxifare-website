from datetime import datetime, time
import requests

date = datetime(2017,7,6)
time = time(10,15,00)
print( datetime.combine(date, time))
params = {'pickup_datetime' : datetime.combine(date, time),
            'pickup_longitude' :  -73.9500,
            'pickup_latitude' :  40.837,
            'dropoff_longitude' : -73.9873,
            'dropoff_latitude' :  40.12736,
            'passenger_count' : 2
}

url = 'https://taxifare.lewagon.ai/predict'

resp = requests.get(url, params=params).json()
print(resp['fare'])
