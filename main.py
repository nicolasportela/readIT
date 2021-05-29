#!/usr/bin/python3
from models.baseModel import BaseModel

prueba = BaseModel()
prueba1 = prueba.to_dict()

print(prueba)
print(prueba.id)
print(prueba1)
