import unittest
from controllers.gestor_usuarios import GestorUsuarios

class TestGestorUsuarios(unittest.TestCase):
    def setUp(self):
        self.gestor = GestorUsuarios()
        self.gestor.registrar_usuario(1, "usuario1", "pass123", "usuario1@mail.com")

    def test_registrar_usuario(self):
        self.gestor.registrar_usuario(2, "usuario2", "pass456", "usuario2@mail.com")
        self.assertIn("usuario2", self.gestor.usuarios)

    def test_iniciar_sesion_correcto(self):
        self.assertTrue(self.gestor.iniciar_sesion("usuario1", "pass123"))

    def test_iniciar_sesion_error(self):
        with self.assertRaises(ValueError):
            self.gestor.iniciar_sesion("usuario1", "incorrecta")

    def test_cambiar_contraseña(self):
        self.assertTrue(self.gestor.cambiar_contraseña("usuario1", "pass123", "newpass"))
