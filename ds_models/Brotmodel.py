import pickle
# import jsonpickle
from resources.CustomerResource import CustomerResource
# from flask import make_response
# from flask_restful import Resource
from flask.views import MethodView
#import pandas as pd
import xgboost
import json

## Daten empfangen:
customer = CustomerResource
print(customer)
loaded_model = pickle.load(open("/Users/benjaminkampka/Desktop/Studium/Semester 7/Future Retail/SmartShopping/ds_models/pima.picklebrot.txt", "rb"))

## Prediction
class test(MethodView):
    def get(self):
        pred = loaded_model.predict(customer)
        return pred

## Bsp. Ausgabe
# print(pred)  # Zusätzliche SQL Abfrage der Productdatenbank <- eventuell hier Sortierung
# GET
## -> Hier muss die "pred" zurpckgeschickt werden.
