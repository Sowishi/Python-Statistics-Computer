def probability(obj,type,A,B):
	sample_space = 0
	object = {"coin":2,"dice":6}
	if obj in object:
		sample_space = object[obj]
	else:
		print(f"Theres no such object: {obj}")
	intersect = len(A & B)
	union = len(A.union(B))
	chance = intersect / sample_space
	if type.lower() == "or":
		chance = union / sample_space
	print(f"Your chance of winning is {chance*100} %")
	
	
probability("dice","and",{1},{4,2,1})
	