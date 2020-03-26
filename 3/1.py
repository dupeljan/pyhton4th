def is_polindrop(s):
	if len(s) in [1,0]:
		return True
	if s[0] == s[-1]:
		return is_polindrop(s[1:-1])
	return False

char_list = list(map(chr, range(97,123)))
str = input("Введите строку: ")
filtered_str = "".join([ char.upper() for char in str if char.lower() in char_list  ])
print(is_polindrop(filtered_str))

#x = "".join([ char.upper() for char in input("Введите строку: ") if char in char_list  ])
#print ( x[:len(x)/2] == x[:len(x)/2:-1])
