def crf_table(data):
	table = {}
	data.sort()
	print(f"Data set: {data}")
	print("Cumulative Frequency Table:")
	print("Value	F	RF")
	sum_freq = 0
	rf_table = []	
	crf_table = []
	sum_rt = 0
	#adding the data to table
	for i in data:
		freq = data.count(i)
		table[i] = freq
	#calculate the freq sum
	for a,x in table.items():
		sum_freq += x
	#calculating the relative freq
	for key,val in table.items():
		rf = val/sum_freq
		rf_table.append(rf)
		print(f"{key}	{val}	{rf}")
	#Calculate the CRF
	daya = rf_table[1] + rf_table[0]
	for y in range(2,len(rf_table)):
		current = daya + rf_table[y]
		crf_table.append(current)
		daya = current
	#Printing the CRF
	daya = rf_table[1] + rf_table[0]
	print("")
	print("CRF")
	print(rf_table[0])
	print(daya)
	for i in crf_table:
		print(i)
		
crf_table([2,2,2,2,4,4,4,5,5,5,7,7])