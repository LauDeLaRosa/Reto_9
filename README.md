# ¿Cuántos retos son?
## Ejercicio #1
De los retos anteriores seleciones 3 funciones y escribalas en forma de lambdas.

### 1.1
```python
if __name__ == "__main__": 
  #Se le pide al usuario los valores de las variables
  N = int(input("Ingrese la cantidad de gallinas: "))
  M = int(input("Ingrese la cantidad de gallos: "))
  K= int(input("Ingrese la cantidad de pollitos: "))
  kilosCarne= (lambda N, M, K: (N*6) + (M*7) + (K*1))(N,M,K) #Se define la operacion para calcular la cantidad de carne
print("La cantidad de carne de aves es de " + str(kilosCarne) + " kilos") #Se imprime el resultado
```
### 1.2
```python
if __name__=="__main__":
    #Se le pide al usuario el valor de las variables
    P=int(input("Ingrese la cantidad de panes:"))
    M= int(input("Ingrese la cantidad de bolsas de leche:"))
    H=int(input("Ingrese la cantidad de huevos:"))
    B=int(input("Ingrese la cantidad del billete en pesos:"))
    vueltas=(lambda P,M,H,B:B-((P*300)+(M*3300)+(H*350)))(P,M,H,B) #Se define el calculo para las vueltas
print("Las vueltas son "+ str(vueltas) + " pesos") #Se imprime el resultado
```

### 1.3
```python
if __name__=="__main__":
    #Se le pide al usuario los valores de las variables
    c=float(input("Ingrese la cantidad del préstamo:"))
    i=float(input("Ingrese el porcentaje de interés:"))
    n=float(input("Ingrese la cantidad de meses:"))
    valorPrestamo=(lambda c,i,n:c*((1+i)**n))(c,i,n) #Se define el calculo para el valor del prestamo
print("El valor del préstamo es de " + str(valorPrestamo)) #Se imprime el resultado
```

## Ejercicio #2
De los retos anteriores seleciones 3 funciones y escribalas con argumentos no definidos (*args).

### 2.1 
```python
# Definimos la función calcular_valor_prestamo con argumentos no definidos
def calcular_valor_prestamo(*args) -> float:
    prestamo = args[0]
    tasa_interes = args[1]
    meses = args[2]
    interes = tasa_interes * prestamo / 100
    return prestamo + meses * interes

if __name__ == '__main__':
    # Se piden los valores al usuario
    p = float(input("Ingrese el valor del préstamo en pesos: "))
    t_i = float(input("Ingrese la tasa de interés en porcentaje: "))
    m = int(input("Ingrese el número de meses para el préstamo: "))
    # Se llama a la funcion y toma los argumentos anteriormente dados por el usuario
    valor_prestamo = calcular_valor_prestamo(p, t_i, m)
    
    # Imprimimos los resultados
    print("El valor a pagar es de: " + str(valor_prestamo))
```
### 2.2 
```python
#Se define la funcion
def d(*args: float) -> float:

    p, m, h, b = args
    total = (p * 300) + (m * 3300) + (h * 350)
    cambio = b - total
    return cambio


if __name__ == '__main__':
    # Se pide los valores de las variables
    p = int(input("Ingrese la cantidad de panes: "))
    m = int(input("Ingrese la cantidad de bolsas de leche: "))
    h = int(input("Ingrese la cantidad de huevos: "))
    b = float(input("Ingrese la cantidad de dinero: "))

    # Calcular las vueltas
    cambio = d(p, m, h, b)

    # Imprimir el resultado.
    if cambio < 0:
        print("El dinero entregado no es suficiente para pagar la compra.")
    else:
        print("El cambio a entregar es de: $" + str(cambio))
```

