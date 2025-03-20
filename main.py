# Import python packages

import matplotlib.pyplot as plt

# Import user-modules
from OpenWeather_data_extract import get_df_hourly_weather_data
from economic_functions import *

# %% Import df_weather_brute
df_weather_brute = get_df_hourly_weather_data(
    latitude_2dec=20.6,
    longitude_2dec=103.3,
    start_date='2024-01-01',
    end_date='2024-01-01'
)


#%% ECONOMICS SECTION --------------

initial_investement = 1750000
# Calculate annual payments over 20 years
p_ann = annual_payment(initial_investement = 1750000,
                         annual_interest_rate = 0.06,
                         n_years= 20)

# Construct df with energy and economic outputs 
df_annual_energy_outputs = annual_energy_outputs(annual_solar_sys_output_kWh=7300,
                                useful_life_years= 20,
                                annual_degradation_rate=0.0025,
                                eff_electricity_rate_dollars_kWh=0.15,
                                eff_annual_rate_increase=0.05)
    
df_annual_energy_outputs["Annual_debt_payments"] = p_ann

# Add negative capital investment to year 1 cash flow
df_annual_energy_outputs.loc[0,"Annual_debt_payments"] = df_annual_energy_outputs.loc[0,"Annual_debt_payments"] - initial_investement

# plt.figure()
# plt.scatter(x = )


# %%
