# -*- coding: utf-8 -*-
"""

@author: JACK LEE
Simple python based plotting program
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

nmax=51
x = np.linspace(0,20,nmax) # create an array x

# plt.ion() Need this sometimes to fix plot issues
plt.figure(1) # open up a figure window
plt.clf() # clear the window
plt.grid(linestyle = "dashed") # make a grid
plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(5)) 
plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(0.5))  
# now plot
plt.plot(x,np.sin(x),color='tab:blue', label = "sin(x)") # plot blue line
plt.xlabel('x') #x label
plt.plot(x,np.cos(x),color='orange', label = "cos(x)") # plot orange cosine line
plt.legend(loc=1)
plt.xlim(0,20)
plt.ylim(-1, 1)
plt.show() # shows the plot window