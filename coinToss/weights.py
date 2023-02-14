"""
Now, think about a coin for which the probability of a head is 0.1%. You toss the coin Ntrial = 10000 times for one experiment. 
If you repeat the experiment 1000 times, what does the distribution look like? Take the mean and standard deviations of the 1000 Nhead values. 
Do they match the predicted mean and standard deviation of the Poisson distribution?
"""

import random
import matplotlib.pyplot as plt
import numpy as np

N = 200
sampleSpace = ['H','T']
t = 100
heads = []

for j in range(t):
    count = 0
    for i in range(N):
        if random.choices(sampleSpace,weights = [0.1,0.9])==['H']:
            count += 1
    heads.append(count)

plt.hist(heads, bins=10)
plt.show()

mean = np.mean(heads)
sd = np.std(heads)
print("the mean is:",mean, "and the standard deviation is",sd)

trueMean = N*0.5
trueSD = np.sqrt(N*0.5*0.5)
print("the mean should be:",trueMean, "and the standard deviation should be",trueSD)
