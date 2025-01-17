#check the year is leap year

year = int(input("Enter the Year :"))

if (year % 4 == 0) and (year % 100 != 0):
	print("leap year :", year)
elif(year % 400 == 0) and (year % 100 == 0):
	print("leap year :", year)
else:
	print("Not leap year :",year)