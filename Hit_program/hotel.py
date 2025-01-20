#Hotel Management System

x = "Hello, Welcome To My Hotel : AMIDHARA"
y = 90
z = x.center(y)
print(z)

print("1. Reservation - ")
print("2. Room Management - ")
print("3. Empty and Full Room - ")
print("4. Room service - ")
print("5. Restaurant - ")
print("6. Billing - ")
print("7. Pyment Method - ")
print("8. Guest Record - ", end = "\n\n")

choice = int(input("Enter your choice :- "))

match choice:
	case 1 :

		print("Your Select Option is :- Reservation ", end = "\n\n")
		print("Room Type")
		print("1. AC Room")
		print("2. Non - AC Room", end = "\n\n")
		room_price = int(input("What do you want  shaw room price ? "))

		match room_price:
				
			case 1:
				print("price =  1. AC Room :- 2000(1 day)")
				print("price =  2. Non - AC Room :- 1700(1 day)", end = "\n\n")
			
		room_type = int(input("Plese Select Your Room Types :- "))
		
		match room_type:
			case 1 : 
				print("You are select a AC Room ", end = "\n\n")
			case 2 :
				print("You are select a Non - AC room ", end = "\n\n")

		class guest():
			Name = ""
			Age = ""
			Mobile_num = ""
			Email_add = ""
			Goverment_id_proof_num = ""

			def __init__(self, Name, Age, Mobile_num, Email_add, Goverment_id_proof_num):
				self.Name = Name
				self.Age = Age
				self.Mobile_num = Mobile_num
				self.Email_add = Email_add
				self.Goverment_id_proof_num = Goverment_id_proof_num

			def get_details(self):
				return f"Name : {self.Name}\nAge : {self.Age}\nMobile_num : {self.Mobile_num}\nEmail_add : {self.Email_add}\nGoverment_id_proof_num : {self.Goverment_id_proof_num}"

		Name = input("\nEnter Your Name : ")
		Age = input("Enter Your Age : ")
		Mobile_num = input("Enter Your Mobile_num : ")
		Email_add = input("Enter Your Email_add : ")
		Goverment_id_proof_num = input("Enter Your Goverment_id_proof_num : ")


		guest_detail = guest(Name, Age, Mobile_num, Email_add, Goverment_id_proof_num)
		print("\nGuest details :- ")
		print(guest_detail.get_details())

		
