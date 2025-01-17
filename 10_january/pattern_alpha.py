#pattern of alphabat 

number = int(input("Enter the Number :"))

for i in range(1, number + 1):
	for j in range(1, i + 1):
		print(chr(64 + j), end = " ")
	print(" ")
