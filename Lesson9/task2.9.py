# Task 2
# Extend Phonebook application

# Functionality of Phonebook application:

# Add new entries
# Search by first name
# Search by last name
# Search by full name
# Search by telephone number
# Search by city or state
# Delete a record for a given telephone number
# Update a record for a given telephone number
# An option to exit the program

# The first argument to the application should be the name of the phonebook.
# Application should load JSON data, if it is present in the folder with application, else raise an error.
# After the user exits, all data should be saved to loaded JSON.
import json
from json.decoder import JSONDecodeError


def get_p_number():
    while True:
        phone_num = input("Enter phone number:\n")
        if phone_num.isdigit() and len(phone_num) == 10:
            return {"phone number": phone_num}
        else:
            return "Phone number you enter is not correct "


def get_name():
    first_name = input("Enter first name :\n")
    last_name = input("Enter last name:\n")
    return {"first name": first_name, "last name": last_name, "full name": first_name + last_name}


def get_address():
    city = input("Enter city:\n")
    state = input("Enter state:\n")
    return {"city": city, "state": state}


def add_contact():
    contact = {}
    contact.update(get_p_number())
    contact.update(get_name())
    contact.update(get_address())
    return contact


def store_contact(add_contact):
    with open("Lesson9\phonebook.json") as file_r:
        try:
            contact_storage = json.load(file_r)
            with open("Lesson9\phonebook.json", "w") as file_w:
                contact_to_add = list(add_contact)
                contact_storage.append(contact_to_add)
                json.dump(contact_storage, file_w, indent=2)
        except JSONDecodeError:
            contact_to_add = list(add_contact)
            with open("Lesson9\phonebook.json", "w") as file_w:
                json.dump(contact_storage, file_w, indent=2)


def contact_search(searh_data):
    search_resalt = {}


if __name__ == "__main__":
    store_contact(add_contact())
