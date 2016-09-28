import os
import math

import rdns

class colours:
	HAWK = '\033[96;4m'
	CYAN = '\033[96m'
	RED = '\033[91m'
	ENDC = '\033[0m'
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	DBLUE = '\033[34m'
def clear():
	os.system('clear')
def margin(length):
	yaxis, xaxis = os.popen('stty size', 'r').read().split()
	if(int(xaxis) <= length):
		preMargin = 1
	else:
		preMargin = math.floor((int(xaxis) - length) / 2)
	margin = " " * preMargin
	return margin
#Logo -------------------------------------------------------
def logo():
	yaxis, xaxis = os.popen('stty size', 'r').read().split()
	clear()
	print("\n")
	if(int(xaxis) >= 75):
		print(margin(72) + colours.RED + "'|.   '|' '||''''|  |''||''|" + colours.CYAN + " '||'  '||'     |     '|| '||'  '|' '||'  |'" + colours.ENDC)
		print(margin(72) + colours.RED + " |'|   |   ||  .       ||" + colours.CYAN + "     ||    ||     |||     '|. '|.  .'   || .'    " + colours.ENDC)
		print(margin(72) + colours.RED + " | '|. |   ||''|       ||" + colours.CYAN + "     ||''''||    |  ||     ||  ||  |    ||'|.    " + colours.ENDC)
		print(margin(72) + colours.RED + " |   |||   ||          ||" + colours.CYAN + "     ||    ||   .''''|.     ||| |||     ||  ||   " + colours.ENDC)
		print(margin(72) + colours.RED + ".|.   '|  .||....|    .||." + colours.CYAN + "   .||.  .||. .|.  .||.     |   |     .||.  ||.\n\n" + colours.ENDC)
	elif(int(xaxis) >= 46):
		print(margin(28) + colours.RED + "'|.   '|' '||''''|  |''||''|")
		print(margin(28) + " |'|   |   ||  .       ||")
		print(margin(28) + " | '|. |   ||''|       ||")
		print(margin(28) + " |   |||   ||          ||")
		print(margin(28) + ".|.   '|  .||....|    .||.\n")
		print(margin(43) + colours.CYAN + "'||'  '||'     |     '|| '||'  '|' '||'  |'")
		print(margin(43) + " ||    ||     |||     '|. '|.  .'   || .'    ")
		print(margin(43) + " ||''''||    |  ||     ||  ||  |    ||'|.    ")
		print(margin(43) + " ||    ||   .''''|.     ||| |||     ||  ||   ")
		print(margin(43) + ".||.  .||. .|.  .||.     |   |     .||.  ||.\n\n" + colours.ENDC)
	else:
		pass
	print(margin(12) + colours.BLUE + "NetHawk v1.0")
	print(margin(30) + colours.BLUE + "Creator : Matt Graham (sp4rk2)" + colours.ENDC)
	print(margin(18) + "Welcome to Nethawk\n\n\n")
#HAWK -------------------------------------------------------
def HAWK(options = []):
	try:
		while True:
			choice = input(colours.HAWK + "HAWK" + colours.ENDC + "> ")
			if choice in options:
				break
			else:
				print(colours.RED + "[!] invalid option" + colours.ENDC)
				pass
		return(choice)
	except KeyboardInterrupt:
		print(colours.RED + "\n[!] keyboard interrupt" + colours.ENDC)
	exit()
#Reverse DNS Scanner(0-1) -------------------------------------------------------
def rdnsMenu():
	logo()

	#offline mode. comment line below
	netInterfaces = rdns.getNetInterfaces()

	#netInterfaces[0+] is the list of interfaces
	#netInterfaces = ["test1", "test2", "test3"]

	options = ["exit", "help", "back"]
	print(colours.GREEN + "[*] " + colours.ENDC + "Network Interfaces")
	for i in range(len(netInterfaces)):
		print(colours.GREEN + "[" + str(i) + "] " + colours.BLUE + netInterfaces[i] + colours.ENDC)
		options.append(str(i))
#	options.append(str(i+1))
	options.append(str(i+2))
