import csv
contacts = []

def save_contact():
    with open('contact.txt','w', newline="") as file:
        header_name = ["Name","Phone","Email","Address"]
        writer = csv.DictWriter(file,fieldnames=header_name)
        writer.writeheader()
        writer.writerows(contacts)

#########################################################
def add_contact():
    print("add new contact")
    name = input("Name:  ")
    phone = input("Phone: ")
    email = input("Email: ")
    address = input("Address: ")
    
    if not phone.isdigit():
        raise ValueError("phone number  must be  numric")
    
    contact = {'Name': name , 'Phone': phone , 'Email': email , 'Address':address}
    contacts.append(contact)
    save_contact()
    print("add new contact sucsesfully done")
#########################################################
def view_contacts():
    for contact in contacts:
        print(f"Name {contact['Name']}")
        print(f"Phone {contact['Phone']}")
        print(f"Email {contact['Email']}")
        print(f"Address {contact['Address']}")
        print("________________________________________")
#########################################################
def open_file():
    try:
        with open("contact.txt",'r') as file:
            lines = csv.DictReader(file)
            for line in lines:
                contacts.append(line)
    except FileNotFoundError:
        print("this file dos not exist")
        

##########################################################
def update_contact():
    phone = input("enter contact for search")
    if not phone.isdigit():
        raise ValueError("phone number must be numric")
    for contact in contacts :
        if contact['Phone']==phone:
            print (f"currect details for contact: ")
            print (f"name {contact  ['Name']}")
            print(f"phone {contact['Phone']}")
            print (f"email {contact  ['Email']}")
            print (f"Address {contact  ['Address']}")

            new_name = input("Name:").strip()
            new_email = input("email: ").strip()
            new_address = input("address").strip()

            if new_name:
                contact['Name']=new_name
            elif new_email:
                contact['Email'] = new_email
            elif new_address:
                contact['Address'] = new_address
            
            save_contact()
            print(f"new details for {contact['Name']}has been change")
            return

##########################################################
def delet_contact():
    print("delet contact ")
    phone = input("enter phone nomber who u want to delet him: ")
    if not phone.isdigit():
        raise ValueError("phone number must be numric")
    for contact in contacts:
        if contact['Phone'] == phone:
            deleted_name=contact['Name']
            contacts.remove(contact)
            save_contact()
            print(f"{deleted_name} has been deleted")
            return
    print("contact not found")
##########################################################
open_file()
while True:
    try:
        print(" address book menu")
        print("1. add contact")
        print("2.   vie contact")
        print("3. update contact")
        print("4. del contact")
        print("5. exit")

        choice = int(input("enter ur choice  ").strip())
        if choice == 1:
            add_contact()
        elif choice == 2:
            view_contacts()
        elif choice == 3:
            update_contact()
        elif choice == 4:
            delet_contact()
        elif choice == 5 :
            print("good by bitch")
            exit()
        else:
            print("rrrrrrridi yebar dige talash kon")
    except Exception as e:
        print(f"Error{e}")
