# pet managemen
name = (input(" ----> type of the pet: "))

print("-----PET CARE SERVICE-----\n")
print("1--->dog walking")
print("2--->pet sitting")
print("3--->grooming")
print("4--->training\n\n")

total_service = 0
total_price = 0

print("--- dog walking ---\n")
print("1. get 1 service")

walk = int(input("enter number you get service: "))
match walk:
	case 1:
		print(f"you get 1 service\n price:-100\n")
		total_service += 1
		total_price += 100
			
print("--- pet sitting ---")
print("1. get 1 service")

sit = int(input("enter number you get service: "))
match sit:
	case 1:
		print(f"you get 1 service\n price:-200")
		total_service += 1
		total_price += 200
	
print("\n--- grooming ---")
print("1. get 1 service")

groom = int(input("Enter number you get service: "))
match groom: 
	case 1:
		print(f"you get 1 service\n price:- 1000\n")
		total_service += 1
		total_price += 1000

print("--- training --- ")
print("1. get 1 service")

train = int(input("enter number you get service: "))
match train:
	case 1:
		print(f"you get 1 service\n price:- 5000\n")
		total_service += 1
		total_price += 5000

print("Total service: ",total_service)
print("Total price: ",	total_price)

print("----- PET CARE PRODUCT -----")
print("\n------ type of food ------")
print("1---->dry food   ")
print("2---->wet food   \n")

total_food = 0 
total_price = 0

print("1. Buy dry food")

dry_food = int(input(" select food for your pet: "))
match dry_food:
	case 1:
		print(f"{name} fed dry food\n price: 180\n")
		total_food += 1 
		total_price += 180

print("1. Buy wet food")

wet_food = int(input(" select food for your pet: "))
match wet_food:
	case 1:
		print(f"{name} fed wet food\n price:- 200")
		total_food += 1
		total_price += 200

print("Total food: ",total_food)
print("Total price: ",total_price)


print("\n\n------ cloths ------")
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
print("   other\n\n")

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

# PET HELTH SYSTEM
print("----PET HELTH SERVICE----")
class PetHealth:
	def __init__(self, pet_name, pet_type):
		self.pet_name = pet_name
		self.pet_type = pet_type
		self.appointments = []

def schedule_appointment(self, illness, doctor_type, treatment):
	appointment = {
		"Illness" : illness,
		"Doctor_type" : doctor_type,
		"Treatment" : treatment
	}		

self.appointments.append(appointment)
print(f"Appointment for {self.pet_name} with {doctor_type} for {illness}")

def display_appointments(self):
	if not self.appointments:
		print(f"no appointments")
		return
	print(f"Appointment for {self.pet_name}")
	for i, appointment in enumerate(self.appointments, 1)	
	print(f" Appointment {i} : {appointment}")

	