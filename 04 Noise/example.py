#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 16:43:19 2018

@author: kiliu
"""

import sys
sys.path.append('../ThinkDsp')


import thinkdsp
import thinkplot

# White noise / UU
signal = thinkdsp.UncorrelatedUniformNoise()
wave = signal.make_wave(duration=0.5, framerate=11025)
wave.write(filename='uu.wav')

segment = wave.segment(start=0, duration=0.01)
segment.plot()
thinkplot.show()

spectrum = wave.make_spectrum()
spectrum.plot()
thinkplot.show()
#spectrum.plot_power()
#thinkplot.show()
spectrum.plot_power(linewidth=1, alpha=0.5)
thinkplot.config(xscale='log', yscale='log')
thinkplot.show()
print(spectrum.estimate_slope())


integ = spectrum.make_integrated_spectrum()
integ.plot_power()
thinkplot.show()


# Brownian noise
signal = thinkdsp.BrownianNoise()
wave = signal.make_wave(duration=1, framerate=11025)
wave.write('browian.wav')
wave.plot()
thinkplot.show()

spectrum = wave.make_spectrum()
spectrum.plot()
thinkplot.show()
spectrum.plot_power(linewidth=1, alpha=0.5)
thinkplot.config(xscale='log', yscale='log')
thinkplot.show()
print(spectrum.estimate_slope())


# Pink noise
signal = thinkdsp.PinkNoise()
wave = signal.make_wave(duration=1, framerate=11025)
wave.write('pink.wav')
wave.plot()
thinkplot.show()
spectrum = wave.make_spectrum()
spectrum.plot()
thinkplot.show()
spectrum.plot_power(linewidth=1, alpha=0.5)
thinkplot.config(xscale='log', yscale='log')
thinkplot.show()
print(spectrum.estimate_slope())


# White / UG
signal = thinkdsp.UncorrelatedGaussianNoise()
wave = signal.make_wave(duration=0.5, framerate=11025)
wave.write('ug.wav')
spectrum = wave.make_spectrum()
spectrum.plot()
thinkplot.show()
spectrum.plot_power(linewidth=1, alpha=0.5)
thinkplot.config(xscale='log', yscale='log')
thinkplot.show()
print(spectrum.estimate_slope())

