import random
import numpy as np
import matplotlib.pyplot as plt
import sys

logfile = sys.argv[1]
logline = open(logfile, "r").readlines()

cte = [0] * len(logline)
x = [0] * len(logline)

for i in range(len(logline)):
    cte[i] = float(logline[i].strip('\n'))
    x[i] = i

plt.plot(x, cte)
plt.show()
