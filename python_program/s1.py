n = int(input("Enter the number of terms in the Fibonacci sequence: "))

# Initializing the first two terms
a, b = 0, 1

# Generating Fibonacci sequence
print("Fibonacci sequence:")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b