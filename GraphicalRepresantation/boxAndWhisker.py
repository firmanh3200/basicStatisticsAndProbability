import matplotlib.pyplot as plt

#box and whisker plot

data = [1.2,0.3,0.4, 1.3,0.7,2.1,0.5,2.3,1.3,1.4,2.4]

plt.xlabel('Data')
plt.title('Box and Whisker Plot')

plt.boxplot(data, vert=False)
plt.show()
