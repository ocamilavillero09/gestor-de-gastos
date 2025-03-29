class Usuario:
    """
    Clase que representa a un usuario del sistema.
    """
    
    def __init__(self, id_usuario: int, nombre: str, contraseña: str, email: str):
        """
        Inicializa un nuevo usuario.

        :param id_usuario: Identificador único del usuario.
        :param nombre: Nombre del usuario.
        :param contraseña: Contraseña del usuario.
        :param email: Dirección de correo electrónico del usuario.
        """
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.contraseña = contraseña
        self.email = email