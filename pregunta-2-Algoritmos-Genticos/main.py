import math
import random

'''
Constantes.

- Longitud; 4
   Constante que representa la longitud de los individuos los cuales son
   arreglos, su valor es de 4 para este trabajo

- pM; 0.4
   pM es la abreviación para Probabilidad de Mutación, este valor nos
   representa la probabilidad de que un individuo mute.
- pE; 0.6
   pE es la abreviación de Probabilidad de Emparejamineto, tiene como función
   determinar cuando un individuo es apto para emparejarlo con otro individuo
   apto.
'''
longitud = 4  # bits
pM = 0.4
pE = 0.6

'''
--- dec2bin ---
Transforma un número a su equivalencia binaria
@param pnum, número que entra por parámetro en base 10 (decimal).
Valor que será transformado.
@return rta, arreglo de binarios con valor del decimal pnum.
'''
def dec2bin(num):

  a = bin(int(num))[2:].zfill(longitud)
  c = []

  for digit in str(a):
    if(digit is not 'b'):
      c.append(int(digit))
    else:
      c.append(0)

    if('b' in str(a)):
       c[0] = 1

  fraccion = num - int(num)
  for i in range(0,4):
    multi = fraccion*2
    c.append(abs(int(multi)))
    fraccion = multi - int(multi)
  
  return c


'''
--- bin2dec ---
Método para transforma números vinarios representados en arreglos a números enteros
@param pArray, arreglo de valores binarios representativos a un número
@return ans, número transformado en base diez (10)
'''
def bin2dec(pArray):
  a = ""
  for i in range(1, int(len(pArray)/2)):
    a+= str(pArray[i])
  ans = int(a,2)

  if(pArray[0]==1):
    ans = ans * (-1)
  
  k = -1
  for j in range(int(len(pArray)/2), len(pArray)):
    if (pArray[j] == 1):
      if(pArray[0] == 1):
        ans -= (2**k)
      else:
        ans += (2**k)
    k-=1
  
  return ans


'''
--- pIni ---
Método para generar un población inicial a partir de un rango.
@param numInferior; numSuperior, números que representan el rango que va abarcar
la población siendo numInferior el mínimo valor y numSuperior el máximo valor.
@return ans, arreglo que contiene la población.
'''
def pIni(numInferior, numSuperior, nIndividuos):
   ans = []
   for i in range(nIndividuos):
       ans.append(round(random.uniform(-2,2),3))

   return ans

'''
--- fitnessA ---
Función de aptitid para el caso A
@param x, valor numerico que representa el individuo
@return fx, valor correspondiente a la solución de la función
'''
def fitnessA(x):
   fx = x * math.sin(10*math.pi*x) + 3
   return fx

'''
--- fitnessB ---
Función de aptitud para el caso B.
@param x, valor numerico que representa el individuo.
@return fx, valor correspondiente a la solución de la función.
'''
def fitnessB(x):
   fx = ((x**3)*(math.sin(x)))+(x)+(3)
   return fx

'''
--- seleccion ---
El método de selección que se implementó fue por Ruleta la cual funciona de la siguiente manera:

    1. A cada individuo de la población se le calcula la función fitness y posterior
    -mente se suman todos los resultados.

    2. Una vez al total se le aplica un función que determina la probabilidad de que
    un individuo sea seleccionado.

    3. De la población de resultados se asigna un número aleatorio y con este número
    mas el criterio de selección se selecciona aquel valor que en la ruleta sea con
    -gruente al resultado, se tomará una muesta donde elegiran los individuos a cruzar 
    y mutar.

@param pPoblacion; es un arreglo que contiene la población inicial.
pNumSeleccionar; es un número entero que determina la cantidad de elementos que selec
-cionaremos para realizar el cruce.
pFuncion; es un char que nos va a identidicar cual de las funciones que se tienen pre
-establacidas se van a usar. opciones de entrada 'A' y 'B'
@return selec, arreglo que contiene los elementos de la población inicial que fueron 
seleccionados para el cruce.
'''
def seleccion(pPoblacion, pNumSeleccionar, pFuncion):
  z = []
  totalF = 0

  for i in range(0,len(pPoblacion)):

    if(pFuncion is 'A'):
      f = fitnessA(pPoblacion[i])
    
    elif(pFuncion is 'B'):
      f = fitnessB(pPoblacion[i])

    z.append(f)
    totalF += f
  
  ado = 0
  for i in range(0,len(z)):
    z[i] = (z[i]/totalF) *100
    ado += z[i]
    z[i] = ado

  
  selec = []
  num = []
  
  k = 0
  i=0
  while(i<pNumSeleccionar):
    var = random.uniform(0, 100)

    for j in range(0,len(z)):
      if(z[j]>=var):
        
        if(j in num):
          i-=1
        else:
          selec.append(pPoblacion[j])
          num.append(j)
        break

    if(k>1000):
      break

    i+=1
    k+=1
 

  return selec

