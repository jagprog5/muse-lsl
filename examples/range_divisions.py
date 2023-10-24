#

import numpy as np

data = np.genfromtxt('output.csv', delimiter=',')
data = data[:, 0] + data[:, 1]
second_threshold = np.median(data)

condition = data < second_threshold

first_half = data[condition]
second_half = data[~condition]

print(np.median(first_half))
print(second_threshold)
print(np.median(second_half))
