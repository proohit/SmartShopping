from flask import json


class Customer():
    def __init__(self,
                 #customer_id=None, #eventuell neu erstellen extra für brot abfrage
                 f0: float = None,
                # age: float = None,
                # city: float = None,
                # price: float = None,
                 f1: float = None,
                # regional: float = None,
                # sustainability: float = None,
                 ) -> None:
       # self.customer_id = customer_id
        self.f0 = f0 # [{"f0": 1.0, "f1": 5.0}]
       # self.age = age
      #  self.regional = regional
        self.f1 = f1 #[{"f0": 1.0, "f1": 5.0}]
     #   self.city = city
      #  self.price = price
     #   self.sustainability = sustainability

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
