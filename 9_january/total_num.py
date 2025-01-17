#Python program to count the total number of digits in a number.
#total char, space, word

num = input("Enter the Number : ")

count = 0
for i in num:
	count += 1

print(f"The total Number is : {count}")