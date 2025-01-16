# Sum of even number 

x = int(input("entre a number, you want to sum of even number : "))
sum = 0

for i in range(0, x):
	if i % 2 == 0:
		sum += i
		

print(sum)
