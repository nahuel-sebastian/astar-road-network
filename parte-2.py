import sys
from algoritmo import AlgoritmoCaminoMinimo
from graph import Grafo


def comprobar_entrada(v1, v2, fichero_entrada, fichero_salida):

    
    try: 
        vertice_1 = int(v1)
        vertice_2 = int(v2)
    except ValueError:
        print(f"Error: los vértices deben ser int")
        sys.exit(1)

    
    grafo = Grafo()
    grafo.cargar(fichero_entrada)

    algoritmo = AlgoritmoCaminoMinimo(grafo, vertice_1, vertice_2)
    print("--------------------------------")
    dijkstra = algoritmo.ejecutarDijkstra()
    print("--------------------------------")
    astar = algoritmo.ejecutarAStar()
    print("--------------------------------")


    print(f"vertices:{grafo.numero_vertices()}")
    print(f"arcos:{grafo.numero_arcos()}")
    print(f"Solucion optima con dijkstra encontrada con coste:{dijkstra[1]}")
    print(f"Solucion optima con A* encontrada con coste:{astar[1]}")
    print(f"nodos expandidos en dijkstra:{dijkstra[2]}")
    print(f"tiempo total en dijkstra:{dijkstra[3]}")
    print(f"nodos expandidos en A*:{astar[2]}")
    print(f"tiempo total en A*:{astar[3]}")


    with open(fichero_salida, 'w') as f:
        f.write("Dijkstra:\n")
        f.write(str(algoritmo.ejecutarDijkstra()))
        f.write("\n")
        f.write("A*:\n")
        f.write(str(algoritmo.ejecutarAStar()))

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Uso: python parte-2.py vértice1 vértice2 <nombre-del-mapa> <fichero-salida>")
    else:
        comprobar_entrada(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])


