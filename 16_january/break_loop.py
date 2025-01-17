#break with loop

i = 0
a = "Helloworld"

while i < len(a):
	if a[i] == "o" or a[i] == "l":
		i += 1
		break

	print(a[i])
	i += 1