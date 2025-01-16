#perfect number

x = int(input("enter a number you want to check : "))
sum = 0

for i in range(1, x):

		if x % i == 0:
			sum += i
if sum == x:
	print("Perfect number : ")
	print("Your sum is = ", sum)
else:
	print("Not perfect number : ")
	print("Your sum is = ", sum)

