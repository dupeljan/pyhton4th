# Вводится кол-во школьников
#Для каждого школьника сколько языков и какие
#Вывести языки, котрые знают хотябы 1 ребенок
#и которые знают все школьники
scholarCount = int(input("Кол-во школьников"))
union = set()
dist = set()
for scholarNum in range(scholarCount):
	x = int(input("Школьник № " + str(scholarNum) + ". Кол-во  его языков "))
	scholarSet = set()
	for i in range(x):
		scholarSet.add(input())
	if not union:
		union = scholarSet
	else:	 
		union = union & scholarSet
	dist = dist | scholarSet
print("Языки, которые знает хотя бы 1 ", dist)
print("Языки, которые знают все ", union)
