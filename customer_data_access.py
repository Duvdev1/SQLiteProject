import sqlite3

DB_PATH = 'C:/Users/user/DataGripProjects/Customer/identifier.sqlite'


class CustomerDataAccess:
    connection = sqlite3.connect(DB_PATH)

    def __init__(self):
        self.cursor = CustomerDataAccess.connection.cursor()

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def get_all_customers(self):
        self.cursor.execute("SELECT * FROM customers")
        return self.cursor.fetchall()

    def get_customer_by_id(self, customer_id):
        self.cursor.execute(f'SELECT * FROM customers WHERE id = {customer_id}')
        return self.cursor.fetchall()[0]

    def insert_customer(self, customer):
        customer_tuple = (customer.id, customer.fname, customer.lname, customer.adress, customer.mobile)
        if not self.get_customer_by_id(customer.id):
            self.cursor.execute("insert into customers (id, fname, lname, adress, mobile) values(?, ?, ?, ?, ?)",
                                customer_tuple)
            CustomerDataAccess.connection.commit()
        else:
            print('customer already exist')

    def delete_customer(self, customer_id):
        self.cursor.execute(f'delete from customers where id = {customer_id}')
        CustomerDataAccess.connection.commit()

    def update_customer(self, customer):
        command = f'update customers set fname = "{customer.fname}", lname = "{customer.lname}", ' \
                  f'adress = "{customer.adress}", mobile = {customer.mobile} where id = {customer.id};'
        self.cursor.execute(command)
        CustomerDataAccess.connection.commit()

    def Exit_System(self):
        self.cursor.close()
        CustomerDataAccess.connection.close()
