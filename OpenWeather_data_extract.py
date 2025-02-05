# pip install openmeteo-requests
# pip install requests-cache retry-requests numpy pandas
# pip install --upgrade numexpr bottleneck

# This code was copied from the https://open-meteo.com/en/docs/historical-weather-api

import openmeteo_requests

import requests_cache
import pandas as pd
from retry_requests import retry

# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after = -1)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

# Make sure all required weather variables are listed here
# The order of variables in hourly or daily is important to assign them correctly below
url = "https://archive-api.open-meteo.com/v1/archive"
params = {
	"latitude": 52.52,
	"longitude": 13.41,
	"start_date": "2020-01-01",
	"end_date": "2025-02-02",
	"hourly": ["temperature_2m", "relative_humidity_2m", "dew_point_2m", "apparent_temperature", "precipitation", "rain", "pressure_msl", "surface_pressure", "cloud_cover", "cloud_cover_low", "cloud_cover_mid", "cloud_cover_high", "et0_fao_evapotranspiration", "vapour_pressure_deficit", "wind_speed_10m", "wind_speed_100m", "wind_direction_10m", "wind_direction_100m", "wind_gusts_10m", "boundary_layer_height", "wet_bulb_temperature_2m", "total_column_integrated_water_vapour", "is_day", "sunshine_duration", "shortwave_radiation", "direct_radiation", "diffuse_radiation", "direct_normal_irradiance", "global_tilted_irradiance", "terrestrial_radiation", "shortwave_radiation_instant", "direct_radiation_instant", "diffuse_radiation_instant", "direct_normal_irradiance_instant", "global_tilted_irradiance_instant", "terrestrial_radiation_instant"]
}
responses = openmeteo.weather_api(url, params=params, verify=False)

# Process first location. Add a for-loop for multiple locations or weather models
response = responses[0]
print(f"Coordinates {response.Latitude()}°N {response.Longitude()}°E")
print(f"Elevation {response.Elevation()} m asl")
print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")

# Process hourly data. The order of variables needs to be the same as requested.
hourly = response.Hourly()
hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()
hourly_relative_humidity_2m = hourly.Variables(1).ValuesAsNumpy()
hourly_dew_point_2m = hourly.Variables(2).ValuesAsNumpy()
hourly_apparent_temperature = hourly.Variables(3).ValuesAsNumpy()
hourly_precipitation = hourly.Variables(4).ValuesAsNumpy()
hourly_rain = hourly.Variables(5).ValuesAsNumpy()
hourly_pressure_msl = hourly.Variables(6).ValuesAsNumpy()
hourly_surface_pressure = hourly.Variables(7).ValuesAsNumpy()
hourly_cloud_cover = hourly.Variables(8).ValuesAsNumpy()
hourly_cloud_cover_low = hourly.Variables(9).ValuesAsNumpy()
hourly_cloud_cover_mid = hourly.Variables(10).ValuesAsNumpy()
hourly_cloud_cover_high = hourly.Variables(11).ValuesAsNumpy()
hourly_et0_fao_evapotranspiration = hourly.Variables(12).ValuesAsNumpy()
hourly_vapour_pressure_deficit = hourly.Variables(13).ValuesAsNumpy()
hourly_wind_speed_10m = hourly.Variables(14).ValuesAsNumpy()
hourly_wind_speed_100m = hourly.Variables(15).ValuesAsNumpy()
hourly_wind_direction_10m = hourly.Variables(16).ValuesAsNumpy()
hourly_wind_direction_100m = hourly.Variables(17).ValuesAsNumpy()
hourly_wind_gusts_10m = hourly.Variables(18).ValuesAsNumpy()
hourly_boundary_layer_height = hourly.Variables(19).ValuesAsNumpy()
hourly_wet_bulb_temperature_2m = hourly.Variables(20).ValuesAsNumpy()
hourly_total_column_integrated_water_vapour = hourly.Variables(21).ValuesAsNumpy()
hourly_is_day = hourly.Variables(22).ValuesAsNumpy()
hourly_sunshine_duration = hourly.Variables(23).ValuesAsNumpy()
hourly_shortwave_radiation = hourly.Variables(24).ValuesAsNumpy()
hourly_direct_radiation = hourly.Variables(25).ValuesAsNumpy()
hourly_diffuse_radiation = hourly.Variables(26).ValuesAsNumpy()
hourly_direct_normal_irradiance = hourly.Variables(27).ValuesAsNumpy()
hourly_global_tilted_irradiance = hourly.Variables(28).ValuesAsNumpy()
hourly_terrestrial_radiation = hourly.Variables(29).ValuesAsNumpy()
hourly_shortwave_radiation_instant = hourly.Variables(30).ValuesAsNumpy()
hourly_direct_radiation_instant = hourly.Variables(31).ValuesAsNumpy()
hourly_diffuse_radiation_instant = hourly.Variables(32).ValuesAsNumpy()
hourly_direct_normal_irradiance_instant = hourly.Variables(33).ValuesAsNumpy()
hourly_global_tilted_irradiance_instant = hourly.Variables(34).ValuesAsNumpy()
hourly_terrestrial_radiation_instant = hourly.Variables(35).ValuesAsNumpy()

