#Hotel Management System
print(end = "\n\n")
x = "Hello, Welcome To My Hotel : AMIDHARA"
y = 90
z = x.center(y)
print(z)

total_ac_rooms_large = 25
total_ac_rooms_small = 25
total_ac_room = 50
ac_room_large_available = total_ac_rooms_large
ac_room_small_available = total_ac_rooms_small
total_non_ac_rooms_large = 25
total_non_ac_rooms_small = 25
total_non_ac_room = 50
non_ac_room_large_available = total_non_ac_rooms_large
non_ac_room_small_available = total_non_ac_rooms_small

total_num_room_booked = 0
ac_room_large_booked = 0
ac_room_small_booked = 0
non_ac_room_large_booked = 0
non_ac_room_small_booked = 0


User_id_counter = 1 
reservations = {}
guest_details = {}

while True:

	print("\n1. Reservation - \n2. Empty and Full Room - \n3. Room service - \n4. Restaurant - \n5. Billing - \n6. Pyment Method - \n7. Guest Record - ", end = "\n\n")

	choice = int(input("Enter your choice :- "))

	match choice:
		case 1 :

			print("Your Select Option is :- Reservation\nRoom Type\n1. AC Room Small Size\n2. AC Room Large Size\n3. Non - AC Room Small Size\n4. Non - AC Room Large Size", end = "\n\n")
		
			room_price = int(input("What do you want  shaw room price ? (click 1)"))

			match room_price:
					
				case 1:
					print("price =  1. AC Room Small Size :- 2000(1 day)\nprice =  2. AC Room Large Size :- 3000(1 day)\nprice =  3. Non - AC Room Small Size :- 1500(1 day)\nprice =  4. Non - AC Room Large Size :- 2200", end = "\n\n")
				
			room_type = int(input("Plese Select Your Room Types :- "))
			
			match room_type:

				case 1 : 
					if ac_room_large_available > 0:
						ac_room_large_available -= 1
						ac_room_large_booked += 1
						total_num_room_booked += 1
						room_reserved = True
						print("You have selected an Large Size AC Room.\n")
						print(f"Remaining Large Size AC Rooms: {ac_room_large_available}")
						print(f"Total AC Room Booked : {ac_room_large_booked}")

					else:
						print("Sorry, the Large Size AC Room is not available.\n")
				case 2 : 
					if ac_room_small_available > 0:
						ac_room_small_available -= 1
						ac_room_small_booked += 1
						total_num_room_booked += 1
						room_reserved = True
						print("You have selected an Large Size AC Room.\n")
						print(f"Remaining Small Size AC Rooms: {ac_room_small_available}")
						print(f"Total AC Room Booked : {ac_room_small_booked}")

					else:
						print("Sorry, the Small Size AC Room is not available.\n")
				case 3 :
					if non_ac_room_large_available > 0:
						non_ac_room_large_available -= 1
						non_ac_room_large_booked += 1
						total_num_room_booked += 1
						room_reserved = True
						print("You have selected a Large Size Non-AC Room.\n")
						print(f"Remaining Large Size Non-AC Rooms: {non_ac_room_large_available}")
						print(f"Total Non-AC Rooms Booked : {non_ac_room_large_booked} ")
					else:
						print("Sorry, the Large Non-AC Room is not available.\n")
				case 4 :
					if non_ac_room_small_available > 0:
						non_ac_room_small_available -= 1
						non_ac_room_small_booked += 1
						total_num_room_booked += 1
						room_reserved = True
						print("You have selected a Small Size Non-AC Room.\n")
						print(f"Remaining Small Size Non-AC Rooms: {non_ac_room_small_available}")
						print(f"Total Non-AC Rooms Booked : {non_ac_room_small_booked} ")
					else:
						print("Sorry, the Small Size Non-AC Room is not available.\n")


			class guest():
				Name = ""
				User_id = 0
				Age = ""
				Mobile_num = ""
				Email_add = ""
				Goverment_id_proof_num = ""


				def __init__(self, Name, User_id, Age, Mobile_num, Email_add, Goverment_id_proof_num):
					self.Name = Name
					self.User_id = User_id
					self.Age = Age
					self.Mobile_num = Mobile_num
					self.Email_add = Email_add
					self.Goverment_id_proof_num = Goverment_id_proof_num

				def get_details(self):
					return f"Name : {self.Name}\nUser_id : {self.User_id}\nAge : {self.Age}\nMobile_num : {self.Mobile_num}\nEmail_add : {self.Email_add}\nGoverment_id_proof_num : {self.Goverment_id_proof_num}"
			if room_reserved:
				Name = input("\nEnter Your Name : ")
				User_id = int(input("Enter User id : "))
				User_id = User_id_counter
				User_id_counter += 1 
				while True:
					Age = input("Enter Your Age : ")
					if Age.isdigit():
						break
					else:
						print("Invalid Age")
				while True:
					Mobile_num = input("Enter Your Mobile_num : ")
					if len(Mobile_num) == 10 and Mobile_num.isdigit():
						break
					else:
						print("Invalid Mobile Number")
				while True:
					Email_add = input("Enter Your Email_add : ")
					if "@" in Email_add and "." in Email_add:
						break
					else:
						print("Invalid Email Address")	
				while True:
					Goverment_id_proof_num = input("Enter Your Goverment_id_proof_num : ")
					if Goverment_id_proof_num.isdigit():
						break
					else:
						print("Invalid Goverment_id_proof_num")

				guest_detail = guest(Name, User_id, Age, Mobile_num, Email_add, Goverment_id_proof_num)
				print("\nGuest details :- ")
				print(guest_detail.get_details())

				reservations[User_id_counter] = room_reserved
				guest_details[User_id_counter] = guest_detail


			
		case 2:
			print(f"Total Number of Large Size AC Room Booked :{ac_room_large_booked}\nTotal Number of Small Size AC Rooms Booked : {ac_room_small_booked}\nTotal Number of Large Size Non-AC Rooms Booked : {non_ac_room_large_booked}\nTotal Number of Small Size Non-AC Rooms Booked : {non_ac_room_small_booked}", end = "\n\n")
			print(f"\nTotal Nummber of Room Booked : {total_num_room_booked}")
		case 3:
			User_id = int(input("Enter Your User_id :"))
			print(end = "\n\n")
			if User_id in reservations and reservations[User_id]:
				print("Your Room Service Is Available.\n1. House Cleaning Service\n2. Eating Service\n3. Other Service")
			else:
				print("Sorry, Your Room Service Is Not Available.")

		case 7:
			print("\nBooked Room User Details")
			if reservations:
				for User_id, room_reserved in reservations.items():
					if room_reserved:
						guest = guest_details[User_id]
						if guest:
								print("\n" + guest.get_details())
			else:
				print("No Rooms have booked yet.")
	continue_choice = input("\nDo you want to  another service? (yes/no): ").strip().lower()
	if continue_choice != "yes":
		print("Thank you for using our service. Have a great day!")
		break 