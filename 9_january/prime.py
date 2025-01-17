#prime number

def prime_num(n):

    if n < 2:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = int(input("Enter number : "))

if prime_num(n):
    print(n, "is prime")
else:
    print(n, "is not prime")    