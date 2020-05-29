# Sampling

# get rows
#birthday = [17,7]
#birthday = [6,7]
import os
import csv
def genSample(birthday = [1,1],dirname=""):
	#birthday = [22,8] 
	col = birthday[0]
	row = birthday[1]
	INPUT = "Random.csv"
	INPUT_FULL = "Input.csv"
	OUTPUT = os.path.join(dirname,"Sample.csv")
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
