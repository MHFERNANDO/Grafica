 # Teoria de Complejidad


## Grafica

La grafica se añadera en el texto del AVAC debido a los directorios

## Actividad Desarrollada 
Este programa tiene como propósito principal analizar y comparar el rendimiento de distintos algoritmos de ordenamiento clásicos. Para ello, genera listas de números aleatorios con distintos tamaños y las ordena utilizando varios métodos: Burbuja, Burbuja Mejorada, Selección e Inserción.

El sistema mide el tiempo que tarda cada algoritmo en ordenar los datos, utilizando pruebas repetibles con arreglos aleatorios. Luego, esos tiempos se registran y se visualizan mediante una gráfica comparativa, lo cual permite observar cómo se comportan los algoritmos conforme crece el tamaño de los datos. De esta manera, se puede analizar empíricamente la eficiencia temporal de cada método y verificar sus complejidades teóricas.

## Salida de Consola 
Benchmarking inicializado <br>
Tamaño: 5000, Método: Burbuja, Tiempo: 1.280307 segundos <br>
Tamaño: 5000, Método: Seleccion, Tiempo: 0.491007 segundos<br>
Tamaño: 5000, Método: Insercion, Tiempo: 0.498111 segundos<br>
Tamaño: 5000, Método: Burbuja Mejorada, Tiempo: 1.303198 segundos<br>
Tamaño: 10000, Método: Burbuja, Tiempo: 5.291779 segundos<br>
Tamaño: 10000, Método: Seleccion, Tiempo: 2.053559 segundos<br>
Tamaño: 10000, Método: Insercion, Tiempo: 2.047579 segundos<br>
Tamaño: 10000, Método: Burbuja Mejorada, Tiempo: 5.476916 segundos
Tamaño: 30000, Método: Burbuja, Tiempo: 53.263972 segundos<br>
Tamaño: 30000, Método: Seleccion, Tiempo: 20.778142 segundos<br>
Tamaño: 30000, Método: Insercion, Tiempo: 21.294961 segundos<br>
Tamaño: 30000, Método: Burbuja Mejorada, Tiempo: 55.882514 segundos<br>
Tamaño: 50000, Método: Burbuja, Tiempo: 150.157139 segundos<br>
Tamaño: 50000, Método: Seleccion, Tiempo: 58.482716 segundos<br>
Tamaño: 50000, Método: Insercion, Tiempo: 59.136276 segundos<br>
Tamaño: 50000, Método: Burbuja Mejorada, Tiempo: 148.723751 segundos<br>
Tamaño: 100000, Método: Burbuja, Tiempo: 612.646331 segundos<br>
Tamaño: 100000, Método: Seleccion, Tiempo: 237.694521 segundos<br>
Tamaño: 100000, Método: Insercion, Tiempo: 239.132272 segundos<br>
Tamaño: 100000, Método: Burbuja Mejorada, Tiempo: 605.902069 segundos<br>



##  CONCLUSIONES CON TERMINOLOGIA DE NOTACION 
 
 - Fernando Martinez: Durante el desarrollo de la práctica, he comprendido a profundidad el funcionamiento de los algoritmos de ordenamiento clásicos y su impacto en el rendimiento computacional. A través de la medición de tiempos de ejecución para diferentes tamaños de entrada, fue posible evidenciar cómo el crecimiento cuadrático O(n²) afecta significativamente el desempeño de métodos como Burbuja, Selección e Inserción.<br>
Especialmente, se observó que la Burbuja Mejorada, aunque incluye una condición de parada anticipada, no mostró mejoras notables en listas aleatorias, lo que demuestra que su complejidad en el peor caso sigue siendo O(n²). En contraste, algoritmos como Inserción y Selección mostraron un mejor comportamiento práctico, debido a la menor cantidad de intercambios requeridos, aunque teóricamente tengan la misma complejidad. Esta práctica me permitió identificar de manera empírica qué métodos son más eficientes para ciertos contextos, consolidando así mi entendimiento de la notación Big O y su aplicación real.<br>
Elkin Maura: Gracias a esta práctica logré identificar cómo la eficiencia de los algoritmos de ordenamiento depende directamente de su complejidad temporal. Al comparar el tiempo que toma cada algoritmo con distintos tamaños de datos, quedó claro que todos los métodos evaluados presentan un crecimiento de tiempo proporcional a O(n²), lo cual los vuelve poco recomendables para grandes volúmenes de información.<br>
Aunque los métodos Burbuja, Selección e Inserción tienen la misma complejidad teórica, noté que Inserción y Selección resultan más rápidos en la práctica porque realizan menos operaciones innecesarias. Esta experiencia fue clave para reconocer cuál algoritmo conviene aplicar según la situación, reafirmando la importancia de comprender la notación Big O al momento de analizar el rendimiento de cualquier algoritmo.
