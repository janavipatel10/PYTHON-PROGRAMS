febonacci

x = int(input("enter a number, you want to fabonacci series:"))
n1 = 0
n2 = 1
n_num = n1
count = 1

while count <= x:
	print(n_num, end=" ")
	count += 1
	n1, n2 = n2, n_num
	n_num = n1 + n2
	
print(end="\n")