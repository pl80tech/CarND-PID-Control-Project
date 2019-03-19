# Import the required packages
import random
import numpy as np
import matplotlib.pyplot as plt
import sys

# Get the data from log and set x, y coordinate
def getLogData(logfile):
	logline = open(logfile, "r").readlines()
	cte = [0] * len(logline)
	x = [0] * len(logline)

	for i in range(len(logline)):
		cte[i] = float(logline[i].strip('\n'))
		x[i] = i

	return x, cte

# Set x, y coordinate for center line
def getCenterLine(len):
	x = [0] * len
	y = [0] * len

	for i in range(len):
		x[i] = i

	return x, y

# Get x, y coordiante from the log files (passed from command line)
x1, cte1 = getLogData(sys.argv[1])
x2, cte2 = getLogData(sys.argv[2])
x3, cte3 = getLogData(sys.argv[3])

# Number of iterations to be visualized
n_iteration = min(len(x1), len(x2), len(x3))

# Get x, y coordinate for center line
center_x, center_y = getCenterLine(n_iteration)

# Plot multiple data in a same figure
plt.plot(x1[0:n_iteration-1], cte1[0:n_iteration-1])
plt.plot(x2[0:n_iteration-1], cte2[0:n_iteration-1])
plt.plot(x3[0:n_iteration-1], cte3[0:n_iteration-1])
plt.plot(center_x, center_y)

# Add title, label and legend
plt.title(sys.argv[4])
plt.xlabel(sys.argv[5])
plt.ylabel(sys.argv[6])
plt.legend([sys.argv[7], sys.argv[8], sys.argv[9]])

# Save visualized data to image file
savefile = sys.argv[10]
plt.savefig(savefile)

# Show on screen
plt.show()
