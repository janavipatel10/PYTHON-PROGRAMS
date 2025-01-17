"""
Write a Python program that takes an integer n as input and prints whether the 
number is Armstrong number or not. An Armstrong number (also known as a 
narcissistic number) is a number that is equal to the sum of its own digits
raised to the power of the number of digits. For example:

153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153.
370 is an Armstrong number because 3^3 + 7^3 + 0^3 = 370."""


x = int(input("Enter the number :"))

sum_of_len = len(str(x))
powr = 0

if x > 0:
	for i in str(x):
		powr += int(i) ** sum_of_len
	print(powr)

	if powr == x:
		print("armstrong", x)
	else:
		print("not armstrong number :", x)
else:
	print("This is not armstrong :", x)
