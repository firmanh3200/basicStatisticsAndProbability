import matplotlib.pyplot as plt 

#histogram

#these are the marks of students in the course Numerical Analysis
data = [100, 58,41,50,65,75,52,55,43,60,66,46,30,50,100,66,60,41,71,100,62,66,71,52,54,89,77,60,66,65,77,55,40,43,40,77,65,41,43,43,56,43,41,73,41,50,40,40,43,60,41,41]

plt.xlabel('Marks')
plt.ylabel('No. of Students')
plt.title('Histogram')

plt.xkcd()
plt.hist(data, color='gray',bins=10)
plt.show()
