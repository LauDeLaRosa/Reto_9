if __name__ == "__main__": 
  #Se le pide al usuario los valores de las variables
  N = int(input("Ingrese la cantidad de gallinas: "))
  M = int(input("Ingrese la cantidad de gallos: "))
  K= int(input("Ingrese la cantidad de pollitos: "))
  kilosCarne= (lambda N, M, K: (N*6) + (M*7) + (K*1))(N,M,K) #Se define la operacion para calcular la cantidad de carne
print("La cantidad de carne de aves es de " + str(kilosCarne) + " kilos") #Se imprime el resultado