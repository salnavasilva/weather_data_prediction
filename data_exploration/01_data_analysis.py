# Import python packages

import matplotlib.pyplot as plt
import sys

sys.path.insert(0, '../weather_data_prediction')


# import os
# print(os.path.exists('/weather_data_prediction'))
# print(os.listdir('/weather_data_prediction'))

# Import user-modules
from OpenWeather_data_extract import get_df_hourly_weather_data


# %% Import df_weather_brute
df_weather_brute = get_df_hourly_weather_data(
    latitude_2dec=20.6,
    longitude_2dec=103.3,
    start_date='2024-01-01',
    end_date='2024-01-02'
)

print(df_weather_brute.head(5))


df_radiation_hourly = df_weather_brute.loc[:,['date','shortwave_radiation', 'direct_radiation', 'diffuse_radiation',
       'direct_normal_irradiance', 'global_tilted_irradiance']]

print(df_radiation_hourly)


plt.figure()
plt.plot(df_radiation_hourly["date"], df_radiation_hourly["global_tilted_irradiance"])
plt.xticks(rotation=45)
plt.show()

