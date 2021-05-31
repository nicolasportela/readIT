#!/usr/bin/python3
from models.baseModel import BaseModel
from engine.dbStorage import DBStorage

engine = DBStorage()
engine.reload()
prueba = BaseModel()
engine.new(prueba)
engine.save()
