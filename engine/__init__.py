#!/usr/bin/python3
"""
Initialize Database
"""

from engine.dbStorage import DBStorage

storage = DBStorage()
storage.reload()
