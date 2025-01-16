#find even odd number in list

a = list(map(int, input("enter a number of stirng : ").split()))


for val in a:
	if val % 2 == 0:
		print("even number : ", val)

	else:
		print("odd number : ", val)