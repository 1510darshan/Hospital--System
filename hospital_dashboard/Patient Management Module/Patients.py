class Patient:
    def __init__(self, name, dob, gender, address, contact):
        self.name = name
        self.dob = dob
        self.gender = gender
        self.address = address
        self.contact = contact
        self.medical_history = []
        self.appointments = []
        self.bed_number = None

    def add_medical_record(self, record):
        self.medical_history.append(record)

    def schedule_appointment(self, appointment):
        self.appointments.append(appointment)

    def allocate_bed(self, bed_number):
        self.bed_number = bed_number

    def discharge(self):
        self.bed_number = None


class Hospital:
    def __init__(self):
        self.patients = []
        self.beds = {}  # Bed number -> Patient

    def register_patient(self, patient):
        self.patients.append(patient)

    def schedule_appointment(self, patient, appointment):
        patient.schedule_appointment(appointment)

    def admit_patient(self, patient, bed_number):
        if bed_number not in self.beds:
            self.beds[bed_number] = patient
            patient.allocate_bed(bed_number)
        else:
            print("Bed already occupied")

    def discharge_patient(self, patient):
        if patient.bed_number:
            del self.beds[patient.bed_number]
            patient.discharge()
        else:
            print("Patient is not admitted")


# Example usage:
hospital = Hospital()

# Registering a patient
patient1 = Patient("John Doe", "1990-01-01", "Male", "123 Main St", "123-456-7890")
hospital.register_patient(patient1)

# Scheduling an appointment
appointment1 = "2024-05-10 10:00 AM"
hospital.schedule_appointment(patient1, appointment1)

# Admitting a patient
hospital.admit_patient(patient1, "101")

# Discharging a patient
hospital.discharge_patient(patient1)
