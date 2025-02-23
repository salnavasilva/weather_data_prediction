# Import python packages
import matplotlib.pyplot as plt

# Import user-modules
from OpenWeather_data_extract import get_df_hourly_weather_data


# Import df_weather_brute
df_weather_brute = get_df_hourly_weather_data(
    latitude_2dec=20.6,
    longitude_2dec=103.3,
    start_date='2024-06-01',
    end_date='2024-07-01'
)



# plt.figure()
# plt.scatter(x = )

