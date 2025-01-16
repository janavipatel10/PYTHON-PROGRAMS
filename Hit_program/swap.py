# with temp variable
a = input("Enter a number / string A : ")
b = input("Enter a number / string B : ")

temp = a
a = b
b = temp

print(f"your number / string A : {a}")
print(f"your number / string B : {b}")


#withohut temp veriable
a = input("Enter a number / string A : ")
b = input("Enter a number / string B : ")

a, b = b, a

print(f"your number / string A : {a}")
print(f"your number / string B : {b}")