#	print(colours.GREEN + "\n[" + str(i+1) + "] " + colours.BLUE + "IP/Domain" + colours.ENDC)
	print(colours.GREEN + "\n[" + str(i+2) + "] " + colours.BLUE + "Previous Menu " + colours.DBLUE + "(or type 'back')\n\n" + colours.ENDC)
	choice = HAWK(options)
	if(str(0) <= choice <= str(i)):

		#offline mode. comment line below
		results = rdns.getIp(netInterfaces[int(choice)])
		if results == 0:
			input(colours.RED + "[!] this network interface seems to be offline" + colours.ENDC)
			rdnsMenu()
		elif results == 1:
			input(colours.RED + "[!] this ip address is not recognised" + colours.ENDC)
			rdnsMenu()

		#results = ["192.168.1.147", "rfc1919", "255", "192.168.1.1#swampdonkey", "192.168.1.10#testphone", "192.168.1.50#testlaptop"]
		#results[0] is your device ip
		#results[1] is the ip type
		#results[2] is the max ip
		#results[3] is the router ip
		#results[4+] is the devices
		#netInterfaces[int(choice)] is the net int


		print("\n" + colours.GREEN + "[*] " + colours.ENDC + "Reverse DNS Scan Results")
		print("\n" + colours.GREEN + "[*] " + colours.ENDC + "IP: " + results[0] + colours.DBLUE + " (" + netInterfaces[int(choice)] + ")" + colours.ENDC)
#		SSID = results[3].split("#")
#		print("\n" + colours.GREEN + "[*] " + colours.BLUE + "SSID: " + "'" + SSID[1] + "'" + colours.ENDC)
#		print(colours.GREEN + "[*] " + colours.BLUE + "DNS: " + SSID[0] +  colours.ENDC)

		for i in range (len(results)):
			if(i > 2):
				device = results[i].split("#")
				print("\n" + colours.GREEN + "[" + str(i-3) + "] " + colours.BLUE + device[1])
				print(colours.GREEN + "[" + str(i-3) + "] " + colours.BLUE + device[0] + colours.ENDC)
				
		input(colours.HAWK + "HAWK" + colours.ENDC + "> ")
		scannersMenu()





#	elif(choice == str(i+1)):
#		print(colours.GREEN + "[?] " + colours.ENDC + "Please Enter IP or Domain")
#		ipOrDomain = input(colours.HAWK + "HAWK" + colours.ENDC + "> ")
#		rdns.publicIpCheck(ipOrDomain)
	elif(choice == "back" or choice == str(i+2)):
		scannersMenu()
#Scanners Menu(0) -------------------------------------------------------
def scannersMenu():
	logo()
	print(colours.GREEN + "[*] " + colours.ENDC + "Scanners")
	print(colours.GREEN + "[0] " + colours.BLUE + "Port Scanner")
	print(colours.GREEN + "[1] " + colours.BLUE + "Reverse Domain Name Scanner")
	print(colours.GREEN + "[2] " + colours.BLUE + "Operating System Discovery")
	print(colours.GREEN + "[3] " + colours.BLUE + "Web Directory and File Scanner")
	print(colours.GREEN + "[4] " + colours.BLUE + "Hashing Identifier")
	print(colours.GREEN + "[5] " + colours.BLUE + "Mac Address Scanner")
	print(colours.GREEN + "[6] " + colours.BLUE + "Personal Detail Web Scraper")
	print(colours.GREEN + "\n[7] " + colours.BLUE + "Previous Menu " + colours.DBLUE + "(or type 'back')\n\n" + colours.ENDC)
	options = ["0", "1", "2", "3", "4", "5", "6", "7", "exit", "help", "back"]
	choice = HAWK(options)
	if(choice == "0"):
		print("Not Available")
	elif(choice == "1"):
		rdnsMenu()
	elif(choice == "back" or choice == "7"):
		mainMenu()
	else:
		exit()
#Main Menu -------------------------------------------------------
def mainMenu():
	logo()
	print(colours.RED + "[!] DISCLAIMER: This program is only for testing or educational purposes and can only be used where strict consent has been given. Do not use this for malicious purposes.\n\n")
	print(colours.GREEN + "[*] " + colours.ENDC + "Main Menu" + colours.DBLUE + " (interaction mode)")
	print(colours.GREEN + "[0] " + colours.BLUE + "Scanners\n\n")
	options = ["0", "exit", "help"]
	choice = HAWK(options)
	if (choice == "0"):
		scannersMenu()
	else:
		exit()
	exit()

mainMenu()





"""  TODO
exit option from main menu
dig +noall +answer -x 192.168.1.147


do dig command
	if dig command produces nothing
		do nslookup
			replace variable
				repeat
	else
		get string






"""


