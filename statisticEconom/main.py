from sample import genSample
from plotting import StatisticSolver
import shutil
import os

def main():
	birthdays = [[22,8],[17,7],[6,7]]
	for birthday in birthdays: 
		dirname = str(birthday[0]) + "." + str(birthday[1])
		sampleFile = os.path.join(dirname,"Sample.csv")
		os.makedirs(dirname, exist_ok=True)
		genSample(birthday=birthday,dirname=dirname )
		ss = StatisticSolver(dirname= dirname,inputFile=sampleFile)
		ss.plot()
		ss.putStatistic("Текс.txt",birthday)
		shutil.make_archive(dirname , 'zip', dirname)


if __name__ == '__main__':
	main()