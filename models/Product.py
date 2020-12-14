from flask import json


class Product():
    def __init__(self,
                 title: str,
                 description='',
                 weight: float = None,
                 price: float = None,
                 warnings='',
                 origin='',
                 product_id=None,
                 distance: float = None,
                 ) -> None:
        self.product_id = product_id
        self.title = title
        self.description = description
        self.origin = origin
        self.weight = weight
        self.price = price
        self.warnings = warnings
        self.distance = distance

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
