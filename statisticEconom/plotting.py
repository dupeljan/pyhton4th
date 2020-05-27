import matplotlib.pyplot as plt
import csv
from collections import Counter
import numpy as np

INPUT = "Sample8.22.csv"

# Get data from sample
table = list(csv.reader(open(INPUT,'r',newline='')))
# Range it 
range_ = table
range_.sort(key= lambda x : int(x[1])) 

rangeSample = [int(x[1]) for x in range_]
counter = Counter(rangeSample)
x = list([0])
y = list([0])
for key in sorted(counter.keys()):
	x.append(key)
	y.append(y[-1] + counter[key])
x = x[1:]
y = y[1:]

plt.step(x, y)
plt.title("Эмпирическая функция расперделения")
plt.show()

len_ = int(max(rangeSample)) - int(min(rangeSample))
min_ = int(min(rangeSample))
max_ = int(max(rangeSample))

x = list()
y = list()
for i in range(min_,max_+1):
	x.append(i)
	y.append(counter.get(i,0))
'''	
for key in sorted(counter.keys()):
	x.append(int(key))
	y.append(counter[key])
'''
plt.bar(x,y,width=1)
plt.xticks(x)
plt.yticks(np.arange(min(y),max(y)+1,1.0))
plt.grid(axis='y')
plt.title("Гисторамма")
#plt.hist(rangeSample,bins=len_+1)
plt.show()

plt.plot(x,y)
plt.xticks(x)
plt.yticks(np.arange(min(y),max(y)+1,1.0))
plt.grid(axis='y')
plt.title("Полигон")
plt.show()