def is_leap_year(year):
	# if year%4 == 0 and year%100 != 0 or year%400 ==0:
	# 	return True
	# else:
	# 	return False
 #上面的代码可以改写为以下代码:
 	return year % 4 == 0 and year % 100 != 0 or year % 400 ==0
def get_day(year,month,date):
	days = 0
	if month == 1:
		return date
	elif month <= 2:
		return 31+date
	elif month <= 12:
		lis_1 = [1,3,5,7,8,10,12]
		lis_2 = [4,6,9,11]
		lis_3 = [2]
		lis = [x for x in range(1,month)]
		for month in lis:
			if month in lis_1:
				days += 31
			elif month in lis_2:
				days += 30
			elif month in lis_3 and is_leap_year(year):
				days += 29
			elif month in lis_3 and not is_leap_year(year):
				days += 28
	return days +date
print(get_day(2019,5,26))