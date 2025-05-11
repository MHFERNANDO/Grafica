import Benchmarking as Be
import metodosOrdenamiento
import matplotlib.pyplot as plt

if __name__ == "__main__":
    print("Funciona")

    # Instancias
    metodosI = metodosOrdenamiento.metodosOrdenamiento()
    benchmarking = Be.Benchmarking()

    nT = [5000, 10000, 30000, 50000, 100000]

    # Generar un arreglo aleatorio base de tamaño máximo
    arreglo_base = benchmarking.buildArreglo(max(nT))

    # Diccionario de métodos
    tiemposByMetodo = {
        "Burbuja": [],
        "Seleccion": [],
        "Insercion": [],
        "Burbuja Mejorada": [],
    }

    # Definir los métodos a comparar
    metodos = {
        "Burbuja": metodosI.sortByBubble,
        "Seleccion": metodosI.sortBySelection,
        "Insercion": metodosI.sortByInsertion,
        "Burbuja Mejorada": metodosI.sortByBubbleUpgrade,
    }

    # Bucle para medir tiempos
    for n in nT:
        arreglo = arreglo_base[:n]  # Subarreglo con los primeros n elementos

        for nombre, metodo in metodos.items():
            tiempo = benchmarking.medir_tiempo(metodo, arreglo)
            tiemposByMetodo[nombre].append(tiempo)
            print(f"Tamaño: {n}, Método: {nombre}, Tiempo: {tiempo:.6f} segundos")

    # Graficar resultados
    plt.figure(figsize=(10, 6))

    for nombre, tiempos in tiemposByMetodo.items():
        plt.plot(nT, tiempos, marker='o', label=nombre)

    plt.grid()
    plt.title("Fernando Martinez-Elkin Maura\nTiempos de Ejecución de Algoritmos de Ordenamiento")
    plt.xlabel("Tamaño del Arreglo")
    plt.ylabel("Tiempo (segundos)")
    plt.legend()
    plt.get_current_fig_manager().set_window_title("Comparación de Métodos - Fernando Martínez - 2025")
    plt.show()
