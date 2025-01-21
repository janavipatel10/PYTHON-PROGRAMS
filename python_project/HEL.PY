class PetHealth:
    def __init__(self, pet_name, pet_type):
        self.pet_name = pet_name
        self.pet_type = pet_type
        self.appointments = []

    def schedule_appointment(self, illness, doctor_type, treatment):
        appointment = {
            "Illness": illness,
            "Doctor Type": doctor_type,
            "Treatment": treatment
        }
        self.appointments.append(appointment)
        print(f"Appointment scheduled for {self.pet_name} with {doctor_type} for {illness}.")

    def display_appointments(self):
        if not self.appointments:
            print("No appointments scheduled.")
            return
        print(f"Appointments for {self.pet_name}:")
        for i, appointment in enumerate(self.appointments, 1):
            print(f"Appointment {i}:")
            for key, value in appointment.items():
                print(f"{key}: {value}")
    
    def get_doctor_type(self, illness):
        # Determine the type of doctor based on illness
        specialist_doctors = {
            "Heart problems": "Cardiologist",
            "Skin issues": "Dermatologist",
            "Eye problems": "Ophthalmologist",
            "Cancer": "Oncologist",
            "Joint problems": "Orthopedic Specialist",
            "Brain issues": "Neurologist",
            "General health": "Veterinarian"
        }
        return specialist_doctors.get(illness, "Veterinarian")  # Default to Veterinarian if no match
    
    def determine_treatment(self, illness):
        # Determine the type of treatment based on the illness
        treatments = {
            "Infection": "Medicine",
            "Fracture": "Surgery and Orthopedic Care",
            "Arthritis": "Orthopedic Care and Medication",
            "Skin allergies": "Medication",
            "Trauma": "Emergency Care and Surgery",
            "Respiratory issue": "Medicine and Emergency Care"
        }
        return treatments.get(illness, "General Care and Medicine")  # Default to general care

# Example usage
if __name__ == "__main__":
    # Create a pet instance
    my_pet = PetHealth("Buddy", "Dog")

    # Simulate illness and scheduling appointment
    illness = "Arthritis"
    doctor_type = my_pet.get_doctor_type(illness)
    treatment = my_pet.determine_treatment(illness)

    # Schedule appointment
    my_pet.schedule_appointment(illness, doctor_type, treatment)

    # Display all appointments
    my_pet.display_appointments()

    # Another example of scheduling an emergency appointment
    emergency_illness = "Trauma"
    emergency_doctor_type = my_pet.get_doctor_type(emergency_illness)
    emergency_treatment = my_pet.determine_treatment(emergency_illness)
    
    my_pet.schedule_appointment(emergency_illness, emergency_doctor_type, emergency_treatment)
    my_pet.display_appointments()
