from datetime import datetime
import pandas as pd
import requests
import streamlit as st

'''
# TaxiFareModel front
'''

url = 'https://taxifare.lewagon.ai/predict'

date = st.date_input('Enter start date')
time = st.time_input('Enter start time')

params = {'pickup_datetime' : datetime.combine(date, time),
            'pickup_longitude' : st.number_input('Input the pickup longitude', min_value=-80., max_value=-70., value=-73.9857),
            'pickup_latitude' : st.number_input('Input the pickup latitude',min_value=35., max_value=45., value=40.7484),
            'dropoff_longitude' : st.number_input('Input the dropoff longitude',min_value=-80., max_value=-70., value=-73.7797),
            'dropoff_latitude' : st.number_input('Input the dropoff latitude',min_value=35., max_value=45., value=40.6446),
            'passenger_count' : st.number_input('Input the number of passengers', min_value=1, max_value=10, value=5, step=1)
}

st.map(
        pd.DataFrame({'lat':[
                        params['pickup_latitude'],
                        params['dropoff_latitude']
                        ],
                    'lon':[
                        params['pickup_longitude'],
                        params['dropoff_longitude']
                        ]}
                    )
        )



if st.button('predict fare'):
    resp = requests.get(url, params=params).json()

    st.markdown(f"""### The predicted fare is :
                # {round(resp['fare'],2)}  $""")
