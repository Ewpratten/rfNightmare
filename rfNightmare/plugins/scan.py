from radios import rtl_sdr as rtlsdr

class Scanner(object):
	def __init__(self,low,high):
		self.range = [low,high]
		self.freq = low
		self.radio = rtlsdr.RTLsdr(low, 'auto')
		self.data = []
	
	def start(self):
		print("Scanning...")
		j = 1
		while self.freq <= self.range[1]:
			print(j,end="\r")
			power,freq,_ = self.radio.readPSD(256*1024)
			self.freq += 2000000
			self.radio.setFreq(self.freq)
			
			for i,point in enumerate(freq):
				if float(str(power[i]).split("e-")[0]) > float(5):# i % 10 == 0 and
					# print(point)
					self.data.append({"frequency":point, "power":power[i]})
			j += 1
		
		if len(self.data) == 0:
			return
		
		print("Found activity on the following frequencies")
		for point in self.data:
			print(f"{str(point['frequency'])}: {str(point['power']).split('e-')[0][:-11]}db")