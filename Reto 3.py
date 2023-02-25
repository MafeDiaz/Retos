import random
dado1 = random.randint(1,6)
dado2 = random.randint(1,6)

print("Craps apuestas a un solo tiro,este juego se lanzan dos dados, se gana si se obtine un lanzamiento con:")
print("Un par de unos en los dados \n"
     ,"Un par de tres en los dados \n"
     ,"Un par de once en los dados \n"
     ,"Un par de dos o once en los dados \n"
     ,"Un total de sietes en los dados , en el resto de situaciones se pierde")

 if dado1 ==1 and dado2 ==1 or dado1 + dado2 == 3 or dado1 + dado2 == 11 or dado1 + dado2 == 2 or dado1 + dado2 == 12 or dado1 + dado2 == 7:
    print("Usted gano")    

