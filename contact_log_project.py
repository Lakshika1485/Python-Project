
contacts_log = { 
    "Name": "Contact",
    
}

def add_contact(name,contact):
    contacts_log[name] = contact
    print(f"Congratulations, {name} is added  with the {contact}!!!")


def update_contact(name,contact):
    if name in contacts_log:
        contacts_log[name]= contact
        print(f"{name} with contact number {contact} is updated.")
    else:
        print(f"{name} is not found in the record..")


def update_name(contacts_log, name, new_name):
    contacts_log[new_name] = contacts_log.pop(name)


def delete_contact(name):
    if name in contacts_log:
        del contacts_log[name]
        print(f"{name} has been successfully deleted from the contact book.")
    else:
        print(f"{name} is not found in the record..")


def display_contact():
    for name, contact in contacts_log.items():
        print("---------------------------------------")
        print(f"{name}: {contact}")
        print("---------------------------------------")


def main():
    while True:
        print("Hi, Everyone!!!\nThe contact log book is here: ")
        print("Contact book")
        print("1. Add contact")
        print("2. Update contact")
        print("3. Update  Name")
        print("4. Delete contact ")
        print("5. Display contact book")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            
            name= input ("Enter the name of contact:")
            contact = input ("Enter the contact number:")
            if len(contact) ==10:
                add_contact(name,contact)
            else:
                print("incorrect no.")
            
                          
        elif choice == 2:
            name = input("Enter the name of contact: ")
            contact = int(input("Enter the contact number: "))
            update_contact(name, contact)
        
        elif choice == 3:
            name= input ("Enter the name of contact:")
            new_name = input ("Enter the new name of contact:")
        
            update_name(contacts_log,name,new_name)


        elif choice == 4:
            name = input("Enter the name: ")
            delete_contact(name)

        

        elif choice == 5:
            display_contact()
        elif choice == 6:
            print("Record is closing")
            break
        else:
            print("Invalid Choice")

main()

