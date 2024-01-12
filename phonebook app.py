def add_contact(contacts):
    name = input("Enter Name: ")
    phone_number = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contact = {
        "name": name,
        "phone_number": phone_number,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    print(f"Contact '{contact['name']}' added successfully!")

def view_contact_list(contacts):
    if not contacts:
        print("Contact list is empty.")
    else:
        print("\nContact List:")
        for contact in contacts:
            print(f"\nName: {contact['name']}")
            print(f"Phone: {contact['phone_number']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            
def search_contact(contacts, query):
    matching_contacts = []

    for contact in contacts:
        if query.lower() in contact['name'].lower():
            matching_contacts.append(contact)

    if not matching_contacts:
        print("No matching contacts found.")
    else:
        print("\nMatching Contacts:")
        for contact in matching_contacts:
            print(f"\nName: {contact['name']}")
            print(f"Phone: {contact['phone_number']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")



def update_contact(contacts, name, new_phone_number, new_email, new_address):
    for contact in contacts:
        if contact['name'] == name:
            contact['phone_number'] = new_phone_number
            contact['email'] = new_email
            contact['address'] = new_address
            print(f"Contact '{name}' updated successfully!")
            return
    print(f"Contact '{name}' not found.")

def delete_contact(contacts, name):
    for contact in contacts:
        if contact['name'] == name:
            contacts.remove(contact)
            print(f"Contact '{name}' deleted successfully!")
            return
    print(f"Contact '{name}' not found.")

def main():
    contacts = []

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contact_list(contacts)
        elif choice == '3':
            query = input("Enter name to search: ")
            search_contact(contacts, query)
        elif choice == '4':
            name = input("Enter the name of the contact to update: ")
            new_phone_number = input("Enter new phone number: ")
            new_email = input("Enter new email: ")
            new_address = input("Enter new address: ")
            update_contact(contacts, name, new_phone_number, new_email, new_address)
        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            delete_contact(contacts, name)
        elif choice == '6':
            print("Exiting app, thank you for using.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

main()