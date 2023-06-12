# Algoritmos-Genéticos
En este documento se presentarán las consideraciones que se tuvieron al desarrollar el ejercicio de maximizar las funciones  f(x) = X * Sen (10 π X) + 3 en el intervalo [-2, 2]. 2) y f(x) = X^3 * Sen (X) + X + 3 en el intervalo [-3, 3]


<b>Longitud de Cromosoma:</b> La longitud de los cromosomas para cada individuo en ambas funciones son de ocho bits, esto se realizó así debido a que los rangos para cada función oscilan entre -3 y 3 que máximo ocupan dos bits, entonces la consideración para manejar números negativos fue la de “Módulo y Signo” donde el primer bit es 1 si es negativo y 0 si es positivo. Lo anterior solo ocuparía tres bits pero debido a la manipulación de los cromosomas en el programa se prefiere manejar cadenas de bits con longitud que sea múltiplo de dos. 
Con lo anterior se tiene que el primer bit corresponde al signo y los siguientes tres a la parte entera del número. Los bits restantes se consideran entonces como la parte fraccionaria (decimal) del número que se calculó mediante la técnica multiplicativa.Por consiguiente la longitud de los cromosomas es de ocho bits

<b>Composición de los Cromosomas:</b> La composición de los cromosomas se maneja como cadenas de bits debido a que fue un requerimiento.

<b>Número de Individuos de la Población (Muestra del Rango de Soluciones):</b> Se eligió treinta debido ya que hay un número de individuos considerables para poder realizar el algoritmo genético.

<b>Individuos Población Inicial:</b> Cada individuo de la población inicial se define mediante un número aleatorio entre el rango de soluciones de cada función.

<b>Probabilidad de Emparejamiento:</b> La probabilidad de emparejamiento es de 0.6, es decir que en el intervalo [0-0.6) el individuo no es apto para emparejamiento mientras que de [0.6-1] si es apto. Al decir que un individuo es apto se traduce a que este se va a emparejar con  otro individuo también apto, aquellos que no sean aptos simplemente no se emparejan.

<b>Probabilidad de Mutación:</b> La probabilidad de mutación es de 0.4, es decir que en el intervalo  [0 - 0.44) el individuo no mutará mientras que en el intervalo [0.4 - 1] el individuo mutará correspondiendo al operador de mutación.

<b>Función de Calidad (Fitness):</b> La función fitness del primer ejercicio es  f(x) = X * Sen (10 π X) + 3 donde el valor de las funciones trigonométricas están dadas en radianes. La función fitness del segundo ejercicio es f(x) = X^3 * Sen (X) + X + 3 donde el valor de las funciones trigonométricas están dadas en radianes.

<b>Operador de Selección:</b> El criterio de selección planteado en ambos ejercicios es el de ruleta, el cual radica en los siguientes casos:

1.	A cada individuo se le se calculará su función fitness y posteriormente se sumarán todos los resultados.

2.	Con los resultados anteriores se aplicará la siguiente función que indicará la probabilidad asociada a la selección del individuo:

    <img src="/docs/fnfit.png" alt="FnFitness"/><br>
    Donde fi = Función Fitness

3.	De la población de resultados se asigna un número aleatorio y con este número se selecciona aquel valor que en la ruleta sea congruente al resultado, se tomará una muestra donde se elegirán los individuos a cruzar y mutar, es decir al final de elegir los individuos de la muestra habrá terminado el proceso de selección.

El número de individuos a seleccionar para el primer ejercicio el n=30 y para el segundo es n=30, para la segunda iteración este corresponde a n/2. En dado caso que se seleccione menos individuos es porque la posición que ocupa un número elegido fue seleccionada mil veces y se debe continuar. 

<b>Operador de Cruzamiento:</b> El criterio de cruzamiento planteado en ambos ejercicios es el de un punto, aquel donde escoge de manera aleatoria un punto para cortar el individuo en dos partes, donde el segmento izquierdo es el que se va intercambiar entre los dos individuos. En el algoritmo solo aquellos que fueron aptos mediante la generación de un número aleatorio y la probabilidad de emparejamiento son cruzados. Para aquellos que no fueron aptos, estos continúan en la generación. Esto sucede porque se considera que aquellos que se cruzan pueden mejorarse mientras que los otros no tienen la necesidad, ya que su información representan su mejor forma.

<b>Operador de Mutación:</b> El criterio de mutación planteado en ambos ejercicios es el de representación de orden, para realizar esta mutación se debe elegir aleatoriamente dos genes del del cromosoma para posteriormente intercambiarlos, para esta situación si ambos números aleatorios son iguales o el número aleatorio generado para comprobar con la probabilidad de mutación no correspondía entonces no se mutaba al individuo.

<b>Generación de Números Aleatorios:</b> Los números aleatorios se generaron mediante la librería random de python, los métodos usados fueron random.random() y random.randint(). Este módulo implementa generadores de números pseudoaleatorios para varias distribuciones. Para enteros, selección uniforme de un rango. Para las secuencias, la selección uniforme de un elemento aleatorio, una función para generar una permutación aleatoria de una lista en el lugar, y una función para el muestreo aleatorio sin reemplazo.



<b>Evidencias de los Resultados</b>
<center>
<img src="/docs/evidencia1.png" alt="Evidencia1"/>
<img src="/docs/evidencia2.png" alt="Evidencia2"/>
</center>


<b>Aclaraciones adicionales:</b> Si en alguno de los espacios aparece un [ ] es porque no hay elementos ya sea porque ninguno pasó la prueba de emparejamiento, de mutación u otra. Se tomó el rango para la población inicial más no para el resultado, es decir no evitamos que la respuesta saliera del rango ya que se supone que el algoritmo se da para que proporcione los mejores resultados dados de una población inicial. Pero si a consideración del usuario no es correcta, simplemente omita el resultado y elija una respuesta con su convicción.
