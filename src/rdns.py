import socket
import subprocess
import os


#def getHost(ip):
#	for i in range(257):
#		IP_ADDRESS = ip + str(i)
#		if IP_ADDRESS != socket.getfqdn(IP_ADDRESS):
#			print(IP_ADDRESS, ": \t", socket.getfqdn(IP_ADDRESS))


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
		print(ip)



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

#RFC 1918
#24-bit block  			10.0.0.0 - 10.255.255.255
#20-bit block 			172.16.0.0 - 172.31.255.255
#16-bit block			192.168.0.0 - 192.168.255.255
