#sum of digits
x = input("enter a number : ")

y = sum(int(i) for i in str(x))
print(y)