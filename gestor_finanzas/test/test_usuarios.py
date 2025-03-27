import unittest
import hashlib
import getpass
from controllers.gestor_usuarios import GestorUsuarios

class TestGestorUsuarios(unittest.TestCase):
    """
    Clase de pruebas para el Gestor de Usuarios.
    """
    
    def setUp(self):
        """
        Configura un entorno de prueba inicializando una instancia del gestor de usuarios
        y registrando un usuario de prueba.
        """
        self.gestor = GestorUsuarios()
        hashed_password = hashlib.sha256("pass123".encode()).hexdigest()
        self.gestor.registrar_usuario(1, "usuario1", hashed_password, "usuario1@mail.com")

    def test_registrar_usuario(self):
        """
        Verifica que un usuario nuevo se registre correctamente.
        """
        hashed_password = hashlib.sha256("pass456".encode()).hexdigest()
        self.gestor.registrar_usuario(2, "usuario2", hashed_password, "usuario2@mail.com")
        self.assertIn("usuario2", self.gestor.usuarios)

    def test_iniciar_sesion_correcto(self):
        """
        Verifica que un usuario pueda iniciar sesión con credenciales correctas.
        """
        contraseña = getpass.getpass("Ingrese su contraseña: ")
        self.assertTrue(self.gestor.iniciar_sesion("usuario1", contraseña))

    def test_iniciar_sesion_error(self):
        """
        Verifica que un usuario no pueda iniciar sesión con una contraseña incorrecta.
        """
        with self.assertRaises(ValueError):
            self.gestor.iniciar_sesion("usuario1", "incorrecta")

    def test_cambiar_contraseña(self):
        """
        Verifica que un usuario pueda cambiar su contraseña correctamente.
        """
        self.assertTrue(self.gestor.cambiar_contraseña("usuario1", "pass123", "newpass"))
