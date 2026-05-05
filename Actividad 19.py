print("Hola, bienvenido") 

opcionPrincipal = 0

while opcionPrincipal != 3:
    print("MENÚ PRINCIPAL")
    print("1. Mostrar estudiantes")
    
    print("2. Operaciones (Submenú)")
    print("3. Salir")

    opcionPrincipal = int(input("Elige una opción (1-3): "))

    # OPCIÓN 1: Mostrar estudiantes
    if opcionPrincipal == 1:
        print("Lista de estudiantes:")
        print("Juan - 18 años")
        print("María - 19 años")
        print("Carlos - 17 años")

    # OPCIÓN 2: Submenú de operaciones
    elif opcionPrincipal == 2:
        opcSub2 = 0
        while opcSub2 != 3:
            print("SUBMENÚ OPERACIONES")
            print("1. Sumar")
            print("2. Restar")
            print("3. Salir")

            opcSub2 = int(input("Elige una opción: "))

            if opcSub2 == 1:
                num1 = int =18
                num2 = int =19
                num3 = int =17
                print("Resultado:", num1 + num2 + num3)

            elif opcSub2 == 2:
                num1 = int =18
                num2 = int =19
                num3 = int =17
                print("Resultado:", num1 - num2 - num3)

            elif opcSub2 == 3:
                print("Saliendo del submenú...")

            else:
                print("Opción inválida")

    # OPCIÓN 3: Salir
    elif opcionPrincipal == 3:
        print("Fin del programa")

    else:
        print("ERROR: opción inválida")