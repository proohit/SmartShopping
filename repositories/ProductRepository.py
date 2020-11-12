class ProductRepository():
    def __init__(self, dbmanager) -> None:
        self.dbmanager = dbmanager

    def get_all_products(self):
        query = "select * from products"
        con = self.dbmanager.get_connection()
        cursor = con.cursor(buffered=True)
        cursor.execute(query)

        products = []
        for product in cursor:
            products.append(product)
        return products

    def create_table(self):
        query = (
            """create table if not exists Products (
                    product_id int PRIMARY KEY AUTO_INCREMENT,
                    title nvarchar(45),
                    description nvarchar(200),
                    origin nvarchar(45),
                    weight numeric,
                    price numeric,
                    warnings nvarchar(45)
                )"""
        )
        con = self.dbmanager.get_connection()
        cursor = con.cursor(buffered=True)
        cursor.execute(query)

    def drop_table(self):
        query = "DROP TABLE IF EXISTS Products"
        con = self.dbmanager.get_connection()
        cursor = con.cursor(buffered=True)
        cursor.execute(query)
