from email.policy import default
from pickle import TRUE
from filehandler import *

AGENDA = {}

def print_contact(contact):
    print("Name:", contact)
    print("Phone:", AGENDA[contact]["tel"])
    print("Email:", AGENDA[contact]["email"])

def print_contact_book():
    if AGENDA:
        for contact in AGENDA:
            print_contact(contact)
            print("----------------------------------")
    else:
        print('>>> Contact book is empty')
    return True

def search_contact(contact):
    try:
        if contact_exist(contact):
            print_contact(contact)
        else:        
            print(">>> {} not on book".format(contact))
    except KeyError:
        print(">>> {} not on book".format(contact))
        
def add_contact(name, phone, email):
    try:
        AGENDA[name] = {
                "tel" : phone,
                "email" : email,
            }
    except:
        pass

def edit_contact(name, phone, email):
    if contact_exist(name):
        add_contact(name, phone, email)
    else:
        print(">>> {} not on book".format(name))

def contact_exist(name):    
    try:
        if name in AGENDA:
            return True
        else:
            return False
    except:
        return False

def remove_contact(contact):
    try:
        if contact_exist(contact):
            AGENDA.pop(contact)
        else:
            print(">>> {} not on book".format(contact))
    except KeyError:
        print(">>> {} not on book".format(contact))

def show_menu():
    print("\n----------------------")
    print("1 - Show All Contacts")
    print("2 - Show Contact")
    print("3 - Add Contact")
    print("4 - Edit Contact")
    print("5 - Remove Contact")
    print("6 - Save Contact Book")
    print("0 - Exit")
    print("----------------------\n")

    option = input()
    return option

def get_valid_contact_info(info):
    try:
        contact = input("Insert contact {}\n".format(info))
        if contact.isascii():
            contact = contact.replace('\r','').replace('\n', '')
            return contact
        else:
            raise NameError('Invalid {}', info)
    except NameError:
        return ""

def process_cmd(cmd):
    match cmd:
        case '1':
            return print_contact_book()
        case '2':
            search_contact(get_valid_contact_info("name"))
            return True
        case '3':
            add_contact(get_valid_contact_info("name"), get_valid_contact_info('phone'), get_valid_contact_info("email"))
            return True
        case '4':
            name = get_valid_contact_info("name")
            if contact_exist(name):
                edit_contact(name, get_valid_contact_info('phone'), get_valid_contact_info("email"))
            else:
                print(">>> {} not on book".format(name))
            return True
        case '5':
            remove_contact(get_valid_contact_info("name"))
            return True
        case '6':
            SaveContactBook(AGENDA)
            return True
        case '0':
            print("Saving contacts before say goodbye\n")
            SaveContactBook(AGENDA)
            return False


AGENDA = ReadContactBook()
while(process_cmd(show_menu())):
    pass