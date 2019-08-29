#! /usr/bin/env/python
# coding=utf-8
import pandas as pd
import numpy as np
from etl_weather.weather_service_fix_data_v2 import get_missing_data_indices, create_filling_df


def test_get_missing_data_indices():
    id = {'location_type': ['current_observation','current_observation','current_observation','current_observation','current_observation'],
         'station_id': ['IENGLAND966','33088','UKLI','LDRI','ISTCZCEC2'],
         'observation_time_rfc822': [pd.Timestamp('2017-12-08 17:54:50'),pd.Timestamp('2017-12-08 18:00:00'),pd.Timestamp('2017-12-08 20:00:00'),pd.Timestamp('2017-12-08 20:00:00'),pd.Timestamp('2017-12-08 20:45:07')],
         'observation_location_latit': [51.6901,51.2833,48.9,45.2667,49.621],
         'observation_location_longit': [0.1126,26.6167,24.7,15.2333,15.0483],
         'observation_location_elevat': [246,505,919,1076,1627],
         'dewpoint_c': [-4,-1,2,4,-4],
         'heat_index_c': ['NA','NA','NA','NA','NA'],
         'precip_1hr_metric': [0,0,0,2,0],
         'precip_today_metric': [0,0,0,6,3],
         'relative_humidity': [69,75,100,77,70],
         'temp_c': [1,2,2,7,1.2],
         'visibility_km': [0,10,0,10,10],
         'wind_degrees': [186,150,0,190,276],
         'wind_gust_kph': [11.1,0,0,0,4],
         'wind_kph': [3.9,4,0,11,1.6]}
    input_df = pd.DataFrame(data=id)

    output_sr = pd.Series({1: 3, 3: 1})

    assert get_missing_data_indices(input_df) == output_sr


def test_create_filling_df():
    id = {'location_type': ['current_observation','current_observation','current_observation','current_observation','current_observation'],
         'station_id': ['IENGLAND966','33088','UKLI','LDRI','ISTCZCEC2'],
         'observation_time_rfc822': ['2017-12-08 17:54:50','2017-12-08 18:00:00','2017-12-08 20:00:00','2017-12-08 20:00:00','2017-12-08 20:45:07'],
         'observation_location_latit': [51.6901,51.2833,48.9,45.2667,49.621],
         'observation_location_longit': [0.1126,26.6167,24.7,15.2333,15.0483],
         'observation_location_elevat': [246,505,919,1076,1627],
         'dewpoint_c': [-4,-1,2,4,-4],
         'heat_index_c': ['NA','NA','NA','NA','NA'],
         'precip_1hr_metric': [0,0,0,2,0],
         'precip_today_metric': [0,0,0,6,3],
         'relative_humidity': [69,75,100,77,70],
         'temp_c': [1,2,2,7,1.2],
         'visibility_km': [0,10,0,10,10],
         'wind_degrees': [186,150,0,190,276],
         'wind_gust_kph': [11.1,0,0,0,4],
         'wind_kph': [3.9,4,0,11,1.6]}
    input_df = pd.DataFrame(data=id)
    input_sr = pd.Series({1: 3, 3: 1})

    od = {'location_type': ['current_observation','current_observation','current_observation','current_observation','current_observation'],
         'station_id': ['IENGLAND966','33088','UKLI','LDRI','ISTCZCEC2'],
         'observation_time_rfc822': ['2017-12-08 17:54:50','2017-12-08 18:00:00','2017-12-08 20:00:00','2017-12-08 20:00:00','2017-12-08 20:45:07'],
         'observation_location_latit': [51.6901,51.2833,48.9,45.2667,49.621],
         'observation_location_longit': [0.1126,26.6167,24.7,15.2333,15.0483],
         'observation_location_elevat': [246,505,919,1076,1627],
         'dewpoint_c': [-4,-1,2,4,-4],
         'heat_index_c': ['NA','NA','NA','NA','NA'],
         'precip_1hr_metric': [0,0,0,2,0],
         'precip_today_metric': [0,0,0,6,3],
         'relative_humidity': [69,75,100,77,70],
         'temp_c': [1,2,2,7,1.2],
         'visibility_km': [0,10,0,10,10],
         'wind_degrees': [186,150,0,190,276],
         'wind_gust_kph': [11.1,0,0,0,4],
         'wind_kph': [3.9,4,0,11,1.6]}
    output_df = pd.DataFrame(data=od)

    assert create_filling_df(input_df, input_sr) == output_df
