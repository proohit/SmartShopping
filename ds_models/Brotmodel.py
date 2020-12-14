import pickle
from repositories.DbManager import dbmanager
from repositories.CustomerRepository import CustomerRepository
from repositories.ProductRepository import ProductRepository
from flask_restful import Resource, request
import pandas as pd
from json import JSONEncoder
import numpy
import xgboost
import json

loaded_model = pickle.load(
    open("ds_models/pima.picklebrot.txt",
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
        predictionstring = json.dumps(pred, cls=NumpyArrayEncoder)
        print("pred")
        print(pred)  # -> <class 'numpy.ndarray'>
        print(type(pred))
        print("predictionstring")
        print(predictionstring)  # -> <class 'str'>
        print(type(predictionstring))

        pred_int = pred.tolist()
        print("pred_int")
        print(pred_int)
        print(type(pred_int))

        product_repo = ProductRepository(dbmanager)
        products = product_repo.get_product_by_id(pred_int)
        print(products)  # -> Object of type Product is not JSON serializable
        return products  # liefert endlich ausgabe -> "[1]" <- als nächstes "Str" to "int"



