import unittest
from controllers.gestor_transacciones import GestorTransacciones
from datetime import datetime

class TestGestorTransacciones(unittest.TestCase):
    """
    Clase de pruebas para el Gestor de Transacciones.
    """
    
    def setUp(self):
        """
        Configura un entorno de prueba inicializando una instancia del gestor de transacciones
        y registrando una transacción de prueba.
        """
        self.gestor = GestorTransacciones()
        self.gestor.registrar_transaccion(1, 1, 1, "ingreso", 100.0, datetime.now())

    def test_registrar_transaccion_correcta(self):
        """
        Verifica que una transacción válida se registre correctamente.
        """
        self.gestor.registrar_transaccion(2, 1, 2, "gasto", 50.0, datetime.now())
        self.assertEqual(len(self.gestor.transacciones), 2)

    def test_registrar_transaccion_monto_cero(self):
        """
        Verifica que no se pueda registrar una transacción con monto igual a cero.
        """
        with self.assertRaises(ValueError):
            self.gestor.registrar_transaccion(3, 1, 1, "ingreso", 0, datetime.now())

    def test_registrar_transaccion_tipo_invalido(self):
        """
        Verifica que no se pueda registrar una transacción con un tipo inválido.
        """
        with self.assertRaises(ValueError):
            self.gestor.registrar_transaccion(4, 1, 1, "otro", 100.0, datetime.now())

    def test_filtrar_por_fecha(self):
        """
        Verifica que el filtrado por fecha devuelva correctamente las transacciones dentro del rango especificado.
        """
        fecha_inicio = datetime(2020, 1, 1)
        fecha_fin = datetime(2030, 1, 1)
        transacciones = self.gestor.filtrar_por_fecha(1, fecha_inicio, fecha_fin)
        self.assertEqual(len(transacciones), 1)
