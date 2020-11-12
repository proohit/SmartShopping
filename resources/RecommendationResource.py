from flask_restful import Resource, request


class RecommendationResource(Resource):
    def get(self):
        args = request.args
        basket = args.getlist('list')
        products = basket[0].split(',')

        if products:
            print(products)

        recommendation = [{"title": "Honig"}]

        return recommendation
