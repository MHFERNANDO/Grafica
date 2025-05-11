import time
import random
import metodosOrdenamiento

class Benchmarking:
    def __init__(self):
        print("Benchmarking inicializado")
        random.seed(42)  # Para que siempre genere el mismo arreglo base
        self.arreglo_base = [random.randint(0, 1000000) for _ in range(100000)]
        self.mOrdenamiento = metodosOrdenamiento.metodosOrdenamiento()

    def ejemplo(self):
        print("Benchmarking ejemplo")
        arreglo = self.buildArreglo(10000)
        tarea = lambda: self.mOrdenamiento.sortByBubble(arreglo.copy())  # copiar para evitar modificar
        tiempoMilles = self.contar_con_current_time_milles(tarea)
        tiempoNano = self.contar_con_nano_time(tarea)
        print(f"Tiempo en milisegundos: {tiempoMilles}")
        print(f"Tiempo en nanosegundos: {tiempoNano}")

    def buildArreglo(self, n):
        return self.arreglo_base[:n].copy()

    def contar_con_current_time_milles(self, tarea):
        start_time = time.time()
        tarea()
        end_time = time.time()
        return (end_time - start_time)

    def contar_con_nano_time(self, tarea):
        start_time = time.time_ns()
        tarea()
        end_time = time.time_ns()
        return (end_time - start_time) / 1e9

    def medir_tiempo(self, metodo, arreglo):
        inicio = time.perf_counter()
        metodo(arreglo.copy())
        fin = time.perf_counter()
        return (fin - inicio)
