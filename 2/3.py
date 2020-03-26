# Дано кол-во партий
# Забастовки длятся ровно 1 день
# Каждая партия может бастовать
# Вводится кол-во дней 
# кол - во партий 
# Вводятся день первой забастовки и период ( через сколько дней она повторится)
# первый день всегда понедельний
# суббота - воскресение выходной
# вывести буднии дни, в которые была забастовка

days = int(input("Кол-во дней "))
partiesCount = int(input("Кол-во партий "))
workdays = { x for x in range(1,days+1) if  not (x % 7) in (0,6)  }
stackDays = set()
for partiNum in range(partiesCount):
	firstStackDay = int(input("Первая дата забастовки "))
	periodStack = int(input("Период забастовки "))
	stackDays = stackDays | {x for x in range(firstStackDay,days,periodStack)}
print("Рабочие дни, в которые была забастовка ", stackDays & workdays ) 
