"""Write a Python program that takes a string s as input
and counts the number of vowels (a, e, i, o, u) in the string. 
The program should be case-insensitive, meaning it should count
both uppercase and lowercase vowels."""

vowels = ("a","e","i","o","u","A","I","O","U")
count = 0

x = input("Enter the string :")

for i in x:
	if i in vowels:
		print(i)
		count += 1

print(count)