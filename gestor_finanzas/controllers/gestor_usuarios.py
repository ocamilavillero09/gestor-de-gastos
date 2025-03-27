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

    def iniciar_sesion(self, nombre_usuario, contraseña):
        """
        Verifica las credenciales de un usuario para iniciar sesión.

        :param nombre_usuario: Nombre de usuario.
        :param contraseña: Contraseña proporcionada para la autenticación.
        :return: True si las credenciales son correctas, False en caso contrario.
        """
        usuario = self.usuarios.get(nombre_usuario)

        if usuario and usuario["contraseña"] == contraseña:
            return True 
        return False

