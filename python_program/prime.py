num = int(input("enter the number:")) 

if num > 1:

    flag = False
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break

    if flag:
        print("number is not prime")
    else:
        print("number is prime")

num = 5
flag = False
range(2, 10) => [2,3,4]


I#1
i = 2, num = 5

I#2
i = 3, num = 5

I#3
i = 4, num = 5

I#4
i = 3, num = 5


0
flag = True

# I#2
# i = 3
# 1 - not prime

