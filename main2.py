#coding:utf-8

#
#  two tube model, draw frequency response, considering mouth radiation
#

import numpy as np
from matplotlib import pyplot as plt
import matplotlib.patches as patches
from twotube import *
from HPF import *

# Check version
#  Python 3.6.4 on win32 (Windows 10)
#  numpy 1.14.0 
#  matplotlib  2.1.1


def plot_freq_res(twotube,label, hpf ):
	plt.xlabel('Hz')
	plt.ylabel('dB')
	plt.title(label)
	amp1, freq=twotube.H0(freq_high=5000, Band_num=256)
	amp2, freq=hpf.H0(freq_high=5000, Band_num=256)
	plt.plot(freq, (amp1+amp2))


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
	
	hpf=Class_HPF() # for mouth radiation effect
	
	
	# draw
	fig = plt.figure()
	
	# /a/
	plt.subplot(4,1,1)
	plot_freq_res(twotube_a, '/a/', hpf)
	# /ae/
	plt.subplot(4,1,2)
	plot_freq_res(twotube_ae, '/ae/', hpf)
	# /i/
	plt.subplot(4,1,3)
	plot_freq_res(twotube_i, '/i/', hpf)
	# /u/
	plt.subplot(4,1,4)
	plot_freq_res(twotube_u, '/u/', hpf)
	
	#
	fig.tight_layout()
	plt.show()
	
#This file uses TAB
