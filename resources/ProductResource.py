import jsonpickle
from flask import make_response
from flask_restful import Resource
from repositories.DbManager import dbmanager
from repositories.ProductRepository import ProductRepository


class ProductResource(Resource):
    def get(self):
        product_repo = ProductRepository(dbmanager)
        products = product_repo.get_all_products()
        response = make_response(
            jsonpickle.encode(products, unpicklable=False))
        response.headers['content-type'] = 'application/json'
        return response
