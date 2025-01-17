# Bank FD
while True:

	print("Banks of your choice for FD :", end = "\n\n")
	print("BANK NAME : ")
	print("1. Suryoday", end = "\n")
	print("2. North East", end = "\n")
	print("3. Shivalik", end = "\n")
	print("4. Utkarsh", end = "\n\n")
	print("0. Exit")


	choice = int(input("Enter your preferred bank for FD : "))
	if choice == 0:
		print("Exiting the program...")
		break

	match choice:
		case 1:
			print("Your selected bank is :- Suryoday", end = "\n\n")
			print("1. Suryoday - 7D - 4%")
			print("2. Suryoday - 6M 1D - 7.25%")
			print("3. Suryoday - 2Y 3M - 8.60%")
			print("4. Suryoday - 5Y - 8.25%", end = "\n\n")
			
			tenure_choice = int(input("Enter your choice : "))

			if tenure_choice == 0:
				continue
			
			match tenure_choice:
				case 1:
					rate = 4
					day = 7 / 365
					amount = int(input("Enter Your amount : "))
					print(end = "\n\n" )
					intam = amount * rate * day / 100
					return_am = intam + amount
					print("Your interest amount is : ", round(intam, 2))
					print("Your return amount is : ", round(return_am, 2))
				case 2:
					rate = 7.25
					day = 181 / 365
					amount = int(input("Enter Your amount : "))
					print(end = "\n\n" )
					intam = amount * rate * day / 100
					return_am = intam + amount
					print("Your interest amount is : ", round(intam, 2))
					print("Your return amount is : ", round(return_am, 2))
				case 3:
					rate = 8.60
					day = 820 / 365
					amount = int(input("Enter Your amount : "))
					print(end = "\n\n" )
					intam = amount * rate * day / 100
					return_am = intam + amount
					print("Your interest amount is : ", round(intam, 2))
					print("Your return amount is : ", round(return_am, 2))

				case 4:
					rate = 8.25
					day = 1825 / 365
					amount = int(input("Enter Your amount : "))
					print(end = "\n\n" )
					intam = amount * rate * day / 100
					return_am = intam + amount
					print("Your interest amount is : ", round(intam, 2))
					print("Your return amount is : ", round(return_am, 2))
				case default:
					print("wrong choice. ")



		case 2:
			print("Your selected bank is :- North East", end = "\n\n")
			print("1. North East - 1Y 5M - 8.75%")
			print("2. North East - 3Y - 9%", end = "\n\n")
			
			tenure_choice = int(input("Enter your choice : "))

			if tenure_choice == 0:
				continue
			
			match tenure_choice:
				case 1:
					rate = 8.75
					day = 506 / 365
					amount = int(input("Enter Your amount : "))
					print(end = "\n\n" )
					intam = amount * rate * day / 100
					return_am = intam + amount
					print("Your interest amount is : ", round(intam, 2))
					print("Your return amount is : ", round(return_am, 2))
				case 2:
					rate = 9
					day = 1095 / 365
					amount = int(input("Enter Your amount : "))
					print(end = "\n\n" )
					intam = amount * rate * day / 100
					return_am = intam + amount
					print("Your interest amount is : ", round(intam, 2))
					print("Your return amount is : ", round(return_am, 2))
				case default:
					print("wrong choice. ")
				

		case 3:
			print("Your selected bank is :- Shivalik", end = "\n\n")
			print("1. Shivalik - 1Y 6M - 8.30%", end = "\n\n")

			tenure_choice = int(input("Enter your choice : "))

			if tenure_choice == 0:
				continue

			match tenure_choice:
				case 1:
					rate = 8.30
					day = 545 / 365
					amount = int(input("Enter Your amount : "))
					print(end = "\n\n" )
					intam = amount * rate * day / 100
					return_am = intam + amount
					print("Your interest amount is : ", round(intam, 2))
					print("Your return amount is : ", round(return_am, 2))
				case default:
					print("wrong choice. ")
					
						

		case 4:
			print("Your selected bank is :- Utkarsh", end = "\n\n")
			print("1. Utkarsh - 4Y 40D - 8.50%", end = "\n\n")

			tenure_choice = int(input("Enter your choice : "))
			
			if tenure_choice == 0:
				continue

			match tenure_choice:
				case 1:
					rate = 8.50
					day = 1500 / 365
					amount = int(input("Enter Your amount : "))
					print(end = "\n\n" )
					intam = amount * rate * day / 100
					return_am = intam + amount
					print("Your interest amount is : ", round(intam, 2))
					print("Your return amount is : ", round(return_am, 2))
				case default:
					print("wrong choice. ")
		
		case default:
			print("Your bank choice is wrong.")
			


