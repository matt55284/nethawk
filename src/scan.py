import os
import math
import six
import random

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
	netInterfaces = rdns.getNetInterfaces()
	options = ["exit", "help", "back"]
	print(colours.GREEN + "[*] " + colours.ENDC + "NETWORK INTERFACES")
	for i in range(len(netInterfaces)):
		print(colours.GREEN + "[" + str(i) + "] " + colours.BLUE + netInterfaces[i] + colours.ENDC)
		options.append(str(i))
#	options.append(str(i+1))
	options.append(str(i+2))
#	print(colours.GREEN + "\n[" + str(i+1) + "] " + colours.BLUE + "IP/Domain" + colours.ENDC)
	print(colours.GREEN + "\n[" + str(i+2) + "] " + colours.BLUE + "Previous Menu " + colours.DBLUE + "(or type 'back')\n\n" + colours.ENDC)
	choice = HAWK(options)
	if(str(0) <= choice <= str(i)):
		rdns.getIp(netInterfaces[int(choice)])
#	elif(choice == str(i+1)):
#		print(colours.GREEN + "[?] " + colours.ENDC + "Please Enter IP or Domain")
#		ipOrDomain = input(colours.HAWK + "HAWK" + colours.ENDC + "> ")
#		rdns.publicIpCheck(ipOrDomain)
	elif(choice == "back" or choice == str(i+2)):
		scannersMenu()
#Scanners Menu(0) -------------------------------------------------------
def scannersMenu():
	logo()
	print(colours.GREEN + "[*] " + colours.ENDC + "SCANNERS")
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
	print(colours.GREEN + "[*] " + colours.ENDC + "MAIN MENU" + colours.DBLUE + " (interaction mode)")
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


