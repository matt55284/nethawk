import subprocess
import math

def latency(portMin, portMax, target):
	pingCount = [1, 2, 3]
	pingLatency = []

	for x in pingCount:
		ping = subprocess.Popen(
			["ping", "-c", "1", target],
			stdout = subprocess.PIPE,
			stderr = subprocess.PIPE
		)

		out, error = ping.communicate()
		pingList = str(out).replace('=', ' ').split()
		pingTime = pingList[pingList.index("time") + 1]
		if(pingTime == "0ms\\n\\n'"):
			pingTime = 0

		pingLatency.append(int(math.ceil(float(pingTime) / 10.0)) / 10)

	eta = timeCalc((portMax - portMin) * max(pingLatency))

	print("ETA = ", eta[0], ":", eta[1], ":", int(eta[2]), sep="")

	#eta is an array with hours, minutes and seconds

def timeCalc(total):
	if(total > 60):
		minutes = int(total / 60)
		seconds = int(((total / 60) % minutes) * 60)
	else:
		seconds = total
		minutes = 0
	if(minutes > 60):
		hours = int(minutes / 60)
		minutes = int(((minutes / 60) % hours) * 60)
	else:
		hours = 0

	time = [hours, minutes, seconds]
	return time

