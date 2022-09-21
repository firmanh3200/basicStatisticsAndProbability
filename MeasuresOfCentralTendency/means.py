# arithmetic mean = sum of the oberservational data / no. of observations

def am(*data):
  return sum(data)/len(data) 

# geometric mean = n th root of their product
# applicable only for non-zero observations

def gm(*data):
    temp_gm = 1
    for i in range(len(data)):
        temp_gm = temp_gm*data[i]
    return temp_gm**(1/len(data))

# harmonic mean = reciprocal of the arithmetic mean of the reciprocals 
# applicable only for non-zero observations

def hm(*data):
    temp_hm = 0
    for i in range(len(data)):
        temp_hm = temp_hm + 1/data[i]
    return len(data)/temp_hm
