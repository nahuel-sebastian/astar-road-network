import sys
class Grafo:
    
    def __init__(self):
        # id_nodo: [(vecino, coste)...]
        self.vertices = {}
        # id_nodo: (longitud, latitud)
        self.coordenadas = {}
        self.num_vertices = 0
        self.num_arcos = 0

    def cargar(self, ruta_base:str):
        ruta_arcos = f"{ruta_base}.gr"
        ruta_vertices = f"{ruta_base}.co"

        # Leer vertices con sus coordenadas
        try:
            with open(ruta_vertices, "r") as f:
                for linea in f:
                    linea = linea.strip()
                    if not linea or not linea.startswith("v "):
                        continue
                    else:
                        letra_inicial, id_str, lon_str, lat_str = linea.split()
                        id_nodo = int(id_str)
                        lon = int(lon_str) / 1000000.0      # Convertir a decimal
                        lat = int(lat_str) / 1000000.0      # Convertir a decimal
                        self.coordenadas[id_nodo] = (lon, lat)
        except FileNotFoundError:
            print(f"Error: no se encuentra el fichero de coordenadas '{ruta_vertices}'")
            sys.exit(1)

        self.num_vertices = len(self.coordenadas)

        # Leer arcos entre vertices y su coste
        try:
            with open(ruta_arcos, "r") as f:
                for linea in f:
                    linea = linea.strip()
                    if not linea or not linea.startswith("a "):
                        continue
                    letra_inicial, v1_str, v2_str, coste_str = linea.split()
                    v1 = int(v1_str)
                    v2 = int(v2_str)
                    coste = int(coste_str)

                    if v1 not in self.vertices:
                        self.vertices[v1] = []
                    self.vertices[v1].append((v2, coste))
                    self.num_arcos += 1
        except FileNotFoundError:
            print(f"Error: no se encuentra el fichero de arcos '{ruta_arcos}'")
            sys.exit(1)

    # Devuelve la lista de vecinos de un nodo
    def vecinos(self, nodo: int):
        return self.vertices.get(nodo, [])

    # Devuelve las coordenadas de un nodo
    def coordenadas(self, nodo: int):
        return self.coordenadas[nodo]
    
    # Devuelve el número de vértices
    def numero_vertices(self):
        return self.num_vertices

    # Devuelve el número de arcos
    def numero_arcos(self):
        return self.num_arcos