import pickle
#import jsonpickle
from resources.CustomerResource import CustomerResource
#from flask import make_response
#from flask_restful import Resource
import pandas as pd
import xgboost
import json

## JSON empfangen:

# def to_json_bread():
# return json.dumps(CustomerResource)


## Model laden + Kuntendaten ins Model laden
loaded_model = pickle.load(open("ds_models/pima.pickle_brot.txt", "rb"))


## Prediction
class BrotPrediction():
        pred = loaded_model.predict(CustomerResource)
        #prediction = make_response(
         #   jsonpickle.encode(pred, unpicklable=False))
        #return pred #FEHLER

## Bsp. Ausgabe
# Zusätzliche SQL Abfrage der Productdatenbank <- eventuell hier Sortierung
# GET
## -> Hier muss die "pred" zurpckgeschickt werden.
