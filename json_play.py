from types import SimpleNamespace

class NestedNamespace(SimpleNamespace):
    def __init__(self, dictionary, **kwargs):
        super().__init__(**kwargs)
        for key, value in dictionary.items():
            if isinstance(value, dict):
                self.__setattr__(key, NestedNamespace(value))
            else:
                self.__setattr__(key, value)

ip = { "Vechile":{"brand":"jaguar","model":"A5","make":"India","coverage":[{"id":"123","name":"cov1"},{"id":"456","name":"cov2"}]}}

path = "Vechile/brand"
val = "RangeRover"

d = SimpleNamespace(**ip)

# print(d.Vechile)

e = NestedNamespace(ip)
print(e.Vechile.brand)

e.Vechile.brand = "RangeRover"

# print(e)

# node =['Vechile','brand']
# tp = ip
# for n in node:
#     tp = tp[n]
# tp = "ragerover"






# ip[node]=val
# print(ip)
