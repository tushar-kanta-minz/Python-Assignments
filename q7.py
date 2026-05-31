student_records = {} # Main dictionary database to store student records

def add_student(roll_no, name, grade):
    student_records[roll_no] = {
        "Name": name,
        "Grade": grade
    }
    print(f"Success: Student {name} added.")

def view_records():
    if not student_records:
        print("📭 No student records found.")
        return
        
    print("\n--- Student Records Database ---")
    for roll_no, details in student_records.items():
        print(f"Roll No: {roll_no} | Name: {details['Name']} | Grade: {details['Grade']}")
    print("-" * 32)

def search_student(roll_no):
    """Searches for a student using their unique Roll Number."""
    if roll_no in student_records:
        details = student_records[roll_no]
        print(f"Found: Roll No: {roll_no} -> Name: {details['Name']}, Grade: {details['Grade']}")
    else:
        print("Error: Student record not found.")

def delete_student(roll_no):
    """Removes a student record from the dictionary."""
    if roll_no in student_records:
        removed = student_records.pop(roll_no)
        print(f"Deleted: {removed['Name']}'s record has been removed.")
    else:
        print("Error: Roll number not found.")

# --- Interactive Menu Shell ---
while True:
    print("\n=== STUDENT RECORD SYSTEM ===")
    print("1. Add Student")
    print("2. View All Records")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")
    
    choice = input("Enter choice (1-5): ")
    
    if choice == "1":
        r_no = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")
        grade = input("Enter Student Grade/Marks: ")
        add_student(r_no, name, grade)
        
    elif choice == "2":
        view_records()
        
    elif choice == "3":
        r_no = input("Enter Roll Number to search: ")
        search_student(r_no)
        
    elif choice == "4":
        r_no = input("Enter Roll Number to delete: ")
        delete_student(r_no)
        
    elif choice == "5":
        print("Exiting system. Goodbye!")
        break
        
    else:
        print("Invalid choice! Please select between 1 and 5.")
