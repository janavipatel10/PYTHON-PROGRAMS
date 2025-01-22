numbers = input("Enter numbers separated by spaces: ").split()
for num in numbers:
    if int(num) % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")
