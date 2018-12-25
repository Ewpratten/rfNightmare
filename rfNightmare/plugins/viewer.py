from radios import rtl_sdr as rtlsdr

class ViewRF(object):
	def __init__(self, freq):
		self.radio = rtlsdr.RTLsdr(freq, 'auto')
		self.freq = freq
	
	def start(self):
		while True:
			power,freq,_ = self.radio.readPSD(512)
			
			for i,point in enumerate(freq):
				if int(round(float(point)*1000000)) == self.freq:
					print(str(power[i]) + "                            ", end="\r")