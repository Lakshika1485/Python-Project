
def add_student(student_id, name, age, grade):
    with open("student.txt","a") as file:
        file.write(f"{student_id}, {name}, {age},{grade}\n")
    print("Student added successfully!")

def insert_student(position, student_id,name, age, grade):
    with open("student.txt","r") as file:
        lines = file.readlines()

    new_record = f"{student_id},{name},{age},{grade}\n"
    lines.insert(position - 1,new_record )

    with open("student.txt","w") as file:
        file.writelines(lines)
    print("Student inserted successfully at the position")

def delete_student(student_id):
    with open("student.txt","r") as file:
        lines = file.readlines()

    with open("student.txt","w") as file:
        deleted = False
        for line in lines:
            if not line.startswith(f"{student_id}"):
                file.write(line)
            else:
                deleted = True

            if deleted:
                print("deleted successfully")



            else:
                print("Student not found.")

def display_student():
    try:
        with open("student.txt","r") as file:
            students = file.readlines()
            if students:
                print("Student Record: ")
                for student in students:
                    print(student.strip())
                
                else:

                    print("No record found")
    except FileNotFoundError:
        print("File not found.")

def main():
    while True:
        print("\n----------STUDENT MANAGEMENT SYSTEM------------")
        print("1. Add Student:")
        print("2. Insert Student at Position")
        print("3. Delete Student by ID")
        print("4. Display All Students")
        print("5. Exit")
        choice  = input("Enter your choice: ")
    
        if choice == "1":
            student_id = input("Enter student id: ")
            name = input("Enter name: ")
            age = input("Enter age:")
            grade=input("Enter grade:")
            add_student(student_id,name, age, grade)

        elif choice == "2":
            position = int(input("Enter the position to insert: "))
            student_id = input("Enter student id: ")
            name = input("Enter name: ")
            age = input("Enter age:")
            grade=input("Enter grade:")
            insert_student(position,student_id,name, age, grade)

        elif choice == "3":
            student_id = input("Enter student id: ")
            delete_student(student_id)


        elif choice == "4":
            display_student()

        elif choice == "5":
            print("Exiting.....")
            break

        else: 
            print("Ops!!\nInvalid Chocie. Please try again!!!")

if __name__ == "__main__":
    main()
        
        