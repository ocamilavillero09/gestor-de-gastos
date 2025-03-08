from controllers.gestor_usuarios import GestorUsuarios
from controllers.gestor_transacciones import GestorTransacciones
from datetime import datetime

gestor_usuarios = GestorUsuarios()
gestor_transacciones = GestorTransacciones()

# Registro e inicio de sesión
gestor_usuarios.registrar_usuario(1, "admin", "1234", "admin@mail.com")
print(gestor_usuarios.iniciar_sesion("admin", "1234"))  # True

# Registro de transacciones
gestor_transacciones.registrar_transaccion(1, 1, 1, "ingreso", 500.0, datetime.now())
gestor_transacciones.registrar_transaccion(2, 1, 2, "gasto", 200.0, datetime.now())

# Ver transacciones
print(gestor_transacciones.obtener_transacciones_por_usuario(1))
