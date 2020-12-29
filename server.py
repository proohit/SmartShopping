# from repositories.DbManager import DbManager
from resources.RecommendationResource import RecommendationResource
from resources.ProductResource import ProductResource
from resources.CustomerResource import CustomerResource
from flask import Flask
from flask_restful import Api
# from flask.views import MethodView
# from repositories.DbManager import dbmanager
from flask_cors import CORS
# import xgboost  # wird benötigt für die Modelle
# Modelle:
from ds_models.Brotmodel import BrotPrediction
from ds_models.Milchmodel import MilchPrediction
from ds_models.Kaesemodel import KaesePrediction

app = Flask(__name__)
CORS(app)
api = Api(app)
# dbmanager.reset_database()
# dbmanager.initialize_database()

api.add_resource(ProductResource, '/products', endpoint='products')
api.add_resource(RecommendationResource, '/products/recommendations', endpoint='productRecommendations')
api.add_resource(CustomerResource, '/customers', endpoint='customers')
api.add_resource(BrotPrediction, '/bread', endpoint='bread')
api.add_resource(KaesePrediction, '/kaese', endpoint='kaese')
api.add_resource(MilchPrediction, '/milch', endpoint='milch')

if __name__ == "__main__":
    app.run(host='localhost')
