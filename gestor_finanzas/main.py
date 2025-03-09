from controllers.gestor_usuarios import GestorUsuarios
from controllers.gestor_transacciones import GestorTransacciones
from datetime import datetime

gestor_usuarios = GestorUsuarios()
gestor_transacciones = GestorTransacciones()

gestor_usuarios.registrar_usuario(1, "admin", "1234", "admin@mail.com")

while True:
    nombre_usuario = input("Ingrese su usuario: ")
    contraseña = input("Ingrese su contraseña: ")

    if gestor_usuarios.iniciar_sesion(nombre_usuario, contraseña):
        print(" Inicio de sesión exitoso.")
        break
    else:
        print(" Usuario o contraseña incorrectos. Intente nuevamente.\n")

while True:
    print("\n¿Qué tipo de transacción desea registrar?")
    print("1. Ingreso")
    print("2. Gasto")
    print("3. Salir")

    opcion = input("Seleccione una opción (1/2/3): ")

    if opcion == "3":
        print(" Transacciones registradas antes de salir:")
        transacciones = gestor_transacciones.obtener_transacciones_por_usuario(1)
        
        if not transacciones:
            print("No hay transacciones registradas.")
        else:
            for transaccion in transacciones:
                print(transaccion)
        
        print("\nSaliendo del sistema...")
        break  

    if opcion not in ["1", "2"]:
        print("Opción inválida. Intente nuevamente.")
        continue

    tipo_transaccion = "ingreso" if opcion == "1" else "gasto"

    while True:
        try:
            monto = float(input(f"Ingrese el monto para el {tipo_transaccion}: "))
            
            if monto <= 0:
                print(" El monto debe ser mayor a 0.")
                continue

            if monto > 1_000_000:  
                print(" El monto es demasiado grande. Ingrese un valor razonable.")
                continue
            
            break  

        except ValueError:
            print("Error: Debe ingresar un número válido.")

    fecha_actual = datetime.now()
    categoria_id = 1  

    gestor_transacciones.registrar_transaccion(
        id_transaccion=len(gestor_transacciones.transacciones) + 1,
        usuario_id=1,
        categoria_id=categoria_id,
        tipo=tipo_transaccion,
        monto=monto,
        fecha=fecha_actual
    )

    print("Transacción registrada con éxito!")
