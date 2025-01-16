#Multiplication Table

n = int(input("enter number, you want to creat multiplication table : "))
counter = 1

while counter <= 10:
	mul = n * counter
	print(f"{n} * {counter} = {mul}") 
	counter = counter + 1
	


# for i in range(1, 11):
#  print(f"{n} * {i} = {n * i}")