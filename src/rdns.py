import socket
import subprocess
import os
import time
import iptype


def getNetInterfaces():
	netInterfaces = []
	netInt = subprocess.Popen("ifconfig -s", shell=True, stdout=subprocess.PIPE)
	netInt = str(netInt.stdout.read(), 'utf-8').split('\n')
	for i in range(1,len(netInt)-1):
		netIntX = netInt[i].split()
		netInterfaces.append(netIntX[0])
	return netInterfaces

def getIp(chosenInterface):
	command = "ifconfig " + chosenInterface + " | grep 'inet addr:'"
	command = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
	command = str(command.stdout.read(), 'utf-8').split()
	if((command[1])[:5] == "addr:"):
		ip = (command[1])[5:]
		ipInfo = iptype.getIpType(ip)
		maxIp = ipInfo[2].split(".")

		results = []
		results.append(ip)
		results.append(ipInfo[0])
		results.append(ipInfo[2])


		for i in range(int(maxIp[0]) + 1):
			if(len(maxIp) >= 2):
				for j in range(int(maxIp[1]) + 1):
					if(len(maxIp) >= 3):
						for k in range(int(maxIp[2]) + 1):
							ip = (ipInfo[1] + "%d.%d.%d" % (i, j, k))
							if ip != socket.getfqdn(ip):
								results.append(ip + "#" + socket.getfqdn(ip))
					else:
						ip = (ipInfo[1] + "%d.%d" % (i, j))
						if ip != socket.getfqdn(ip):
							results.append(ip + "#" + socket.getfqdn(ip))
			else:
				ip = (ipInfo[1] + "%d" % (i))
				if ip != socket.getfqdn(ip):
					results.append(ip + "#" + socket.getfqdn(ip))
		return results











def publicIpCheck(ipOrDomain):
	command = "dig +noall +answer -x " + ipOrDomain
	command = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
	command = command.stdout.read()
	if(len(command) == 0):
		domain = "nslookup " + ipOrDomain + " | grep Address:"
		domain = subprocess.Popen(domain, shell=True, stdout=subprocess.PIPE)
		domain = str(domain.stdout.read(), 'utf-8')
		print(domain)
	else:
		print(command)
