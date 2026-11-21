
import database

USER_CHOICE = """
Enter:

- 'a' to add a new patient
- 'l' to list all patients
- 's' to search for a patient
- 'd' to delete a patient
- 'v' to view all doctors
- 'b' to book an appointment
- 'p' to view all appointments
- 'q' to quit

Your choice:
"""

# Create the required lists and doctors
database.create_table() if hasattr(database, "create_table") else None

def menu():
    while True:
        choice = input(USER_CHOICE).lower()

        if choice == "a":
            patient_id = int(input("Enter patient ID: "))
            name = input("Enter patient name: ")
            age = int(input("Enter patient age: "))
            gender = input("Enter gender: ")
            phone = input("Enter phone number: ")

            database.add_patient(
                patient_id, name, age, gender, phone
            )

        elif choice == "l":
            patients = database.get_all_patients()

            if len(patients) == 0:
                print("No patients found!")
            else:
                for patient in patients:
                    print(patient)

        elif choice == "s":
            patient_id = int(input("Enter patient ID: "))
            print(database.search_patient(patient_id))

        elif choice == "d":
            patient_id = int(input("Enter patient ID: "))
            print(database.delete_patient(patient_id))

        elif choice == "v":
            doctors = database.get_all_doctors()

            for doctor in doctors:
                print(doctor)

        elif choice == "b":
            patient_id = int(input("Enter patient ID: "))
            doctor_id = int(input("Enter doctor ID: "))
            date = input("Enter appointment date: ")

            print(
                database.book_appointment(
                    patient_id, doctor_id, date
                )
            )

        elif choice == "p":
            appointments = database.get_all_appointments()

            if len(appointments) == 0:
                print("No appointments found!")
            else:
                for appointment in appointments:
                    print(appointment)

        elif choice == "q":
            print("Thank you for using Hospital Appointment System!")
            break

        else:
            print("Invalid choice! Please try again.")


menu()
