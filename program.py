from Customer import Customer
import sqlite3

from customer_data_access import CustomerDataAccess

data_access = CustomerDataAccess()

get_all_customers = 1
get_customers_by_id = 2
insert_customer = 3
delete_customer = 4
update_customer = 5
exit = 6


def print_menu():
    menu_messages = ['Welcome to Roy Project here is the menu',
                     'command 1 - get all customers',
                     'command 2 - get customer by id',
                     'command 3 - insert new customer',
                     'command 4 - delete customer by id',
                     'command 5 - update customer info',
                     'command 6 - exit the system']

    for msg in menu_messages:
        print(msg)


def input_customer():
    id = int(input('enter id: '))
    fname = input('enter first name: ')
    lname = input('enter last name: ')
    adress = input('enter adress: ')
    mobile = input('enter the mobile: ')
    return Customer(id, fname, lname, adress, mobile)


def handle_commands(command):
    if command == 1:
        customers = data_access.get_all_customers()
        for customer in customers:
            print(customer)
    elif command == 2:
        customer_id = int(input('please enter id to recall info'))
        print(data_access.get_customer_by_id(customer_id))
    elif command == 3:
        customer = input_customer()
        data_access.insert_customer(customer)
        print('insert success')
    elif command == 4:
        delete_id = int(input('please enter id to delete info'))
        data_access.delete_customer(delete_id)
        print('deletion success')
    elif command == 5:
        customer1 = input_customer()
        data_access.update_customer(customer1)
        print("updated customer succeed")
    elif command == 6:
        data_access.Exit_System()
        print('Good Bye')


print_menu()
command = int(input('Insert a number between 1 to 6: '))

while command != 6:
    handle_commands(command)
    command = int(input('Insert a number between 1 to 6: '))

# first we will print the menu
# 1 ..
# 2 ..

# next, get input from user (number 1-6)

# do the action
# for example, the user chose get all...
# data_access.print_all_customers()

# for example, the user chose delete
# ask the user that id he wish to delete
# data_access.delete_customer(id)

# for example, the user chose add
# ask the user to input: id, name. last_name, city, mobile
# data_access.insert_customer(....)


# customer = Customer(1, 'dani', 'gim', 'vegas',  125)
# insert_customer(cursor, customer)
# update_customer(cursor, '2', Customer('2', 'moshe', 'verbano', 'LA', 555))
# delete_customer(cursor, 2)
# connection.commit()
# print_all_customers(cursor)
