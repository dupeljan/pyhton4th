# Дан строковый файл, содержащий даты в формате "dd/mm/yyyy".
# Создать два файла целых чисел, первый из которых содержит значения месяцев, а второй 
# - значение лет для дат из исходного строкового файла (в обратном порядке), причем даты должны быть не позднее заданной
import os

INPUT = 'dateFile.txt'
OUTPUT1 = 'output1.txt'
OUTPUT2 = 'output2.txt'
'''

'''
CACHE_LINES = 1000
TMP_PATH = "TMP"

def date_str(n):
	if n < 10:
		return "0" + str(n)
	return str(n)
def gen_dateFile():
	with open(INPUT,'w') as out:
		for x in range(1999,2021):
			for y in range(1,13):
				for z in range(1,28):
					out.write(date_str(z)+"/"+date_str(y)+"/"+str(x)+"\n")
def solve():
	ealiers_data = int(input('Введите дату: ').split('/')[2])
	if not os.path.exists(TMP_PATH):
		os.makedirs(TMP_PATH)
	cache = []
	file_count = 0
	with open(INPUT,'r') as inp, open(OUTPUT1,'w') as out1:
		for line in inp:
			date = line.split('/')
			out1.write(date[1]+"\n")
			if int(date[2]) > ealiers_data:
				if len(cache) == CACHE_LINES:
					file_count += 1
					f = open(os.path.join(TMP_PATH, str(file_count)),'w')
					for l in cache[::-1]:
						f.write(l)
					cache = []
				cache.append(date[2])
	## merge cache files
	with open(OUTPUT2,'w') as out2:
		for l in cache[::-1]:
			out2.write(l)
		for x in range(file_count,0,-1):
			f = open(os.path.join(TMP_PATH, str(x)),'r')
			for l in f:
				out2.write(l)
			f.close()
			# delete TMP
			os.remove(os.path.join(TMP_PATH, str(x)))
	
	print('Success')


				

def main():
	solve()
if __name__ == '__main__':
 	main() 