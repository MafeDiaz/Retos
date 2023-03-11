import random
ppt = random.randint(1,3)

contin = "s" or "S" #declaración variable con valor inicial que hace verdadera la condición del ciclo.

while contin == "s" or contin=="S":



    print("Bienvenido al juego de piedra, papel, tijera!!! \n")
    num = int(input("Oprima 1 para Piedra, 2 para Papel y 3 para Tijera: \n"))
    if num >= 4:
        print("Usted marco una opción incorrecta!!!")
    elif ppt == 1 and num == 1:
        print ("El resultado es: ",ppt,"= Piedra es un empate, usted escogio",num,"= Piedra")
    elif ppt ==1 and num == 2:
        print ("El resultado es: ",ppt,"= Piedra, usted gano, usted escogio",num,"= Papel")
    elif ppt ==1 and num == 3:
        print ("El resultado es: ",ppt,"= Piedra, usted perdio, usted escogio",num,"= Tijera")
    elif ppt == 2 and num == 2:
        print("El resultado es: ",ppt,"= Papel, es un empate, usted escogio",num,"= Papel")
    elif ppt == 2 and num == 1:
        print("El resultado es: ",ppt,"= Papel, usted perdio, usted escogio",num,"= Piedra")
    elif ppt == 2 and num == 3:
        print("El resultado es: ",ppt,"= Papel, usted gano, usted escogio",num,"= Tijera")
    elif ppt == 3 and num == 3:
        print("El resultado es: ",ppt,"= Tijera, es un empate, usted escogio",num,"= Tijera")
    elif ppt == 3 and num == 1:
        print("El resultado es: ",ppt,"= Tijera, usted gano, usted escogio",num,"= Piedra")
    else:
        print("El resultado es: ",ppt,"= Tijera, usted perdio, usted escogio",num,"= Papel")
    
    contin = input("Para volver a jugar presione s/S o presione cualquier tecla para terminar: \n")
    




