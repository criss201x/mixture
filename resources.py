from prueba import Cuadrangular
import json

class CuadrangularResource:
    def on_get(self, req, resp):
        prueba = Cuadrangular()
        prueba.calcular()
        resp.body = ('')