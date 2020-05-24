with open("rawRandom.txt", 'r') as f:
	for x in f:
		print(len(x.split()))