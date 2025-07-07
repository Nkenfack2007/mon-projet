import math as m



# equation du premier degre 
def deg1(a,b):
    if a == 0:
        if b== 0:
            print (" l'equation admet une infinite de solution")
        else :
            print(" l'equation admet aucune solution")
    else :
        x = -b/a
        print(" la solution est :", x)
    return x
# equation du deuxieme degre 
def degre2 (a, b, c):
    if a == 0:
        if b==0:
            if c== 0:
                print(" l'equation possede une infinite de solution ")
            else:
                print(" aucune solution")
        else:
            deg1(b,c)
    else:
         d = b*b - 4*a*c
         if d == 0:
             print(" l'equation possede une solution double," -b/(2*a))
         elif d> 0:
             print(" l'equation possede une solution double")
             x=(-b-m.sqrt(d))/(2*a)
             y=(-b+m.sqrt(d))/(2*a)
             print( " x1 = ", x, "x2 = ", y)
         else:
             print( " l'equation ne possede pas de solution ")
            
 # table de multiplication d'un nombre entier
# demander a l'utilisateur d'entrer un nombre positif

def multi ():
    
   n= int(input(" veuillez entrer un nombre positif: "))
   print(" table de multiplication de 1 a %s:" %(n))
        
 # travaillons 
   
   for i in range(1, n+1):
     print(" ")
     print(f"la table de multiplication de {i}")
   for j in range (1, 11):
     print(f"{i} × {j} = {i * j}")

           
             
         
     