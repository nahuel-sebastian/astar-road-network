import heapq

class Abierta:
    def __init__(self):
        # Cada elemento: (prioridad, vertice)  
        self._heap = []

    # Añade un vértice con una prioridad dada.
    def insertar(self, vertice: int, prioridad: float): 
        heapq.heappush(self._heap, (prioridad, vertice))
    
    # Devuelve el vértice con menor prioridad (lanza IndexError si está vacía).
    def extraer_min(self):
        prioridad, vertice = heapq.heappop(self._heap)
        return vertice, prioridad

    # Devuelve True si la abierta está vacía.
    def esta_vacia(self) -> bool:
        return len(self._heap) == 0

    # Devuelve el número de elementos en la abierta.
    def __len__(self):
        return len(self._heap)