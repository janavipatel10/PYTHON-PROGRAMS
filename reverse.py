#Python program that accepts a word from the user and reverses it.

give_string = input("Enter the string :")
reverse_string = ""

for i in give_string:
	reverse_string = i + reverse_string

print(reverse_string)