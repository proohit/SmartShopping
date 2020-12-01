from models.Customer import Customer
from typing import List


class CustomerRepository():
    def __init__(self, dbmanager) -> None:
        self.dbmanager = dbmanager

    def get_all_customer(self) -> List[Customer]:
        query = "select customer_id, gender, age, city, regional, health, sustainability from customer"
        con = self.dbmanager.get_connection()
        cursor = con.cursor(buffered=True)
        cursor.execute(query)

        result = cursor.fetchall()
        customers = []
        for customers in result:
            customers.append(Customer(customer_id=customers[0], gender=customers[1], age=customers[2],
                                    city=customers[3], regional=customers[4], health=customers[5], sustainability=customers[6]))
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
                    gender int(1),
                    age int(1),
                    city int(1),
                    price int(1),
                    regional int(1),
                    health int(1),
                    sustainability int(1)
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

