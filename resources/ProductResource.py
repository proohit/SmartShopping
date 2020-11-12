from repositories.ProductRepository import ProductRepository
from flask_restful import Resource
from repositories.DbManager import dbmanager


class ProductResource(Resource):
    def get(self):
        product_repo = ProductRepository(dbmanager)
        products = product_repo.get_all_products()
        return products
