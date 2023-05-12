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