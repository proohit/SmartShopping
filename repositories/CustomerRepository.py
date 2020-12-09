from models.Customer import Customer
from typing import List


class CustomerRepository():
    def __init__(self, dbmanager) -> None:
        self.dbmanager = dbmanager

    def get_all_customer(self) -> List[Customer]:
        query = "select gender as f0, health as f1 from customer"
        con = self.dbmanager.get_connection()
        cursor = con.cursor(buffered=True)
        cursor.execute(query)

        result = cursor.fetchall()
        customers = []
        for customer in result:
            customers.append(Customer(f0=customer[0], f1=customer[1]))
        return customers
    # NEUER PART FÜR SPEZIFISCHE VORAUSSAGE NACH PRODUKTGRUPPE
    def get_customer_by_id_bread(self, id) -> Customer: # wir müssen hierhin Switchen + ergänzen durch Milch und Käse
        query = f"select gender as f0, health as f1  from customer where customer_id={id}"
        con = self.dbmanager.get_connection()
        cursor = con.cursor(buffered=True)
        cursor.execute(query)

        result = cursor.fetchall()
        customers_bread = []
        for customer in result:
            customers_bread.append(Customer(f0=customer[0], f1=customer[1]))
        return customers_bread

    def get_customer_by_id_milk_chees(self, id) -> Customer: # ergänzung Milch und Käse
        query = f"select regional as f0, sustainability as f1  from customer where customer_id={id}"
        con = self.dbmanager.get_connection()
        cursor = con.cursor(buffered=True)
        cursor.execute(query)
        result = cursor.fetchall()
        customers_milk_chees = []
        for customer in result:
            customers_milk_chees.append(Customer(f0=customer[0], f1=customer[1]))
        return customers_milk_chees

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
