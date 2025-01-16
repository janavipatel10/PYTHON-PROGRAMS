#Prime number

n = int(input("enter  a number : "))

if n <= 1:
	print("not prime number")

else:
	for i in range(2, n):
		if n % 2 == 0:
			print("not prime number")
			break
	else:
		print("prime nuber")

