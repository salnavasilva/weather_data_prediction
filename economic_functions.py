'''
Author : 
Description :
functions present
 - A
 - B
 - C

'''

# Importation packages
import pandas as pd
import numpy as np

def energy_ouput_n_year(solar_sys_output_kWh, n_year, annual_degradation_rate = 0.05):
    
    enery_ouput_for_n_year = solar_sys_output_kWh * (1 - annual_degradation_rate)**(n_year-1)

    return energy_ouput_n_year

def annual_payment(initial_investement, annual_interest_rate, n_years):

    p_ann = initial_investement * (annual_interest_rate/(1 - (1 + annual_interest_rate)**(-n_years)))

    return np.round(p_ann, 2)


def annual_energy_outputs(annual_solar_sys_output_kWh,  useful_life_years,
                        eff_electricity_rate_dollars_kWh = 0.15,
                        eff_annual_rate_increase = 0.05,
                        annual_degradation_rate = 0.05,
                        round_value = 1):

    # Init. list
    temp_data_list = []

    # Init. cumul cost counter 
    cumulative_cost_energy_mxn_kWh = 0

    for n_year in range(1, useful_life_years+1):
        
        #Init dict
        dict1={}
        
        # calculate energy ouput for the year "n"
        energy_ouput_for_n_year = np.round(annual_solar_sys_output_kWh * (1 - annual_degradation_rate)**(n_year-1), round_value)
        
        # The cost of a kWh of energy in $/kWh with an effective anual rate increase upon the cost
        annual_effective_cost_energy_kWh = np.round(eff_electricity_rate_dollars_kWh * (1 + eff_annual_rate_increase)**(n_year-1), 4)
        
        # calculate cost of energy ouput for the year "n" in $/kWh
        cost_energy_mxn_kWh_per_year = np.round(energy_ouput_for_n_year * annual_effective_cost_energy_kWh, round_value)
        
        # cumulative cost per year
        cumulative_cost_energy_mxn_kWh = cumulative_cost_energy_mxn_kWh + cost_energy_mxn_kWh_per_year

        # stock new data into a new dict 
        new_row = {"Year":n_year,
                "Energy_produced_kWh_per_year": energy_ouput_for_n_year,
                "Cost_energy_mxn_kWh_per_year": cost_energy_mxn_kWh_per_year,
                "Cumulative_cost_energy_mxn_kWh": cumulative_cost_energy_mxn_kWh}
        
        # append the data to dict1
        dict1.update(new_row)

        # append to the list
        temp_data_list.append(dict1)

        # print(annual_effective_cost_energy_kWh)

    # Save dict data to df 
    df_energy_produced_by_year = pd.DataFrame(temp_data_list, columns=["Year", "Energy_produced_kWh_per_year",
                                                                        "Cost_energy_mxn_kWh_per_year", "Cumulative_cost_energy_mxn_kWh"])

    return df_energy_produced_by_year


# def 

    
if __name__ == "__main__":
    
    print(annual_energy_outputs(annual_solar_sys_output_kWh=7300,
                                useful_life_years= 2000,
                                annual_degradation_rate=0.0025,
                                eff_electricity_rate_dollars_kWh=0.15,
                                eff_annual_rate_increase=0.05))
    
    print(annual_payment(initial_investement = 1750000,
                         annual_interest_rate = 0.06,
                         n_years= 20))
