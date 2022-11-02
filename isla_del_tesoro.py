#Isla del tesoro Programa en Python

print("Bienvenido a la isla; Tu misión será encontrar el tesoro...")
print("Estás en un sendero...")

menu_de_interaccion = int(input("Selecciona 1.Para ir a la DERECHA o 2.Para ir a la IZQUIERDA: "))

if menu_de_interaccion == 1:
    print("Elejiste la opción DERECHA")
    print("Caíste en un agujero")
    print("GAME OVER")

elif menu_de_interaccion == 2:
    print("Elejiste la opción IZQUIERDA")
    print("Te subiste a un barco que esta a punto de hundirse")
    menu_de_interaccion = int(input("Selecciona 1.Para ESPERAR o 2.Para NADAR: "))
    if menu_de_interaccion == 1:
        print("Elejiste la opción ESPERAR")
        print("Te hundiste con el barco")
        print("GAME OVER")

    elif menu_de_interaccion == 2:
        print("Elejiste la opción NADAR")
        print("Llegate a una playa de la isla")
        print("Hay dos caminos")
        menu_de_interaccion = int(input("Selecciona 1.PANTANO lleno de serpientes o 2.Camino hacia un PALACIO: "))
        if menu_de_interaccion == 1:
            print("Elejiste la opción PANTANO")
            print("Te comieron las serpientes")
            print("GAME OVER")

        elif menu_de_interaccion == 2:
            print("Elejiste la opción PALACIO")
            print("Estás dentro del palacio")
            print("Hay tres puertas")
            menu_de_interaccion = int(input("Selecciona 1.Puerta ROJA o 2.Puerta AZUL o 3.Puerta AMARILLA: "))
            if menu_de_interaccion == 1:
                print("Elejiste la opción PUERTA ROJA")
                print("Eres Quemado")
                print("GAME OVER")

            elif menu_de_interaccion == 2:
                print("Elejiste la opción PUERTA AZUL")
                print("Devorado por Bestias")
                print("GAME OVER")

            elif menu_de_interaccion == 3:
                print("Elejiste la opción PUERTA AMARILLA")
                print("Encontraste el tesoro")
                print("Haz ganado")
            
            else:
               print("elije una opcion valida")
        else:
               print("elije una opcion valida")
    else:
        print("elije una opcion valida")          
else:
    print("elije una opcion valida")  

