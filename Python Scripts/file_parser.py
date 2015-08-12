import glob   
import re
import matplotlib
from matplotlib import pyplot
path = 'C:\/Python27\/reading_hbase\/*.log'   
files=glob.glob(path)   
print "Target\tThread\tThroughput\tUpdateLatency\tReadLatency"
hash_throughput = dict()
hash_latency = dict()
for file in files:     
	filedetails = file.split("_");
	target = filedetails[2]
	threadvalue = filedetails[3].split(".")
	thread = threadvalue[0]
	if thread not in hash_throughput:
			hash_throughput[thread] = []
	if thread not in hash_latency:
			hash_latency[thread] = []
	f=open(file, 'r') 
	for line in f:
		throughput = re.search('(?<=\[OVERALL\], Throughput\(ops\/sec\), )\d+\.\d+', line)
		if throughput:
			throughputvalue = throughput.group(0)
		m = re.search('(?<=\[UPDATE\], AverageLatency\(us\), )\d+\.\d+', line)	
		if m:
			updatevalue = m.group(0)
	print throughputvalue
	throughputvalue = round(throughputvalue,0)

	hash_throughput.setdefault(thread,{})[throughputvalue] = {}
	#hash_latency[thread].append(updatevalue)
	f.close()
