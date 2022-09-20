import matplotlib.pyplot as plt 

#pie diagram

# visit - No. of persons
# frequently - 49
# occasionally - 71
# Rarely - 24
# never - 6

data = {'frequently':49, 'occasionally':71, 'rarely':24, 'never':6}
visit = list(data.keys())
noOfPersons = list(data.values())

plt.title('Pie Diagram')

plt.pie(noOfPersons, labels = visit, autopct='%0.1f%%') #autopct is to label the pies

#the plt.pie will automatically 

plt.show()
