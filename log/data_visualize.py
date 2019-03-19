import random
import numpy as np
import matplotlib.pyplot as plt
import sys

def getLogData(logfile):
	logline = open(logfile, "r").readlines()
	cte = [0] * len(logline)
	x = [0] * len(logline)

	for i in range(len(logline)):
		cte[i] = float(logline[i].strip('\n'))
		x[i] = i

	return x, cte

if len(sys.argv) > 1:
	logfile = sys.argv[1]
	print("Log file to be visualized: " + str(logfile))
else:
	print("No file to be visualized")

x, cte = getLogData(logfile)

plt.plot(x, cte)

if len(sys.argv) > 2:
	savefile = sys.argv[2]
	print("Save visualized data to " + str(savefile))
	plt.savefig(savefile)
else:
	print("Not save the visualized data")

plt.show()
