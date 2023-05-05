"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaa91u7avj5o48emrr0-a.oregon-postgres.render.com/",
        database="todo_d2u5",
        user="amitesh",
        password="49akBxSfYMzanvCYmy4VQHmsXNmIRLdA")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
