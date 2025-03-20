
import numpy as np
import matplotlib.pyplot as plt

def solar_declination(day_number_n):
    
    beta = np.radians((360/365) * (day_number_n - 1))  # Convert beta to radians
    sigma = (0.006918 - 0.399912 * np.cos(beta) + 0.070257 * np.sin(beta) 
             - 0.006758 * np.cos(2 * beta) + 0.000907 * np.sin(2 * beta) 
             - 0.002697 * np.cos(3 * beta) + 0.00148 * np.sin(3 * beta)) * (180/np.pi) # chnage from radians to degrees
    
    # sigma = 23.45 * np.sin(np.radians((360/365) * (day_number_n - 81)))
    return np.round(sigma,1)


    


if __name__ == "__main__":

    days_vector = []
    declination_angle_vector = []
    for n in range(1, 365):
        print(n, solar_declination(n))
        days_vector.append(n)
        declination_angle_vector.append(solar_declination(n))

    plt.figure()
    plt.plot(days_vector, declination_angle_vector)
    plt.show()