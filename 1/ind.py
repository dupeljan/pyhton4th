from math import log
INPUT = "input.txt"

def main():
	tree = set()
	i = 0
	min2 = None
	min1 = None
	with open(INPUT,'r') as f:
		min0 = int(f.readline())
		for x in f:
			r = int(x)
			if r <= min0:
				min2 = min1
				min1 = min0
				min0 = r
			elif not min1:
				min1 = r
			elif not min2:
				min2 = r
			elif r <= min1:
				min2 = min1
				min1 = r
			elif r <= min2:
				min2 = r

	
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
