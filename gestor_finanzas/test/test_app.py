import pytest
from controllers.gestor_usuarios import GestorUsuarios
from controllers.gestor_transacciones import GestorTransacciones
from datetime import datetime

@pytest.fixture
def gestor_usuarios():
    """
    Crea una instancia del gestor de usuarios con un usuario de prueba.
    """
    gestor = GestorUsuarios()
    gestor.registrar_usuario(1, "admin", "1234", "admin@mail.com")
    return gestor

@pytest.fixture
def gestor_transacciones():
    """
    Crea una instancia del gestor de transacciones vacía.
    """
    return GestorTransacciones()

# Pruebas para `GestorUsuarios`
def test_iniciar_sesion_exitoso(gestor_usuarios):
    """
    Verifica que un usuario con credenciales correctas pueda iniciar sesión.
    """
    assert gestor_usuarios.iniciar_sesion("admin", "1234") == True

def test_iniciar_sesion_fallido(gestor_usuarios):
    """
    Verifica que un usuario con contraseña incorrecta no pueda iniciar sesión.
    """
    assert gestor_usuarios.iniciar_sesion("admin", "incorrecto") == False

def test_usuario_inexistente(gestor_usuarios):
    """
    Verifica que un usuario inexistente no pueda iniciar sesión.
    """
    assert gestor_usuarios.iniciar_sesion("usuario_fake", "1234") == False

# Pruebas para `GestorTransacciones`
def test_registrar_transaccion(gestor_transacciones):
    """
    Verifica que una transacción válida se registre correctamente.
    """
    fecha = datetime.now()
    gestor_transacciones.registrar_transaccion(1, 1, 1, "ingreso", 100, fecha)
    transacciones = gestor_transacciones.obtener_transacciones_por_usuario(1)
    assert len(transacciones) == 1

def test_transaccion_monto_negativo(gestor_transacciones):
    """
    Verifica que una transacción con monto negativo no se registre.
    """
    fecha = datetime.now()
    gestor_transacciones.registrar_transaccion(1, 1, 1, "gasto", -50, fecha)
    transacciones = gestor_transacciones.obtener_transacciones_por_usuario(1)
    assert len(transacciones) == 0  # No debería registrarse

def test_transaccion_monto_extremo(gestor_transacciones):
    """
    Verifica que una transacción con un monto extremadamente alto no se registre.
    """
    fecha = datetime.now()
    gestor_transacciones.registrar_transaccion(1, 1, 1, "ingreso", 1_000_001, fecha)
    transacciones = gestor_transacciones.obtener_transacciones_por_usuario(1)
    assert len(transacciones) == 0  # No debería registrarse
