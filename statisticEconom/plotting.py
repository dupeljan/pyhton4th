import matplotlib.pyplot as plt
import csv
from collections import Counter
import numpy as np
import statistics as st
from scipy import stats
import math
import os



EmpericDistributionFunName = "Эмпирическая функция расперделения.png"
HistName = "Гисторамма.png"
PoligonName = "Полигон.png"
CorrelationName = "Кореляционное облако.png"


DPI = 300
FIG_DIMS = [16,9]


OUTPUTCORR = "CorrelationTable.csv"

class StatisticSolver:
	def __init__(self,dirname,inputFile):
		self.dirname = dirname

		self.partA = True
		self.partB = True

		# Get data from sample
		table = list(csv.reader(open(inputFile,'r',newline='')))
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
		self.K = sum_
		print("Pirson kriterion",sum_)

		
		# Correlation table
		self.min_y = min([x[2] for x in self.range_])
		self.max_y = max([x[2] for x in self.range_])
		self.len_y = self.max_y - self.min_y
		pairs = [[x[1], x[2]] for x in self.range_ ]
		with open(os.path.join(self.dirname, OUTPUTCORR),'w',newline='') as out:
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

	def putStatistic(self,filename,birthday):
		with open(os.path.join(self.dirname,filename), 'w') as out:
			lines = list()
			lines += ["Решение задачи по статистике"]
			lines += ["ДР " + str( birthday)]
			lines += ["1) см файл Sample.csv"]
			lines += ["2) см изображения в текущей папке"]
			lines += ["3) Для множества Х"]
			lines += ["Размер интервала " + str(self.h)]
			lines += ["Кол-во групп " + str(self.bins)]
			lines += ["Размер выборки " + str(self.n)]
			lines += ["Выборочная средняя " + str(self.mean_)]
			lines += ["Выборочная дисперсия " + str(self.disp)]
			lines += ["Выборочное среднеквадратическое отклонение " + str(self.standDeviation)]
			lines += ["Несмещенная выборочная дисперсия " + str(self.dispEstim)]
			lines += ["Несмещенное выборочное среднеквадратическое отклонение " + str(self.standDeviationEstim)]
			lines += ["Точность " + str(self.accuracy)]
			lines += ["Параметр t " + str(self.t)]
			lines += ["Параметр q " + str(self.q)]
			lines += ["Параметр дельта " + str(self.delta)]
			lines += ["Интервальная оценка мат ожидания "]
			lines += [str(self.mean_ - self.delta )+','+ str(self.mean_ + self.delta)]
			lines += ["Интервальная оценка среднеквадратического отклонения "]		
			lines += \
						[str(self.standDeviationEstim / ( 1 + self.q) )+ ',' + str(self.standDeviationEstim / ( 1 - self.q))]
			lines += ["4) Критерий Пирсона " + str(self.K)]
			self.xi = list()
			for x in [0.95,0.975,0.99]:

				self.xi += [stats.distributions.chi2.ppf(x,self.bins -3)]
			
				lines += [" На уровне значимости " + str(np.round(1-x,3)) + " хи квадрат критический равен " + 
						str(self.xi[-1])]
				var = "принимается" if self.xi[-1] > self.K else "отвергается"
				lines += ["Гипотеза о норматьном распределении " + var]
				if var == "принимается":
					break
			lines += ["5) см изображения в текущей папке"]
			lines += ["6) см файл CorrelationTable.csv"]
			lines += ["7) Коэффициент кореляции " + str(self.CorrelationCoef)]
			lines += ["8) Уравнение регрессии: y = ax + b"]
			lines += ["a " + str(self.a)]
			lines += ["b " + str(self.b)]
			lines = [ x + "\n" for x in lines ]
			out.writelines(lines)

	def plot(self):

		
		plt.rcParams["figure.figsize"] = FIG_DIMS
		if self.partA:

			# Emperic distribution fun
			plt.step(self.xAccum, self.yAccum)
			plt.title("Эмпирическая функция расперделения")
			#plt.show()
			plt.savefig(os.path.join(self.dirname,EmpericDistributionFunName),dpi=DPI)
			plt.clf()

			# Gistogram for X var
			plt.bar(self.x,self.y,width=self.h)
			plt.xticks(self.x)
			plt.yticks(np.arange(min(self.y),max(self.y)+1,1.0))
			plt.grid(axis='y')
			plt.title("Гисторамма")
			#plt.hist(rangeSample,bins=len_+1)
			#plt.show()
			#figure = plt.gcf()

			#figure.set_size_inches(10, 6)
			plt.savefig(os.path.join(self.dirname,HistName),dpi=DPI)
			plt.clf()

			# Poligon for X var
			plt.plot(self.x,self.y)
			plt.xticks(self.x)
			plt.yticks(np.arange(min(self.y),max(self.y)+1,1.0))
			plt.grid(axis='y')
			plt.title("Полигон")
			#plt.show()
			plt.savefig(os.path.join(self.dirname,PoligonName),dpi=DPI)
			plt.clf()

		if self.partB:
			# Scatter XY
			plt.scatter(*zip(*[(x[1],x[2]) for x in self.range_]),label='Элементы выборки')
			plt.plot(range(self.min_,self.max_+1),[self.a * x +self.b for x in range(self.min_,self.max_+1)]
				,'r',label='Прямая регрессии y = {0}x + ({1})'.format(np.round(self.a,3),np.round(self.b,3) ))
			plt.title("Кореляционное облако")
			plt.legend()
			#plt.show()
			plt.savefig(os.path.join(self.dirname,CorrelationName),dpi=DPI)
			plt.clf()
def main():
	pass
	#s = StatisticSolver()
	#s.plot()

if __name__ == '__main__':
	main()