'''
--- cruce ---
Método que realiza el cruce entre dos individuos que fueron emparejados. El tipo de cruce
es de un (1) punto, por lo tanto se escoge de manera aleatoría un punto para
cortar el individuo (arreglo) en dos partes, donde el segmento izquierdo es el que se va
intercambiar entre los dos individuos.
@param A;B , Dos (2) arreglos con datos [0,1] que representan a los individuos.
@return Array, Retorno de un arreglo que contiene los dos (2) individuos cruzados.
'''
def cruce(A, B):
  posi = int(random.uniform(0, len(A)-1))     
  swp1 = A[:posi]
  swp2 = B[:posi]

  A[:posi] = swp2
  B[:posi] = swp1

  return [A, B]


fff = []
ggg = []

'''
--- mutacion ---
Método para el proceso de mutación de un individuo. El tipo de mutación es
representación de orden , en la cual se cogen dos cromosomas de forma aleatoría
y se intercambia sus posiciones entre sí.
@param arreglo, arreglo con datos numéricos con valores binarios representando
a un individuo que muta.
@return arreglo, arreglo con datos numéricos con valore binarios representando
al individuo mutado.
'''
def mutacion(arreglo):
   random1 = random.randint(0, len(arreglo)-1)
   random2 = random.randint(0, len(arreglo)-1)
   random3 = random.random()

   if (random1 != random2) and (random3 >= pM):
       fff.append(arreglo.copy())
       temp = arreglo[random1]
       arreglo[random1] = arreglo[random2]
       arreglo[random2] = temp
       ggg.append(arreglo.copy())

   return arreglo


'''
--- algoritmoGenetico ---
Método que ejecuta todo el proceso del algoritmo donde se implementan los procesos
de selección, cruce y mutación.
@param seleccion(pPoblacion, pSeleccionados, pFuncion).
@return arreglo, 
[0] contenedor de los individuos que durante el proceso de mutación
lograr los mejores resultados según su operación fitness y son el resultado de las
mejores respuestas.
[1] individuos seleccionados
[2] individuos aptos para cruce
[3] duplas de cruce
[4] duplas cruzadas
[5] individuos aptos a cruzar
[6] resultado de mutaciones
'''
def algoritmoGenetico(pPoblacion, pFuncion, pSeleccionados):
  seleccionados = seleccion(pPoblacion, pSeleccionados, pFuncion)
  aptos = []
  ng = []

  for i in range (0, len(seleccionados)):
    r = random.random()
    if(r >= 0.6):
      aptos.append(dec2bin(seleccionados[i]))
    else:
      ng.append(dec2bin(seleccionados[i]))

  if(len(aptos)%2==1):
    ng.append(aptos.pop())

  #Copia de aptos
  ia = aptos.copy()
  #Duplas de cruce
  ib = []
  #Resultado de duplas de cruce
  ic = []
  #Aptos a mutar
  fff.clear()
  #Resultado de mutación
  ggg.clear()

  while(len(aptos)!=0):
    r1 = random.randint(0,len(aptos)-1)
    h = aptos.pop(r1)
    r2 = random.randint(0,len(aptos)-1)
    k = aptos.pop(r2)

    if isinstance(h, (list,)) == False:
      h = dec2bin(h)
    if isinstance(k, (list,)) == False:
      k = dec2bin(k)

    dupla = [h,k]
    ib.append(dupla.copy())
    dupla = cruce(dupla[0], dupla[1])
    ic.append(dupla.copy())

    ng.append(dupla[0])
    ng.append(dupla[1])
  
  for i in range(0,len(ng)):
    ng[i] = mutacion(ng[i])
    ng[i] = bin2dec(ng[i])
 
  
  iaa = cAdAbin2dec(ia.copy())
  ibb = cAdAdAbin2dec(ib.copy())
  icc = cAdAdAbin2dec(ic.copy())
  
  ffff = cAdAbin2dec(fff.copy())
  gggg = cAdAbin2dec(ggg.copy())
  
  return [ng, seleccionados, iaa, ibb, icc, ffff, gggg]

'''
--- cAdAbin2dec ---
Método que transforma una matríz de arreglos binarios a sus respectivos
valores en base diez.
@param pArray, matriz contenedora de los valores binarios.
@return new, arreglo con los valores en base diez.
'''
def cAdAbin2dec(pArray):
  new = []
  for i in range(0,len(pArray)):
    np = bin2dec(pArray[i])
    new.append(np)
  return new

'''
--- cAdAdAbin2dec ---
Método que transforma un grupo de binarios a sus respectivos valores decimales
con parte entera y decimal.
@param pArry, arreglo con los valores decimales.
@return new, arreglo con los individuos en base diez. 
'''
def cAdAdAbin2dec(pArray):
  new = []
  for i in range(0,len(pArray)):
    np = cAdAbin2dec(pArray[i])
    new.append(np)
  return new

