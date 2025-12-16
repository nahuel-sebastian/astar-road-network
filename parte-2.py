from _ssl import ALERT_DESCRIPTION_UNEXPECTED_MESSAGE
import sys

def leer_instancia(ruta_fichero):
    ruta_arcos = f"{ruta_fichero}.gr"
    ruta_vertices = f"{ruta_fichero}.co"
    
    try:
        with open(ruta_vertices, 'r') as f:
            for i in range(7):
                f.readline()
            
            lineas_vertices = [l.strip() for l in f.readlines() if l.strip()]
      
    except FileNotFoundError:
        print(f"Error: No se encuentra el fichero '{ruta_fichero}'")
        sys.exit(1)

    try: 
        with open(ruta_arcos, 'r') as f:
            for i in range(7):
                f.readline()
            
            lineas_arcos = [l.strip() for l in f.readlines() if l.strip()]

    except FileNotFoundError:
        print(f"Error: No se encuentra el fichero '{ruta_fichero}'")
        sys.exit(1)

    return lista_vertices, lista_arcos

def resolver(v1, v2, fichero_entrada, fichero_salida):

    
    try: 
        vertice_1 = int(v1)
        vertice_2 = int(v2)
    except ValueError:
        print(f"Error: los vértices deben ser int")
        sys.exit(1)


    lista_vertices, lista_arcos = leer_instancia(fichero_entrada)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Uso: python parte-2.py vértice1 vértice2 <nombre-del-mapa> <fichero-salida>")
    else:
        resolver(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

class Vertice:
    def __init__(self):
        self.id = id
        self.latitud = latitud
        self.altitud = altitud
        self.arcos = {} # {vecino:coste}
        


class Graph:
    def __init__(self):
        self.vertices = []
        self.n_vertices = n_vertices
        self.n_arcos = n_arcos
    def cargar_datos(self, )