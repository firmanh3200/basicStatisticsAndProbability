#Uses concept of limit to show that lim 1/x as x goes to 0 doesn't exist

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1,1,100) #taking value from -1 to +1
y = 1/x

plt.plot(x,y,color='gray',label=r'$y=\frac{1}{x}$')
plt.legend()

plt.show()
