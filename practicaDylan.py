#Dylan Alegria 
#Universidad Polictenica

def aerea_rectangulo(a,b):#### a es altura y b  es base esta funcion multiplica la base x altura 
    return a * b  
def aerea_circulo(r):### r es el radio se eleva a las dos y se multiplica por el pi 
    pi= 3.14
    return (r**2) * pi    
def relacion(a,b):
    if a>b:
        print ("1")
    elif a<b :
        print("-1")
        
    elif a==b :
        print("0") 
def intermedio(a,b):
    return (a+b)/2 
def recortar (num,mini ,maxi):
    if mini > num:
        print(mini)
    elif maxi <num:
        print(maxi)
    if mini < num and maxi> num :
        print(num)        
def separar():
    lis=[1,2,10,4,3,6,7,8,9,5]
    par=[]
    inpar=[]
    for x in lis:# For recorre la lista 
      print ("----------------------------")
      if x % 2==0: # si el numero al dividirlo hay un 0 es un numero par si no es un numro inpar
            print ("El Numero es Par", x)
            
            par.append(x)#se guarda en la lista de nuemero par
            par.sort()
      else:
          print ("El Numero NO es Par", x)
          
          inpar.append(x)#se guarda en la lista de impar 
          inpar.sort() 
    print("Lista de Numeros Pares",par)   
    print("Lista de Inpares",inpar)   
def menu():
 while True:
    print("-----------------------------------------------------------------------------------------")
    
    print("Elija 1 si quiere calcular la aerea de un Cuadrado ")
    print("Elija 2 si quiere calcular la area de un Circulo ")
    print("Elija 3 si quiere hacer la funcion Relacion ")
    print("Elija 4 si quieres el saber el intermedio de dos numero  ")
    print("Elija 5 di quiere usar la funcion recortar")
    print("Elija 6 que quiere usar la funcion separar ")
    print("Elija 7 si quiere salir ")
    x=int(input())
    if x==1:
        base= int(input("Digite la base del rectangulo"))
        altura = int(input("Digite la Altura  del rectangulo"))
        print ("el aerea de le rectagulo es :",aerea_rectangulo(altura,base))
        
    elif x==2 :
        radio= int(input("Digite el Radio del Circulo"))
        print("El aerea del circulo es : ",aerea_circulo(radio))
       
    elif x==3: 
        n1= int(input("Digite numero 1"))
        n2= int(input("Digite numero 2 "))   
        relacion (n1,n2)
        
    elif x==4:
        l1= int(input("Digite un numero"))
        l2= int(input("Digite un otro numero"))
        print("El intermedio de los numero son : ",intermedio(l1,l2))
        
    elif x==5: 
        r1= int(input("Digite un numero"))
        r2= int(input("Digite el segundo  numero"))
        r3= int(input("Digite el tercer  numero"))
        recortar(r1,r2,r3)
    
    elif x==6:
        separar()
    
    if x==7:
        break
 




