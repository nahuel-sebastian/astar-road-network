class Cerrada:
    def __init__(self):
        # Conjunto de nodos ya expandidos
        self._set = set()
    
    # Devuelve True si el nodo ya está en la lista cerrada.
    def contiene(self, nodo: int) -> bool:
        return nodo in self._set

    # Inserta un nodo en la lista cerrada (expandido).
    def insertar(self, nodo: int):
        self._set.add(nodo)

    # Devuelve el número de nodos en la lista cerrada.
    def __len__(self):
        return len(self._set)

    # Limpia la lista cerrada.
    def limpiar(self):
        self._set.clear()
