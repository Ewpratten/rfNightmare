from plugins.scan import Scanner
from plugins.viewer import ViewRF
from plugins.waterfall import Waterfall
import sys


if len(sys.argv) < 2:
	print("Invalid arguments!")
	print("scan <lower bound> <upper bound>")
	print("view <frequency>")
	print("waterfall <frequency>")
	
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
	

if sys.argv[1] == "view":
	# print bar graph of signal for a frequency
	if len(sys.argv) != 3:
		print("Invalid arguments!")
		exit(1)
	
	plugin = ViewRF(int(sys.argv[2]))

if sys.argv[1] == "waterfall":
	if len(sys.argv) != 3:
		print("Invalid arguments!")
		exit(1)
	
	plugin = Waterfall(int(sys.argv[2]))


plugin.start()