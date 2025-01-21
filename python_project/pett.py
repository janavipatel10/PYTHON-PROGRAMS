print("------ cloths ------")
print("1---->jeckat")
print("2---->shirt")
print("3---->t-shirt\n\n")

# Initialize counters for total clothes and total price
total_cloths = 0
total_price = 0

# Buying jackets
print("1---->jeckat")
print("1. Buy 1 jeckat")
print("2. Buy 1+ jeckat\n")

jeck = int(input("Enter number you buy jeckat:  "))
match jeck:
    case 1:
        print("--->You buy a 1 jeckat\n price:-899", end="\n\n")
        total_cloths += 1
        total_price += 899
    case 2:
        x = int(input("How many jeckat you buy ?: "))
        print(f"--->You buy {x} jeckat\n price {x * 899}\n")
        total_cloths += x
        total_price += x * 899

# Buying shirts
print("2---->shirt")
print("1. Buy 1 shirt")
print("2. Buy 1+ shirt\n")

shirt = int(input("Enter number you buy shirt:  "))
match shirt:
    case 1:
        print("--->You buy a 1 shirt\n price:- 399", end="\n\n")
        total_cloths += 1
        total_price += 399
    case 2:
        y = int(input("How many shirt you buy ?: "))
        print(f"--->You buy {y} shirt\n price {y * 399}\n")
        total_cloths += y
        total_price += y * 399

# Buying t-shirts
print("3---->t-shirt")
print("1. Buy 1 t-shirt")
print("2. Buy 1+ t-shirt\n")

t_shirt = int(input("Enter number you buy t-shirt: "))
match t_shirt:
    case 1:
        print("--->You buy a 1 t-shirt\n price:- 199", end="\n\n")
        total_cloths += 1
        total_price += 199  # Corrected here to add price to total_price
    case 2:
        z = int(input("How many t-shirt you buy ?: "))
        print(f"--->You buy {z} t-shirt\n price {z * 199}\n")
        total_cloths += z
        total_price += z * 199

# Print the total number of clothes and total price
print("Total cloths is:", total_cloths)    
print("Total price is ", total_price, end="\n\n")
