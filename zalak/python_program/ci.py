p = int(input("enter the principal amount: "))
r = float(input("enter the rat of intrest: "))
print("enter the time period: ")

year = int(input("year : "))
if year == 0:
	print("0")
else:
	print(year)

month = int(input("month : "))
if month == 0:
	print("0")

else:
	print(month)

day = int(input("day : "))

if day == 0:
	print("0")

else:
	print(day)

t = year + (month / 12) + (day / 365)

# def cal_intrest(p, r, t):
a = p * pow((1+ r / 100), t)
ci = a-p 
print(f"compound intrest is: {round(ci, 2)}")

# cal_intrest(p, r, t)
	
 