### 2.3
```python
import math
# Se define la funcion
def calcular_volumen(*args):
    radio_esfera = args[0]
    radio_cono = args[1]
    altura_cono = args[2]

    volumen_esfera = (4/3) * (radio_esfera**3) * math.pi
    volumen_cono = (altura_cono/3) * (radio_cono**2) * math.pi
    return volumen_esfera + volumen_cono    

# Definimos la función calcular_area con argumentos no definidos
def calcular_area(*args):
    radio_esfera = args[0]
    radio_cono = args[1]
    altura_cono = args[2]
    area_esfera = 4 * math.pi * radio_esfera**2
    altura_oblicua = math.sqrt(altura_cono*2 + radio_cono*2)
    area_cono = (math.pi * radio_cono * altura_oblicua) + (math.pi * radio_cono**2)
    return area_esfera + area_cono

if __name__ == '__main__':
    # Se piden los valores al usuario
    rad_e = float(input("Ingrese el radio de la esfera en cm: "))
    rad_c = float(input("Ingrese el radio del cono en cm: "))
    alt_c = float(input("Ingrese la altura del cono en cm: "))
    # Se llama a las funciones y toman los argumentos anteriormente dados por el usuario
    vol = calcular_volumen(rad_e, rad_c, alt_c)
    area = calcular_area(rad_e, rad_c, alt_c)
    
    # Se imprimen los resultados
    print("El volumen de la figura es: " + str(vol) + " cm^3")
    print("El área de la figura es: " + str(area) + " cm^2") 
```

## Ejercicio #3
Escriba una función recursiva para calcular la operación de la potencia.
```pyhton
# Definir la funcion
def PotenciaRecursivo(n : int,p : int)-> int:
  if p == 0: 
    return 1
  else: 
    # Condicion de la funcion recursiva
    return n*PotenciaRecursivo(n,p-1) 


if __name__ == "__main__":
    # Se le pide al usuario los valores 
    n = int(input("Ingrese numero: "))
    p = int(input("Ingrese la potencia o exponenete: "))
    # Se llama la funcion 
    Potencia_del_numero = PotenciaRecursivo(n,p) 
    # Se imprime el resultado
    print(str(n) + " elevado a la " + str(p) + " es "+ str( Potencia_del_numero)) 
```

## Ejercicio #4
Utilice la siguiente plantilla de code para contar el tiempo:
```python
import time

start_time = time.time()
# instrucciones sobre las cuales se quiere medir tiempo de ejecución
end_time = time.time()

timer = end_time - start_time
print(timer)
```
Realice pruebas para calcular fibonacci con iteración o con recursión. Determine desde que número de la serie la diferencia de tiempo se vuelve significativa.
```python
import time  # Importamos el módulo time para medir el tiempo de ejecución

# Definimos la función para calcular Fibonacci con recursión
def fibonacci_recursion(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)

# Definimos la función para calcular Fibonacci con iteración
def fibonacci_iteration(n):
    if n <= 1:
        return n
    else:
        a, b = 0, 1
        for i in range(n-1):
            a, b = b, a + b
        return b

# Pedimos al usuario que ingrese el valor de n
n = int(input("Ingrese el valor de n: "))

# Fibonacci con recursión
start_time_recursion = time.time()  # Tomamos el tiempo actual
fib_recursion = fibonacci_recursion(n)  # Calculamos Fibonacci con recursión
end_time_recursion = time.time()  # Tomamos el tiempo actual nuevamente
timer_recursion = end_time_recursion - start_time_recursion  # Calculamos la diferencia de tiempo
print("El tiempo de ejecución de Fibonacci con recursión fue de: " + str(timer_recursion) + " segundos.")

# Fibonacci con iteración
start_time_iteration = time.time()  # Tomamos el tiempo actual
fib_iteration = fibonacci_iteration(n)  # Calculamos Fibonacci con iteración
end_time_iteration = time.time()  # Tomamos el tiempo actual nuevamente
timer_iteration = end_time_iteration - start_time_iteration  # Calculamos la diferencia de tiempo
print("El tiempo de ejecución de Fibonacci con iteración fue de: " + str(timer_iteration) + " segundos.")

# Comparamos tiempos
if timer_recursion > timer_iteration:
    print("Fibonacci con iteración es más rápido que con recursión.")
else:
    print("Fibonacci con recursión es más rápido que con iteración.")
 ```
 
 ## Ejercicio #5
 ![image](https://github.com/LauDeLaRosa/Reto_9/assets/124603892/84b18fa2-2c12-4c7b-9078-05d3127a9f03)

## Ejercicio #6
![image](https://github.com/LauDeLaRosa/Reto_9/assets/124603892/aad28937-ba6a-4a6a-85c4-3f49a1da47ec)
