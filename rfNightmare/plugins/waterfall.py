from scipy.interpolate import interp1d
from radios import rtl_sdr as rtlsdr
from collections import deque

small = interp1d([0,1], [0,4])
medium = interp1d([0,10], [0,4])
large = interp1d([0,100], [0,4])
xlarge = interp1d([0,1000], [0,4])

red = "\u001b[41m "
yellow = "\u001b[43m "
green = "\u001b[42m "
blue = "\u001b[44m "
purple = "\u001b[45m "

gradient = [purple,blue,green,yellow,red]

screen = deque([])
for i in range(1,34):
	screen.append("")

reset = "\u001b[0m"

class Waterfall(object):
	def __init__(self,freq):
		self.radio = rtlsdr.RTLsdr(freq, 'auto')
		self.freq = freq
		
	
	def start(self):
		# try:
		while True:
			try:
				power,freq,_ = self.radio.readPSD(512)
			except:
				continue
			
			for i,point in enumerate(freq):
				if int(round(float(point)*1000000)) == self.freq:
					# print(power[i], end="\r")
					print("")
					if float(power[i]) <= 1:
						position = int(round(float(str(small(power[i])).split("e-")[0])))
					elif float(power[i]) <= 10:
						position = int(round(float(str(medium(power[i])).split("e-")[0])))
					elif float(power[i]) <= 100:
						position = int(round(float(str(large(power[i])).split("e-")[0])))
					elif float(power[i]) <= 1000:
						position = int(round(float(str(xlarge(power[i])).split("e-")[0])))
					else:
						continue
					
					
					position = 4 if position >= 4 else position
					colour = gradient[position]
					screen.appendleft(colour)
					screen.pop()
					
					for i,c in enumerate(screen):
						self.__putChar(1,i,c)
					
					self.__moveTo(3,4)
					print(reset + str(power[i]))
		# except:
		# 	print(reset)
		# 	exit()
	
	def __putChar(self, x,y,char):
		self.__moveTo(x,y)
		print(char, end="")

	def __moveTo(self, x,y):
		print(f"\033[{y};{x}f", end="")