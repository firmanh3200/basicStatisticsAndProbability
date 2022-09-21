#rms = sqrt(mean of sum of squared data)

def rms(*data):
  temp_rms = 0
  for i in range(len(data)):
    temp_rms = temp_rms + (data[i])**2
  return (temp_rms/len(data))**0.5
