from abierta import Abierta
from cerrada import Cerrada

class AlgoritmoCaminoMinimo:
    def __init__(self, grafo, origen: int, destino: int):
        self.grafo = grafo
        self.origen = origen
        self.destino = destino
