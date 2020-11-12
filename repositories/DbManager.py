from repositories.ProductRepository import ProductRepository
from config import config
import mysql.connector


class DbManager():
    def get_connection(self):
        return mysql.connector.connect(
            host=config.db.host,
            user=config.db.user,
            password=config.db.password,
            port=config.db.port,
            database=config.db.database,
        )

    def reset_database(self):
        product_repo = ProductRepository(self)
        product_repo.drop_table()

    def initialize_database(self):
        product_repo = ProductRepository(self)
        product_repo.create_table()


dbmanager = DbManager()
