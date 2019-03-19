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

# Get the log file from command line
if len(sys.argv) > 1:
	logfile = sys.argv[1]
	print("Log file to be visualized: " + str(logfile))
else:
	print("No file to be visualized")

# Plot the data from log file
x, cte = getLogData(logfile)
center_x, center_y = getCenterLine(len(x))

plt.plot(x, cte)
plt.plot(center_x, center_y)
plt.title(sys.argv[3])
plt.ylabel(sys.argv[4])
plt.xlabel(sys.argv[5])
plt.legend([sys.argv[6], sys.argv[7]])

# Save visualized data to image file
if len(sys.argv) > 2:
	savefile = sys.argv[2]
	print("Save visualized data to " + str(savefile))
	plt.savefig(savefile)
else:
	print("Not save the visualized data")

# Show on screen
plt.show()
