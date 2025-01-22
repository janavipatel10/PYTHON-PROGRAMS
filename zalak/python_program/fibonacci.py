x = int(input("enter the number for fibonacci series : ")) 
a = 0
b = 1
n_num = a
counter = 1

while counter <= x:
	print(n_num, end="\n")
	counter += 1
	a, b = b, n_num		
	n_num = a + b


