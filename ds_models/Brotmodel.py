import pickle
import jsonpickle
from resources.CustomerResource import CustomerResource
from repositories.DbManager import dbmanager
from repositories.CustomerRepository import CustomerRepository
from flask import make_response
from flask_restful import Resource
from flask.views import MethodView
import pandas as pd
import xgboost
import json

## Daten empfangen:
#customers = CustomerResource
loaded_model = pickle.load(
    open("/Users/benjaminkampka/Desktop/Studium/Semester 7/Future Retail/SmartShopping/ds_models/pima.picklebrot.txt",
         "rb"))


## Prediction
# class test(MethodView):
#   def get(self):
#pred = loaded_model.predict(customers)


class BrotPrediction(Resource):
    def get(self):
        customer_repo = CustomerRepository(dbmanager)
        customers = customer_repo.get_all_customer()
        response_customer = make_response(
           jsonpickle.encode(customers, unpicklable=False))
        response_customer.headers['content-type'] = 'application/json'
        #print(response_customer)
        #test = json.dumps(response_customer)
        #test = pd.DataFrame(response_customer,index=response_customer[:,0])
        #print(test)
        #pred = loaded_model.predict(response_customer)
        #print(pred)

        # HIER SCHAUEN:
        # -> https://stackoverflow.com/questions/25398218/getting-json-response-using-requests-object-flask
        print(type(response_customer))
        return response_customer


       # print(customer)
       # response = make_response(jsonpickle.encode(customer,
                                                  # unpicklable=False))  # {"py/type": "resources.CustomerResource.CustomerResource"}
       # response.headers[
        #    'content-type'] = 'application/json'  # {"py/type": "resources.CustomerResource.CustomerResource"}
      #  return response

## Bsp. Ausgabe
# print(pred)  # Zusätzliche SQL Abfrage der Productdatenbank <- eventuell hier Sortierung
# GET
## -> Hier muss die "pred" zurpckgeschickt werden.
