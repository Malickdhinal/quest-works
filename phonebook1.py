phonebook = {}

while True:
    # Menu
    print("1. Add\n2. Update\n3. Delete\n4. View\n5. Display All")
    choice = int(input("Enter choice: "))

    # Add
    if choice == 1:
        contacts = {}
        name = input("Enter name: ")
        
        email_count = int(input("Enter email count: "))
        emails = [input(f"Enter email {i+1}: ") for i in range(email_count)]
        
        phone_count = int(input("Enter phone count: "))
        phones = [input(f"Enter phone number {i+1}: ") for i in range(phone_count)]
        
        contacts['name'] = name
        contacts['email'] = emails
        contacts['phone'] = phones
        phonebook[name] = contacts
        print("Contact added successfully.")

    # Update
    elif choice == 2:
        contact_to_update = input("Enter the contact name you want to update: ")
        if contact_to_update in phonebook:
            print("1. Update Name\n2. Update Email\n3. Update Phone")
            update_choice = int(input("Enter the type of data you want to update: "))
            if update_choice == 1:
                new_name = input("Enter new name: ")
                phonebook[contact_to_update]['name'] = new_name
            elif update_choice == 2:
                new_email = input("Enter new email: ")
                phonebook[contact_to_update]['email'] = new_email
            elif update_choice == 3:
                new_phone = input("Enter new phone number: ")
                phonebook[contact_to_update]['phone'] = new_phone
            print("Contact updated successfully.")
        else:
            print("Contact not found.")

    # Delete
    elif choice == 3:
        name = input("Enter the name you want to delete: ")
        if name in phonebook:
            phonebook.pop(name)
            print("Contact deleted successfully.")
        else:
            print("Invalid contact.")

    # View
    elif choice == 4:
        name = input("Enter the name: ")
        if name in phonebook:
            print(phonebook[name])
        else:
            print("Contact not found.")

    # Display All
    elif choice == 5:
        for contact in phonebook.values():
            print(contact)

    else:
        print("Invalid choice. Please try again.")