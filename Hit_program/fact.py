#Fectorial Number

fect = int(input("Enter number, you want factorial number : "))
count = 1

while fect > 1:
	count *= fect
	fect -= 1

print(f"The Factorial Number Is : {count}")
	

	