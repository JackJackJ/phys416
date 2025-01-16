

# -*- coding: utf-8 -*-
"""

@author: JACK LEE
Simple python based plotting program
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

nmax=2001
x = np.linspace(0,20,nmax) # create an array x
fig, axs = plt.subplots(2, 2)

#sine vs cosine
axs[0][0].grid(linestyle = "dashed") # make a grid
axs[0][0].xaxis.set_major_locator(ticker.MultipleLocator(5)) #resize grid
axs[0][0].yaxis.set_major_locator(ticker.MultipleLocator(0.5))  #resize grid
# now plot
axs[0][0].set_xlabel('x') #x label
axs[0][0].plot(x,np.sin(x),color='tab:blue', label = "sin(x)") # plot blue line
axs[0][0].plot(x,np.cos(x),color='orange', label = "cos(x)") # plot orange cosine line
axs[0][0].legend(loc=1) #create legend
axs[0][0].set_xlim(0,20) #resize window
axs[0][0].set_ylim(-1, 1) #resize window

#dampened sine wave
axs[0][1].grid(linestyle = "dashed") # make a grid
axs[0][1].xaxis.set_major_locator(ticker.MultipleLocator(5))  #resize grid tickers
axs[0][1].yaxis.set_major_locator(ticker.MultipleLocator(0.5))  #resize grid tickers
# now plot
axs[0][1].set_xlabel('x') #x label

dampenedSine = np.exp((-1/4)*x) * np.sin(x)
axs[0][1].plot(x,dampenedSine,color='tab:blue', label = "e^(-x/4)sin(x)") # plot dampened blue sine
border = np.exp((-1/4)*x)
axs[0][1].plot(x,border,color='red', ls = "--", label = "e^(-x/4)") # plot red upper border
axs[0][1].plot(x,-1 * border,color='red', ls = "--", label = "-e^(-x/4)") # plot red lower border

for i in range(5):
    axs[0][1].plot(x[i * 400], dampenedSine[i * 400], 'go', label='Upper Intersections')
    axs[0][1].plot(x[i * 400], dampenedSine[i * 400], 'go', label='Lower Intersections')

    axs[0][1].plot(x[2000], dampenedSine[2000], 'go', label='Upper Intersections')
    axs[0][1].plot(x[2000], dampenedSine[2000], 'go', label='Lower Intersections')
axs[0][1].set_title(r'$y = e^{}$', y=1.02)  
axs[0][1].set_xlim(0,20.01)
axs[0][1].set_ylim(-1, 1)

plt.show() # shows the plot window

