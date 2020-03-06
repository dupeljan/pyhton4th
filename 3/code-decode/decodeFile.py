# Кодировка файла +1 по алфавиту
def get_next_char(c):
	if ord(c.lower()) not in range(1072,1104):
		return c
	if c.lower() == 'я':
		return 'а' if c.lower() == c else 'А'
	if c == ' ':
		return c
	return chr(ord(c)+1)

INPUT = "input.txt"
OUTPUT = 'output.txt'

with open(INPUT,'r') as inp, open(OUTPUT,'w') as out: 
	for line in inp:
		res = "".join(list(map(get_next_char,[x for x in line])))
		out.write(res)