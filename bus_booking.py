class Bus:
	def __init__(self, bus_number, bus_place, total_seats, ticket_price):
		self.bus_number = bus_number
		self.bus_place = bus_place
		self.total_seats = total_seats
		self.available_seats = total_seats
		self.ticket_price = ticket_price

	def show_details(self):
		print(f"Bus number : {self.bus_number} , Bus name : {self.bus_place} ---- total available seat : {self.available_seats} ---- Ticket price : {self.ticket_price}")

	def update_available_seats(self, num_seats):
		self.available_seats -= num_seats

class User:
	def __init__(self, name, email, phone_num):
		self.name = name
		self.email = email
		self.phone_num = phone_num
		self.bookings = []

	def book_ticket(self, bus, num_seats):
		if bus.available_seats >= num_seats:
			bus.available_seats -= num_seats
			total_cost = num_seats * bus.ticket_price
			self.bookings.append((bus, num_seats,total_cost))
			print(f"Booking successful!! {num_seats} is book for {bus.bus_number}. --- Total price : ₹{total_cost}")
		else:
			print("Not available for this bus seats")

def display_bus_and_book(bus, user):
	print("\nAvailable Bus")
	bus.show_details()

	try:
		num_seats = int(input(f"Enter the book bus number {bus.bus_number}:"))
		user.book_ticket(bus, num_seats)

	except ValueError:
		print("Enter the valid number. This is not valid input.")

def main_menu():
	bus = Bus(111, "kashmir", 40, 10000)
	users = []

	print("WELCOME TO THE OUR BUS BOOKING SYSTEM!")
	while True:
		name = input("Enter your name ---> ")
		email = input("Enter your email ---> ")
		phone_num = input("Enter your phone_num ---> ")	

		user = User(name, email, phone_num)

		while True:
			print("\n---> Main Menu <---")
			print("1---> View Available Bus")
			print("2---> Book Ticket")
			print("3---> Exit")

			choice = input("\nEnter your choice :")

			if choice == "1":
				bus.show_details()
			elif choice == "2":
				display_bus_and_book(bus, user)
			elif choice == "3":
				print("Thank you for using the Bus Booking System!!")
				break
			else:
				print("Enter valid number choice")

		continue_choice = input("Do you want to add another user? (y/n): ")
		if continue_choice.lower() != "y":
			break


main_menu()