import matplotlib.pyplot as plt
import csv
from collections import Counter
import numpy as np
import statistics as st
from scipy import stats
import math
import os

birthday = [22,8] 
col = birthday[0]
row = birthday[1]
INPUT = "Sample" + str(col)+"." + str(row) + ".csv"
OUTPUT = "CorrelationTable" + str(col)+"." + str(row) + ".csv"

class StatisticSolver:
	def __init__(self):

		self.partA = False
		self.partB = True

		# Get data from sample
		table = list(csv.reader(open(INPUT,'r',newline='')))
		# Range it 
		self.range_ = table
		self.range_ = [[int(x[0]),int(x[1]), int(x[2])] for x in self.range_]
		self.range_.sort(key= lambda x : x[1]) 

		 
		self.rangeSample = [x[1] for x in self.range_]
		self.counter = Counter(self.rangeSample)
		self.n = len(self.rangeSample)


		self.min_ = min(self.rangeSample)
		self.max_ = max(self.rangeSample)
		self.len_ = self.max_ - self.min_
		self.h = int(np.round((self.max_ - self.min_) / ( 1 + 3.28*np.log(self.len_)) ))
		self.bins = np.round(self.len_ / self.h)


		''' CALCULATION '''
		# Mean
		self.mean_ = st.mean(self.rangeSample)
		print("X mean",self.mean_)
		# Dispersion
		sum_ = 0
		self.ni = list()
		for i in range(self.min_,self.max_+1,self.h):
			self.ni.append( sum([self.counter.get(j,0) for j in range(i,i+self.h)]) )
			sum_ += self.ni[-1] * (( ((2*i+self.h)/ 2) - self.mean_ ) ** 2)
		self.disp = sum_ / self.n
		print("X Dispersion", self.disp)

		self.standDeviation =  np.sqrt(self.disp)
		print("X standDeviation", self.standDeviation)

		self.dispEstim = self.disp * (self.n/(self.n-1))
		self.standDeviationEstim  = self.standDeviation * np.sqrt(self.n/(self.n-1))
		print("X Dispersion estimation",self.dispEstim)
		print("X standDeviation estimation",self.standDeviationEstim)

		# Computing for intervals
		self.accuracy = 0.95
		self.t = 1.96
		self.q = 0.099
		print("accuracy", self.accuracy, "t",self.t, "n", self.n, "q", self.q)
		self.delta = self.t * self.standDeviation / np.sqrt(self.n) 
		print("Expected value interval(",
				self.mean_ - self.delta,',',
				self.mean_ + self.delta,
				") delta = ", self.delta)

		print("standDeviation interval(",
				self.standDeviationEstim / ( 1 + self.q),',',
				self.standDeviationEstim / ( 1 - self.q),
				") ")

		

		
		F = lambda x: self.h * stats.norm.pdf((x-self.mean_)/self.standDeviationEstim)/self.standDeviationEstim
		# Gets Pirson kriterion
		self.pi = list()
		sum_ = 0
		for i,x in enumerate(range(self.min_,self.max_+1,self.h)):
			self.pi.append(F((2*x+self.h)/2))
			numerator = (self.ni[i] - self.n * self.pi[-1]) ** 2
			sum_ += numerator / (self.n * self.pi[-1])
		
		print("Pirson kriterion",sum_)

		
		# Correlation table
		self.min_y = min([x[2] for x in self.range_])
		self.max_y = max([x[2] for x in self.range_])
		self.len_y = self.max_y - self.min_y
		pairs = [[x[1], x[2]] for x in self.range_ ]
		with open(OUTPUT,'w',newline='') as out:
			writer = csv.writer(out, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
			writer.writerow(["#"] + [ x for x in range(self.min_,self.max_+1)])
			for y in range(self.min_y,self.max_y+1):
				writer.writerow([y] + [ pairs.count([x,y]) for x in range(self.min_,self.max_+1) ])
			
		# Correlation coef
		self.mean_y = st.mean([x[2] for x in self.range_])
		numerator = 0
		sumX = 0
		sumY = 0
		for x in pairs:
			numerator += (x[0] - self.mean_)*(x[1] - self.mean_y)
			sumX += (x[0] - self.mean_) ** 2
			sumY += (x[1] - self.mean_y) ** 2

		self.CorrelationCoef = numerator / np.sqrt(sumX * sumY)

		print("Correlation coef", self.CorrelationCoef)

		# Compute regretion fun
		self.sumX = sum([x[0] for x in pairs])
		self.sumY = sum([x[1] for x in pairs])
		self.sumXY = sum( [x[0] * x[1] for x in pairs])
		self.sumXSqr = sum( [ x[0] ** 2 for x in pairs])

		self.a = self.n * self.sumXY - self.sumX * self.sumY
		self.a /= self.n * self.sumXSqr - self.sumX ** 2

		self.b = self.sumY - self.a * self.sumX
		self.b /= self.n 

		print("Regression equation: y = ax + b")
		print("a",self.a,"b",self.b)
		self.xAccum = list([0])
		self.yAccum = list([0])

		self.x = list()
		self.y = list()
		for i in range(self.min_,self.max_+1,self.h):
			self.x.append(i)
			self.y.append(sum([self.counter.get(j,0) for j in range(i,i+self.h)]))
			self.xAccum.append(i)
			self.yAccum.append(self.yAccum[-1] + self.y[-1])
			
		self.xAccum = self.xAccum[1:]
		self.yAccum = self.yAccum[1:]

	def plot(self):
		if self.partA:

			# Emperic distribution fun
			plt.step(self.xAccum, self.yAccum)
			plt.title("Эмпирическая функция расперделения")
			plt.show()

			# Gistogram for X var
			plt.bar(self.x,self.y,width=self.h)
			plt.xticks(self.x)
			plt.yticks(np.arange(min(self.y),max(self.y)+1,1.0))
			plt.grid(axis='y')
			plt.title("Гисторамма")
			#plt.hist(rangeSample,bins=len_+1)
			plt.show()

			# Poligon for X var
			plt.plot(self.x,self.y)
			plt.xticks(self.x)
			plt.yticks(np.arange(min(self.y),max(self.y)+1,1.0))
			plt.grid(axis='y')
			plt.title("Полигон")
			plt.show()

		if self.partB:
			# Scatter XY
			plt.scatter(*zip(*[(x[1],x[2]) for x in self.range_]),label='Элементы выборки')
			plt.plot(range(self.min_,self.max_+1),[self.a * x +self.b for x in range(self.min_,self.max_+1)]
				,'r',label='Прямая регрессии y = {0}x + ({1})'.format(np.round(self.a,3),np.round(self.b,3) ))
			plt.title("Кореляционное облако")
			plt.legend()
			plt.show()
def main():
	s = StatisticSolver()
	s.plot()

if __name__ == '__main__':
	main()