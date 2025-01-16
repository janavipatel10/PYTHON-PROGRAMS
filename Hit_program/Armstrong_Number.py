#Armstrong Number
#digit**

num = int(input("Enter number, you want to check armstrong number : "))

total_number_of_digit = len(str(num))

sum_of_power = 0

temp = num

while temp > 0:
	digit = temp % 10
	sum_of_power += digit ** total_number_of_digit
	temp //= 10

if num == sum_of_power:
	print("that number is Armstrong number")

else:
	print("that is not Armstrong number")




# 123
# total_number_of_digit = 3
# temp = 123
# yes 
# digit = 3
# sum_of_power = 27
# tem = 12