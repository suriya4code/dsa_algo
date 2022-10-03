
from dataclasses import dataclass


@dataclass
class Car:

    id:int
    name: str
    model: str




bmw = Car(id=1, name="Bmw", model="Bmw")
# audi = Car()

# bmw.name = "BMW"
# audi.name = "AUDI"


print(bmw.name)
# print(audi.name)

d = {"id": 0, "name": "vento", "model":"2019"}

vento = Car(**d)

print(vento.name)

print(list(range(1, 5)))