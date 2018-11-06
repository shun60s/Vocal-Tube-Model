#coding:utf-8

#
# three tube model, draw frequency response and waveform, considering glottal voice source and mouth radiation
#                   save generated waveform as a wav file
#                   and,
#                   draw cross-sectional view (area)

import numpy as np
from matplotlib import pyplot as plt
import matplotlib.patches as patches
from scipy.io.wavfile import write as wavwrite
from threetube import *
from glottal import *
from HPF import *

# Check version
#  Python 3.6.4 on win32 (Windows 10)
#  numpy 1.14.0 
#  matplotlib  2.1.1
#  scipy 1.0.0


def plot_freq_res(twotube, label, glo, hpf):
	plt.xlabel('Hz')
	plt.ylabel('dB')
	plt.title(label)
	amp0, freq=glo.H0(freq_high=5000, Band_num=256)
	amp1, freq=twotube.H0(freq_high=5000, Band_num=256)
	amp2, freq=hpf.H0(freq_high=5000, Band_num=256)
	plt.plot(freq, (amp0+amp1+amp2))

def plot_waveform(twotube, label, glo, hpf):
	# you can get longer input source to set bigger repeat_num 
	yg_repeat=glo.make_N_repeat(repeat_num=5) # input source of three tube model
	y2tm=twotube.process(yg_repeat)
	yout=hpf.iir1(y2tm)
	plt.xlabel('mSec')
	plt.ylabel('level')
	plt.title('Waveform')
	plt.plot( (np.arange(len(yout)) * 1000.0 / glo.sr) , yout)
	return yout

def save_wav( yout, wav_path, sampling_rate=48000):
	wavwrite( wav_path, sampling_rate, ( yout * 2 ** 15).astype(np.int16))
	print ('save ', wav_path) 

def add_draw_patch(ax1, threetube):
	ax1.add_patch( patches.Rectangle((0, -0.5* threetube.A1), threetube.L1, threetube.A1, hatch='/', fill=False))
	ax1.add_patch( patches.Rectangle((threetube.L1, -0.5* threetube.A2), threetube.L2, threetube.A2, hatch='/', fill=False))
	ax1.add_patch( patches.Rectangle((threetube.L1 + threetube.L2, -0.5* threetube.A3), threetube.L3, threetube.A3, hatch='/', fill=False))
	ax1.set_xlim([0, 25])
	ax1.set_ylim([-5, 5])

if __name__ == '__main__':
	
	# Length & Area value, from problems 3.8 in "Digital Processing of Speech Signals" by L.R.Rabiner and R.W.Schafer
	#
	# /a/
	L1_a=9.0    # set list of 1st tube's length by unit is [cm]
	A1_a=1.0    # set list of 1st tube's area by unit is [cm^2]
	L2_a=8.0    # set list of 2nd tube's length by unit is [cm]
	A2_a=7.0    # set list of 2nd tube's area by unit is [cm^2]

	# /u/
	L1_u=10.0   # set list of 1st tube's length by unit is [cm]
	A1_u=7.0    # set list of 1st tube's area by unit is [cm^2]
	L2_u=7.0    # set list of 2nd tube's length by unit is [cm]
	A2_u=3.0    # set list of 2nd tube's area by unit is [cm^2]
	
	# /o/ extend factor to /a/ connecting as /u/
	L3_o= L2_a * (L2_u / L1_u)     # set list of 3rd tube's length by unit is [cm]
	A3_o= A2_a * (A2_u / A1_u)     # set list of 3rd tube's area by unit is [cm^2]
	
	# insatnce
	threetube_o  =  Class_ThreeTube(L3_o,A3_o)
	
	glo=Class_Glottal()   # instance as glottal voice source
	hpf=Class_HPF()       # instance for mouth radiation effect
	
	# draw
	fig = plt.figure()
	
	# /o/
	plt.subplot(2,2,1)
	plot_freq_res(threetube_o, '/o/', glo, hpf)
	plt.subplot(2,2,2)
	yout_o=plot_waveform(threetube_o, '/o/', glo, hpf)
	save_wav(yout_o, 'yout_o.wav')  # save generated waveform as a wav file
	ax1=fig.add_subplot(2,2,4)
	add_draw_patch(ax1, threetube_o) # draw cross-sectional view (area)
	
	#
	fig.tight_layout()
	plt.show()
	
#This file uses TAB
