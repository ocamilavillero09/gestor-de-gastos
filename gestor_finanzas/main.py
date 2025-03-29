import hashlib
import getpass
from controllers.gestor_usuarios import GestorUsuarios
from controllers.gestor_transacciones import GestorTransacciones
from datetime import datetime

# Inicialización de los gestores
gestor_usuarios = GestorUsuarios()
gestor_transacciones = GestorTransacciones()

# Función para encriptar contraseñas
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Menú principal
while True:
    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Iniciar sesión")
    print("2. Registrarse")
    print("3. Salir")

    opcion = input("Seleccione una opción (1/2/3): ")

    if opcion == "3":
        print("Saliendo del sistema...")
        break

    elif opcion == "2":
        print("\n=== REGISTRO DE USUARIO ===")
        nombre_usuario = input("Ingrese un nombre de usuario: ")
        
        if gestor_usuarios.obtener_usuario(nombre_usuario):  # Verifica si el usuario ya existe
            print(" El usuario ya existe. Intente con otro nombre.")
            continue

        email = input("Ingrese su correo electrónico: ")
        contraseña = getpass.getpass("Ingrese una contraseña: ")
        contraseña_confirmacion = getpass.getpass("Confirme su contraseña: ")

        if contraseña != contraseña_confirmacion:
            print(" Las contraseñas no coinciden. Intente de nuevo.")
            continue

        contraseña_hasheada = hash_password(contraseña)
        user_id = len(gestor_usuarios.obtener_todos_los_usuarios()) + 1

        gestor_usuarios.registrar_usuario(user_id, nombre_usuario, contraseña_hasheada, email)
        print("✅ Usuario registrado con éxito. Ahora puede iniciar sesión.")

    elif opcion == "1":
        print("\n=== INICIO DE SESIÓN ===")
        nombre_usuario = input("Ingrese su usuario: ")
        contraseña = getpass.getpass("Ingrese su contraseña: ")
        contraseña_hasheada = hash_password(contraseña)

        if gestor_usuarios.iniciar_sesion(nombre_usuario, contraseña_hasheada):
            print("✅ Inicio de sesión exitoso.")

            # Menú de transacciones después de iniciar sesión
            while True:
                print("\n===== MENÚ DE TRANSACCIONES =====")
                print("1. Registrar ingreso")
                print("2. Registrar gasto")
                print("3. Ver transacciones registradas")
                print("4. Cerrar sesión")

                opcion_transaccion = input("Seleccione una opción (1/2/3/4): ")

                if opcion_transaccion == "4":
                    print("Cerrando sesión...\n")
                    break

                elif opcion_transaccion in ["1", "2"]:
                    tipo_transaccion = "ingreso" if opcion_transaccion == "1" else "gasto"

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

                    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Formato legible
                    categoria_id = 1  # Puedes cambiar esto según las categorías disponibles

                    gestor_transacciones.registrar_transaccion(
                        id_transaccion=len(gestor_transacciones.transacciones) + 1,
                        usuario_id=1,  # Aquí deberías obtener el ID del usuario autenticado
                        categoria_id=categoria_id,
                        tipo=tipo_transaccion,
                        monto=monto,
                        fecha=fecha_actual
                    )

                    print(f"Transacción registrada con éxito el {fecha_actual}!")

                elif opcion_transaccion == "3":
                    print("\n=== TRANSACCIONES REGISTRADAS ===")
                    
                    transacciones = gestor_transacciones.obtener_transacciones_por_usuario(1)

                    if not transacciones:  # Si transacciones es None o una lista vacía
                        print(" No hay transacciones registradas.")
                    else:
                        for t in transacciones:
                            if isinstance(t, dict):  # Asegurar que t sea un diccionario antes de acceder a sus claves
                                print(f"📝 ID: {t.get('id', 'N/A')} | Tipo: {t.get('tipo', 'N/A')} | Monto: ${t.get('monto', 'N/A')} | Fecha: {t.get('fecha', 'N/A')} | Categoría ID: {t.get('categoria_id', 'N/A')}")
                            else:
                                print("⚠ Error: La transacción no tiene el formato esperado.")

        else:
            print(" Usuario o contraseña incorrectos. Intente nuevamente.\n")

