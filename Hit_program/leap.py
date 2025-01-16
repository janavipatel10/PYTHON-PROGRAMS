#Leap Year

year = int(input("enter year, you want to check leap year: "))

if year%4 == 0 and year%100 != 0:
	print("leap year")

elif year%400 == 0 and year%100 == 0:
	print("leap year")
	
else:
	print("not leap year")





# year = int(input("enter year: "))

# if year%4 == 0:
# 	print("leap year")

# elif year%400 == 0:
# 	print("leap year")

# else:
# 	print("not leap year")
# e
	# 