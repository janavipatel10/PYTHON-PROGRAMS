# pet managemen
name = (input(" ----> type of the pet: "))

print("\n------ type of food ------")
print("     dry food   ")
print("     wet food   \n")

food_type = input(" select food for your pet: ")
	
if food_type == "dry food":
	print(f"-->   the {name} fed dry food \n")
elif food_type == "wet food":
	print(f"-->   the {name} fed wet food \n")
else:
	print(f"-->   {name} fed other food \n")
	break

print("-----pet care service-----\n")
print("1--->dog walking")
print("2--->pet sitting")
print("3--->grooming")
print("4--->training")

total_service = 0
total_price = 0

print("--- dog walking ---")
print("1. get 1 service")

walk = int(nput("enter number you get service: "))
match walk:
	case 1:
		print(f"you get 1 service\n price:-100\n")
		total_service += 1
		total_price += 100
			
print("--- pet sitting ---")
print("1. get 1 service")

sit = int(input("enter number you get service:"))
match sit:
	case 1:
		print(f"you get 1 service\n price:-200\n")
		total_service += 1
		total_price += 200
	
print("--- grooming ---")
print("1. get 1 service")

groom = int(input("Enter number you get service: "))
match groom: 
	case 1:
		print(f"you get 1 service\n price:- 1000")
		total_service += 1
		total_price += 1000

print("--- training --- ")
print("1. get 1 service")

train = int(nput("enter number you get service: "))
match train:
	case 1:
		print(f"you get 1 service\n price:- 5000")
		total_service += 1
		total_price += 5000
print("Total service: ",total_service)
print("Total price: " total_price)

print("------ cloths ------")
print("1---->jeckat")
print("2---->shirt")
print("3---->t-shirt\n\n")

total_cloths = 0
total_price = 0 

print("1---->jeckat")
print("1. Buy 1 jeckat")
print("2. Buy 1+ jeckat\n")

jeck = int(input("Enter number you buy jeckat:  "))
match jeck:
	case 1:
		print("--->You buy a 1 jeckat\n price:-899", end = "\n\n")
		total_cloths += 1
		total_price += 899

	case 2:
		x = int(input("how many jeckat you buy ?: "))
		print(f"--->you buy {x} jeckat\n price {x * 899}\n")
		total_cloths += x
		total_price += x * 899

print("2---->shirt")
print("1. Buy 1 shirt")
print("2. Buy 1+ shirt\n")

shirt = int(input("Enter number you buy shirt:  "))
match shirt:
	case 1:
		print("--->You buy a 1 shirt\n price:- 399", end = "\n\n")
		total_cloths += 1
		total_price += 399 

	case 2:
		y = int(input("how many shirt you buy ?: "))
		print(f"--->you buy {y} shirt\n price {y * 399}\n")
		total_cloths += y
		total_price += y * 399

print("3---->t-shirt")
print("1. Buy 1 t-shirt")
print("2. Buy 1+ t-shirt\n")

t_shirt = int(input("Enter number you buy t-shirt: "))
match t_shirt:
	case 1:
		print("--->You buy a 1 t-shirt\n price:- 199", end = "\n\n")
		total_cloths += 1
		total_price += 199

	case 2:
		z = int(input("how many t-shirt you buy ?: "))
		print(f"--->you buy {z} t-shirt\n price {z * 199}\n")
		total_cloths += z
		total_price += z * 199

print("Total cloths is:", total_cloths)	
print("Total price is ", total_price , end = "\n\n")


print("------ aessasory ------")
print("   belt")
print("   blancket")
print("   food bowl")
print("   nail clipper")
print("   other\n")

print("1---->belt")
print("1. Buy 1 belt")
print("2. Buy 1+ belt\n")

total_aessasory = 0
total_price = 0

belt = int(input("Enter number you buy belt: "))
match belt:
	case 1:
		print("--->you buy 1 belt\n price:- 700\n\n")
		total_aessasory += 1
		total_price += 700
	case 2:
		a = int(input("how many belt you buy?: "))
		print(f"--->you buy {belt} belt\n price {a * 700}\n")
		total_aessasory += a
		total_price +=  a * 700

print("----blancket")
print("1. Buy 1 blancket")
print("2. Buy 1+ blancket\n")

blancket = int(input("Enter number you buy blancket: "))
match blancket:
	case 1:
		print(f"--->You buy 1 blancket\n price :- 500\n\n")
		total_aessasory += 1
		total_price += 500
	case 2:
		b = int(input("how many blancket you buy?: "))
		print(f"--->you buy {blancket} blancket\n price {b * 500}\n")
		total_aessasory += b
		total_price += b * 500 

print("----food bowl")
print("1. Buy 1 food bowl")
print("2. Buy 1+ food bowl\n")

bowl = int(input(f"Enter number you buy food bowl: "))	
match bowl:
	case 1:
		print(f"--->you buy 1 food bowl\n price:- 100\n\n")
		total_aessasory += 1
		total_price += 100
	case 2:
		c = int(input("how many food bowl you buy ?: "))
		print(f"---> you buy {bowl} bowl\n price {c * 100}\n")
		total_aessasory += c
		total_price += c * 100   

print("---nail clipper")
print("1. Buy 1 nail clipper")
print("2. Buy 1+ nail clipper\n")		

nail = int(input("Enter number you buy nail clipper: "))
match nail:
	case 1:
		print(f"--->you buy 1 nail clipper\n price:- 70\n\n")
		total_aessasory += 1
		total_price += 70
	case 2:
		d = int(input("how many nail clipper you buy? :"))
		print(f"--->you buy {nail} nail clipper\n price {d * 70}\n")
		total_aessasory += d
		total_price += d * 70

print("------ Other aessasory-----\n")	
other = input("Do you want to buy other aessasory? (yes/no)? : ").lower()
if other == "yes":
	e = input(f"name of you want to buy aessasory: ")
	f = int(input(f" How many {e} you buy?: "))
	price = float(input(f" what is the price of 1 {e}: "))
	print(f"---->you buy {f} {e} \n price:- {f * price}\n")
	total_aessasory += f
	total_price += f * price
else:
	print(f"no other aessasory selectd.\n")

print("Total aessasory: ",total_aessasory)
print("total price: ",total_price, end = " \n\n")

# medical section
print("------PET CARE ------\n\n")
print("---> appoinment")
import re
name = input("---->name of the pet : ")
age = float(input("--->age of pet: "))
illness = input("--->illness of pet: ")
gender = input("--->gender of pet: ")
mobil_num = (input("--->Enter your mobile number: "))
pattern = r'^\d{10}$'
if re.match(pattern, mobil_num):
	print("valid  mobile number\n")
else:
	print("invalid  mobile number")
	mobil_num = input(f"--->please re-enter your 10 digit mobile number: ")
	if not re.match(pattern, mobil_num):
		print("invalid  mobile number")
		
email = input("--->enter your e-mail: ")
pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
if re.match(pattern, email):
	print("vaild e-mail")
else:
	print("invalid e-mail")	
	email = input(f"--->please re-enter your e-mail :")
	if re.match(pattern, email):
		print("valid e-mail")
