from models.Product import Product
from typing import List


class ProductRepository():
    def __init__(self, dbmanager) -> None:
        self.dbmanager = dbmanager

    def get_all_products(self) -> List[Product]:
        query = "select product_id, title, description, origin, weight, price, warnings from products"
        con = self.dbmanager.get_connection()
        cursor = con.cursor(buffered=True)
        cursor.execute(query)

        result = cursor.fetchall()
        products = []
        for product in result:
            products.append(Product(product_id=product[0], title=product[1], description=product[2],
                                    origin=product[3], weight=product[4], price=product[5], warnings=product[6]))
        return products

    def get_product_by_id(self, id) -> Product:
        query = "select * from products where product_id={id}"
        con = self.dbmanager.get_connection()
        cursor = con.cursor(buffered=True)
        cursor.execute(query)
        products = cursor.fetchall()
        if(len(products)):
            return products[0]
        return None

    def create_table(self):
        query = (
            """create table if not exists Products (
                    product_id int PRIMARY KEY AUTO_INCREMENT,
                    title nvarchar(45),
                    description nvarchar(200),
                    origin nvarchar(45),
                    weight float,
                    price float,
                    warnings nvarchar(45)
                )"""
        )
        con = self.dbmanager.get_connection()
        cursor = con.cursor(buffered=True)
        cursor.execute(query)
        con.commit()
        print('created product table')

    def drop_table(self):
        query = "DROP TABLE IF EXISTS Products"
        con = self.dbmanager.get_connection()
        cursor = con.cursor(buffered=True)
        cursor.execute(query)

    def create_product(self, product: Product) -> Product:
        sql_insert_query = """INSERT INTO Products
                       (title, description, origin, weight, price, warnings)
                       VALUES (%s,%s,%s,%s,%s,%s);"""
        product_tuple = (product.title, product.description, product.origin,
                         product.weight, product.price, product.warnings)
        con = self.dbmanager.get_connection()
        cursor = con.cursor(dictionary=True)
        cursor.execute(sql_insert_query, product_tuple)
        con.commit()
        created_product = self.get_product_by_id(cursor.lastrowid)
        print(created_product)
        return created_product
