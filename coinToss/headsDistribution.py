#write a python code that gives the number of head after N times tossing a 'fair' coin. Repeat this experiment t times and then plot the histogram.

import random
import matplotlib.pyplot as plt

N = 200 #no of trials to get a get
t = 100 #no of trials to repeat the experiment
sampleSpace = ['H','T']

heads = [] #array to save the no of heads

for j in range(t):
    count = 0
    for i in range(N):
        if random.choices(sampleSpace)==['H']:
            count += 1
    heads.append(count)

plt.hist(heads, bins=10)  #plotting
plt.show()
