'''
 Найти количество людей, чей балл выше общего среднего балла. Вывести их список.
'''
import csv
import os
import re

DIR = "files"
infile = open(os.path.join(DIR,"1.csv"), 'r')
# for each csv file
sum = 0
count = 0

for fileName in os.listdir(DIR):
	# open CSV
	with open(os.path.join(DIR,fileName), 'r') as inp:
		file = list(csv.reader(inp))
		# get Mark index
		i = file[0].index([x for x in file[0] if x[:6] == 'Оценка'][0])
		
		# Get divider
		divider = int(file[0][i].split('/')[1].split(",")[0]) / 10
		# get sum and count 
		for row in file[1:-2]:
			
			if row[i] != '-':
				sum += int(row[i].split(',')[0])/divider
				count+=1


m = sum / count
print("Средний бал", m)
for fileName in os.listdir(DIR):
	
	# open CSV
	with open(os.path.join(DIR,fileName), 'r') as inp:
		file = list(csv.reader(inp))
		# get Mark index
		i = file[0].index([x for x in file[0] if x[:6] == 'Оценка'][0])
		# Get divider
		divider = int(file[0][i].split('/')[1].split(",")[0]) / 10
		# get sum and count 
		for row in file[1:-2]:
			if row[i] != '-' and int(row[i].split(',')[0])/divider >= m:
				print(row)




