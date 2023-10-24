#!/usr/bin/env python3
import sys
import numpy as np

# assumed that there is a particular sample rate.
# for every n inputs there is 1 output
IN_OUT_RATIO = 2
in_count = 0

last_n = np.zeros(IN_OUT_RATIO)

for line in sys.stdin:
    alpha, beta = line.split(',')
    val = float(alpha) + float(beta)

    last_n[in_count] = val

    in_count += 1
    if in_count == IN_OUT_RATIO:
        in_count = 0
        # send output line
        
        avg_last_n = np.average(last_n)
        sys.stdout.write(str(avg_last_n) + '\n')
        sys.stdout.flush()
