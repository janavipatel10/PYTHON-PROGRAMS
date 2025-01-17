#used to filter function

a = [33, 55, 12, 66, 43]

def num(x):
	b = [44, 66, 23, 43]
	if (x in b):
		return True
	else:
		return False

filtered = filter(num, a)
for element in filtered:
	print(element)