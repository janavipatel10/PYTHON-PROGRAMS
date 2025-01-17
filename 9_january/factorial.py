#factorial number

number = int(input("Enter the Number :"))
fact = 1

for i in range(1, number +1 ):
	fact = fact * i

print("The factorial is", fact)