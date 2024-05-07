import tkinter as tk
from tkinter import ttk

class HospitalManagementSystemGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")

        # Create notebook
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True)

        # Create tabs
        self.patient_tab = ttk.Frame(self.notebook)
        self.appointment_tab = ttk.Frame(self.notebook)
        self.bed_management_tab = ttk.Frame(self.notebook)

        # Add tabs to notebook
        self.notebook.add(self.patient_tab, text="Patient Management")
        self.notebook.add(self.appointment_tab, text="Appointment Management")
        self.notebook.add(self.bed_management_tab, text="Bed Management")

        # Populate Patient Management tab
        self.create_patient_widgets()

        # Populate Appointment Management tab
        self.create_appointment_widgets()

        # Populate Bed Management tab
        self.create_bed_management_widgets()

    def create_patient_widgets(self):
        # Patient Registration Frame
        patient_registration_frame = ttk.LabelFrame(self.patient_tab, text="Patient Registration")
        patient_registration_frame.pack(padx=10, pady=10, fill='both', expand=True)

        # Widgets for patient registration
        ttk.Label(patient_registration_frame, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        ttk.Entry(patient_registration_frame).grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(patient_registration_frame, text="DOB:").grid(row=1, column=0, padx=5, pady=5)
        ttk.Entry(patient_registration_frame).grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(patient_registration_frame, text="Gender:").grid(row=2, column=0, padx=5, pady=5)
        ttk.Combobox(patient_registration_frame, values=["Male", "Female", "Other"]).grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(patient_registration_frame, text="Address:").grid(row=3, column=0, padx=5, pady=5)
        ttk.Entry(patient_registration_frame).grid(row=3, column=1, padx=5, pady=5)

        ttk.Label(patient_registration_frame, text="Contact:").grid(row=4, column=0, padx=5, pady=5)
        ttk.Entry(patient_registration_frame).grid(row=4, column=1, padx=5, pady=5)

        ttk.Button(patient_registration_frame, text="Register").grid(row=5, columnspan=2, padx=5, pady=5)

    def create_appointment_widgets(self):
        # Appointment Scheduling Frame
        appointment_frame = ttk.LabelFrame(self.appointment_tab, text="Appointment Scheduling")
        appointment_frame.pack(padx=10, pady=10, fill='both', expand=True)

        # Widgets for appointment scheduling
        ttk.Label(appointment_frame, text="Select Patient:").grid(row=0, column=0, padx=5, pady=5)
        ttk.Combobox(appointment_frame).grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(appointment_frame, text="Appointment Date:").grid(row=1, column=0, padx=5, pady=5)
        ttk.Entry(appointment_frame).grid(row=1, column=1, padx=5, pady=5)

        ttk.Button(appointment_frame, text="Schedule Appointment").grid(row=2, columnspan=2, padx=5, pady=5)

    def create_bed_management_widgets(self):
        # Bed Management Frame
        bed_management_frame = ttk.LabelFrame(self.bed_management_tab, text="Bed Management")
        bed_management_frame.pack(padx=10, pady=10, fill='both', expand=True)

        # Widgets for bed management
        ttk.Label(bed_management_frame, text="Select Patient:").grid(row=0, column=0, padx=5, pady=5)
        ttk.Combobox(bed_management_frame).grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(bed_management_frame, text="Bed Number:").grid(row=1, column=0, padx=5, pady=5)
        ttk.Entry(bed_management_frame).grid(row=1, column=1, padx=5, pady=5)

        ttk.Button(bed_management_frame, text="Admit Patient").grid(row=2, columnspan=2, padx=5, pady=5)


def main():
    root = tk.Tk()
    app = HospitalManagementSystemGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