hourly_data = {"date": pd.date_range(
	start = pd.to_datetime(hourly.Time(), unit = "s", utc = True),
	end = pd.to_datetime(hourly.TimeEnd(), unit = "s", utc = True),
	freq = pd.Timedelta(seconds = hourly.Interval()),
	inclusive = "left"
)}

hourly_data["temperature_2m"] = hourly_temperature_2m
hourly_data["relative_humidity_2m"] = hourly_relative_humidity_2m
hourly_data["dew_point_2m"] = hourly_dew_point_2m
hourly_data["apparent_temperature"] = hourly_apparent_temperature
hourly_data["precipitation"] = hourly_precipitation
hourly_data["rain"] = hourly_rain
hourly_data["pressure_msl"] = hourly_pressure_msl
hourly_data["surface_pressure"] = hourly_surface_pressure
hourly_data["cloud_cover"] = hourly_cloud_cover
hourly_data["cloud_cover_low"] = hourly_cloud_cover_low
hourly_data["cloud_cover_mid"] = hourly_cloud_cover_mid
hourly_data["cloud_cover_high"] = hourly_cloud_cover_high
hourly_data["et0_fao_evapotranspiration"] = hourly_et0_fao_evapotranspiration
hourly_data["vapour_pressure_deficit"] = hourly_vapour_pressure_deficit
hourly_data["wind_speed_10m"] = hourly_wind_speed_10m
hourly_data["wind_speed_100m"] = hourly_wind_speed_100m
hourly_data["wind_direction_10m"] = hourly_wind_direction_10m
hourly_data["wind_direction_100m"] = hourly_wind_direction_100m
hourly_data["wind_gusts_10m"] = hourly_wind_gusts_10m
hourly_data["boundary_layer_height"] = hourly_boundary_layer_height
hourly_data["wet_bulb_temperature_2m"] = hourly_wet_bulb_temperature_2m
hourly_data["total_column_integrated_water_vapour"] = hourly_total_column_integrated_water_vapour
hourly_data["is_day"] = hourly_is_day
hourly_data["sunshine_duration"] = hourly_sunshine_duration
hourly_data["shortwave_radiation"] = hourly_shortwave_radiation
hourly_data["direct_radiation"] = hourly_direct_radiation
hourly_data["diffuse_radiation"] = hourly_diffuse_radiation
hourly_data["direct_normal_irradiance"] = hourly_direct_normal_irradiance
hourly_data["global_tilted_irradiance"] = hourly_global_tilted_irradiance
hourly_data["terrestrial_radiation"] = hourly_terrestrial_radiation
hourly_data["shortwave_radiation_instant"] = hourly_shortwave_radiation_instant
hourly_data["direct_radiation_instant"] = hourly_direct_radiation_instant
hourly_data["diffuse_radiation_instant"] = hourly_diffuse_radiation_instant
hourly_data["direct_normal_irradiance_instant"] = hourly_direct_normal_irradiance_instant
hourly_data["global_tilted_irradiance_instant"] = hourly_global_tilted_irradiance_instant
hourly_data["terrestrial_radiation_instant"] = hourly_terrestrial_radiation_instant

hourly_dataframe = pd.DataFrame(data = hourly_data)
print(hourly_dataframe)


import matplotlib.pyplot as plt

plt.scatter(x=hourly_dataframe.loc[:,"date"], y=hourly_dataframe.loc[:,"temperature_2m"])

plt.show()

