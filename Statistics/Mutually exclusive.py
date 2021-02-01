def mutually_exclusive(A,B):
	intersect = A & B
	if intersect == set():
		print("Mutually Exclusive")
	else:
		print("Not mutually exclusive")
		
		
mutually_exclusive({1,6},{2,7})
	
	
	