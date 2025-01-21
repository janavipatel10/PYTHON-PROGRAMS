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
        # Determine the doctor type based on illness
        if illness in ["Fracture", "Trauma", "Surgery"]:
            return "Surgeon"  # Surgeons handle surgeries
        elif illness in ["Cold", "Fever", "Infection"]:
            return "Veterinarian"  # General vet for common illnesses
        else:
            return "Animal Specialist"  # Default to animal specialist for other conditions
    
    def determine_treatment(self, illness):
        # Determine the treatment based on the illness
        if illness in ["Cold", "Fever", "Infection"]:
            return "Medicine"  # Medicine for common illnesses
        elif illness in ["Fracture", "Surgery", "Trauma"]:
            return "Surgery"  # Surgery for severe conditions
        else:
            return "Medicine"  # Default to medicine for other illnesses
