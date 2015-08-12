import glob   
import re
import matplotlib
from matplotlib import pyplot
from matplotlib.legend_handler import HandlerLine2D
import numpy as np
from math import factorial

files = 'C:\/Python27\/hbase-read.csv'   
hash_throughput = dict()
hash_latency = dict()
f=open(files, 'r') 
for line in f:
	#print line
	(thread, throughput, update) = line.split(",")
	if thread not in hash_throughput:
			hash_throughput[thread] = []
	if thread not in hash_latency:
			hash_latency[thread] = []
	hash_throughput[thread].append(throughput)
	hash_latency[thread].append(update)
f.close()
axes = pyplot.gca()
#axes.set_xlim([xmin,xmax])
axes.set_ylim([0,50000])
axes.set_xlim([0,25000])
pyplot.xlabel('Actual Throughput operations per second')
pyplot.ylabel('Average Read Latency in milliseconds')
pyplot.grid(True)
line1, = pyplot.plot(hash_throughput['5'], hash_latency['5'], marker='o', label='5 Threads')   
pyplot.plot(hash_throughput['10'], hash_latency['10'], marker='o', label='10 Threads')
pyplot.plot(hash_throughput['50'], hash_latency['50'], marker='o', label='50 Threads')
pyplot.plot(hash_throughput['100'], hash_latency['100'],marker='o', label='100 Threads')
pyplot.plot(hash_throughput['150'], hash_latency['150'], marker='o', label='150 Threads')
pyplot.plot(hash_throughput['200'], hash_latency['200'], marker='o', label='200 Threads')
pyplot.plot(hash_throughput['250'], hash_latency['250'], marker='o', label='250 Threads')
pyplot.plot(hash_throughput['300'], hash_latency['300'], '--', marker='o', label='300 Threads')
pyplot.plot(hash_throughput['350'], hash_latency['350'], '--', marker='o', label='350 Threads')
pyplot.plot(hash_throughput['400'], hash_latency['400'], '--', marker='o', label='400 Threads')
#line2, = plt.plot([3,2,1], label="Line 2", linewidth=4)
pyplot.plot(hash_throughput['450'], hash_latency['450'], '--', marker='o', label='450 Threads')
pyplot.plot(hash_throughput['500'], hash_latency['500'], '--', marker='o', label='500 Threads')
pyplot.title('Throughput vs Average Read Latency - HBase')
pyplot.legend(handler_map={line1: HandlerLine2D(numpoints=4)})
pyplot.show()   
