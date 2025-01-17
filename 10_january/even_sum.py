#even num sum

n = int(input("Enter the Number :"))

if (n < 0):
	("Enter the valid Number :")
else:
	sum = 0
	while (n >0):
		sum += n
		n -= 2
	print("This is sum of the :", sum)