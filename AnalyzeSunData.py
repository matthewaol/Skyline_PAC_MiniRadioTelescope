#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 14:43:21 2017

@author: jaguirre
"""

import numpy as np
import matplotlib.pyplot as plt
from glob import glob
import ephem

def readMRT(filename):
    dat = np.load(filename)
    d = {}
    for item in dat.items():
        d[item[0]] = item[1]
#   Determine active axis
    if (np.median(np.diff(d['az']))==0):
        d['aa'] = 'el'
    else:
        d['aa'] = 'az'
    return d

filenames = glob('Fri_Jun_30_*.npz')
for i,filename in enumerate(filenames):
    d = readMRT(filename)
    plt.figure(i)
    plt.clf()
    plt.plot(d[d['aa']],d['pwr'])
    plt.title(filename)
    plt.xlabel(d['aa']+' scan (deg)')
    plt.ylabel(r'Power ($\mu$W)')
    
    
# Calibration seems to be roughly 300 K = 17 microW
# El_true = El_measured + 4. (for the 15:56:03 data)