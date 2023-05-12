if __name__=="__main__":
    #Se le pide al usuario los valores de las variables
    c=float(input("Ingrese la cantidad del préstamo:"))
    i=float(input("Ingrese el porcentaje de interés:"))
    n=float(input("Ingrese la cantidad de meses:"))
    valorPrestamo=(lambda c,i,n:c*((1+i)**n))(c,i,n) #Se define el calculo para el valor del prestamo
print("El valor del préstamo es de " + str(valorPrestamo)) #Se imprime el resultado