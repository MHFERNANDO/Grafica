class metodosOrdenamiento:
    def sortByBubble(self, arreglo):
        arreglo = arreglo.copy()
        n = len(arreglo)
        for i in range(n):
            for j in range(0, n - i - 1):  # debe ser hasta n-i-1
                if arreglo[j] > arreglo[j + 1]:
                    arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]
        return arreglo

    def sortBySelection(self, arreglo):
        arreglo = arreglo.copy()
        n = len(arreglo)
        for i in range(n - 1):
            min_index = i
            for j in range(i + 1, n):
                if arreglo[j] < arreglo[min_index]:
                    min_index = j
            if min_index != i:  # esta línea estaba mal indentada en tu versión
                arreglo[i], arreglo[min_index] = arreglo[min_index], arreglo[i]
        return arreglo

    def sortByBubbleUpgrade(self, arreglo):
        arreglo = arreglo.copy()
        n = len(arreglo)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if arreglo[j] > arreglo[j + 1]:
                    arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]
                    swapped = True
            if not swapped:
                break  # mejora: si no hubo intercambios, el arreglo ya está ordenado
        return arreglo

    def sortByInsertion(self, arreglo):
        arreglo = arreglo.copy()
        n = len(arreglo)
        for i in range(1, n):
            key = arreglo[i]
            j = i - 1
            while j >= 0 and arreglo[j] > key:
                arreglo[j + 1] = arreglo[j]
                j -= 1
            arreglo[j + 1] = key
        return arreglo
