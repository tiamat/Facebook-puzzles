#!/usr/bin/python2.7

import sys, getopt


# Function checks if a number is divisible by three
def isDivisibleByThree(number):
	if number % 3 == 0:
		return True
	else:
		return False


# Function checks if a number is divisible by five 
def isDivisibleByFive(number):
	if number % 5 == 0:
		return True
	else: 
		return False


# Outputs the usage
def usage():
	print 'Usage: hoppity.py -f "file_name"'
	return


try:
	# getting options
	options, arguments = getopt.getopt(sys.argv[1:], "f:")
	if len(options) == 1:
		hoppityLoc = options[0][1]
	else:
		print "ERROR: No option provided. Hoppity needs options"
		usage()
		sys.exit(2)

	# Reading the file
	hoppityFH = open(hoppityLoc, 'r')
	hoppityContents = hoppityFH.readline()
	hoppityContents.strip()
	hoppityContents = int(hoppityContents)
	hoppityFH.close()
	
	# After every 15 iterations output repeats
	# there is no need to loop therough all numbers fed to function
	hoppityRepeats = hoppityContents/15
	hoppityRemainder = hoppityContents%15
		
	if hoppityRepeats > 0:
		for rp in range(hoppityRepeats):
			print "Hoppity\nHophop\nHoppity\nHoppity\nHophop\nHoppity\nHop"

	# printing out the resat between 15n and the given number
	for it in range(1, hoppityRemainder + 1, 1):
		divBy3, divBy5 = isDivisibleByThree(it), isDivisibleByFive(it)

		if divBy3 and divBy5:
			print 'Hop'
			continue
		if divBy3:
			print 'Hoppity'
			continue
		if divBy5:
			print 'Hophop'
			continue

except IOError:
	print 'ERROR: can not open ' + hoppityLoc

except ValueError:
	print 'ERROR: The input file contains no number, but something else'

except getopt.GetoptError, err:
	print 'ERROR: No argument provided' + str(err)
	usage()
	sys.exit(2)