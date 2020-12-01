from flask import json


class Customer():
    def __init__(self,
                 customer_id=None,
                 gender: int = None,
                 age: int = None,
                 city: int = None,
                 price: int = None,
                 regional: int = None,
                 sustainability: int = None,
                 ) -> None:
        self.customer_id = customer_id
        self.gender = gender
        self.age = age
        self.regional = regional
        self.city = city
        self.price = price
        self.sustainability = sustainability

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
