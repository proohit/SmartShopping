from repositories.DbManager import DbManager
from resources.RecommendationResource import RecommendationResource
from resources.ProductResource import ProductResource
from flask import Flask
from flask_restful import Api
from repositories.DbManager import dbmanager

app = Flask(__name__)
api = Api(app)

dbmanager.reset_database()
dbmanager.initialize_database()

api.add_resource(ProductResource, '/products', endpoint='products')
api.add_resource(RecommendationResource,
                 '/products/recommendations', endpoint='productRecommendations')


if __name__ == "__main__":
    app.run()
