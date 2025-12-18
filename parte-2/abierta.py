class Abierta:
    def __init__(self):
        # Cada elemento: (prioridad, vertice)
        self._heap = []

    def insertar(self, vertice: int, prioridad: float):
        # Añade al final y hace "flotar" el elemento (up-heap)
        self._heap.append((prioridad, vertice))
        self._subir(len(self._heap) - 1)

    def extraer_min(self):
        if self.esta_vacia():
            raise IndexError("La lista abierta está vacía")
        
        # El mínimo es la raíz
        min_prioridad, min_vertice = self._heap[0]
        
        # Mueve el último elemento a la raíz y lo hace "hundir" (down-heap)
        ultimo = self._heap.pop()
        if not self.esta_vacia():
            self._heap[0] = ultimo
            self._bajar(0)
            
        return min_vertice, min_prioridad

    def _subir(self, i):
        while i > 0:
            padre = (i - 1) // 2
            if self._heap[i][0] < self._heap[padre][0]:
                self._heap[i], self._heap[padre] = self._heap[padre], self._heap[i]
                i = padre
            else:
                break

    def _bajar(self, i):
        n = len(self._heap)
        while True:
            izq = 2 * i + 1
            der = 2 * i + 2
            mas_pequeno = i
            
            if izq < n and self._heap[izq][0] < self._heap[mas_pequeno][0]:
                mas_pequeno = izq
            if der < n and self._heap[der][0] < self._heap[mas_pequeno][0]:
                mas_pequeno = der
                
            if mas_pequeno != i:
                self._heap[i], self._heap[mas_pequeno] = self._heap[mas_pequeno], self._heap[i]
                i = mas_pequeno
            else:
                break

    def esta_vacia(self) -> bool:
        return len(self._heap) == 0

    def __len__(self):
        return len(self._heap)