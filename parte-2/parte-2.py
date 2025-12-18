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


    camino_dijkstra, coste_total_dijkstra, expandidos_dijkstra, tiempo_dijkstra = algoritmo.ejecutarDijkstra()
    camino_astar, coste_total_astar, expandidos_astar, tiempo_astar = algoritmo.ejecutarAStar()
   


    print(f"vertices: {grafo.numero_vertices()}")
    print(f"arcos: {grafo.numero_arcos()}")
    print(f"Solucion optima con dijkstra encontrada con coste {coste_total_dijkstra}")
    print(f"Solucion optima con A* encontrada con coste {coste_total_astar}")
    print(f"nodos expandidos en dijkstra: {expandidos_dijkstra}")
    print(f"tiempo total en dijkstra: {tiempo_dijkstra}")
    print(f"nodos expandidos en A*: {expandidos_astar}")
    print(f"tiempo total en A*: {tiempo_astar}")

    # Suponiendo que 'camino' es la lista [1, 308, 309] devuelta por reconstruir_camino
    if camino_dijkstra:
        resultado = str(camino_dijkstra[0]) # Empezamos con el primer nodo
        
        for i in range(len(camino_dijkstra) - 1):
            v_actual = camino_dijkstra[i]
            v_siguiente = camino_dijkstra[i+1]
        
            # Buscamos el coste del arco entre estos dos nodos en el grafo
            coste_arco = 0
            for vecino, c in grafo.vecinos(v_actual):
                if vecino == v_siguiente:
                    coste_arco = c
                    break
        
            # Añadimos el segmento con el formato -(coste)-nodo
            resultado += f"-({coste_arco})-{v_siguiente}"
    
    # Escritura en el fichero
    with open(fichero_salida, 'w') as f:
        f.write(resultado + "\n")
    

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Uso: python parte-2.py vértice1 vértice2 <nombre-del-mapa> <fichero-salida>")
    else:
        comprobar_entrada(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])


