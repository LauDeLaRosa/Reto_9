if __name__=="__main__":
    #Se le pide al usuario el valor de las variables
    P=int(input("Ingrese la cantidad de panes:"))
    M= int(input("Ingrese la cantidad de bolsas de leche:"))
    H=int(input("Ingrese la cantidad de huevos:"))
    B=int(input("Ingrese la cantidad del billete en pesos:"))
    vueltas=(lambda P,M,H,B:B-((P*300)+(M*3300)+(H*350)))(P,M,H,B) #Se define el calculo para las vueltas
print("Las vueltas son "+ str(vueltas) + " pesos") #Se imprime el resultado