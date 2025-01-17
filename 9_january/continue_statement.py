number = 25

for i in range(1, number + 1):
	if i % 4 == 0 and i % 5 == 0:
		print("Diveded by 4 and 5")
		continue

	if i % 4 == 0 and i % 5 != 0:
		print("Diveded by 4")
		continue

	if i % 5 == 0 and i % 4 != 0:
		print("Diveded by 5")

	else:
		print(i)
		