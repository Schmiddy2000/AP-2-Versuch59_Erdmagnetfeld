import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
import data as d

from tqdm import tqdm
import time

L = 0.439
N = 135


def getMagneticFieldStrength(N, I, d, l):
    nominator = N * I
    denominator = np.sqrt(d ** 2 + l ** 2)
    H = nominator / denominator
    return H


def lin_model(x, m, c): return m * x + c


def square_model(x, m, c): return m / x ** 2 + c


def find_best_fit(x_array, y_array):
    popt, pcov = curve_fit(lin_model, x_array, y_array, maxfev=1000)
    bestM = popt[0]
    bestC = popt[1]
    m_err = np.sqrt(pcov[0][0])
    c_err = np.sqrt(pcov[1][1])
    # dA = np.sqrt(pcov[0][0])
    # dAlpha = np.sqrt(pcov[1][1])
    # dPhi = np.sqrt(pcov[2][2]) * 180
    # print('A =', round(A, 3), '+-', round(dA, 3), ', Alpha =', round(alpha), '+-',
    #       round(dAlpha), 'and Phi =', round(phi * 180, 4), '+-', round(dPhi * 180, 4))
    return bestM, bestC, m_err, c_err


plt.figure(figsize=(10, 5))

plt.scatter(d.I1_broken_array, 1 / np.square(d.T1_broken_array))
plt.scatter(d.I1_working_array, - 1 / np.square(d.T1_working_array))
plt.scatter(d.I2_working_array, - 1 / np.square(d.T2_working_array))

# plt.scatter(d.I1_broken_array, d.T1_broken_array, marker='x')
# plt.errorbar(d.I1_broken_array, d.T1_broken_array, yerr=d.T1_broken_uncertainty_array,
#              xerr=d.I1_broken_uncertainty_array, fmt='none', ecolor='black', capsize=5, capthick=0.8, elinewidth=0.8)
# plt.scatter(d.I1_working_array, d.T1_working_array)
# plt.errorbar(d.I1_working_array, d.T1_working_array, yerr=d.T1_working_uncertainty_array,
#              xerr=d.I1_working_uncertainty_array, fmt='none', ecolor='black', capsize=5, capthick=0.8, elinewidth=0.8)

I2_working_lin = np.linspace(-0.5, 0, 100)

newMn, newCn, newErrMn, newErrCn = find_best_fit(d.I2_working_array, d.T2_working_array)
# print(d.I2_working_array, d.T2_working_array)
print('M =', newMn, '+-', newErrMn, 'and C =', newCn, '+-', newErrCn)

upperBestFit = lin_model(d.I2_working_array, newMn + newErrMn, newCn + newErrCn)
lowerBestFit = lin_model(d.I2_working_array, newMn - newErrMn, newCn - newErrCn)

plt.scatter(d.I2_working_array, d.T2_working_array)
plt.plot(I2_working_lin, lin_model(I2_working_lin, newMn, newCn))
# plt.fill_between(d.I2_working_array, upperBestFit, lowerBestFit, where=lowerBestFit > upperBestFit,
#                  interpolate=True, color='pink', alpha=0.5, label='Konfidenzband')
# plt.fill_between(d.I2_working_array, upperBestFit, lowerBestFit, where=upperBestFit >= lowerBestFit, interpolate=True,
#                  color='pink', alpha=0.5)
# plt.errorbar(d.I1_broken_array, d.T1_broken_array, yerr=d.T1_broken_uncertainty_array,
#              xerr=d.I1_broken_uncertainty_array, fmt='none', ecolor='black', capsize=5, capthick=0.8, elinewidth=0.8)

# plt.ylim(0, 3)
# plt.xlim(-0.1, 0.15)
plt.show()
