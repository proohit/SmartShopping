from repositories.DbManager import DbManager
from resources.RecommendationResource import RecommendationResource
from resources.ProductResource import ProductResource
from resources.CustomerResource import CustomerResource
from flask import Flask
from flask_restful import Api
from repositories.DbManager import dbmanager
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)
# dbmanager.reset_database()
# dbmanager.initialize_database()

api.add_resource(ProductResource, '/products', endpoint='products')
api.add_resource(RecommendationResource,
                 '/products/recommendations', endpoint='productRecommendations')
api.add_resource(CustomerResource, '/customer', endpoint='customer')


if __name__ == "__main__":
    app.run(host='0.0.0.0')
