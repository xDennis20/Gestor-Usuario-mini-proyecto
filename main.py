from Logicagestor import GestorUsuario
gestor = GestorUsuario()

while True:
    print("\n---- MENÚ GESTOR DE USUARIOS ----")
    print("1. Registrar usuario")
    print("2. Agregar usuario al gestor")
    print("3. Buscar usuario por correo")
    print("4. Listar usuarios mayores de edad")
    print("5. Eliminar usuario por correo")
    print("6. Mostrar todos los usuarios")
    print("7. Salir")

    opcion = input("Selecciona una opción: ").strip()

    if opcion == "1":
        nuevo_usuario = GestorUsuario.registrar_usuario()

    elif opcion == "2":
        try:
            gestor.agregar_usuario(nuevo_usuario)
        except NameError:
            print("Primero debes registrar un usuario con la opción 1.")

    elif opcion == "3":
        correo = input("Ingresa el correo a buscar: ")
        resultado = gestor.buscar_usuario(correo)
        if resultado:
            print("Usuario encontrado:", resultado)
        else:
            print("Usuario no encontrado.")

    elif opcion == "4":
        mayores = gestor.usuario_mayores()
        print("Usuarios mayores de edad:")
        for u in mayores:
            print(u)

    elif opcion == "5":
        correo = input("Correo del usuario a eliminar: ")
        eliminado = gestor.eliminar_usuario(correo)
        if eliminado:
            print("Usuario eliminado.")
        else:
            print("No se encontró el usuario.")

    elif opcion == "6":
        print("Usuarios actuales:")
        for u in gestor.lista_usuarios:
            print(u)

    elif opcion == "7":
        print("¡Hasta luego!")
        break

    else:
        print("Opción no válida. Intenta otra vez.")

