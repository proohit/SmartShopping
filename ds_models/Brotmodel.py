import pickle
import jsonpickle
import json
from repositories.DbManager import dbmanager
from repositories.CustomerRepository import CustomerRepository
from repositories.ProductRepository import ProductRepository
from flask_restful import Resource, request
from flask import make_response
import pandas as pd
from json import JSONEncoder
import numpy
# import xgboost
loaded_model = pickle.load(
    open("ds_models/pima.pickle_brot.txt",
         "rb"))
def obj_dict(obj):
    return obj.__dict__
class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, numpy.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)
class BrotPrediction(Resource):
    def get(self):
        customer_repo = CustomerRepository(dbmanager)
        args = request.args
        customer_id = args.get('customer')
        customers = customer_repo.get_customer_by_id_bread(customer_id)
        customerjson = json.dumps(customers, default=obj_dict)
        pandadf = pd.read_json(customerjson)
        pred = loaded_model.predict(pandadf)
        pred_int = pred.tolist()
        strings = [str(integer) for integer in pred_int]
        a_string = "".join(strings)
        pred_int = int(a_string)
        product_repo = ProductRepository(dbmanager)
        products = product_repo.get_product_by_id(pred_int)
        response = make_response(
            jsonpickle.encode(products, unpicklable=False))
        response.headers['content-type'] = 'application/json'
        return response
