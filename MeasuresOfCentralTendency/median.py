#mode is the measure of the data that divided the dataset into two equal parts
def median(*data):
  data = sorted(data)
  if len(data) % 2 == 0:
    median = ((data[int(len(data)/2)-1]) + (data[int((len(data)/2)+1)-1]))/2
  else:
    median = data[int((len(data)+1)/2)-1]
  return median
