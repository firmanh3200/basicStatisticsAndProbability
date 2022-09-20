import matplotlib.pyplot as plt 

#bar diagram

# visit - No. of persons
# frequently - 49
# occasionally - 71
# Rarely - 24
# never - 6

data = {'frequently':49, 'occasionally':71, 'rarely':24, 'never':6} #made a dictionary of the data

visit = list(data.keys()) #x-axis data
noOfPersons = list(data.values()) #y-axis data

plt.xlabel('Visit')
plt.ylabel('No. of Persons')
plt.title('Bar Diagram')

plt.xkcd() #this was called just to make it a xkcd comic style

plt.bar(visit,noOfPersons,color='gray')
plt.show()
Footer
