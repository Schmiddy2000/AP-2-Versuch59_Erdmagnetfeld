# ToDo's:
# --- Still have to account for the errors of the digital voltmeter...

import numpy as np

'''
t denotes the measured time
T denotes the periodic time
L denotes the length of the coil
d denotes the diameter of the coil
I denotes the electrical current
'''

# uncertainties(in [s] und [m]):
delta_t_human = 0.2
delta_t_res = 0.01

delta_L = 1e-3
delta_d = 1e-4

# General values (in [m]):
L = 43.9 * 1e-2
N = 135
d_no_cables = 9.011 * 1e-2
d_with_cables = 9.411 * 1e-2

# Measurements (in [A] und [s]):
I1_broken_array = np.array([0, 18, 60, 80, 103, 147, 155, 197, 220, 283, 293, 348, 400]) * 1e-3
I1_broken_uncertainty_array = (np.array([0, 10, 10, 5, 3, 5, 0, 5, 5, 2, 1, 1, 1]) + 1) * 1e-3

t1_broken_array5 = np.array([13.5, 14.5])
t1_broken_array10 = np.array([13.83, 13.87, 14.12, 12.98, 13.23, 11.56, 11.16, 9.24, 9.45, 8.36, 6.75])

T1_broken_array1 = t1_broken_array5 / 5
T1_broken_array2 = t1_broken_array10 / 10

T1_broken_array = np.concatenate((T1_broken_array1, T1_broken_array2))
T1_broken_uncertainty_array = np.zeros(len(T1_broken_array)) + 0.021

I1_working_array = np.array([20, 26, 70, 91]) * 1e-3
I1_working_uncertainty_array = np.array([1, 0, 1, 1]) * 1e-3

t1_working_array10 = np.array([14.67, 13.1, 13.87, 13.77])

T1_working_array = t1_working_array10 / 10
T1_working_uncertainty_array = np.zeros(len(T1_working_array)) + 0.021

I2_working_array = np.array([5, 12, 33, 36, 73, 99, 113, 131, 168, 195, 240, 266, 296, 344, 392]) * 1e-3
I2_working_array = I2_working_array[::-1] * (-1)
I2_working_uncertainty_array = np.array([0, 3, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1]) * 1e-3
I2_working_uncertainty_array = I2_working_uncertainty_array[::-1]

t2_working_array10 = np.array([13.43, 13.77, 14.12, 13.16, 12.29, 11.4, 11.23, 10.91, 9.66, 9.25, 8.53, 8.06,
                               7.53, 6.34, 6.59])
T2_working_array = t2_working_array10[::-1] / 10

# AllIs_array = np.concatenate(())
