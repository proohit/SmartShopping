from models.Customer import Customer
from typing import List


class CustomerRepository():
    def __init__(self, dbmanager) -> None:
        self.dbmanager = dbmanager

    def get_all_customer(self) -> List[Customer]:
        query = "select customer_id, gender, age, city, price, regional, health, sustainability from customer"
        con = self.dbmanager.get_connection()
        cursor = con.cursor(buffered=True)
        cursor.execute(query)

        result = cursor.fetchall()
        customers = []
        for customer in result:
            customers.append(Customer(customer_id=customer[0], gender=customer[1], age=customer[2], city=customer[3], price=customer[4], regional=customer[5], health=customer[6], sustainability=customer[7]))
        return customers

    def get_customer_by_id(self, id) -> Customer:
        query = f"select * from customer where customer_id={id}"
        con = self.dbmanager.get_connection()
        cursor = con.cursor(buffered=True)
        cursor.execute(query)
        customers = cursor.fetchall()
        if(len(customers)):
            return customers[0]
        return None

    def create_table_customer(self):
        query = (
            """create table if not exists customer (
                    customert_id int PRIMARY KEY AUTO_INCREMENT,
                    gender float,
                    age float,
                    city float,
                    price float,
                    regional float,
                    health float,
                    sustainability float
                )"""
        )
        con = self.dbmanager.get_connection()
        cursor = con.cursor(buffered=True)
        cursor.execute(query)
        con.commit()
        print('created product table')

    def drop_table_customer(self):
        query = "DROP TABLE IF EXISTS customer"
        con = self.dbmanager.get_connection()
        cursor = con.cursor(buffered=True)
        cursor.execute(query)

    def create_customer(self, customer: Customer) -> Customer:
        sql_insert_query = """INSERT INTO Customer
                       (gender, age, city, price, regional, health, sustainability)
                       VALUES (%s,%s,%s,%s,%s,%s,%s);"""
        customer_tuple = (customer.gender, customer.age, customer.city, customer.price, customer.regional, customer.health, customer.sustainability)
        con = self.dbmanager.get_connection()
        cursor = con.cursor(dictionary=True)
        cursor.execute(sql_insert_query, customer_tuple)
        con.commit()
        created_customer = self.get_product_by_id(cursor.lastrowid)
        print(created_customer)
        return created_customer
