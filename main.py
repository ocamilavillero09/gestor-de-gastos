import hashlib
import getpass
from controllers.gestor_usuarios import GestorUsuarios
from controllers.gestor_transacciones import GestorTransacciones
from datetime import datetime

# Inicialización de los gestores
gestor_usuarios = GestorUsuarios()
gestor_transacciones = GestorTransacciones()

# Registro de usuarios con contraseñas encriptadas
def hash_password(password):
    """
    Genera un hash SHA-256 para la contraseña proporcionada.
    """
    return hashlib.sha256(password.encode()).hexdigest()

gestor_usuarios.registrar_usuario(1, "admin", "03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4ad", "admin@mail.com")
gestor_usuarios.registrar_usuario(2, "admin2", "03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4", "admin2@mail.com")

# Inicio de sesión con getpass
while True:
    nombre_usuario = input("Ingrese su usuario: ")
    contraseña = getpass.getpass("Ingrese su contraseña: ")
    
    if gestor_usuarios.iniciar_sesion(nombre_usuario, hash_password(contraseña)):
        print("Inicio de sesión exitoso.")
        break
    else:
        print("Usuario o contraseña incorrectos. Intente nuevamente.\n")

# Menú de transacciones
while True:
    print("\n¿Qué tipo de transacción desea registrar?")
    print("1. Ingreso")
    print("2. Gasto")
    print("3. Salir")

    opcion = input("Seleccione una opción (1/2/3): ")

    if opcion == "3":
        print("Transacciones registradas antes de salir:")
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
                print("El monto debe ser mayor a 0.")
                continue

            if monto > 1_000_000:  
                print("El monto es demasiado grande. Ingrese un valor razonable.")
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
