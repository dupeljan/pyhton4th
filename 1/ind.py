from math import log
INPUT = "input.txt"
'''

def dixotomy(elem,array):
	l = len(array)
	i = int(l / 2)
	for k in range(int(log(l,2))-1):
		print(k,i)
		if array[i] > elem:
			i +=  int(l / (2 ** (k+2)))
		else:
			i -=  int(l /( 2 ** (k+2)))
	if array[i] == elem:
		return array[abs(i-1)]
	else:
		return array[i]

def main():
	# minimum array
	min_a = []
	with open(INPUT,'r') as f:
		min_ = int(f.readline())
		min_a.append(min_)
		# create min array
		for line in f:
			l = int(line)
			if l < min_:
				min_ = l
			min_a.append(min_)
		if len(min_a) == 2:
			return min_a[0] * min_a[1]
		min_res = []
		# find first min
		print(min_a)
		min_res.append(min_a[-1])
		# find second min
		min_res.append(dixotomy(min_res[0],min_a))
		# if sum is odd - return the answer
		res = min_res[0] + min_res[1]
		print(min_res)
		if res % 2 == 0:
			return res
		# find third min
		min_res.append(dixotomy(min_res[1],min_a))
		res = min_res[0] + min_res[2]
		print(min_res)
		if res % 2 == 0:
			return res
		return min_res[1] + min_res[2]

'''
'''
Условие:
надо поискать
12 вариант 
В прошлый раз 
'''
def main():
	tree = set()
	i = 0
	with open(INPUT,'r') as f:
		min0 = min1 = min2 =int(f.readline())
		for x in f:
			i += 1
			r = int(x)
			if r <= min0:
				min2 = min1
				min1 = min0
				min0 = r
	
	print(min0,min1,min2)
	res = min0 + min1
	if res % 2 == 0 or i == 2:
		return res
	res = min0 + min2
	if res % 2 == 0:
		return res  
	return min1 + min2






if __name__ == '__main__':
	print(main())
