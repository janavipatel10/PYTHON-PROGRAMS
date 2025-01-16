#pelindrom number

n = input("enter number you want to check : ")

if n == n[::-1]:
	print("pelindrom number")
else:
	print("not pelindrom number")