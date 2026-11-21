
# Store patient details
patients = []

# Store doctor details using tuples
doctors = [
    (101, "Ramesh", "Cardiologist"),
    (102, "Suresh", "Dermatologist"),
    (103, "Kiran", "General Physician")
]

# Store appointment details
appointments = []


# Add patient
def add_patient(patient_id, name, age, gender, phone):
    patient = {
        "id": patient_id,
        "name": name,
        "age": age,
        "gender": gender,
        "phone": phone
    }

    patients.append(patient)
    print("Patient added successfully!")


# Display all patients
def get_all_patients():
    return patients


# Search patient
def search_patient(patient_id):
    for patient in patients:
        if patient["id"] == patient_id:
            return patient

    return "Patient not found"


# Delete patient
def delete_patient(patient_id):
    for patient in patients:
        if patient["id"] == patient_id:
            patients.remove(patient)
            return "Patient deleted successfully!"

    return "Patient not found"


# Display doctors
def get_all_doctors():
    return doctors


# Book appointment
def book_appointment(patient_id, doctor_id, date):
    patient_exists = any(
        patient["id"] == patient_id for patient in patients
    )

    doctor_exists = any(
        doctor[0] == doctor_id for doctor in doctors
    )

    if patient_exists and doctor_exists:
        appointment = {
            "patient_id": patient_id,
            "doctor_id": doctor_id,
            "date": date
        }

        appointments.append(appointment)
        return "Appointment booked successfully!"

    return "Invalid patient ID or doctor ID"


# Display appointments
def get_all_appointments():
    return appointments
