from flask import json


class Customer():
    def __init__(self,
                 customer_id=None,
                 gender: float = None,
                 age: float = None,
                 city: float = None,
                 price: float = None,
                 health: float = None,
                 regional: float = None,
                 sustainability: float = None,
                 ) -> None:
        self.customer_id = customer_id
        self.gender = gender
        self.age = age
        self.regional = regional
        self.health = health
        self.city = city
        self.price = price
        self.sustainability = sustainability

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
