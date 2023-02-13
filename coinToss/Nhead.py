#write a python code that gives the number of head after N times tossing a 'fair' coin.

import random

N = 200 #number of trials
sampleSpace = ['H','T'] 
count = 0 #no of heads

for i in range(N):
    if random.choices(sampleSpace)==['H']:
        count += 1
print(count)
