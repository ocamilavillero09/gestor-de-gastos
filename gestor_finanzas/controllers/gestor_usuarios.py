class GestorUsuarios:
    """
    Clase para gestionar usuarios.
    Permite registrar usuarios y gestionar el inicio de sesión.
    """
    
    def __init__(self):
        """
        Inicializa un diccionario vacío para almacenar los usuarios.
        """
        self.usuarios = {}

    def registrar_usuario(self, usuario_id, nombre_usuario, contraseña, email):
        """
        Registra un nuevo usuario en el sistema.

        :param usuario_id: Identificador único del usuario.
        :param nombre_usuario: Nombre de usuario único.
        :param contraseña: Contraseña del usuario.
        :param email: Dirección de correo electrónico del usuario.
        """
        self.usuarios[nombre_usuario] = {
            "id": usuario_id,
            "contraseña": contraseña,
            "email": email
        }

    def obtener_usuario(self, nombre_usuario):
        """
        Devuelve los datos del usuario si existe, de lo contrario, None.

        :param nombre_usuario: Nombre de usuario a buscar.
        :return: Diccionario con los datos del usuario o None si no existe.
        """
        return self.usuarios.get(nombre_usuario)

    def obtener_todos_los_usuarios(self):
        """
        Devuelve una lista con todos los nombres de usuario registrados.
        """
        return list(self.usuarios.keys())  # Devuelve solo los nombres de usuario

    def iniciar_sesion(self, nombre_usuario, contraseña):
        """
        Verifica las credenciales de un usuario para iniciar sesión.

        :param nombre_usuario: Nombre de usuario.
        :param contraseña: Contraseña proporcionada para la autenticación.
        :return: True si las credenciales son correctas, False en caso contrario.
        """
        usuario = self.obtener_usuario(nombre_usuario)  

        if usuario and usuario["contraseña"] == contraseña:
            return True 
        return False
    
    def registrar_transaccion(self, id_transaccion, usuario_id, categoria_id, tipo, monto, fecha):
        """
        Registra una nueva transacción en la lista.
        """
        self.transacciones.append({
            "id": id_transaccion,
            "usuario_id": usuario_id,
            "categoria_id": categoria_id,
            "tipo": tipo,
            "monto": monto,
            "fecha": fecha
        })

    def obtener_transacciones_por_usuario(self, usuario_id):
        """
        Retorna una lista de transacciones filtradas por usuario_id.
        Si no hay transacciones, devuelve una lista vacía.
        """
        return [t for t in self.transacciones if t["usuario_id"] == usuario_id]


