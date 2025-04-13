def collect_patient_data():
    
    patient_list = []
    patient_id_counter = 1  # Start with ID 1

    while True:
        print("\nEnter patient details (or type 'done' to finish):")
        name = input("Enter patient name: ").strip()
        if name.lower() == 'done':
            break

        while True:
            age_str = input("Enter patient age: ").strip()
            if age_str.isdigit():
                age = int(age_str)
                break
            else:
                print("Invalid age. Please enter a number.")

        # Create a dictionary to store the patient's information
        patient_info = {
            'id': patient_id_counter,
            'name': name,
            'age': age
        }

        # Add the patient's information to the list
        patient_list.append(patient_info)

        # Increment the ID counter for the next patient
        patient_id_counter += 1

    return patient_list

def display_patient_details(patient_list, patient_id):
    
    found = False
    for patient in patient_list:
        if patient['id'] == patient_id:
            print("\nPatient Details:")
            print(f"ID: {patient['id']}")
            print(f"Name: {patient['name']}")
            print(f"Age: {patient['age']}")
            found = True
            break

    if not found:
        print(f"Patient with ID {patient_id} not found.")

# --- Main part of the program ---
if __name__ == "__main__":
    print("Welcome to the Patient Data Entry System!")
    patients = collect_patient_data()

    print("\n--- All Entered Patient Data ---")
    if patients:
        for patient in patients:
            print(f"ID: {patient['id']}, Name: {patient['name']}, Age: {patient['age']}")
    else:
        print("No patient data entered.")

    # Now, let's try to pull up patient details based on ID
    if patients:
        while True:
            search_id_str = input("\nEnter the ID of the patient you want to view (or type 'exit'): ").strip()
            if search_id_str.lower() == 'exit':
                break
            if search_id_str.isdigit():
                search_id = int(search_id_str)
                display_patient_details(patients, search_id)
            else:
                print("Invalid ID. Please enter a number.")

    print("\nThank you for using the Patient Data Entry System!")

    
    
   