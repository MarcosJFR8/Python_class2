

"""closet = ["Pantalon","Camisa","Harina"]
#closet=          0         1        2

print(closet[2])"""


netflix=["Batman","Simon","Ley de los audaces"]

running = True

while running:
    print("1.Añadir\n2.Ver lista\n3.Borrar elemento\n4.Salir\n")
    opcion=int(input("Ingrese una opcion: "))

    if opcion == 1:
        pelicula=input("Añade una pelicula: ")
        netflix.append(pelicula) #.append= Agrega un elemento determinado a la lista
    
    if opcion == 2:
        print(netflix)

    if opcion == 3:
        indice= (input("Ingrese el numero que desea borrar"))
        netflix.remove(indice) #.pop= Borra un elemento determinado de la lista
                               #.remove= Eliminarlos por el nombre textual del elemento. Remover "int" de un numero
    
    if opcion == 4:
        print("Vuelva pronto")
        running = False
    
    print("\n")
    