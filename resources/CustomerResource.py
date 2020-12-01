import jsonpickle
from flask import make_response
from flask_restful import Resource
from repositories.DbManager import dbmanager
from repositories.CustomerRepository import CustomerRepository


class CustomerResource(Resource):
    def get(self):
        customer_repo = CustomerRepository(dbmanager)
        customers = customer_repo.get_all_customer()
        response_customer = make_response(
            jsonpickle.encode(customers, unpicklable=False))
        response_customer.headers['content-type'] = 'application/json'
        return response_customer
