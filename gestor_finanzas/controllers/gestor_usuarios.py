class GestorUsuarios:
    def __init__(self):
        self.usuarios = {}

    def registrar_usuario(self, usuario_id, nombre_usuario, contraseña, email):
        self.usuarios[nombre_usuario] = {
            "id": usuario_id,
            "contraseña": contraseña,
            "email": email
        }

    def iniciar_sesion(self, nombre_usuario, contraseña):
        usuario = self.usuarios.get(nombre_usuario)

        if usuario and usuario["contraseña"] == contraseña:
            return True 
        return False 

