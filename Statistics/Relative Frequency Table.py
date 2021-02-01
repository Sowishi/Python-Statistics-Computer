def rf_table(data):
	table = {}
	data.sort()
	print(f"Data set: {data}")
	print("Relative Frequency Table:")
	print("Value	F	RF")
	sum = 0
	rf_sum = 0
	for i in data:
		freq = data.count(i)
		table[i] = freq
	for a,x in table.items():
		sum += x
	for key,val in table.items():
		rf = val/sum
		rf_sum += rf
		print(f"{key}	{val}	{rf}")
	print(f"		{rf_sum}")
		
rf_table([2,2,2,2,2,2,3,3,4,4,5,5,5])