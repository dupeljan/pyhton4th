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

len_ = int(max(rangeSample)) - int(min(rangeSample))
min_ = int(min(rangeSample))
max_ = int(max(rangeSample))
h = int(np.round((max_ - min_) / ( 1 + 3.28*np.log(len_)) ))
bins = np.round(len_ / h)
print(bins)
counter = Counter(rangeSample)
xAccum = list([0])
yAccum = list([0])

x = list()
y = list()
for i in range(min_,max_+1,h):
	x.append(i)
	y.append(sum([counter.get(j,0) for j in range(i,i+h)]))
	xAccum.append(i)
	yAccum.append(yAccum[-1] + y[-1])
	print(yAccum[-1])

xAccum = xAccum[1:]
yAccum = yAccum[1:]

print(yAccum)
plt.step(xAccum, yAccum)
plt.title("Эмпирическая функция расперделения")
plt.show()


'''
x = list()
y = list()
for i in range(min_,max_+1):
	x.append(i)
	y.append(counter.get(i,0))
	'''
'''	
for key in sorted(counter.keys()):
	x.append(int(key))
	y.append(counter[key])
'''
plt.bar(x,y,width=h)
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