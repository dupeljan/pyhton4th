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


# Sampling

# get rows
#birthday = [17,7]
#birthday = [6,7]
birthday = [22,8] 
col = birthday[0]
row = birthday[1]
INPUT = "Random.csv"
INPUT_FULL = "Input.csv"
OUTPUT = "Sample" + str(row)+"." + str(col) + ".csv"
with open(INPUT,'r',newline='') as inp:
	with open(OUTPUT, 'w', newline='') as out:
		sampleRows = list()
		sampleRows += [birthday[1]]

		lines = list(csv.reader(inp))
		elem = str(lines[row][col])
		if len(elem) == 3:
			elem = "0" + elem
		b = int(elem[1])
		if b in sampleRows:
			b += 1
		sampleRows += [b]
		c = 10 + int(elem[2])
		if c in sampleRows:
			c += 1
		sampleRows += [c]
		d = 10 + int(elem[3])
		if d in sampleRows:
			d += 1
		sampleRows += [d]
		print("Num", elem,"Rows",sampleRows)

		
		# Got chosen rows

		rand = list()
		for x in sampleRows:
			rand += lines[x]

		# Write it to the samples file
		with open(INPUT_FULL,'r',newline='') as inpFull:
			writer = csv.writer(out, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
			lines = list(csv.reader(inpFull))
			linesCount = len(lines)
			choosen = list()
			for r in rand:
				# Get last three digit
				num = int(str(r)[-3:]) % linesCount 
				while  num in choosen:
					num = (num + 1) % linesCount
				writer.writerow([num] + lines[num])
				choosen += [num]




