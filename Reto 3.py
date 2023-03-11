import random

dado1 = random.randint(1,6)
dado2 = random.randint(1,6)

print ("Craps apuestas a un solo tiro")
print ("Usted gana si: ")
print ("Un par de unos en los dados \n"
       ,"Un total de 3 en los dados\n"
       ,"Un total de 11 en los dados \n"
       ,"Si se obtiene 2 o 12 en los dados\n"
       ,"Un total de 7 en los dados"
       ,"Cualquier otro resultado pierde")

if dado1 ==1 and dado2 ==1:
    print("Que suerte tiene, usted gano!!!") 
elif dado1 + dado2 == 3:
    print("Que suerte tiene, usted gano!!!")
elif dado1 + dado2 == 11:
    print("Que suerte tiene, usted gano!!!")
elif dado1 + dado2 == 2:
    print("Que suerte tiene, usted gano!!!")
elif dado1 + dado2 == 12:
    print("Que suerte tiene, usted gano!!!")
elif dado1 + dado2 == 7:
    print("Que suerte tiene, usted gano!!!")
else:
    print ("Lo sentimos usted perdio!!!")    
print ("Dado 1: ",dado1)
print ("Dado 2: ",dado2)
