import math
def sd(data):
	#Calculate the mean
	mean = sum(data) / len(data)
	#Calculate the sum of (x-mean) **2
	container = 0
	for x in data:
		container += (x - mean) ** 2
	#Printing and calculating the result
	result = container / (len(data) -1)
	output = math.sqrt(result)
	print(output)
		
	
	
sd([7,8,10,5,2])