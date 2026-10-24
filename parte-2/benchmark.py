import random
import statistics
import sys
import time

from algoritmo import AlgoritmoCaminoMinimo
from graph import Grafo


# Compara Dijkstra, A* con la heurística original (haversine en metros, sin
# escalar) y A* con la heurística escalada, sobre pares aleatorios del grafo.
def benchmark(ruta_mapa, num_pares, semilla):
    grafo = Grafo()
    grafo.cargar(ruta_mapa)

    inicio = time.time()
    factor = AlgoritmoCaminoMinimo(grafo, 1, 1).calcular_factor_heuristica()
    tiempo_factor = time.time() - inicio
    print(f"factor de escala: {factor:.4f} (calculado en {tiempo_factor:.2f} s)")

    variantes = [("Dijkstra", None), ("A* original", 1.0), ("A* escalada", factor)]
    expandidos = {nombre: [] for nombre, _ in variantes}
    tiempos = {nombre: [] for nombre, _ in variantes}

    nodos = list(grafo.coordenadas)
    aleatorio = random.Random(semilla)
    pares = 0
    while pares < num_pares:
        origen, destino = aleatorio.sample(nodos, 2)
        costes = set()
        for nombre, f in variantes:
            algoritmo = AlgoritmoCaminoMinimo(grafo, origen, destino, f if f is not None else 0)
            if f is None:
                _, coste, nodos_exp, tiempo = algoritmo.ejecutarDijkstra()
            else:
                _, coste, nodos_exp, tiempo = algoritmo.ejecutarAStar()
            costes.add(coste)
            expandidos[nombre].append(nodos_exp)
            tiempos[nombre].append(tiempo)
        if None in costes:
            # Sin camino entre los dos nodos: se descarta el par
            for nombre, _ in variantes:
                expandidos[nombre].pop()
                tiempos[nombre].pop()
            continue
        assert len(costes) == 1, f"costes distintos para {origen}->{destino}: {costes}"
        pares += 1

    base_exp = statistics.mean(expandidos["Dijkstra"])
    base_t = statistics.mean(tiempos["Dijkstra"])
    print(f"{pares} pares, mismo coste óptimo en las tres variantes\n")
    print(f"{'variante':<14}{'expandidos (media)':>20}{'vs Dijkstra':>13}{'tiempo (media)':>17}{'vs Dijkstra':>13}")
    for nombre, _ in variantes:
        e = statistics.mean(expandidos[nombre])
        t = statistics.mean(tiempos[nombre])
        print(f"{nombre:<14}{e:>20,.0f}{(e / base_exp - 1):>+13.0%}{t:>15.3f} s{(t / base_t - 1):>+13.0%}")


if __name__ == "__main__":
    if len(sys.argv) not in (2, 3, 4):
        print("Uso: python benchmark.py <nombre-del-mapa> [num-pares] [semilla]")
    else:
        num_pares = int(sys.argv[2]) if len(sys.argv) > 2 else 20
        semilla = int(sys.argv[3]) if len(sys.argv) > 3 else 0
        benchmark(sys.argv[1], num_pares, semilla)
