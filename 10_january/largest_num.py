#Largest number of 3 number

x = int(input("Enter the Number in x:"))
y = int(input("Enter the Number in y :"))
z = int(input("Enter the Number in z :"))


if (x >= y) and (x >= z):
	print(x)
elif (y >= z) and (y >= x):
	print(y)
else:
	print(z)