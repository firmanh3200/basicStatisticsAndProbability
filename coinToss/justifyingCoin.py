#write a python code that gives the number of head after N times tossing a 'fair' coin. Repeat this experiment t times 
#What is the mean and standard deviation of these 1000 numbers? Does it match the predicted mean and standard deviation using formulae for the Binomial distribution?

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
        if random.choices(sampleSpace)==['H']:
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
