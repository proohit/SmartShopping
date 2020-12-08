# from repositories.DbManager import DbManager
from resources.RecommendationResource import RecommendationResource
from resources.ProductResource import ProductResource
from resources.CustomerResource import CustomerResource
from ds_models.Brotmodel import BrotPrediction
from flask import Flask
from flask_restful import Api
#from flask.views import MethodView
#from repositories.DbManager import dbmanager
from flask_cors import CORS
import xgboost


app = Flask(__name__)
CORS(app)
api = Api(app)
# dbmanager.reset_database()
# dbmanager.initialize_database()

api.add_resource(ProductResource, '/products', endpoint='products')
api.add_resource(RecommendationResource, '/products/recommendations', endpoint='productRecommendations')
api.add_resource(CustomerResource, '/customers', endpoint='customers')
api.add_resource(BrotPrediction, '/bread', endpoint='bread')
#app.add_url_rule('/bread', view_func=test.as_view('pred'))


if __name__ == "__main__":
    app.run(host='localhost')
