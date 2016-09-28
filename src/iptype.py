#RFC 1918
#24-bit block  			10.0.0.0 - 10.255.255.255
#20-bit block 			172.16.0.0 - 172.31.255.255
#16-bit block			192.168.0.0 - 192.168.255.255

def getIpType(ip):

	ipInfo = []
	
#	RFC1918 16-bit
	if(ip[:8] == "192.168."):
		ipInfo.append("RFC1918_16")
		ipInfo.append(ip)
		ipInfo.append("255")
		return ipInfo

#	RFC1919 24-bit
	elif(ip[:3] == "10."):
		ipInfo.append("RFC1918_24")
		ipInfo.append(ip)
		ipInfo.append("255")
		return ipInfo

	else:
		ipInfo.append(0)
		return ipInfo




#192.168.1.147

#255.255.255.0



#11000000.10101000.00000001.10010011

#11111111.11111111.11111111.00000000

#11000000.10101000.00000001.00000000


#192.168.1.0