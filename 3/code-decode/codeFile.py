def get_pred_char(c):
	if ord(c.lower()) not in range(1072,1104):
		return c
	if c.lower() == 'а':
		return 'я' if c.lower() == c else 'Я'
	return chr(ord(c)-1)

INPUT = "output.txt"
OUTPUT = 'input.txt'

with open(INPUT,'r') as inp, open(OUTPUT,'w') as out: 
	for line in inp:
		res = "".join(list(map(get_pred_char,[x for x in line if x !=''])))
		out.write(res)