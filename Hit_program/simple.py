# simple Interest


pri = int(input("enter amount: "))
rate = float(input("entre annual rate : "))
print("enter a time period : ")
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
 
time = year + (month / 12) + (day / 365)
si = pri * rate * time / 100
print(f"Simple Interest is : {round(si, 2)}")