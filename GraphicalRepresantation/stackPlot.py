#this code is imported from @ShifatHasanGNS (https://github.com/ShifatHasanGNS/Practice/blob/master/Python/Data_Visualization/Matplotlib/)
import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]

sleeping = [7, 8, 6, 11, 7]
eating = [2, 3, 4, 3, 2]
working = [7, 8, 7, 2, 2]
playing = [8, 5, 7, 8, 13]

plt.plot([], [], color='lightgray', label='Sleeping')
plt.plot([], [], color='lightgreen', label='Eating')
plt.plot([], [], color='lightblue', label='Working')
plt.plot([], [], color='lightpink', label='Playing')

colors = ['lightgray', 'lightgreen', 'lightblue', 'lightpink']

plt.stackplot(days, sleeping, eating, working, playing, colors=colors)

plt.title('Interesting Graph\nCheck It Out')

plt.xlabel('X')
plt.ylabel('Y')

plt.legend()
plt.show()
