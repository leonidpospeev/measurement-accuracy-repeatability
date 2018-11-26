import math
import numpy as np
import matplotlib.pyplot as plt


# Number of measurements
MSRMT_QTY = 30

# True quantity value
TRUE_QTY_VALUE = np.array([100, 100])

# What is considered a poor accuracy
BAD_MSRMT_ACCURACY = 10


#
# Case 1
# Generate measurements results for good accuracy and good repeatability case
#
# generating normal distribution of random numbers
rand_factor1 = 1 + 0.005 * np.random.randn(MSRMT_QTY, 2)
# generating initial measurement with good accuracy
measurement_init1 = np.array([TRUE_QTY_VALUE[0] * rand_factor1[0, 0],
                              TRUE_QTY_VALUE[1] * rand_factor1[0, 1]])
# generating subsequent measurements with good repeatability
measurement_subseq1 = np.array([measurement_init1[0] * rand_factor1[1:, 0],
                                measurement_init1[1] * rand_factor1[1:, 1]])
# merging results together
measurement1 = np.concatenate((np.reshape(measurement_init1, (2, 1)), measurement_subseq1), axis=1)


#
# Case 2
# Generate measurements results for good accuracy and poor repeatability case
#
# generating normal distribution of random numbers
rand_factor2 = 1 + 0.015 * np.random.randn(MSRMT_QTY, 2)
# taking the initial measurement with good accuracy from the previous case
measurement_init2 = measurement_init1
# generating subsequent measurement with poor repeatability
measurement_subseq2 = np.array([measurement_init2[0] * rand_factor2[1:, 0],
                                measurement_init2[1] * rand_factor2[1:, 1]])
# merging results together
measurement2 = np.concatenate((np.reshape(measurement_init2, (2, 1)), measurement_subseq2), axis=1)


#
# Case 3
# Generate measurements results for poor accuracy and good repeatability case
#
# generating normal distribution of random numbers
rand_factor3 = 1 + 0.005 * np.random.randn(MSRMT_QTY, 2)
# generating random angle from 0 to 2*Pi
angle = 2 * math.pi * np.random.uniform()
# generating initial measurement with poor accuracy as a point with polar coordinates of BAD_MSRMT_ACCURACY
# and a random angle relative to the true value
measurement_init3 = np.array([TRUE_QTY_VALUE[0] + BAD_MSRMT_ACCURACY * np.sin(angle),
                              TRUE_QTY_VALUE[1] + BAD_MSRMT_ACCURACY * np.cos(angle)])
# generating subsequent measurements with poor repeatability
measurement_subseq3 = np.array([measurement_init3[0] * rand_factor3[1:, 0],
                                measurement_init3[1] * rand_factor3[1:, 1]])
# merging results together
measurement3 = np.concatenate((np.reshape(measurement_init3, (2, 1)), measurement_subseq3), axis=1)


#
# Case 4
# Generate measurements results for poor accuracy and poor repeatability case
#
# generating normal distribution of random numbers
rand_factor4 = 1 + 0.1 * np.random.randn(MSRMT_QTY)
# generating random a set of random angles from 0 to 2*Pi
angle = 2 * math.pi * np.random.uniform(0, 1, MSRMT_QTY)
# generating the initial and all subsequent measurements
measurement4 = np.array([TRUE_QTY_VALUE[0] + BAD_MSRMT_ACCURACY * np.multiply(np.sin(angle), rand_factor4),
                         TRUE_QTY_VALUE[1] + BAD_MSRMT_ACCURACY * np.multiply(np.cos(angle), rand_factor4)])



#
# Plotting results
#
xlim = (85, 115)
ylim = (85, 115)

f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)

ax1.set_title('Good accuracy and repeatability')
ax1.set_xlim(xlim)
ax1.set_ylim(ylim)
ax1.scatter(measurement1[0], measurement1[1], marker='x', c='g', label='Measured values')
ax1.plot(TRUE_QTY_VALUE[0], TRUE_QTY_VALUE[1], 'rx', label='True value')
ax1.legend()
ax1.grid(linestyle='--', alpha=0.4, axis='both')

ax2.set_title('Good accuracy and poor repeatability')
ax2.set_xlim(xlim)
ax2.set_ylim(ylim)
ax2.scatter(measurement2[0], measurement2[1], marker='x', c='g', label='Measured values')
ax2.plot(TRUE_QTY_VALUE[0], TRUE_QTY_VALUE[1], 'rx', label='True value')
ax2.legend()
ax2.grid(linestyle='--', alpha=0.4, axis='both')

ax3.set_title('Poor accuracy and good repeatability')
ax3.set_xlim(xlim)
ax3.set_ylim(ylim)
ax3.scatter(measurement3[0], measurement3[1], marker='x', c='g', label='Measured values')
ax3.plot(TRUE_QTY_VALUE[0], TRUE_QTY_VALUE[1], 'rx', label='True value')
ax3.legend()
ax3.grid(linestyle='--', alpha=0.4, axis='both')
ax3.grid(linestyle='--', alpha=0.4, axis='both')

ax4.set_title('Poor accuracy and repeatability')
ax4.set_xlim(xlim)
ax4.set_ylim(ylim)
ax4.scatter(measurement4[0], measurement4[1], marker='x', c='g', label='Measured values')
ax4.plot(TRUE_QTY_VALUE[0], TRUE_QTY_VALUE[1], 'rx', label='True value')
ax4.legend()
ax4.grid(linestyle='--', alpha=0.4, axis='both')
ax4.grid(linestyle='--', alpha=0.4, axis='both')

plt.show()
