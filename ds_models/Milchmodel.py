import pickle
from repositories.DbManager import dbmanager
from repositories.CustomerRepository import CustomerRepository
from flask_restful import Resource
import pandas as pd
from json import JSONEncoder
import numpy
import xgboost
import json

# customers = CustomerResource
loaded_model = pickle.load(
    open("ds_models/pima.picklemilch.txt",
         "rb"))

def obj_dict(obj):
    return obj.__dict__

class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, numpy.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)

class MilchPrediction(Resource):
    def get(self):
        customer_repo = CustomerRepository(dbmanager)
        customers = customer_repo.get_all_customer()
        customerjson = json.dumps(customers, default=obj_dict)
        pandadf = pd.read_json(customerjson)
        pred = loaded_model.predict(pandadf)
        predictionstring = json.dumps(pred, cls=NumpyArrayEncoder)
        return predictionstring # liefert endlich ausgabe ->