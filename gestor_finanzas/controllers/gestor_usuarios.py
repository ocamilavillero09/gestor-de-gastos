from models.usuario import Usuario

class GestorUsuarios:
    def __init__(self):
        self.usuarios = {}

    def registrar_usuario(self, id_usuario: int, nombre: str, contraseña: str, email: str):
        if nombre in self.usuarios:
            raise ValueError("El usuario ya existe")
        self.usuarios[nombre] = Usuario(id_usuario, nombre, contraseña, email)

    def iniciar_sesion(self, nombre: str, contraseña: str):
        usuario = self.usuarios.get(nombre)
        if not usuario or usuario.contraseña != contraseña:
            raise ValueError("Credenciales incorrectas")
        return True

    def cambiar_contraseña(self, nombre: str, contraseña_actual: str, nueva_contraseña: str):
        usuario = self.usuarios.get(nombre)
        if not usuario or usuario.contraseña != contraseña_actual:
            raise ValueError("Contraseña incorrecta")
        usuario.contraseña = nueva_contraseña
        return True
