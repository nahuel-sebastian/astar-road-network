from abierta import Abierta
from cerrada import Cerrada
from graph import Grafo
import time
import math

class AlgoritmoCaminoMinimo:
    def __init__(self, grafo, origen: int, destino: int):
        self.grafo = grafo
        self.origen = origen
        self.destino = destino
    def resolver(self, usar_heuristica: bool):
        
        lista_padres = {}
        lista_abierta = Abierta()
        lista_cerrada = Cerrada()
        nodos_expandidos = 0
        tiempo_inicio = time.time()
        g = {self.origen: 0}
        h = {}
        f = {}

        lista_abierta.insertar(self.origen, 0)


       
        lista_padres[self.origen] = None
        if usar_heuristica:
            h[self.origen] = self.distancia_haversine(self.origen, self.destino)
        else:
            h[self.origen] = 0
        f[self.origen] = g[self.origen] + h[self.origen]

        lista_abierta.insertar(self.origen, f[self.origen])

        while not lista_abierta.esta_vacia():
            v_actual, prioridad = lista_abierta.extraer_min()

            if v_actual == self.destino:
                tiempo_fin = time.time()
                tiempo_total = tiempo_fin - tiempo_inicio
                coste = g[v_actual]
                return self.reconstruir_camino(lista_padres, v_actual), coste, nodos_expandidos, tiempo_total
            
            if lista_cerrada.contiene(v_actual):
                continue

            lista_cerrada.insertar(v_actual)

            nodos_expandidos += 1

            for vecino, coste in self.grafo.vecinos(v_actual):

                if lista_cerrada.contiene(vecino):
                    continue
                
                g_nuevo = g[v_actual] + coste

                if vecino not in g or g_nuevo < g[vecino]:
                    g[vecino] = g_nuevo
                    lista_padres[vecino] = v_actual

                    if usar_heuristica:
                        h[vecino] = self.distancia_haversine(vecino, self.destino)
                    else:
                        h[vecino] = 0
                    f[vecino] = g[vecino] + h[vecino]
                    lista_abierta.insertar(vecino, f[vecino])

        tiempo_fin = time.time()
        tiempo_total = tiempo_fin - tiempo_inicio    
        return None, None, nodos_expandidos, tiempo_total        
  
        
    def reconstruir_camino(self, lista_padres, v_actual):
        camino = []
        while v_actual is not None:
            camino.append(v_actual)
            v_actual = lista_padres[v_actual]
        return camino[::-1]
    def distancia_haversine(self, n1, n2):
        lon1, lat1 = self.grafo.obtener_coordenadas(n1)
        lon2, lat2 = self.grafo.obtener_coordenadas(n2)
        r = 6371000 # Radio Tierra en metros
        phi1, phi2 = math.radians(lat1), math.radians(lat2)
        dphi = math.radians(lat2 - lat1)
        dlam = math.radians(lon2 - lon1)
        a = math.sin(dphi/2)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(dlam/2)**2
        return 2 * r * math.atan2(math.sqrt(a), math.sqrt(1-a))
    

    def ejecutarDijkstra(self):
        return self.resolver(False)
    def ejecutarAStar(self):
        return self.resolver(True)