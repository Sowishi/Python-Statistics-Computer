def outlier_calculator(list):
	list.sort()
	#Sccaning if index of list is odd
	if len(list) - 1 & 1:
		#The median index of list
		index = (len(list)-1)//2
		avg = (list[(len(list)-1)//2] + list[(len(list)-1)//2+1])// 2
		list.insert(index+1,avg)
	#index of q2
	q2 = (len(list) -1) // 2
	#Scanning of index of q1 is odd
	if len(list[0:q2]) & 1:
		#The median index of q1
		index = q2 // 2
		avg = (list[q2] + list[q2+1]) // 2
		list.insert(index,avg)
	#index of q1
	q1 = q2 // 2
	#Scanning again
	if len(list[q2:]) & 1:
		#The median index of q2
		index = (q2+len(list)-1) // 2
		avg = (list[(q2+len(list)-1) // 2] + list[(q2+len(list)-1) // 2 + 1]) // 2
		list.insert(index,avg)
	q3 = (q2+len(list)-1) // 2
	#Calculatinf IQR
	iqr = list[q3] - list[q1]
	#Calculating boundaries
	min = list[q1] - (1.5 * iqr)
	max = list[q3] + (1.5 * iqr)
	#===================
	print(f"Data set: {list}\n")
	print(f"Q1: {list[q1]} Q2: {list[q2]} Q3: {list[q3]} IQR: {iqr}")
	print(f"Range: {min} -> {max}\n")
	#Printing weather outlier or not
	for i in list:
		if i not in range(int(min),int(max)):
			print(f"Outlier: {i}")
		else:
			print(f"Not outlier: {i}")
			
outlier_calculator([13,16,18,18,22,23,25,28,29,31,38,50])
	