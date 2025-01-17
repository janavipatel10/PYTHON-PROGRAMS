#while True

total = 0

while True:
    num = int(input("Enter a number (or 0 to exit): "))

    if num == 0:
        break
    total += num

print("Total:", total)
