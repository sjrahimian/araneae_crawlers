# Sama Rahimian, 0.1
# Prowl a list of random IP addresses and record response

import random
from subprocess import call as cmd

# Generate random list L of IP addresses
def createAddresses():
	# IP Adresss = 129.100.?.?
	prefix = "129.100."

	#list L of random IP addresses
	size = random.randint(1,10)
	print(f'Building {size} IP addresses.')

	addresses = set()
	for x in range(size):
		suffix = str(random.randint(0,255)) + "." + str(random.randint(0,255)) 
		addresses.add((prefix + suffix))
		
	return addresses

# Issue ping for each IP address then record as pass/fail
def ping(addresses):
	ping = "ping -n 1 -w 3 "
	lin = " &> /dev/null"
	win = " 2> nul"
	
	success = 0
	fail = 0
	
	for ip in addresses:
		if cmd(ping + ip + lin) == 0:
			success += 1
		else:
			fail += 1
	
	tally(success, fail)

# Count the number of passes and fails
def tally(s, f):
	print("~~Tallying responses~~\n")
	percentPass = (s / (s + f)) * 100
	print(f"Success: {s} | {percentPass:.2f}%\nFail: {f} | {100 - percentPass:.2f}%")
	print(f"Total IP Addresses checked: {s + f}\n\n")	
	print("~~Tally completed~~\n")



def main():
	print("Zora - Miturgidae (\"Prowling spider\")\n")
	ipAddresses = createAddresses()
	print("Random addresses built.\n")

	print("Harvesting pings\n")
	ipResponses = ping(ipAddresses)
	print("Responses recorded\n")
	
	
main()