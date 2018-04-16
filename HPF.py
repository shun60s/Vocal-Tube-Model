#coding:utf-8

#
# Convert from Volume Velocity to Sound Pressure using High Pass Filter, for mouth radiation effect
#

import numpy as np
from matplotlib import pyplot as plt

# Check version
#  Python 3.6.4 on win32 (Windows 10)
#  numpy 1.14.0 
#  matplotlib  2.1.1


class Class_HPF(object):
	def __init__(self, fc=1000, sampling_rate=48000):
		# initalize
		self.fc= fc # cut off frequency of High Pass Filter by unit is [Hz]
		self.sr= sampling_rate
		self.a, self.b = self.hpf1()
		
	def hpf1(self,):
		# primary digital filter
		a= np.ones(2)
		b= np.ones(2)
		wc= 2.0 * np.pi * self.fc / self.sr
		g0= np.tan( wc/2.0)
		a[1]= (g0 - 1.0) / ( g0 + 1.0)
		b[0]= 1.0 / (1.0 + g0)
		b[1]= -1.0 * b[0]
		return  a,b
		
	def iir1(self,x):
		# calculate iir filter: x is input, y is output
		# y[0]= b[0] * x[0]  + b[1] * x[-1]
		# y[0]= y[0] - a[1] * y[-1]
		y= np.zeros(len(x))
		for n in range(len(x)):
			for i in range(len(self.b)):
				if n - i >= 0:
					y[n] += self.b[i] * x[n - i]
			for j in range(1, len(self.a)):
				if n - j >= 0:
					y[n] -= self.a[j] * y[n - j]
		return y
		
	def fone(self, xw):
		# calculate one point of frequecny response
		f= xw / self.sr
		yi= self.b[0] + self.b[1] * np.exp(-2j * np.pi * f)
		yb= self.a[0] + self.a[1] * np.exp(-2j * np.pi * f)
		val= yi/yb
		return np.sqrt(val.real ** 2 + val.imag ** 2)

	def H0(self, freq_low=100, freq_high=5000, Band_num=256):
		# get Log scale frequecny response, from freq_low to freq_high, Band_num points
		amp=[]
		freq=[]
		bands= np.zeros(Band_num+1)
		fcl=freq_low * 1.0    # convert to float
		fch=freq_high * 1.0   # convert to float
		delta1=np.power(fch/fcl, 1.0 / (Band_num)) # Log Scale
		bands[0]=fcl
		#print ("i,band = 0", bands[0])
		for i in range(1, Band_num+1):
			bands[i]= bands[i-1] * delta1
			#print ("i,band =", i, bands[i]) 
		for f in bands:
			amp.append(self.fone(f))
		return   np.log10(amp) * 20, bands # = amp value, freq list



if __name__ == '__main__':
	
	# instance
	hpf=Class_HPF()
	
	# draw frequecny response
	plt.xlabel('Hz')
	plt.ylabel('dB')
	plt.title('High Pass Filter')
	amp, freq=hpf.H0(freq_high=5000, Band_num=256)
	plt.plot(freq, amp)
	plt.show()
	
#This file uses TAB
