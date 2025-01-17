#Python program to check if the given string is a palindrome.

give_string = input("Enter the string value : ")
reverse_string = give_string[::-1]

if(give_string == reverse_string):
	print("This is a",give_string, "Palindrome")
else:
	print("This is not",give_string, "Palindrome")