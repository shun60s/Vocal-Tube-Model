#coding:utf-8

#
# Vocal tract Two Tube Model, A python Class to calculate frequecny response
#

import numpy as np
from matplotlib import pyplot as plt

# Check version
#  Python 3.6.4 on win32 (Windows 10)
#  numpy 1.14.0 



class Class_TwoTube(object):
	def __init__(self, L1, L2, A1, A2, rg0=0.95, rl0=0.9):
		# initalize Tube length and Tube area
		self.L1= L1 # set list of 1st tube's length by unit is [cm]
		self.L2= L2 # set list of 1st tube's area by unit is [cm^2]
		self.A1= A1 # set list of 2nd tube's length by unit is [cm]
		self.A2= A2 # set list of 2nd tube's area by unit is [cm^2]
		C0=35000.0  # speed of sound in air, round 35000 cm/second
		self.tu1=self.L1 / C0   # delay time in 1st tube
		self.tu2=self.L2 / C0   # delay time in 2nd tube
		self.r1=( self.A2 - self.A1) / ( self.A2 + self.A1)  # reflection coefficient between 1st tube and 2nd tube
		self.rg0=rg0 # rg is reflection coefficient between glottis and 1st tube
		self.rl0=rl0 # reflection coefficient between 2nd tube and mouth
		REDUCTION_FACTOR=0.98  # amplitude decrease ratio per cm in tube
		self.beta1=np.power(REDUCTION_FACTOR , self.L1)
		self.beta2=np.power(REDUCTION_FACTOR , self.L2)
		
	def fone(self, xw):
		# calculate one point of frequecny response
		yi= 0.5 * ( 1.0 + self.rg0 ) * ( 1.0 + self.r1)  * ( 1.0 + self.rl0 ) * np.exp( -1.0j * ( self.tu1 + self.tu2 ) * xw) * self.beta1 * self.beta2
		yb= 1.0 + self.r1 * self.rg0 *  np.exp( -2.0j * self.tu1 * xw ) * self.beta1  + self.r1 * self.rl0 * np.exp( -2.0j * self.tu2 * xw ) * self.beta2 + self.rl0 * self.rg0 * np.exp( -2.0j * (self.tu1 + self.tu2) * xw ) * self.beta1 * self.beta2
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
			amp.append(self.fone(f * 2.0 * np.pi))
		return   np.log10(amp) * 20, bands # = amp value, freq list




if __name__ == '__main__':
	
	# Length & Area value, from problems 3.8 in "Digital Processing of Speech Signals" by L.R.Rabiner and R.W.Schafer
	#
	# /a/
	L1_a=9.0    # set list of 1st tube's length by unit is [cm]
	A1_a=1.0    # set list of 1st tube's area by unit is [cm^2]
	L2_a=8.0    # set list of 2nd tube's length by unit is [cm]
	A2_a=7.0    # set list of 2nd tube's area by unit is [cm^2]
	# /ae/
	L1_ae=4.0    # set list of 1st tube's length by unit is [cm]
	A1_ae=1.0    # set list of 1st tube's area by unit is [cm^2]
	L2_ae=13.0   # set list of 2nd tube's length by unit is [cm]
	A2_ae=8.0    # set list of 2nd tube's area by unit is [cm^2]
	# /i/
	L1_i=9.0    # set list of 1st tube's length by unit is [cm]
	A1_i=8.0    # set list of 1st tube's area by unit is [cm^2]
	L2_i=6.0    # set list of 2nd tube's length by unit is [cm]
	A2_i=1.0    # set list of 2nd tube's area by unit is [cm^2]
	# /u/
	L1_u=10.0   # set list of 1st tube's length by unit is [cm]
	A1_u=7.0    # set list of 1st tube's area by unit is [cm^2]
	L2_u=7.0    # set list of 2nd tube's length by unit is [cm]
	A2_u=3.0    # set list of 2nd tube's area by unit is [cm^2]
	
	# insatnce
	twotube_a  =  Class_TwoTube(L1_a,L2_a,A1_a,A2_a)
	twotube_ae =  Class_TwoTube(L1_ae,L2_ae,A1_ae,A2_ae)
	twotube_i  =  Class_TwoTube(L1_i,L2_i,A1_i,A2_i)
	twotube_u  =  Class_TwoTube(L1_u,L2_u,A1_u,A2_u)
	
	
#This file uses TAB
