def is_polindrom(s):
	return s == s[::-1]

s = input("Введите строку: ")
i = 0
while not(is_polindrom(s[i:])):
	i+=1
print(s+(s[:i])[::-1]," ",i) 

