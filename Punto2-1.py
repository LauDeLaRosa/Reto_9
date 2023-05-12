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
