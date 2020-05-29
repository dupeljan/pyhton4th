INPUT = "rawInput.txt"
OUTPUT = "Input.csv"

import csv

with open(INPUT) as inp:
	with open(OUTPUT, 'w', newline='') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
		x_line = list()
		y_line = list()
		for i, x in enumerate(inp):
			# x line
			if  (i % 3) == 1:
				x_line += x.split()[1:]
			# y line
			if  (i % 3) == 2:
				y_line += x.split()[1:]
				

		
		for x in zip(x_line,y_line):
			spamwriter.writerow(list(x))

INPUT = "rawRandom.txt"
OUTPUT = "Random.csv"
pieceInRow = [50]
rows = [20]
with open(INPUT) as inp:
	with open(OUTPUT, 'w', newline='') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
		for i, x in enumerate(inp):
			for y in range(rows[i]):
				spamwriter.writerow(x.split()[pieceInRow[i]*y:pieceInRow[i]*(y+1)])


