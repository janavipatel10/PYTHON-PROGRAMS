rows = int(input("Enter number of rows: "))

k = 0

for i in range(1, rows+1):
	print(f'loop ---->{i}')
	for j in range(1, (rows-i)+1):
		print(f'loop ---->{j}row:{(rows-i)+1}')
		print(end="  ")

	while k!=(2*i-1):
		print("* ", end="")
		k += 1
	k = 0
	print(end="\n")





    # 5
    # i =1
    # space = 1
    # *
