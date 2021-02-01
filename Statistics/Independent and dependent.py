def probability(data,type,A,B):
	value = {}
	total = 0
	#Putting the data in dictionary
	for i in data:
		splitted = i.split("=")
		value[splitted[0].strip().lower()] = int(splitted[1])
	#Calculating the sum
	for key,val in value.items():
		total += val
	#Finding if dependent or not
	if type.lower() == "without":
		return (value[a] / total ) * (value[b] / (total - 1)) * 100
	#Finding if there's two variables
	a = A.lower()
	if B != None:
		b = B.lower()
		return (value[a] / total) * (value[b] / total) * 100
	#returning this if none up above is True
	return value[a] / total * 100
	
''' Data -> The sample space
	Type -> Dependent or Not
	A and B -> The object 
'''

print(probability(["Spade=13","Queen=4","Other=35"],"With","Spade",None))
		