import argparse
from plugins.scan import Scanner
import sys

# parser = argparse.ArgumentParser(description='A tool for misusing SDRs')
# parser.add_argument('--scan', help='Scan a range (Usage: --scan <low limit> <high limit> )')

# args = parser.parse_args()

if len(sys.argv) < 2:
	print("Invalid arguments!")
	print("scan <lower bound> <upper bound>")
	
	exit()

if sys.argv[1] == "scan":
	scan = True
else:
	scan = False

if scan:
	# check that required data exsists
	if len(sys.argv) != 4:
		print("Invalid arguments!")
		exit(1)
	plugin = Scanner(int(sys.argv[2]), int(sys.argv[3]))
	plugin.start()
	