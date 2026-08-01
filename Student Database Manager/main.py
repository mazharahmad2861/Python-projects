FILE_NAME = "students.txt"


def add_student():
    """Function to add a new student record to the file."""
    student_id = input("Enter Student Roll Number (Numeric): ").strip()
    if not student_id.isdigit():
        print("Invalid Roll Number! It should contain only numbers.")
        return

    # Check if student already exists
    with open(FILE_NAME, "r") as file:
        for line in file:
            if line.startswith(student_id + ","):
                print("Student Roll Number already exists. Use update option instead.")
                return

    name = input("Enter First Name: ").strip()
    if not name.isalpha():  # Ensuring only alphabets, no spaces
        print("Invalid Name! Name should contain only alphabets.")
        return

    age = input("Enter Age: ").strip()
    if not age.isdigit() or int(age) > 100:
        print("Invalid Age! Age should be a number under 100.")
        return

    course = input("Enter Course: ").strip()
    department = input("Enter Department: ").strip()

    # Append data to the file
    with open(FILE_NAME, "a") as file:
        file.write(f"{student_id},{name},{age},{course},{department}\n")

    print("Student added successfully!")


def view_students():
    with open(FILE_NAME, "r") as file:
        lines = file.readlines()
    
    if not lines:
        print("No student records found.")
        return
    
    print("\nStudent Records:")
    print('Roll Number\tName\tAge\tCourse\tDepartment')

    for line in lines:
        student_id, name, age, course, department = line.strip().split(",")
        print(student_id,"\t\t",name,"\t",age,"\t",course,"\t",department)

    
def search_student():
    search_query = input("Enter Student Roll Number or Name to search: ").strip()
    with open(FILE_NAME, "r") as file:
        for line in file:
            student_id, name, age, course, department = line.strip().split(",")
            if search_query == student_id or search_query.lower() == name.lower():
                print("\nStudent Found:")
                print('Roll Number\tName\tAge\tCourse\tDepartment')
                print(student_id,"\t\t",name,"\t",age,"\t",course,"\t",department)
                return
    print("Student not found.")



def update_student():
    """Function to update an existing student record in the file."""
    student_id = input("Enter Student Roll Number to update: ").strip()
    with open(FILE_NAME, "r") as file:
        lines = file.readlines()

    updated_lines = []
    found = False

    for line in lines:
        if line.startswith(student_id + ","):
            found = True
            student_id, name, age, course, department = line.strip().split(",")

            new_name = input(f"Enter New Name ({name}): ").strip()
            if new_name and not new_name.isalpha():
                print("Invalid Name! Name should contain only alphabets.")
                return
            new_name = new_name or name  # Keep the old value if input is empty

            new_age = input(f"Enter New Age ({age}): ").strip()
            if new_age and (not new_age.isdigit() or not (1 <= int(new_age) <= 100)):
                print("Invalid Age! Age should be a number between 1 and 100.")
                return
            new_age = new_age or age  # Keep the old value if input is empty

            new_course = input(f"Enter New Course ({course}): ").strip() or course
            new_department = input(f"Enter New Department ({department}): ").strip() or department

            updated_lines.append(f"{student_id},{new_name},{new_age},{new_course},{new_department}\n")
        else:
            updated_lines.append(line)

    if not found:
        print("Student not found.")
        return

    with open(FILE_NAME, "w") as file:
        file.writelines(updated_lines)
    print("Student record updated successfully!")



# -------------------------------------------------
def delete_student():
    student_id = input("Enter Student Roll Number to delete: ").strip()
    
    with open(FILE_NAME, "r") as file:
        lines = file.readlines()

    updated_lines = []
    found = False

    for line in lines:
        if line.startswith(student_id + ","):
            found = True
        else:
            updated_lines.append(line)

    if not found:
        print("Student not found.")
        return

    with open(FILE_NAME, "w") as file:
        file.writelines(updated_lines)
    
    print("Student record deleted successfully!")
# -------------------------------------------------

def user_choice(choice):
    """Handles user input and calls the corresponding function."""
    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        update_student()
    elif choice == '5':
        delete_student()
    elif choice == '6':
        print("Exiting Student Database Manager...")
        return
    else:
        print("Invalid choice. Please enter a valid option.")

if __name__ == '__main__':
    while True:
        print("\n Student Database Manager")
        print("1. Add a Student")
        print("2. View All Students")
        print("3. Search Student by ID or Name")
        print("4. Update Student Details")
        print("5. Delete Student")
        print("6. Exit")
        choice = input("Choose an option (1-6): ").strip()
        user_choice(choice)
        if(choice==6):
            break
