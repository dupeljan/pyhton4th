# Найди кол-во всех потомков элементов дерева для каждого элемента
# Вывести в отсортированном виде

INPUT = "input.txt"
# Кол-во всех предков в дереве, заданном 

def f(v,res,tree):
	# Находим детей
	childs = [ x for x in tree.keys() if tree[x] == v]
	# кол-во потомков
	descendantsCount = 0
	for x in childs:
		descendantsCount += 1 + f(x,res,tree)
	res[v] = descendantsCount
	return descendantsCount

#формирует результат
def gen_res(tree):
	result = {}
	#Найдем родоначальника
	for x in tree.values():
		if not x in tree:
			gParent = x
	print ("gParent ", gParent)
	#Найдем всех их предков
	var = f(gParent,result,tree)
	return result

#Ввод
'''
count = int(input("Кол-во элементов в дереве: "))
tree = {}
for x in range(count):
	parent,child = input("родитель - ребенок: ").split()
	tree[child] = parent
'''
def main():
	tree = {}
	with open(INPUT,'r') as f:
		for line in f:
			parent,child = line.split()
			tree[child] = parent
	print(tree)
	res = gen_res(tree)
	print(res)
	keys = list(res.keys())
	keys.sort()
	print(keys)
	for k in keys:
		print(k,":",res[k])

if __name__ == '__main__':
	main()