import csv
import contacts
import users
import pickle
import validators

#گنگ
def contact_save_data():
    f=open(r'C:\Users\asus\Desktop\contact_manager\data\contacts.pickle','wb')
    cl=pickle.dump(contacts.Contact.contacts, f)
    print(cl)

def user_save_data():
    f=open(r'C:\Users\asus\Desktop\contact_manager\data\users.pickle' , 'wb') 
    h=pickle.dump(users.User.users, f)
    print(h)

def contact_load_data():  # try and except because of Eof error!!
    try:
        with open(r'C:\Users\asus\Desktop\contact_manager\data\contacts.pickle', "rb") as f:
            contacts.Contact.contacts = pickle.load(f)
    except:
        print("file is empty :)")


def user_load_data():
    try:
        with open(r"C:\Users\asus\Group5\contact_manager\data\users.pickle", "rb") as f:
            users.User.users = pickle.load(f)#for EofError
    except:
        print("empty!")


def view_all_contacts():
    all_contacts = list()
    contact_load_data()
    if len(contacts.Contact.contacts) == 0:
        print("There is no contacts")
    else:
        for contact in contacts.Contact.contacts:
            all_contacts.append(contact.name)
            print(all_contacts)


def export_to_csv():
    contact_load_data()
    with open("data/contacts_csv.csv", "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        for contact in contacts.Contact.contacts:
            writer.writerow([contact.name, contact.email, contact.phone])
    print("contacts added to the csv file successfully.")


def import_from_csv():
    name = input("Enter the chosen contact name: ")
    try:
        with open("data/contacts_csv.csv", "r") as csv_file:
            reader = csv.reader(csv_file)
            for data in reader:
                if data[0] == name:
                    print(f"contact name: {data[0]}, contact email: {data[1]}, contact phone: {data[2]}")


    except:
        print("csv file is empty")


def search_contacts():
    contact_load_data()
    operation = input("Ener 1.name or 2.email address to search for me: ")
    search_results = []
    if operation == "1":
        name_input = input("Enter contacts name: ")
        for contact in contacts.Contact.contacts:
            if name_input == contact.name:
                search_results.append(contact)
    elif operation == "2":
        email_input = input("Enter contacts email: ")
        for contact in contacts.Contact.contacts:
            if email_input == contact.email:
                search_results.append(contact)
    else:
        print("Wrong operation.")
        return
    if len(search_results) == 0:
        print("No matching contacts found.")
    else:
        print("Searched contacts:")
        for contact in search_results:
            print(f"contacts name: {contact.name}, contacts email: {contact.email}, contacts phone: {contact.phone}")


while True:
    print("1. Create an account")
    print("2. Authenticate existing account")
    operation = input("Enter your chosen number: ")

    if operation == "1":
        user_load_data()
        username = input("Enter a new username: ")
        password = input("Enter a new password: ")

        password_check = validators.password_validator(password)

        if password_check is True:
            user = users.User(username, password)
            user_save_data()
            print(f"Welcome {username}")
            break
        else:
            print("Password is in a wrong format. try again.")
    elif operation == "2":
        user_load_data()
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if users.User.authenticate(username, password) is True:
            break
        else:
            print("Authentication failed. Please try again.")
    else:
        print("Invalid choice. Please try again.")

while True:
    print("\nThe Contact Management:")
    print("1. Add a new contact")
    print("2. Edit an existing contact")
    print("3. Delete a contact")
    print("4. View all contacts")
    print("5. Search for contacts")
    print("6. jhkModify an existing user")
    print("7. Exporting contacts to the csv file")
    print("8. importing contacts to the csv file")
    print("9. Exit bye")

    operation = input("Enter your chosen number: ")

    if operation == "1":
        contacts.Contact.adding()
        contact_save_data()
    elif operation == "2":
        contacts.Contact.editing()
        contact_save_data()
    elif operation == "3":
        contacts.Contact.deleting()
        contact_save_data()
    elif operation == "4":
        view_all_contacts()
    elif operation == "5":
        search_contacts()
    elif operation == "6":
        users.User.modifying()
        user_save_data()
    elif operation == "7":
        export_to_csv()
    elif operation == "8":
        import_from_csv()
    elif operation == "9":
        print("Done with Contacts Management!!!")
        break
    else:
        print("Wrong operation! try again.")