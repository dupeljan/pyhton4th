n = int(input("Введите номер"))
ans = "1"
n -= 1
for x in range(n):
	res = []
	l = ans.split()
	j = 0
	for i in range(len(l)-1):
		if l[i] != l[i+1]:
			ans = ans[:i+j]+" "+ans[i+j:]
			j += 1

	print(ans)
	print(zip(list(map(str, list(map(len, ans.split())))),[str(x[0]) for x in ans.split]))
	ans = "".join(zip(list(map(str, list(map(len, ans.split())))),[str(x[0]) for x in ans.split]))
	
