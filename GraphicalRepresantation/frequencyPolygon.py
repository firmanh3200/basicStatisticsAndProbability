import numpy as np
import matplotlib.pyplot as plt

#generating 8 midpoint values which are uniformly distributed from 5.4 to 34.5
x = np.linspace(6.5,34.5,8)
y = [6,19,23,18,9,3,1,1]

plt.plot(x,y,'o-', color='gray')

plt.xlabel('Mid Values')
plt.ylabel('Data')
plt.title('Frequency polygon')

plt.show()
