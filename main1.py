#coding:utf-8

#
# two tube model, draw frequency response and cross-sectional view (area)
#

import numpy as np
from matplotlib import pyplot as plt
import matplotlib.patches as patches
from twotube import *

# Check version
#  Python 3.6.4 on win32 (Windows 10)
#  numpy 1.14.0 
#  matplotlib  2.1.1


def plot_freq_res(twotube, label):
	plt.xlabel('Hz')
	plt.ylabel('dB')
	plt.title(label)
	amp, freq=twotube.H0(freq_high=5000, Band_num=256)
	plt.plot(freq, amp)


def add_draw_patch(ax1, twotube):
	ax1.add_patch( patches.Rectangle((0, -0.5* twotube.A1), twotube.L1, twotube.A1, hatch='/', fill=False))
	ax1.add_patch( patches.Rectangle((twotube.L1, -0.5* twotube.A2), twotube.L2, twotube.A2, hatch='/', fill=False))
	ax1.set_xlim([0, 20])
	ax1.set_ylim([-5, 5])


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
	
	
	# draw
	fig = plt.figure()
	
	# /a/
	plt.subplot(4,2,1)
	plot_freq_res(twotube_a, '/a/')
	ax1=fig.add_subplot(4,2,2)
	add_draw_patch(ax1, twotube_a)
	# /ae/
	plt.subplot(4,2,3)
	plot_freq_res(twotube_ae, '/ae/')
	ax1=fig.add_subplot(4,2,4)
	add_draw_patch(ax1, twotube_ae)
	# /i/
	plt.subplot(4,2,5)
	plot_freq_res(twotube_i, '/i/')
	ax1=fig.add_subplot(4,2,6)
	add_draw_patch(ax1, twotube_i)
	# /u/
	plt.subplot(4,2,7)
	plot_freq_res(twotube_u, '/u/')
	ax1=fig.add_subplot(4,2,8)
	add_draw_patch(ax1, twotube_u)
	
	#
	fig.tight_layout()
	plt.show()
	
#This file uses TAB
