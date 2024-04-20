

# While garantiza que el codigo se ejecute constantemente

"""while:running
    print("hola")"""



running = True


while running:
    edad= int(input("ingresa tu edad: ")) 

    if(edad>15):
        running= False

    else:
        print("Hola")