'''
--- mejorIndividuo ---
Método para determinar cual es el mejor individuo de un arreglo según su función
fitness.
@param pArreglos; arreglo que contiene los individuos a ser evaluados.
pFuncion; string que representa a que función se van a comparar los individuos del
arreglo.
@return mejor, individuo que mejor se desempeñó en su función fitness.
'''
def mejorIndividuo(pArreglo, pFuncion):
  mejor = None

  if pFuncion is 'A':
    for i in range(0, len(pArreglo)):
      if mejor is None:
       mejor = pArreglo[i]
      elif(fitnessA(pArreglo[i]) > fitnessA(mejor)):
        mejor = pArreglo[i]

  elif pFuncion is 'B':
    for i in range(0, len(pArreglo)):
      if mejor is None:
       mejor = pArreglo[i]
      elif(fitnessB(pArreglo[i]) > fitnessB(mejor)):
       mejor = pArreglo[i]


  return mejor


#-------------------------------------------------------------------------------      

poblacionA = pIni(-2,2,30)

primeraGeneracionA = algoritmoGenetico(poblacionA, 'A', int(len(poblacionA)/2))

print('\nAlgoritmo Genético para la función', ' f(x) = X * Sen (10 π X) + 3 en el intervalo [-2, 2] \n')

print("--------------------Primera Iteración--------------------")
print('Población Inicial:' ,poblacionA)
print('Población después de la Selección:' , primeraGeneracionA[1])
print('Individuos aptos a cruzar: ', primeraGeneracionA[2]) 
print('Duplas a cruzar: ', primeraGeneracionA[3])
print('Resultado del Cruce:', primeraGeneracionA[4])
print('Individuos aptos a mutar: ', primeraGeneracionA[5])
print('Resultado de la mutación: ', primeraGeneracionA[6])
print('')
print('Generación Resultante:', primeraGeneracionA[0])
mejorA = mejorIndividuo(primeraGeneracionA[0], 'A')
fitMejorA = fitnessA(mejorA)
print('El mejor individuo de esta generación es:', mejorA)
print(' - Con un fitness de ', round(fitMejorA,33))

segundaGeneracionA = algoritmoGenetico(primeraGeneracionA[0],'A',int(len(primeraGeneracionA[0])/2))

print("\n--------------------Segunda Iteración--------------------")
print('Población Inicial:' ,primeraGeneracionA[0])
print('Población después de la Selección:' , segundaGeneracionA[1])
print('Individuos aptos a cruzar: ', segundaGeneracionA[2]) 
print('Duplas a cruzar: ', segundaGeneracionA[3])
print('Resultado del Cruce:', segundaGeneracionA[4])
print('Individuos aptos a mutar: ', segundaGeneracionA[5])
print('Resultado de la mutación: ', segundaGeneracionA[6])
print('')
print('Generación Resultante:', segundaGeneracionA[0])

mejorA2 = mejorIndividuo(segundaGeneracionA[0], 'A')
fitMejorA2 = fitnessA(mejorA2)
print('El mejor individuo de esta generación es:', mejorA2)
print(' - Con un fitness de ', round(fitMejorA2,33))

#-----------------------------------------------------------------------------------

poblacionB = pIni(-3,3,30)

primeraGeneracionB = algoritmoGenetico(poblacionB, 'B', int(len(poblacionB)/2))

print('\n\nAlgoritmo Genético para la función', '  f(x) = X^3 * Sen (X) + X + 3 en el intervalo [-3, 3] \n')

print("--------------------Primera Iteración--------------------")
print('Población Inicial:' ,poblacionB)
print('Población después de la Selección:' , primeraGeneracionB[1])
print('Individuos aptos a cruzar: ', primeraGeneracionB[2]) 
print('Duplas a cruzar: ', primeraGeneracionB[3])
print('Resultado del Cruce:', primeraGeneracionB[4])
print('Individuos aptos a mutar: ', primeraGeneracionB[5])
print('Resultado de la mutación: ', primeraGeneracionB[6])
print('')
print('Generación Resultante:', primeraGeneracionB[0])
mejorB = mejorIndividuo(primeraGeneracionB[0], 'B')
fitMejorB = fitnessB(mejorB)
print('El mejor individuo de esta generación es:', mejorB)
print(' - Con un fitness de ', round(fitMejorB,33))

segundaGeneracionB = algoritmoGenetico(primeraGeneracionB[0],'B',int(len(primeraGeneracionB[0])/2))

print("\n--------------------Segunda Iteración--------------------")
print('Población Inicial:' ,primeraGeneracionB[0])
print('Población después de la Selección:' , segundaGeneracionB[1])
print('Individuos aptos a cruzar: ', segundaGeneracionB[2]) 
print('Duplas a cruzar: ', segundaGeneracionB[3])
print('Resultado del Cruce:', segundaGeneracionB[4])
print('Individuos aptos a mutar: ', segundaGeneracionB[5])
print('Resultado de la mutación: ', segundaGeneracionB[6])
print('')
print('Generación Resultante:', segundaGeneracionB[0])
mejorB2 = mejorIndividuo(segundaGeneracionB[0], 'B')
fitMejorB2 = fitnessB(mejorB2)
print('El mejor individuo de esta generación es:', mejorB2)
print(' - Con un fitness de ', round(fitMejorB2,33))
