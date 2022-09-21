import matplotlib.pyplot as plt

data = [1.2,0.3,0.4, 1.3,0.7,2.1,0.5,2.3,1.3,1.4,2.4]

#histogram
plt.figure(figsize=(8,4))
plt.subplot(1,2,1) #means we have a 1 by 2 plot and this is the 1st sub-plot of the plot
plt.hist(data,bins=4,edgecolor='Black',color='Gray')
plt.title('Histogram')

#box and whisker plot
plt.subplot(1,2,2)
plt.boxplot(data, vert=False)
plt.title('Box and Whisker Plot')

plt.show()
